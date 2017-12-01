import gns
import click
from app.async_downloader import \
    AsyncDownloaderHelper, \
    DefaultDownloader, \
    DiscoveryDownloader, \
    PagingDownloader, \
    PagingDiscoveryDownloader


class Outputter:
    def will_download(self, url):
        click.echo("Q: {}".format(click.style(url, fg='yellow')))

    def did_download(self, url):
        click.echo("R: {}".format(click.style(url, fg='green')))

    def did_write(self, path):
        click.echo("P: {}".format(click.style(path, fg='magenta')))

    def ratelimit_wait(self):
        pass
        #click.echo(".. {} {}".format(click.style("Awaiting", fg='blue'), self.url))

    def ratelimit_continue(self):
        click.echo(".. {} {}".format(click.style("Hit rate limit and continuing", fg='blue'), self.url))


class PathURLHelper():
    mb_api_base = gns.config.managebac.api_url
    oa_api_base = gns.config.openapply.api_url
    jsons_base = gns.config.paths.jsons

    @classmethod
    def build_json_entrypoint_path(cls, filename):
        return "{base}/{filename}.json".format(base=cls.jsons_base, filename=filename)

    @classmethod
    def build_entrypoint_url(cls, section):
        return "{base}/{section}".format(base=cls.mb_api_base, section=section)

    @classmethod
    def build_members_url(cls, path, id_):
        return "{base}/{path}".format(base=cls.mb_api_base, path=path.format(id=id_))

    @classmethod
    def build_oa_entrypoint_url(cls, section):
        return "{base}/{section}".format(base=cls.oa_api_base, section=section)

    @classmethod
    def build_oa_members_url(cls, path, id_):
        return "{base}/{path}".format(base=cls.oa_api_base, path=path.format(id=id_))


class MyDefaultDownloader(Outputter, DefaultDownloader):
    """
    """
    pass

class OpenApplyPagingDiscovery(Outputter, PagingDiscoveryDownloader):
    klass = MyDefaultDownloader

    def __init__(self, section, api_path, *args, **kwargs):
        self.section = section
        self.api_path = api_path
        super().__init__(*args, **kwargs)

    def will_download(self, url):
        click.echo("Q: {} (since_id={})".format(click.style(url, fg='yellow'), self.params['since_id']))

    def did_download(self, url):
        click.echo("S: {} (since_id={})".format(click.style(url, fg='green'), self.params['since_id']))

    def discover_urls(self, resp_json):
        ret = []
        for group in resp_json.get(self.section.replace('-', '_')):
            ret.append( PathURLHelper.build_oa_members_url(self.api_path, group['id']) )
        return ret

    def discover_path(self, resp_json, url):
        """ Return the path to save it to, if applicable; returning None means we want the result """
        tailend = url.split('/')[-2:]
        tailend.insert(0, self.section)  # differentiate between classes and ibgroups this way
        return PathURLHelper.build_json_entrypoint_path("-".join(tailend))

    def update_json(self, response_json):
        students = response_json.get('students')
        links = response_json.get('links')
        if students:
            self._json['students'].extend(students)
        if links:
            parents = links.get('parents')
            self._json['parents'].extend(parents)

    def needs_next_page(self, response_json):
        """ Determine whether or not """
        return bool(response_json.get('students'))

    def update_params_for_page(self, response_json):
        """ Allows you to send new parameters in url to get the next page """
        self.params['since_id'] = response_json['students'][-1].get('id')
