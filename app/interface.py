from app.async_downloader import AsyncDownloaderHelper
from app.oa_downloader import PathURLHelper, OpenApplyPagingDiscovery, MyDefaultDownloader
import gns
import json
import aiofiles
from app.db import DBSession
from app.model import UOpenapplyIntegration
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


class IndividualDownloader(MyDefaultDownloader):
    async def write(self, res_json, path):
        student = res_json['student']
        with DBSession() as session:
            try:
                entry = session.query(UOpenapplyIntegration).filter_by(id=student['id']).one()
            except NoResultFound:
                entry = UOpenapplyIntegration()
            except MultipleResultsFound:
                raise "Too many!"
            entry.id = student['id']
            entry.ps_student_number = student['student_id']
            entry.oa_name = "{} {}".format(student['first_name'], student['last_name'])
            session.add(entry)


class AllStudentsDownloader(OpenApplyPagingDiscovery):
    klass = IndividualDownloader

    def discover_urls(self, resp_json):
        ret = []
        for student in resp_json.get(self.section.replace('-', '_')):
            if student.get('status') and student['status'] == 'applied':
                ret.append( PathURLHelper.build_oa_members_url(self.api_path, student['id']) )
        return ret


class OADownloader(AsyncDownloaderHelper):
    """
    Downloads all the user, classes, ib_groups information provided by ManageBac/OpenApply APIs
    """

    def __init__(self, *args, **kwargs):
        """
        Sets up the downloaders, using the class structure
        """
        mb_api_token = gns.config.managebac.api_token
        oa_api_token = gns.config.openapply.api_token

        super().__init__(*args, **kwargs)

        urls_to_traverse = [
            PathURLHelper.build_entrypoint_url('students'),
            PathURLHelper.build_entrypoint_url('parents'),
            PathURLHelper.build_entrypoint_url('teachers'),
            PathURLHelper.build_entrypoint_url('ib-groups'),
            PathURLHelper.build_entrypoint_url('classes'),
            PathURLHelper.build_oa_entrypoint_url('students'),
        ]

        #These appear in order of how long it takes to download, each
        self.add_downloader(
            AllStudentsDownloader,
            'students',
            'students/{id}',
            urls_to_traverse[5],
            params=dict(since_id=0, count=500, auth_token=oa_api_token), 
            path=PathURLHelper.build_json_entrypoint_path("open_apply_users")
        )