# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, ForeignKeyConstraint, Index, LargeBinary, Numeric, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.dialects.oracle.base import RAW
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Accessadmin(Base):
    __tablename__ = 'accessadmin'

    accessadminid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    teachersdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    accountidentifier = Column(String(32), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Accessschool(Base):
    __tablename__ = 'accessschool'

    accessschoolid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    schoolsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    studpswdmgmtlowgrade = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("100 "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Accessstudent(Base):
    __tablename__ = 'accessstudent'

    accessstudentid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    accountidentifier = Column(String(32), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Accessteacher(Base):
    __tablename__ = 'accessteacher'

    accessteacherid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    teachersdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    accountidentifier = Column(String(32), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Addres(Base):
    __tablename__ = 'address'
    __table_args__ = (
        Index('address_u2', 'studentid', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    addr_type_cd = Column(String(10))
    effective_start_dt = Column(DateTime)
    effective_end_dt = Column(DateTime)
    street_name = Column(String(80))
    line_two_text = Column(String(80))
    city = Column(String(80))
    county = Column(String(80))
    state_cd = Column(String(10))
    postal_code = Column(String(14))
    district_of_residence = Column(String(80))
    country_cd = Column(String(10), index=True)


class Adminalert(Base):
    __tablename__ = 'adminalert'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    returncomment = Column(String(200))
    returnstatus = Column(String(30), nullable=False)
    readflag = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    readdate = Column(DateTime)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class AggAttDetail(Base):
    __tablename__ = 'agg_att_detail'
    __table_args__ = (
        Index('agg_att_detail_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    agg_attendanceid = Column(Numeric(10, 0, asdecimal=False), index=True)
    attendance_codeid = Column(Numeric(10, 0, asdecimal=False), index=True)
    att_code_cnt = Column(Numeric(10, 0, asdecimal=False))


class AggAttendance(Base):
    __tablename__ = 'agg_attendance'
    __table_args__ = (
        Index('agg_attendance_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    calendar_dayid = Column(Numeric(10, 0, asdecimal=False), index=True)
    att_mode_code = Column(String(20), index=True)
    ada_value_period = Column(Float)
    ada_value_code = Column(Float)
    ada_value_time = Column(Float)
    adm_value = Column(Float)
    att_minutes = Column(Numeric(10, 0, asdecimal=False))
    district_num = Column(String(40))
    start_dt = Column(DateTime, index=True)
    end_dt = Column(DateTime)
    programid = Column(Numeric(10, 0, asdecimal=False), index=True)
    agg_calc_type = Column(String(15))
    rprt_days_num = Column(Numeric(10, 0, asdecimal=False))
    backfill_status_code = Column(String(10))


class Aggstat(Base):
    __tablename__ = 'aggstats'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    type = Column(String(20))
    server = Column(String(31), index=True)
    date_value = Column(DateTime, index=True)
    time = Column(Numeric(10, 0, asdecimal=False))
    hits = Column(Numeric(10, 0, asdecimal=False))
    pageviews = Column(Numeric(10, 0, asdecimal=False))
    parenthits = Column(Numeric(10, 0, asdecimal=False))
    parentpvs = Column(Numeric(10, 0, asdecimal=False))
    studenthits = Column(Numeric(10, 0, asdecimal=False))
    studentpvs = Column(Numeric(10, 0, asdecimal=False))
    enrollment = Column(Numeric(10, 0, asdecimal=False))
    parentlogins = Column(Numeric(10, 0, asdecimal=False))
    studentlogins = Column(Numeric(10, 0, asdecimal=False))
    numschools = Column(Numeric(10, 0, asdecimal=False))
    pgihits = Column(Numeric(10, 0, asdecimal=False))
    pg3hits = Column(Numeric(10, 0, asdecimal=False))
    adminpvs = Column(Numeric(10, 0, asdecimal=False))
    totlogins = Column(Numeric(10, 0, asdecimal=False))
    servername = Column(String(80))
    portalpvs = Column(Numeric(10, 0, asdecimal=False))
    teacherpvs = Column(Numeric(10, 0, asdecimal=False))
    totalpvs = Column(Numeric(10, 0, asdecimal=False))
    reportqueuejobs = Column(Numeric(10, 0, asdecimal=False))
    server_instanceid = Column(Numeric(10, 0, asdecimal=False), index=True)


t_ap_apexirpagedef = Table(
    'ap_apexirpagedef', metadata,
    Column('interactive_report_id', Numeric(asdecimal=False), nullable=False),
    Column('workspace', String(255)),
    Column('workspace_display_name', String(4000)),
    Column('application_id', Numeric(asdecimal=False), nullable=False),
    Column('page_id', Numeric(asdecimal=False), nullable=False),
    Column('region_id', Numeric(asdecimal=False)),
    Column('page_name', String(255), nullable=False),
    Column('page_alias', String(255)),
    Column('page_title', String(255)),
    Column('page_requires_authentication', String(3)),
    Column('page_access_protection', String(28)),
    Column('page_group_id', Numeric(asdecimal=False)),
    Column('page_group', String(255))
)


t_apex_appln_bckp = Table(
    'apex_appln_bckp', metadata,
    Column('whencaptured', DateTime),
    Column('app_id', Numeric(asdecimal=False)),
    Column('appln_code', Text)
)


t_apex_pages_bckp = Table(
    'apex_pages_bckp', metadata,
    Column('whencaptured', DateTime),
    Column('app_id', Numeric(asdecimal=False)),
    Column('page_id', Numeric(asdecimal=False)),
    Column('page_code', Text)
)


t_apex_prefs_bckp = Table(
    'apex_prefs_bckp', metadata,
    Column('name', String(255), nullable=False),
    Column('value', String(4000), nullable=False),
    Column('created_on', DateTime),
    Column('last_updated_on', DateTime),
    Column('pref_desc', String(4000)),
    Column('security_group_id', Numeric(asdecimal=False), nullable=False)
)


t_apex_wkspc_bckp = Table(
    'apex_wkspc_bckp', metadata,
    Column('whencaptured', DateTime),
    Column('workspace_id', Numeric(asdecimal=False)),
    Column('workspace_code', Text)
)


class Appeventsqueue(Base):
    __tablename__ = 'appeventsqueue'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    objtype = Column(Numeric(scale=0, asdecimal=False), index=True)
    primarykey = Column(String(50))
    secondarykey = Column(String(50))
    schoolnum = Column(String(50))
    eventtime = Column(DateTime)
    eventaction = Column(Numeric(scale=0, asdecimal=False))
    eventdata = Column(Text)
    ready = Column(Numeric(scale=0, asdecimal=False), index=True)


class Applicationcomponent(Base):
    __tablename__ = 'applicationcomponent'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    description = Column(String(200))
    componentname = Column(String(30), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Assignment(Base):
    __tablename__ = 'assignment'

    assignmentid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    hasstandards = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0           "))
    standardscoringmethod = Column(String(30))
    standardcalcdirection = Column(String(30), nullable=False, server_default=text("'NONE'    "))
    standardrollupmethod = Column(String(30))
    standardrollupmetric = Column(String(30))
    createdbyplugin = Column(String(100))
    whocreated = Column(String(100), nullable=False, server_default=text("USER        "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE     "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER        "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE     "))


class Assignmentcategoryassoc(Base):
    __tablename__ = 'assignmentcategoryassoc'

    assignmentcategoryassocid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    assignmentsectionid = Column(ForeignKey('assignmentsection.assignmentsectionid'), nullable=False, index=True)
    teachercategoryid = Column(ForeignKey('teachercategory.teachercategoryid'), nullable=False, index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    isprimary = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0     "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    assignmentsection = relationship('Assignmentsection')
    teachercategory = relationship('Teachercategory')


class Assignmentdroppedbylowscore(Base):
    __tablename__ = 'assignmentdroppedbylowscore'
    __table_args__ = (
        Index('assignmentdroppedbylowscore_u5', 'sectionsdcid', 'studentsdcid', 'schoolsdcid', 'reportingtermbinsdcid', 'assignmentscoreid', unique=True),
    )

    assignmentdroppedbylowscoreid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    schoolsdcid = Column(ForeignKey('schools.dcid'), nullable=False, index=True)
    sectionsdcid = Column(ForeignKey('sections.dcid'), nullable=False, index=True)
    schedulingtermsdcid = Column(ForeignKey('terms.dcid'), nullable=False, index=True)
    reportingtermbinsdcid = Column(ForeignKey('termbins.dcid'), nullable=False, index=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    assignmentscoreid = Column(ForeignKey('assignmentscore.assignmentscoreid'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    assignmentscore = relationship('Assignmentscore')
    termbin = relationship('Termbin')
    term = relationship('Term')
    school = relationship('School')
    section = relationship('Section')
    student = relationship('Student')


class Assignmentretakescore(Base):
    __tablename__ = 'assignmentretakescore'

    assignmentretakescoreid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    parentscoreretakeid = Column(ForeignKey('assignmentretakescore.assignmentretakescoreid'), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    assignmentscoreid = Column(ForeignKey('assignmentscore.assignmentscoreid'), nullable=False, index=True)
    standardretakescoreid = Column(ForeignKey('standardretakescore.standardretakescoreid'), index=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    islate = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    iscollected = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isexempt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    ismissing = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isabsent = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isincomplete = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    actualscoreentered = Column(String(30), nullable=False)
    actualscorekind = Column(String(30))
    actualscoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    displayposition = Column(Numeric(6, 0, asdecimal=False))
    scorepercent = Column(Numeric(18, 6))
    scorepoints = Column(Numeric(18, 6))
    scorelettergrade = Column(String(30))
    scorenumericgrade = Column(Numeric(18, 6))
    scoreentrydate = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    scoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    altnumericgrade = Column(Numeric(18, 6))
    altalphagrade = Column(String(30))
    altscoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradescaleitem = relationship('Gradescaleitem', primaryjoin='Assignmentretakescore.actualscoregradescaledcid == Gradescaleitem.dcid')
    gradescaleitem1 = relationship('Gradescaleitem', primaryjoin='Assignmentretakescore.altscoregradescaledcid == Gradescaleitem.dcid')
    assignmentscore = relationship('Assignmentscore')
    parent = relationship('Assignmentretakescore', remote_side=[assignmentretakescoreid])
    gradescaleitem2 = relationship('Gradescaleitem', primaryjoin='Assignmentretakescore.scoregradescaledcid == Gradescaleitem.dcid')
    standardretakescore = relationship('Standardretakescore', primaryjoin='Assignmentretakescore.standardretakescoreid == Standardretakescore.standardretakescoreid')
    student = relationship('Student')


class Assignmentscore(Base):
    __tablename__ = 'assignmentscore'
    __table_args__ = (
        Index('assignmentscore_u2', 'assignmentsectionid', 'studentsdcid', unique=True),
    )

    assignmentscoreid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    assignmentsectionid = Column(ForeignKey('assignmentsection.assignmentsectionid'), nullable=False, index=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    islate = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0         "))
    iscollected = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0         "))
    isexempt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0         "))
    ismissing = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0         "))
    isabsent = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0         "))
    isincomplete = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0         "))
    actualscoreentered = Column(String(30))
    actualscorekind = Column(String(30))
    actualscoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    scorepercent = Column(Numeric(18, 6))
    scorepoints = Column(Numeric(18, 6))
    scorelettergrade = Column(String(30))
    scorenumericgrade = Column(Numeric(18, 6))
    scoreentrydate = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))
    scoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    altnumericgrade = Column(Numeric(18, 6))
    altalphagrade = Column(String(30))
    altscoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    hasretake = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL          "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER      "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER      "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))

    gradescaleitem = relationship('Gradescaleitem', primaryjoin='Assignmentscore.actualscoregradescaledcid == Gradescaleitem.dcid')
    gradescaleitem1 = relationship('Gradescaleitem', primaryjoin='Assignmentscore.altscoregradescaledcid == Gradescaleitem.dcid')
    assignmentsection = relationship('Assignmentsection')
    gradescaleitem2 = relationship('Gradescaleitem', primaryjoin='Assignmentscore.scoregradescaledcid == Gradescaleitem.dcid')
    student = relationship('Student')


class Assignmentscorecomment(Base):
    __tablename__ = 'assignmentscorecomment'

    assignmentscorecommentid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    assignmentscoreid = Column(ForeignKey('assignmentscore.assignmentscoreid'), nullable=False, unique=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    commentvalue = Column(String(4000), nullable=False)
    assignmentretakescoreid = Column(ForeignKey('assignmentretakescore.assignmentretakescoreid'), unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    assignmentretakescore = relationship('Assignmentretakescore')
    assignmentscore = relationship('Assignmentscore')
    student = relationship('Student')


class Assignmentsection(Base):
    __tablename__ = 'assignmentsection'
    __table_args__ = (
        Index('assignmentsection_u3', 'sectionsdcid', 'duedate', unique=True),
        Index('assignmentsection_u2', 'sectionsdcid', 'assignmentid', unique=True)
    )

    assignmentsectionid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    sectionsdcid = Column(ForeignKey('sections.dcid'), nullable=False, index=True)
    assignmentid = Column(ForeignKey('assignment.assignmentid'), nullable=False, index=True)
    relatedgradescaleitemdcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    name = Column(String(50), nullable=False)
    duedate = Column(DateTime, server_default=text("""\
SYSDATE + 1
            """))
    description = Column(String(4000))
    scoretype = Column(String(30))
    scoreentrypoints = Column(Numeric(18, 6), nullable=False)
    extracreditpoints = Column(Numeric(18, 6))
    weight = Column(Numeric(18, 6), server_default=text("1                   "))
    totalpointvalue = Column(Numeric(18, 6))
    iscountedinfinalgrade = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1               "))
    isscoringneeded = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0               "))
    publishoption = Column(String(30), nullable=False, server_default=text("'Immediately' "))
    publishdaysbeforedue = Column(Numeric(3, 0, asdecimal=False), server_default=text("0                   "))
    publishonspecificdate = Column(DateTime, server_default=text("NULL                "))
    publisheddate = Column(DateTime, server_default=text("sysdate             "))
    publishedscoretypeid = Column(Numeric(16, 0, asdecimal=False))
    isscorespublish = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1               "))
    maxretakeallowed = Column(Numeric(6, 0, asdecimal=False), server_default=text("0                   "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER            "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE         "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER            "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE         "))

    assignment = relationship('Assignment')
    gradescaleitem = relationship('Gradescaleitem')
    section = relationship('Section')


class Assignmentsectonlinework(Base):
    __tablename__ = 'assignmentsectonlinework'

    assignmentsectonlineworkid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    assignmentsectionid = Column(ForeignKey('assignmentsection.assignmentsectionid'), nullable=False, unique=True)
    pluginname = Column(String(256), nullable=False, index=True)
    onlineworktype = Column(String(30), nullable=False, index=True, server_default=text("'Dropbox'  "))
    onlineworksubtype = Column(String(30))
    isgraded = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0            "))
    issubtypeopt1enabled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0            "))
    issubtypeopt2enabled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0            "))
    isextracredit = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0            "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER         "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE      "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER         "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE      "))

    assignmentsection = relationship('Assignmentsection')


class Assignmentstandardassoc(Base):
    __tablename__ = 'assignmentstandardassoc'
    __table_args__ = (
        Index('assignmentstandardassoc_u2', 'standardid', 'assignmentid', unique=True),
    )

    assignmentstandardassocid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    standardid = Column(ForeignKey('standard.standardid'), nullable=False, index=True)
    assignmentid = Column(ForeignKey('assignment.assignmentid'), nullable=False, index=True)
    iscountedinstandardgrade = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    scoreentrypoints = Column(Numeric(18, 6))
    rollupweight = Column(Numeric(18, 6))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    assignment = relationship('Assignment')
    standard = relationship('Standard')


class Assignmentstudentassoc(Base):
    __tablename__ = 'assignmentstudentassoc'

    studentsdcid = Column(ForeignKey('students.dcid'), primary_key=True, nullable=False, index=True)
    assignmentsectionid = Column(ForeignKey('assignmentsection.assignmentsectionid'), primary_key=True, nullable=False, index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER       "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE    "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER       "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE    "))

    assignmentsection = relationship('Assignmentsection')
    student = relationship('Student')


class AtnConsecutiveprocessing(Base):
    __tablename__ = 'atn_consecutiveprocessing'

    atn_consecutiveprocessing_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    consec_date = Column(DateTime)
    group_id = Column(Numeric(10, 0, asdecimal=False))
    sub_group_id = Column(Numeric(10, 0, asdecimal=False))


t_atn_enrollment = Table(
    'atn_enrollment', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False), index=True),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('fteid', Numeric(10, 0, asdecimal=False), index=True),
    Column('entrydate', DateTime, index=True),
    Column('exitdate', DateTime, index=True)
)


t_atn_itvlbellscheditms = Table(
    'atn_itvlbellscheditms', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), index=True),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False), index=True),
    Column('period_id', Numeric(10, 0, asdecimal=False), index=True),
    Column('start_time', Numeric(10, 0, asdecimal=False)),
    Column('end_time', Numeric(10, 0, asdecimal=False)),
    Column('minutes_attended', Numeric(10, 0, asdecimal=False)),
    Column('daily_attendance_code', Numeric(10, 0, asdecimal=False)),
    Column('daily_time_in_default', Numeric(10, 0, asdecimal=False)),
    Column('daily_time_out_default', Numeric(10, 0, asdecimal=False)),
    Column('ada_code', Numeric(10, 0, asdecimal=False)),
    Column('interval_number', Numeric(10, 0, asdecimal=False), index=True)
)


class AtnMeetingconversion(Base):
    __tablename__ = 'atn_meetingconversion'

    atn_meetingconversion_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    converionvalue = Column(Numeric(3, 2))


class AtnNotifyrectoproces(Base):
    __tablename__ = 'atn_notifyrectoprocess'

    atn_notifyrectoprocess_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    unexcuseddate = Column(DateTime)
    rectype = Column(String(2))
    termval = Column(Numeric(10, 0, asdecimal=False))
    levelname = Column(String(30))
    cntval = Column(Numeric(10, 0, asdecimal=False))
    lvl = Column(Numeric(10, 0, asdecimal=False), index=True)
    loaded = Column(Numeric(10, 0, asdecimal=False), index=True)


t_atn_schoolattendancecode = Table(
    'atn_schoolattendancecode', metadata,
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_type', String(50))
)


t_atn_schooldays = Table(
    'atn_schooldays', metadata,
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('school_date', DateTime),
    Column('day_number', Numeric(10, 0, asdecimal=False))
)


t_atn_termorder = Table(
    'atn_termorder', metadata,
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('termtype', Numeric(10, 0, asdecimal=False)),
    Column('firstday', DateTime),
    Column('lastday', DateTime),
    Column('termorder', Numeric(10, 0, asdecimal=False))
)


class AttCodeCodeEntity(Base):
    __tablename__ = 'att_code_code_entity'
    __table_args__ = (
        Index('att_code_code_entity_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    attendance_codeid = Column(Numeric(10, 0, asdecimal=False), index=True)
    code_entityid = Column(Numeric(10, 0, asdecimal=False), index=True)
    psguid = Column(String(50), unique=True)


t_att_daypart_curyear = Table(
    'att_daypart_curyear', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('student_track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('potential_periods_present', Numeric(10, 0, asdecimal=False)),
    Column('potential_minutes_present', Numeric(10, 0, asdecimal=False)),
    Column('periods_absent', Numeric(10, 0, asdecimal=False)),
    Column('minutes_absent', Numeric(10, 0, asdecimal=False)),
    Column('daypartid', Numeric(10, 0, asdecimal=False)),
    Column('whenmodified', DateTime, nullable=False, server_default=text("SYSDATE ")),
    Index('att_daypart_curyear_n1', 'schoolid', 'calendardate', 'daypartid')
)


t_att_daypart_prevyear = Table(
    'att_daypart_prevyear', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('student_track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('potential_periods_present', Numeric(10, 0, asdecimal=False)),
    Column('potential_minutes_present', Numeric(10, 0, asdecimal=False)),
    Column('periods_absent', Numeric(10, 0, asdecimal=False)),
    Column('minutes_absent', Numeric(10, 0, asdecimal=False)),
    Column('daypartid', Numeric(10, 0, asdecimal=False)),
    Column('whenmodified', DateTime, nullable=False, server_default=text("SYSDATE ")),
    Index('att_daypart_prevyear_u1', 'studentid', 'schoolid', 'calendardate', 'daypartid', unique=True)
)


t_att_nightly_log = Table(
    'att_nightly_log', metadata,
    Column('process', String(4)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('starttime', DateTime),
    Column('endtime', DateTime),
    Column('cutoffday', DateTime),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('rowsprocessed', Numeric(10, 0, asdecimal=False)),
    Index('att_nightly_log_n1', 'schoolid', 'process')
)


t_att_nightly_schools = Table(
    'att_nightly_schools', metadata,
    Column('schoolid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('procname', String(30), nullable=False),
    Column('rowsprocessed', Numeric(10, 0, asdecimal=False)),
    Column('whencreated', DateTime, nullable=False, server_default=text("SYSDATE ")),
    Column('whocreated', String(100), nullable=False, server_default=text("USER ")),
    Column('whenmodified', DateTime, nullable=False, server_default=text("SYSDATE ")),
    Column('whomodified', String(100), nullable=False, server_default=text("USER "))
)


class Attendance(Base):
    __tablename__ = 'attendance'
    __table_args__ = (
        Index('attendance_u2', 'studentid', 'yearid', 'dcid', unique=True),
        Index('attendance_n14', 'schoolid', 'studentid', 'att_mode_code', 'att_date', 'ccid', 'periodid'),
        Index('attendance_n12', 'att_date', 'studentid'),
        Index('attendance_n13', 'studentid', 'att_date', 'ccid', 'id')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    attendance_codeid = Column(Numeric(10, 0, asdecimal=False), index=True)
    calendar_dayid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    ccid = Column(Numeric(10, 0, asdecimal=False), index=True)
    periodid = Column(Numeric(10, 0, asdecimal=False), index=True)
    parent_attendanceid = Column(Numeric(10, 0, asdecimal=False), index=True)
    att_mode_code = Column(String(20), index=True)
    att_comment = Column(Text)
    att_interval = Column(Numeric(10, 0, asdecimal=False), index=True)
    prog_crse_type = Column(String(10))
    lock_teacher_yn = Column(Numeric(10, 0, asdecimal=False))
    lock_reporting_yn = Column(Numeric(10, 0, asdecimal=False))
    transaction_type = Column(String(20))
    total_minutes = Column(Float)
    att_date = Column(DateTime)
    ada_value_code = Column(Float)
    ada_value_time = Column(Float)
    adm_value = Column(Float)
    programid = Column(Numeric(10, 0, asdecimal=False), index=True)
    att_flags = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)
    whomodifiedid = Column(Numeric(10, 0, asdecimal=False))
    whomodifiedtype = Column(String(1))
    ip_address = Column(String(39))


class AttendanceCode(Base):
    __tablename__ = 'attendance_code'
    __table_args__ = (
        Index('attendance_code_u2', 'id', 'dcid', unique=True),
        Index('attendance_code_n4', 'schoolid', 'yearid', 'att_code')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    att_code = Column(String(10))
    alternate_code = Column(String(80))
    description = Column(Text)
    presence_status_cd = Column(String(10))
    unused1 = Column(String(2))
    course_credit_points = Column(Float)
    assignment_filter_yn = Column(Numeric(10, 0, asdecimal=False))
    calculate_ada_yn = Column(Numeric(10, 0, asdecimal=False))
    calculate_adm_yn = Column(Numeric(10, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    attendancecodeinfo_guid = Column(String(32), index=True)
    psguid = Column(String(50), unique=True)


class AttendanceConversion(Base):
    __tablename__ = 'attendance_conversion'
    __table_args__ = (
        Index('attendance_conversion_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    year_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(80))


class AttendanceConversionItem(Base):
    __tablename__ = 'attendance_conversion_items'
    __table_args__ = (
        Index('attendance_conversion_items_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    attendance_conversion_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    input_value = Column(Numeric(10, 0, asdecimal=False))
    attendance_value = Column(Float)
    comment_value = Column(Text)
    fteid = Column(Numeric(10, 0, asdecimal=False), index=True)
    conversion_mode_code = Column(String(10))
    unused = Column(Numeric(10, 0, asdecimal=False))
    daypartid = Column(ForeignKey('daypart.id'), nullable=False, index=True, server_default=text("0 "))

    daypart = relationship('Daypart')


class AttendanceTaken(Base):
    __tablename__ = 'attendance_taken'
    __table_args__ = (
        Index('attendance_taken_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    att_date = Column(DateTime, index=True)
    periodid = Column(Numeric(10, 0, asdecimal=False), index=True)
    att_interval = Column(Numeric(10, 0, asdecimal=False), index=True)
    att_taken_dt = Column(DateTime)
    whomodifiedid = Column(Numeric(10, 0, asdecimal=False))
    whomodifiedtype = Column(String(1))
    ip_address = Column(String(39))


class AttendanceTime(Base):
    __tablename__ = 'attendance_time'
    __table_args__ = (
        Index('attendance_time_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    attendanceid = Column(Numeric(10, 0, asdecimal=False), index=True)
    time_in = Column(Numeric(10, 0, asdecimal=False))
    time_out = Column(Numeric(10, 0, asdecimal=False))
    atttm_comment = Column(Text)
    omit_min_yn = Column(Numeric(10, 0, asdecimal=False))
    total_minutes = Column(Numeric(10, 0, asdecimal=False))


class Attendancequeue(Base):
    __tablename__ = 'attendancequeue'
    __table_args__ = (
        Index('attendancequeue_u2', 'studentid', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    att_date = Column(DateTime)
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    daterecorded = Column(DateTime)
    sectionid = Column(Numeric(10, 0, asdecimal=False))
    timerecorded = Column(Numeric(10, 0, asdecimal=False))
    ccid = Column(Numeric(10, 0, asdecimal=False))
    unused2 = Column(Numeric(10, 0, asdecimal=False))
    att_comment = Column(Text)
    att_interval = Column(Numeric(10, 0, asdecimal=False))
    att_mode_code = Column(String(20))
    attendance_codeid = Column(Numeric(10, 0, asdecimal=False))
    calendar_dayid = Column(Numeric(10, 0, asdecimal=False))
    lock_teacher_yn = Column(Numeric(10, 0, asdecimal=False))
    parent_attendanceid = Column(Numeric(10, 0, asdecimal=False))
    periodid = Column(Numeric(10, 0, asdecimal=False))
    program_name = Column(String(80))
    total_minutes = Column(Float)
    transaction_type = Column(String(20))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    oldattendance_codeid = Column(Numeric(10, 0, asdecimal=False))


t_au_standardgraderollup = Table(
    'au_standardgraderollup', metadata,
    Column('aud_seq', Numeric(19, 0, asdecimal=False), nullable=False, unique=True),
    Column('transaction_date', DateTime, nullable=False),
    Column('dml_type', String(1), nullable=False),
    Column('standardgraderollupid', Numeric(16, 0, asdecimal=False), index=True),
    Column('o_standardaveragepercent', Float),
    Column('n_standardaveragepercent', Float),
    Column('o_standardaveragegrade', String(50)),
    Column('n_standardaveragegrade', String(50)),
    Column('o_standardhighpercent', Float),
    Column('n_standardhighpercent', Float),
    Column('o_standardhighgrade', String(40)),
    Column('n_standardhighgrade', String(40)),
    Column('o_numscores', Numeric(10, 0, asdecimal=False)),
    Column('n_numscores', Numeric(10, 0, asdecimal=False)),
    Column('o_isadminmodified', Numeric(1, 0, asdecimal=False)),
    Column('n_isadminmodified', Numeric(1, 0, asdecimal=False)),
    Column('ip_address', String(39)),
    Column('whomodifiedid', Numeric(10, 0, asdecimal=False)),
    Column('whomodifiedtype', String(1))
)


t_au_standardgraderollupcomment = Table(
    'au_standardgraderollupcomment', metadata,
    Column('aud_seq', Numeric(19, 0, asdecimal=False), nullable=False, unique=True),
    Column('transaction_date', DateTime, nullable=False),
    Column('dml_type', String(1), nullable=False),
    Column('standardgraderollupcommentid', Numeric(16, 0, asdecimal=False)),
    Column('standardgraderollupid', Numeric(16, 0, asdecimal=False)),
    Column('o_commentvalue', Text),
    Column('n_commentvalue', Text),
    Column('ip_address', String(39)),
    Column('whomodifiedid', Numeric(10, 0, asdecimal=False)),
    Column('whomodifiedtype', String(1)),
    Index('au_standardgraderollupcomm_n1', 'standardgraderollupcommentid', 'standardgraderollupid')
)


t_au_standardgradesection = Table(
    'au_standardgradesection', metadata,
    Column('aud_seq', Numeric(19, 0, asdecimal=False), nullable=False, unique=True),
    Column('transaction_date', DateTime, nullable=False),
    Column('dml_type', String(1), nullable=False),
    Column('standardgradesectionid', Numeric(16, 0, asdecimal=False), index=True),
    Column('o_standardpercent', Float),
    Column('n_standardpercent', Float),
    Column('o_standardgrade', String(50)),
    Column('n_standardgrade', String(50)),
    Column('o_isadminmodified', Numeric(1, 0, asdecimal=False)),
    Column('n_isadminmodified', Numeric(1, 0, asdecimal=False)),
    Column('ip_address', String(39)),
    Column('whomodifiedid', Numeric(10, 0, asdecimal=False)),
    Column('whomodifiedtype', String(1))
)


t_au_standardgradesectioncomment = Table(
    'au_standardgradesectioncomment', metadata,
    Column('aud_seq', Numeric(19, 0, asdecimal=False), nullable=False, unique=True),
    Column('transaction_date', DateTime, nullable=False),
    Column('dml_type', String(1), nullable=False),
    Column('standardgradesectioncommentid', Numeric(16, 0, asdecimal=False)),
    Column('standardgradesectionid', Numeric(16, 0, asdecimal=False)),
    Column('o_commentvalue', String(4000)),
    Column('n_commentvalue', String(4000)),
    Column('ip_address', String(39)),
    Column('whomodifiedid', Numeric(10, 0, asdecimal=False)),
    Column('whomodifiedtype', String(1)),
    Index('au_standardgradesectioncomm_n1', 'standardgradesectioncommentid', 'standardgradesectionid')
)


class AuditLog(Base):
    __tablename__ = 'audit_log'
    __table_args__ = (
        Index('audit_log_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    db_objectid = Column(Numeric(10, 0, asdecimal=False), index=True)
    log_dt = Column(DateTime, index=True)
    old_data = Column(String(80))
    pkid = Column(Numeric(10, 0, asdecimal=False), index=True)
    userid = Column(Numeric(10, 0, asdecimal=False))
    transaction_type = Column(String(10))
    modify_by = Column(String(40))
    modify_dt = Column(DateTime)
    log_tm = Column(Numeric(10, 0, asdecimal=False))
    ipaddress = Column(String(20))


class Autocalendarsetting(Base):
    __tablename__ = 'autocalendarsetting'
    __table_args__ = (
        Index('autocalendarsetting_u1', 'districtcalendarid', 'schoolid', 'yearid', 'settingname', unique=True),
    )

    autocalendarsettingid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    districtcalendarid = Column(ForeignKey('districtcalendar.id'))
    schoolid = Column(ForeignKey('schools.school_number'))
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    settingname = Column(String(50), nullable=False)
    settingvalue = Column(String(256))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    districtcalendar = relationship('Districtcalendar')
    school = relationship('School')


class Autocomm(Base):
    __tablename__ = 'autocomm'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(60))
    filenum = Column(Numeric(10, 0, asdecimal=False))
    hour = Column(Numeric(10, 0, asdecimal=False))
    days = Column(String(20))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    path = Column(Text)
    transfermeth = Column(String(20))
    fieldsvalue = Column(Text)
    synchmode = Column(Numeric(10, 0, asdecimal=False))
    fielddelim = Column(String(20))
    recdelim = Column(String(20))
    surround = Column(Numeric(10, 0, asdecimal=False))
    importexport = Column(String(20))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    search = Column(Text)
    ftpacctname = Column(String(20))
    ftppassword = Column(String(20))
    ftpflag = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    ftphost = Column(String(60))
    whichatt = Column(Numeric(10, 0, asdecimal=False))
    updaterecsmode = Column(Numeric(10, 0, asdecimal=False))
    usenumberofrecs = Column(Numeric(10, 0, asdecimal=False))
    date1 = Column(DateTime)
    date2 = Column(DateTime)
    useuploadtype = Column(Numeric(10, 0, asdecimal=False))
    minutes = Column(Numeric(10, 0, asdecimal=False))
    disabled = Column(Numeric(10, 0, asdecimal=False))
    reportemail = Column(Text)
    studentenrollstatus = Column(Numeric(10, 0, asdecimal=False))
    passivemode = Column(Numeric(10, 0, asdecimal=False))
    timeout = Column(Numeric(10, 0, asdecimal=False))
    charset = Column(String(20))
    pluginurlendpointid = Column(Numeric(19, 0, asdecimal=False))


class Autosend(Base):
    __tablename__ = 'autosend'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(40))
    datatype = Column(String(20))
    hour = Column(Numeric(10, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    path = Column(Text)
    transfermeth = Column(Numeric(10, 0, asdecimal=False))
    whichatt = Column(Numeric(10, 0, asdecimal=False))


class AwschedConstraint(Base):
    __tablename__ = 'awsched_constraint'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    termid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    teacherid2 = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    studentid2 = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    constraint_code = Column(String(8))
    section_type = Column(String(2))
    course_number = Column(String(11), index=True)
    course_number2 = Column(String(11), index=True)
    section_number = Column(String(10))
    section_number2 = Column(String(10))
    classroom = Column(String(10))
    constraintflagfield1 = Column(Numeric(10, 0, asdecimal=False))
    expression = Column(String(80))
    bitmap = Column(LargeBinary)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class AwschedPreference(Base):
    __tablename__ = 'awsched_preference'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    use_bldg = Column(Numeric(10, 0, asdecimal=False))
    use_house = Column(Numeric(10, 0, asdecimal=False))
    dpcycle = Column(Numeric(10, 0, asdecimal=False))
    loadmin = Column(Numeric(10, 0, asdecimal=False))
    loadpct = Column(Float)
    loadusemax = Column(Numeric(10, 0, asdecimal=False))
    maxsubsatatime = Column(Numeric(10, 0, asdecimal=False))
    maxsubstperstud = Column(Numeric(10, 0, asdecimal=False))
    ppd = Column(Numeric(10, 0, asdecimal=False))
    rndseed = Column(Numeric(10, 0, asdecimal=False))
    sterms = Column(Numeric(10, 0, asdecimal=False))
    useglobalsubstitution = Column(Numeric(10, 0, asdecimal=False))
    usestudentcrssubstitution = Column(Numeric(10, 0, asdecimal=False))


class Batch(Base):
    __tablename__ = 'batches'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    userid = Column(Numeric(10, 0, asdecimal=False))
    date_value = Column(DateTime, index=True)
    starttime = Column(Numeric(10, 0, asdecimal=False))
    endtime = Column(Numeric(10, 0, asdecimal=False))
    ipaddress = Column(String(20))
    numtransactions = Column(Numeric(10, 0, asdecimal=False))
    cash = Column(Float)
    batchtype = Column(String(20))


class BellSchedule(Base):
    __tablename__ = 'bell_schedule'
    __table_args__ = (
        Index('bell_schedule_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    year_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    attendance_conversion_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(80))
    psguid = Column(String(50), unique=True)


class BellScheduleItem(Base):
    __tablename__ = 'bell_schedule_items'
    __table_args__ = (
        Index('bell_schedule_items_n4', 'bell_schedule_id', 'daily_attendance_code', 'daily_time_in_default', 'daily_time_out_default'),
        Index('bell_schedule_items_n3', 'bell_schedule_id', 'start_time', 'end_time'),
        Index('bell_schedule_items_u2', 'id', 'dcid', unique=True)
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    bell_schedule_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    period_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    start_time = Column(Numeric(10, 0, asdecimal=False))
    end_time = Column(Numeric(10, 0, asdecimal=False))
    minutes_attended = Column(Numeric(10, 0, asdecimal=False))
    daily_attendance_code = Column(Numeric(10, 0, asdecimal=False))
    daily_time_in_default = Column(Numeric(10, 0, asdecimal=False))
    daily_time_out_default = Column(Numeric(10, 0, asdecimal=False))
    ada_code = Column(Numeric(10, 0, asdecimal=False))
    daypartid = Column(ForeignKey('daypart.id'), nullable=False, index=True, server_default=text("0 "))
    psguid = Column(String(50), unique=True)

    daypart = relationship('Daypart')


class Blob(Base):
    __tablename__ = 'blobs'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(20), index=True)
    data = Column(Text)
    lastmoddate = Column(DateTime)
    studentid = Column(Numeric(10, 0, asdecimal=False))


class Book(Base):
    __tablename__ = 'books'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    callnumber = Column(String(25))
    title = Column(String(80))
    author = Column(String(60))
    subjectheading = Column(String(80))
    pages = Column(Numeric(10, 0, asdecimal=False))
    price = Column(Float)
    barcodenumber = Column(String(20))
    publisher = Column(String(60))
    isbn = Column(String(40))
    illustrator = Column(String(50))


class Bulletinitem(Base):
    __tablename__ = 'bulletinitems'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(80))
    startdate = Column(DateTime, index=True)
    enddate = Column(DateTime, index=True)
    sortorder = Column(Numeric(10, 0, asdecimal=False), index=True)
    body = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    audience = Column(Numeric(10, 0, asdecimal=False))


class CacheMessage(Base):
    __tablename__ = 'cache_message'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    server_instanceid = Column(Numeric(10, 0, asdecimal=False), index=True)
    cache_name = Column(String(80))
    cache_row_ident = Column(Text)
    event_type = Column(String(20))
    created_ts = Column(Numeric(10, 0, asdecimal=False))


class Calendar(Base):
    __tablename__ = 'calendar'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    date1 = Column(DateTime)
    date2 = Column(DateTime)
    daysinrange = Column(Numeric(10, 0, asdecimal=False))
    code = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(80))
    unused1 = Column(String(2))


class CalendarDay(Base):
    __tablename__ = 'calendar_day'
    __table_args__ = (
        Index('calendar_day_u2', 'schoolid', 'date_value', 'dcid', unique=True),
        Index('calendar_day_n6', 'schoolid', 'insession', 'date_value'),
        Index('calendar_day_n8', 'date_value', 'insession')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    date_value = Column(DateTime, index=True)
    scheduleid = Column(String(20))
    a = Column(Numeric(10, 0, asdecimal=False))
    b = Column(Numeric(10, 0, asdecimal=False))
    c = Column(Numeric(10, 0, asdecimal=False))
    d = Column(Numeric(10, 0, asdecimal=False))
    e = Column(Numeric(10, 0, asdecimal=False))
    f = Column(Numeric(10, 0, asdecimal=False))
    insession = Column(Numeric(10, 0, asdecimal=False))
    membershipvalue = Column(Float)
    note = Column(String(50))
    type = Column(String(20), index=True)
    cycle_day_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    bell_schedule_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    week_num = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)
    whomodifiedid = Column(Numeric(10, 0, asdecimal=False))
    whomodifiedtype = Column(String(1))
    ip_address = Column(String(39))


class Canonicalfieldlist(Base):
    __tablename__ = 'canonicalfieldlist'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(50))
    description = Column(String(100), nullable=False)
    tablename = Column(ForeignKey('tablenumbermap.tablename'), nullable=False, index=True)
    country = Column(String(10))
    state = Column(String(10))
    issronly = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    tablenumbermap = relationship('Tablenumbermap')


class Categoryschoolexcludeassoc(Base):
    __tablename__ = 'categoryschoolexcludeassoc'
    __table_args__ = (
        Index('categoryschoolexcludeassoc_u1', 'districtteachercategoryid', 'schoolsdcid', unique=True),
    )

    categoryschoolexcludeassocid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    districtteachercategoryid = Column(ForeignKey('districtteachercategory.districtteachercategoryid'), nullable=False, index=True)
    schoolsdcid = Column(ForeignKey('schools.dcid'), index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    districtteachercategory = relationship('Districtteachercategory')
    school = relationship('School')


class Cc(Base):
    __tablename__ = 'cc'
    __table_args__ = (
        Index('cc_n15', 'studentid', 'schoolid', 'dateenrolled', 'dateleft'),
        Index('cc_u2', 'studentid', 'termid', 'dcid', unique=True),
        Index('cc_n14', 'sectionid', 'dateleft', 'dateenrolled', 'studentid'),
        Index('cc_n13', 'schoolid', 'termid'),
        Index('cc_n18', 'studentid', 'dateenrolled')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    dateenrolled = Column(DateTime, index=True)
    dateleft = Column(DateTime, index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    termid = Column(Numeric(10, 0, asdecimal=False), index=True)
    period_obsolete = Column(String(7))
    attendance_type_code = Column(Numeric(10, 0, asdecimal=False), index=True)
    unused2 = Column(Numeric(10, 0, asdecimal=False))
    currentabsences = Column(Numeric(10, 0, asdecimal=False))
    currenttardies = Column(Numeric(10, 0, asdecimal=False))
    attendance = Column(Text)
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    lastgradeupdate = Column(DateTime)
    section_number = Column(String(10))
    course_number = Column(String(11), index=True)
    origsectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    unused3 = Column(Numeric(10, 0, asdecimal=False))
    teachercomment = Column(Text)
    lastattmod = Column(DateTime, index=True)
    asmtscores = Column(Text)
    firstattdate = Column(DateTime)
    finalgrades = Column(Text)
    studyear = Column(Numeric(10, 0, asdecimal=False), index=True)
    log = Column(Text)
    expression = Column(String(80))
    custom = Column(Text)
    studentsectenrl_guid = Column(String(32), index=True)
    teacherprivatenote = Column(Text)
    ab_course_cmp_fun_flg = Column(String(2))
    ab_course_cmp_ext_crd = Column(String(2))
    ab_course_cmp_met_cd = Column(String(4))
    ab_course_eva_pro_cd = Column(String(2))
    ab_course_cmp_sta_cd = Column(String(3))
    psguid = Column(String(50), unique=True)


class SCcX(Cc):
    __tablename__ = 's_cc_x'

    ccdcid = Column(ForeignKey('cc.dcid'), primary_key=True)
    isauditing = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Classrank(Base):
    __tablename__ = 'classrank'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    schoolname = Column(String(60))
    storecode = Column(String(10))
    grade_level = Column(Numeric(10, 0, asdecimal=False))
    gpamethod = Column(String(50))
    gpa = Column(String(80))
    rank = Column(Numeric(10, 0, asdecimal=False))
    outof = Column(Numeric(10, 0, asdecimal=False))
    dateranked = Column(DateTime)
    log = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)


class CodeEntity(Base):
    __tablename__ = 'code_entity'
    __table_args__ = (
        Index('code_entity_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    componentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    ce_entity = Column(String(40))
    ce_code = Column(String(10))
    external_name = Column(String(80))
    internal_name = Column(String(80))
    effective_start_dt = Column(DateTime)
    effective_end_dt = Column(DateTime)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    description = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)


class Component(Base):
    __tablename__ = 'component'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(80))


class ConfigGroup(Base):
    __tablename__ = 'config_group'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(40))
    description = Column(Text)
    created_by = Column(String(40))
    created_ts = Column(Numeric(10, 0, asdecimal=False))


class Configitem(Base):
    __tablename__ = 'configitem'
    __table_args__ = (
        Index('configitemu2', 'source', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    configvalue = Column(String(4000), nullable=False)
    description = Column(String(256))
    districtflag = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    name = Column(String(256), nullable=False)
    source = Column(String(256), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Configschoolitem(Base):
    __tablename__ = 'configschoolitem'
    __table_args__ = (
        Index('configschoolitemu2', 'name', 'schoolid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    configvalue = Column(String(4000), nullable=False)
    description = Column(String(256))
    name = Column(String(256), nullable=False)
    source = Column(String(256), nullable=False)
    schoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Consecutivedaysalert(Base):
    __tablename__ = 'consecutivedaysalert'

    school_number = Column(ForeignKey('schools.school_number'), primary_key=True, nullable=False)
    studentsdcid = Column(ForeignKey('students.dcid'), primary_key=True, nullable=False)
    absencecount = Column(Numeric(3, 0, asdecimal=False), nullable=False)

    school = relationship('School')
    student = relationship('Student')


class Countryisocodelu(Base):
    __tablename__ = 'countryisocodelu'

    countryisocode = Column(String(3), primary_key=True)
    displaylabel = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class CourseRelationship(Base):
    __tablename__ = 'course_relationship'
    __table_args__ = (
        Index('course_relationship_u2', 'id', 'dcid', unique=True),
        Index('course_relationship_n1', 'schoolid', 'yearid')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    course_number1 = Column(String(11))
    course_number2 = Column(String(11))
    relationship_type = Column(String(15))
    relationship_code = Column(String(15))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))


class Courseequivalency(Base):
    __tablename__ = 'courseequivalency'
    __table_args__ = (
        Index('courseequivalency_u1', 'course_number_original', 'course_number_equivalent', 'start_date', 'end_date', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    course_number_original = Column(String(11), nullable=False, index=True)
    course_number_equivalent = Column(String(11), nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Coursefee(Base):
    __tablename__ = 'coursefee'
    __table_args__ = (
        Index('coursefee_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    courseid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    course_number = Column(String(11))
    feetype = Column(String(20))
    amount = Column(Float)


class Courseprereqevaluated(Base):
    __tablename__ = 'courseprereqevaluated'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    courseprereqruleid = Column(ForeignKey('courseprereqrule.id'), index=True)
    courseid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    coursenumber = Column(String(40))
    status = Column(String(20))
    rulename = Column(String(20))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))

    courseprereqrule = relationship('Courseprereqrule')


class Courseprereqoverride(Base):
    __tablename__ = 'courseprereqoverride'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    courseid = Column(Numeric(10, 0, asdecimal=False))
    coursenumber = Column(String(11))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    comments = Column(String(4000))
    createdbyuserid = Column(Numeric(10, 0, asdecimal=False))
    modifiedbyuserid = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class Courseprereqrecommend(Base):
    __tablename__ = 'courseprereqrecommend'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    courseid = Column(Numeric(10, 0, asdecimal=False))
    coursenumber = Column(String(11))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    comments = Column(String(4000))
    createdbyuserid = Column(Numeric(10, 0, asdecimal=False))
    modifiedbyuserid = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class Courseprereqrule(Base):
    __tablename__ = 'courseprereqrule'
    __table_args__ = (
        Index('courseprereqrule_indx', 'courseid', 'coursenumber'),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    courseid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    coursenumber = Column(String(11))
    note = Column(String(512))
    ruleexpression = Column(Text)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class Course(Base):
    __tablename__ = 'courses'
    __table_args__ = (
        Index('courses_u2', 'id', 'dcid', unique=True),
        Index('courses_n3', 'course_number', 'vocational'),
        Index('courses_n5', 'course_number', 'id')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    course_number = Column(String(11), index=True)
    course_name = Column(String(40))
    credit_hours = Column(Float)
    add_to_gpa = Column(Float)
    code = Column(String(20))
    prerequisitesvalue = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    corequisites = Column(Text)
    powerlink = Column(String(50))
    powerlinkspan = Column(String(80))
    regavailable = Column(Numeric(10, 0, asdecimal=False))
    reggradelevels = Column(String(40))
    regteachers = Column(Text)
    targetclasssize = Column(Numeric(10, 0, asdecimal=False))
    maxclasssize = Column(Numeric(10, 0, asdecimal=False))
    regcoursegroup = Column(String(80))
    multiterm = Column(String(40))
    termsoffered = Column(Text)
    sectionstooffer = Column(Numeric(10, 0, asdecimal=False))
    schoolgroup = Column(Numeric(10, 0, asdecimal=False))
    vocational = Column(Numeric(10, 0, asdecimal=False))
    status = Column(Numeric(10, 0, asdecimal=False))
    credittype = Column(String(20))
    crhrweight = Column(Float)
    sched_year = Column(Numeric(10, 0, asdecimal=False))
    sched_department = Column(String(12))
    sched_coursesubjectareacode = Column(String(8))
    sched_fullcatalogdescription = Column(Text)
    sched_coursepackage = Column(Numeric(10, 0, asdecimal=False))
    sched_coursepkgcontents = Column(Text)
    sched_scheduled = Column(Numeric(10, 0, asdecimal=False))
    sched_scheduletypecode = Column(String(8))
    sched_sectionsoffered = Column(Numeric(10, 0, asdecimal=False))
    sched_teachercount = Column(Numeric(10, 0, asdecimal=False))
    sched_periodspermeeting = Column(Numeric(10, 0, asdecimal=False))
    sched_frequency = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumperiodsperday = Column(Numeric(10, 0, asdecimal=False))
    sched_minimumperiodsperday = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumdayspercycle = Column(Numeric(10, 0, asdecimal=False))
    sched_minimumdayspercycle = Column(Numeric(10, 0, asdecimal=False))
    sched_consecutiveperiods = Column(Numeric(10, 0, asdecimal=False))
    sched_blockstart = Column(Numeric(10, 0, asdecimal=False))
    sched_validstartperiods = Column(Text)
    sched_validdaycombinations = Column(Text)
    validextradaycombinations = Column(Text)
    sched_extradayscheduletypecode = Column(String(8))
    sched_lengthinnumberofterms = Column(Numeric(10, 0, asdecimal=False))
    sched_consecutiveterms = Column(Numeric(10, 0, asdecimal=False))
    sched_balanceterms = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumenrollment = Column(Numeric(10, 0, asdecimal=False))
    sched_concurrentflag = Column(Numeric(10, 0, asdecimal=False))
    sched_facilities = Column(String(50))
    sched_multiplerooms = Column(Numeric(10, 0, asdecimal=False))
    sched_labflag = Column(Numeric(10, 0, asdecimal=False))
    sched_labfrequency = Column(Numeric(10, 0, asdecimal=False))
    sched_labperiodspermeeting = Column(Numeric(10, 0, asdecimal=False))
    sched_repeatsallowed = Column(Numeric(10, 0, asdecimal=False))
    sched_loadpriority = Column(Numeric(10, 0, asdecimal=False))
    sched_loadtype = Column(String(15))
    sched_substitutionallowed = Column(Numeric(10, 0, asdecimal=False))
    sched_globalsubstitution1 = Column(String(10))
    sched_globalsubstitution2 = Column(String(10))
    sched_globalsubstitution3 = Column(String(10))
    sched_usepreestablishedteams = Column(Numeric(10, 0, asdecimal=False))
    sched_closesectionaftermax = Column(Numeric(10, 0, asdecimal=False))
    sched_usesectiontypes = Column(Numeric(10, 0, asdecimal=False))
    sched_balancepriority = Column(String(10))
    sched_periodspercycle = Column(Numeric(10, 0, asdecimal=False))
    gradescaleid = Column(Numeric(10, 0, asdecimal=False))
    gpa_addedvalue = Column(Float)
    excludefromgpa = Column(Numeric(10, 0, asdecimal=False))
    excludefromclassrank = Column(Numeric(10, 0, asdecimal=False))
    excludefromhonorroll = Column(Numeric(10, 0, asdecimal=False))
    sched_lunchcourse = Column(Numeric(10, 0, asdecimal=False))
    sched_do_not_print = Column(Numeric(10, 0, asdecimal=False))
    exclude_ada = Column(Numeric(10, 0, asdecimal=False))
    programid = Column(Numeric(10, 0, asdecimal=False), index=True)
    excludefromstoredgrades = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))
    psguid = Column(String(50), unique=True)
    maxcredit = Column(Float)


class Coursescorefield(Course):
    __tablename__ = 'coursescorefields'

    coursesdcid = Column(ForeignKey('courses.dcid'), primary_key=True)
    alt_course_number = Column(String(4000))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SCrsCrdcX(Course):
    __tablename__ = 's_crs_crdc_x'

    coursesdcid = Column(ForeignKey('courses.dcid'), primary_key=True)
    creditrecovery_yn = Column(String(1))
    distancelearning_yn = Column(String(1))
    dualenrollment_yn = Column(String(1))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Coursesbyyear(Base):
    __tablename__ = 'coursesbyyear'

    coursesdcid = Column(Numeric(10, 0, asdecimal=False))
    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    coursesid = Column(Numeric(10, 0, asdecimal=False))
    course_number = Column(String(11))
    course_name = Column(String(40))
    credit_hours = Column(Float)
    add_to_gpa = Column(Float)
    code = Column(String(20))
    prerequisitesvalue = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    corequisites = Column(Text)
    powerlink = Column(String(50))
    powerlinkspan = Column(String(80))
    regavailable = Column(Numeric(10, 0, asdecimal=False))
    reggradelevels = Column(String(40))
    regteachers = Column(Text)
    targetclasssize = Column(Numeric(10, 0, asdecimal=False))
    maxclasssize = Column(Numeric(10, 0, asdecimal=False))
    regcoursegroup = Column(String(80))
    multiterm = Column(String(40))
    termsoffered = Column(Text)
    sectionstooffer = Column(Numeric(10, 0, asdecimal=False))
    schoolgroup = Column(Numeric(10, 0, asdecimal=False))
    vocational = Column(Numeric(10, 0, asdecimal=False))
    status = Column(Numeric(10, 0, asdecimal=False))
    credittype = Column(String(20))
    crhrweight = Column(Float)
    sched_year = Column(Numeric(10, 0, asdecimal=False))
    sched_department = Column(String(12))
    sched_coursesubjectareacode = Column(String(8))
    sched_fullcatalogdescription = Column(Text)
    sched_coursepackage = Column(Numeric(10, 0, asdecimal=False))
    sched_coursepkgcontents = Column(Text)
    sched_scheduled = Column(Numeric(10, 0, asdecimal=False))
    sched_scheduletypecode = Column(String(8))
    sched_sectionsoffered = Column(Numeric(10, 0, asdecimal=False))
    sched_teachercount = Column(Numeric(10, 0, asdecimal=False))
    sched_periodspermeeting = Column(Numeric(10, 0, asdecimal=False))
    sched_frequency = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumperiodsperday = Column(Numeric(10, 0, asdecimal=False))
    sched_minimumperiodsperday = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumdayspercycle = Column(Numeric(10, 0, asdecimal=False))
    sched_minimumdayspercycle = Column(Numeric(10, 0, asdecimal=False))
    sched_consecutiveperiods = Column(Numeric(10, 0, asdecimal=False))
    sched_blockstart = Column(Numeric(10, 0, asdecimal=False))
    sched_validstartperiods = Column(Text)
    sched_validdaycombinations = Column(Text)
    validextradaycombinations = Column(Text)
    sched_extradayscheduletypecode = Column(String(8))
    sched_lengthinnumberofterms = Column(Numeric(10, 0, asdecimal=False))
    sched_consecutiveterms = Column(Numeric(10, 0, asdecimal=False))
    sched_balanceterms = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumenrollment = Column(Numeric(10, 0, asdecimal=False))
    sched_concurrentflag = Column(Numeric(10, 0, asdecimal=False))
    sched_facilities = Column(String(50))
    sched_multiplerooms = Column(Numeric(10, 0, asdecimal=False))
    sched_labflag = Column(Numeric(10, 0, asdecimal=False))
    sched_labfrequency = Column(Numeric(10, 0, asdecimal=False))
    sched_labperiodspermeeting = Column(Numeric(10, 0, asdecimal=False))
    sched_repeatsallowed = Column(Numeric(10, 0, asdecimal=False))
    sched_loadpriority = Column(Numeric(10, 0, asdecimal=False))
    sched_loadtype = Column(String(15))
    sched_substitutionallowed = Column(Numeric(10, 0, asdecimal=False))
    sched_globalsubstitution1 = Column(String(10))
    sched_globalsubstitution2 = Column(String(10))
    sched_globalsubstitution3 = Column(String(10))
    sched_usepreestablishedteams = Column(Numeric(10, 0, asdecimal=False))
    sched_closesectionaftermax = Column(Numeric(10, 0, asdecimal=False))
    sched_usesectiontypes = Column(Numeric(10, 0, asdecimal=False))
    sched_balancepriority = Column(String(10))
    sched_periodspercycle = Column(Numeric(10, 0, asdecimal=False))
    gradescaleid = Column(Numeric(10, 0, asdecimal=False))
    gpa_addedvalue = Column(Float)
    excludefromgpa = Column(Numeric(10, 0, asdecimal=False))
    excludefromclassrank = Column(Numeric(10, 0, asdecimal=False))
    excludefromhonorroll = Column(Numeric(10, 0, asdecimal=False))
    sched_lunchcourse = Column(Numeric(10, 0, asdecimal=False))
    sched_do_not_print = Column(Numeric(10, 0, asdecimal=False))
    exclude_ada = Column(Numeric(10, 0, asdecimal=False))
    programid = Column(Numeric(10, 0, asdecimal=False))
    excludefromstoredgrades = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    maxcredit = Column(Float)


class Creq(Base):
    __tablename__ = 'creq'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    course_number = Column(String(11), index=True)
    preference = Column(Numeric(10, 0, asdecimal=False))
    reqid = Column(Numeric(10, 0, asdecimal=False))
    termid = Column(Numeric(10, 0, asdecimal=False))
    requesttype = Column(String(7))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)


class CstAssociatedresult(Base):
    __tablename__ = 'cst_associatedresult'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    resultid = Column(ForeignKey('cst_result.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    associatedresultname = Column(String(60))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))

    cst_result = relationship('CstResult')


class CstAssocresultforeignkey(Base):
    __tablename__ = 'cst_assocresultforeignkey'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    assocresultid = Column(ForeignKey('cst_associatedresult.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    sourcefield = Column(String(30))
    targetfield = Column(String(30))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))

    cst_associatedresult = relationship('CstAssociatedresult')


class CstChildreport(Base):
    __tablename__ = 'cst_childreport'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportconfigid = Column(ForeignKey('cst_reportconfig.id'), index=True)
    childreportname = Column(String(100), nullable=False)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_reportconfig = relationship('CstReportconfig')


class CstConfigfile(Base):
    __tablename__ = 'cst_configfile'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    filename = Column(String(50), index=True)
    filepath = Column(String(255))
    lastmodifiedtime = Column(Numeric(19, 0, asdecimal=False))
    statecode = Column(String(20))
    configtype = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class CstDataimportlog(Base):
    __tablename__ = 'cst_dataimportlog'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    userid = Column(Numeric(19, 0, asdecimal=False))
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    tablename = Column(String(100))
    recordsfound = Column(Numeric(10, 0, asdecimal=False))
    existingrecords = Column(Numeric(10, 0, asdecimal=False))
    recordsinserted = Column(Numeric(10, 0, asdecimal=False))
    recordsupdated = Column(Numeric(10, 0, asdecimal=False))
    invalidrecords = Column(Numeric(10, 0, asdecimal=False))
    executionmode = Column(String(100))
    status = Column(String(100))
    errormessage = Column(Text)
    tempimporttable = Column(String(100))
    headerrowexists = Column(Numeric(1, 0, asdecimal=False))
    delimiter = Column(Numeric(10, 0, asdecimal=False))
    insertupdatemode = Column(String(100))
    module = Column(String(1000))
    filename = Column(String(100))


class CstDshconfigfile(Base):
    __tablename__ = 'cst_dshconfigfiles'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    filename = Column(String(500), nullable=False, unique=True)
    lastupdate = Column(DateTime, nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class CstDshdataviewgroup(Base):
    __tablename__ = 'cst_dshdataviewgroup'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    groupname = Column(String(100), unique=True)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)


class CstDshdataviewgroupquery(Base):
    __tablename__ = 'cst_dshdataviewgroupquery'

    cst_dshdataviewgroupid = Column(Numeric(19, 0, asdecimal=False), primary_key=True, nullable=False)
    cst_dshdataviewqueryid = Column(Numeric(19, 0, asdecimal=False), primary_key=True, nullable=False, unique=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class CstDshdataviewidlink(Base):
    __tablename__ = 'cst_dshdataviewidlinks'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    id_coretable = Column(String(30), nullable=False, unique=True)
    id_fileno = Column(String(5), nullable=False)
    id_url = Column(String(500), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)


class CstDshdataviewquery(Base):
    __tablename__ = 'cst_dshdataviewquery'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    queryname = Column(String(50), nullable=False, unique=True)
    querylabel = Column(String(200), nullable=False)
    queryinfocontent = Column(Text)
    disablesort = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    querysql = Column(Text, nullable=False)
    replacelabelunderscore = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    lea_query = Column(String(1), nullable=False, server_default=text("'0' "))
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)
    sort_index = Column(Numeric(5, 0, asdecimal=False))
    no_caching = Column(Numeric(5, 0, asdecimal=False))
    validation_rule = Column(String(30))
    validation_group = Column(String(30))


class CstDshdataviewquerycol(Base):
    __tablename__ = 'cst_dshdataviewquerycols'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    cst_dshdataviewqueryid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    columnindex = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    db_colname = Column(String(30), nullable=False)
    db_alias = Column(String(30), nullable=False)
    column_label = Column(String(100))
    parameter_indexes = Column(String(100))
    altsortname = Column(String(30))
    display_column = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)
    no_filter = Column(Numeric(5, 0, asdecimal=False))
    id_colname = Column(String(30))
    id_coretable = Column(String(30))
    studentselection = Column(Numeric(1, 0, asdecimal=False))


class CstDshdataviewqueryfilter(Base):
    __tablename__ = 'cst_dshdataviewqueryfilters'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    cst_dshdataviewquerycolid = Column(Numeric(19, 0, asdecimal=False), nullable=False, unique=True)
    filter_type_input = Column(String(20), nullable=False)
    java_type = Column(String(100), nullable=False)
    cst_dshfilteroptionsid = Column(Numeric(19, 0, asdecimal=False))
    filtercompares = Column(String(50))
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)


class CstDshdataviewqueryparam(Base):
    __tablename__ = 'cst_dshdataviewqueryparams'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    cst_dshdataviewqueryid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    param_name = Column(String(100), nullable=False)
    param_index = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    java_type = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)


class CstDshdataviewtemptable(Base):
    __tablename__ = 'cst_dshdataviewtemptables'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    querygroup = Column(String(100), nullable=False)
    queryname = Column(String(50), nullable=False)
    externalid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    temptablename = Column(String(30), nullable=False)
    tablecreatedate = Column(DateTime, nullable=False)
    status = Column(String(10), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)
    userid = Column(Numeric(19, 0, asdecimal=False))
    paramlist = Column(String(4000))


class CstDshfilteroption(Base):
    __tablename__ = 'cst_dshfilteroptions'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    option_list_name = Column(String(50), nullable=False, unique=True)
    option_query = Column(Text)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)
    include_blank_option = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    blank_option_label = Column(String(100), server_default=text("'Unknown'"))


class CstDshfilteroptvalue(Base):
    __tablename__ = 'cst_dshfilteroptvalues'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    cst_dshfilteroptionsid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    option_index = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    option_value = Column(String(100), nullable=False)
    option_label = Column(String(1000), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)


class CstDshfilterparam(Base):
    __tablename__ = 'cst_dshfilterparams'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    cst_dshfilteroptionsid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    param_name = Column(String(100), nullable=False)
    param_index = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    java_type = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)


class CstDshreportdataviewgroup(Base):
    __tablename__ = 'cst_dshreportdataviewgroup'

    cst_dshreport_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    groupname = Column(String(100), nullable=False)
    sort_index = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))


class CstDshreportpref(Base):
    __tablename__ = 'cst_dshreportprefs'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dshreport_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    prefname = Column(String(100), nullable=False)
    prefvalue = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)


class CstDshreport(Base):
    __tablename__ = 'cst_dshreports'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportconfig_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    report_state = Column(String(10), nullable=False)
    report_title = Column(String(100), nullable=False)
    report_description = Column(String(200), nullable=False)
    report_type = Column(String(10), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)
    sort_index = Column(Numeric(10, 0, asdecimal=False))
    report_subtype = Column(String(20))
    executepackage = Column(String(65))


class CstDshreportsubmission(Base):
    __tablename__ = 'cst_dshreportsubmissions'
    __table_args__ = (
        Index('cst_dshreportsubmissions_u1', 'schoolid', 'yearid', 'dshreport_id', 'submission_index', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dshreport_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    report_subtitle = Column(String(100), nullable=False)
    submission_index = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    reportruntimerequest_id = Column(Numeric(19, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    schoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    start_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime)
    due_date_localid = Column(Numeric(19, 0, asdecimal=False))
    due_date_offset = Column(Numeric(10, 0, asdecimal=False))
    last_run_date = Column(DateTime)
    last_run_by = Column(Numeric(10, 0, asdecimal=False))
    validation_run_date = Column(DateTime)
    validation_run_by = Column(Numeric(10, 0, asdecimal=False))
    approval_date = Column(DateTime)
    approved_by = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)
    status = Column(String(80))
    profilecode = Column(String(10))
    interxname = Column(String(50), index=True)
    schedule_lea_option = Column(String(20))
    schedule_local_dates_only = Column(Numeric(1, 0, asdecimal=False))
    schedule_start_date = Column(DateTime)
    schedule_start_time = Column(String(20))
    schedule_cycle = Column(String(20))
    schedule_month_year_option = Column(String(50))
    schedule_weekdays_only = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_day_fri = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_day_mon = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_day_sat = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_day_sun = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_day_thu = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_day_tue = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_day_wed = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_apr = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_aug = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_dec = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_feb = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_jan = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_jul = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_jun = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_mar = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_may = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_nov = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_oct = Column(Numeric(1, 0, asdecimal=False))
    schedule_select_month_sep = Column(Numeric(1, 0, asdecimal=False))
    schedule_end_date = Column(DateTime)
    directstatus = Column(String(50))
    directstartdate = Column(DateTime)
    sql_id = Column(String(13))


class CstDshreportsubparam(Base):
    __tablename__ = 'cst_dshreportsubparams'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dshreportsubmission_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    param_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    param_name = Column(String(255), nullable=False)
    param_type = Column(String(50))
    param_value = Column(Text)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)
    param_label = Column(String(200))
    sort_index = Column(Numeric(10, 0, asdecimal=False))
    param_group = Column(String(30))
    param_category = Column(String(50))


class CstDshreportsubprereq(Base):
    __tablename__ = 'cst_dshreportsubprereqs'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dshreportsubmission_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    dshreportsubmission_prereq_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)


class CstDshreportsubschedule(Base):
    __tablename__ = 'cst_dshreportsubschedule'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dshreportsubmission_id = Column(ForeignKey('cst_dshreportsubmissions.id'), nullable=False)
    reportruntimerequest_id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    last_run_date = Column(DateTime)
    next_run_date = Column(DateTime)
    cycle = Column(String(100))
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)
    cronexpression = Column(String(255))
    end_date = Column(DateTime)

    dshreportsubmission = relationship('CstDshreportsubmission')


class CstDshreportsubschpref(Base):
    __tablename__ = 'cst_dshreportsubschprefs'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dshreportsubmission_id = Column(ForeignKey('cst_dshreportsubmissions.id'), nullable=False)
    dshreportpref_id = Column(ForeignKey('cst_dshreportprefs.id'), nullable=False)
    prefvalue = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)

    dshreportpref = relationship('CstDshreportpref')
    dshreportsubmission = relationship('CstDshreportsubmission')


class CstDshrptsubparamcustom(Base):
    __tablename__ = 'cst_dshrptsubparamcustom'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dshreportsubmission_id = Column(ForeignKey('cst_dshreportsubmissions.id'), nullable=False)
    param_name = Column(String(255), nullable=False)
    param_value = Column(Text, nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)

    dshreportsubmission = relationship('CstDshreportsubmission')


class CstDshsubreportpref(Base):
    __tablename__ = 'cst_dshsubreportprefs'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dshreport_id = Column(ForeignKey('cst_dshreports.id'), nullable=False)
    submission_index = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    dshreportpref_id = Column(ForeignKey('cst_dshreportprefs.id'), nullable=False)
    prefvalue = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)

    dshreport = relationship('CstDshreport')
    dshreportpref = relationship('CstDshreportpref')


class CstDshupdatecyclelock(Base):
    __tablename__ = 'cst_dshupdatecyclelock'

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    counter = Column(Numeric(scale=0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class CstExternaladapter(Base):
    __tablename__ = 'cst_externaladapter'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportconfigid = Column(ForeignKey('cst_reportconfig.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    externaladapterclass = Column(String(255))
    externaladaptername = Column(String(255))
    externaladaptersequence = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_reportconfig = relationship('CstReportconfig')


class CstImportvalidationlog(Base):
    __tablename__ = 'cst_importvalidationlog'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    importlogid = Column(ForeignKey('cst_dataimportlog.id'))
    importrowid = Column(Numeric(10, 0, asdecimal=False))
    importfilelinenum = Column(Numeric(10, 0, asdecimal=False))
    importfieldname = Column(String(100))
    importfieldvalue = Column(String(4000))
    validationerrormessage = Column(Text)

    cst_dataimportlog = relationship('CstDataimportlog')


class CstPackageTracking(Base):
    __tablename__ = 'cst_package_tracking'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    package_name = Column(String(30), nullable=False)
    current_version = Column(String(10))
    previous_version = Column(String(10))
    last_updated = Column(DateTime)
    dev_comment = Column(String(4000))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("CURRENT_DATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("CURRENT_DATE "))
    sr_release_version = Column(String(100))
    package_status = Column(String(20))


class CstParam(Base):
    __tablename__ = 'cst_param'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportconfigid = Column(ForeignKey('cst_reportconfig.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    name = Column(String(255))
    description = Column(String(4000))
    javacolltype = Column(String(50))
    javatype = Column(String(50))
    inputtype = Column(String(50))
    inputlabel = Column(String(255))
    isrequired = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    optdatasrc = Column(String(4000))
    optdatavaluefld = Column(String(4000))
    optdatatextfld = Column(String(4000))
    optdatawherestmt = Column(String(4000))
    optdatasortbystmt = Column(String(4000))
    isinternal = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    sortorder = Column(Numeric(19, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    optdatadefltvalstmt = Column(String(4000))
    defaultval = Column(Text)
    issavedisabled = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))

    cst_reportconfig = relationship('CstReportconfig')


class CstParamdefault(Base):
    __tablename__ = 'cst_paramdefault'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    paramid = Column(ForeignKey('cst_param.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    schoolid = Column(Numeric(19, 0, asdecimal=False))
    defaultvalue = Column(Text)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))

    cst_param = relationship('CstParam')


class CstPrefconfig(Base):
    __tablename__ = 'cst_prefconfig'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(255))
    value = Column(Text)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    configfileid = Column(ForeignKey('cst_configfile.id'))

    cst_configfile = relationship('CstConfigfile')


class CstPropertyfile(Base):
    __tablename__ = 'cst_propertyfiles'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    statecode = Column(String(20))
    configfileid = Column(ForeignKey('cst_configfile.id'), index=True)
    filename = Column(String(150))
    basename = Column(String(50))
    language = Column(String(30))
    country = Column(String(20))
    variant = Column(String(20))
    filedata = Column(LargeBinary)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))

    cst_configfile = relationship('CstConfigfile')


class CstPubDeletehistory(Base):
    __tablename__ = 'cst_pub_deletehistory'
    __table_args__ = (
        Index('cst_pub_deletehistory_n2', 'resourcename', 'profileid', 'dashboardid', 'schoolyear'),
    )

    publishjobid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    externalrefid = Column(String(300), nullable=False, index=True)
    resourcename = Column(String(100), nullable=False)
    profileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    dashboardid = Column(Numeric(19, 0, asdecimal=False))
    schoolyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    status = Column(String(1), nullable=False)
    messagetype = Column(String(100))
    message = Column(String(4000))
    messagereference = Column(String(4000))
    subdistrictid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    nodeid = Column(String(50))
    headers = Column(String(4000))
    origcreated = Column(DateTime)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubPublishhistory(Base):
    __tablename__ = 'cst_pub_publishhistory'
    __table_args__ = (
        Index('cst_pub_publishhistory_n2', 'publishedid', 'profileid', 'resourcename'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUB_PUBLISHHISTORY_SQ"."NEXTVAL""))
    externalrefid = Column(String(300), nullable=False, index=True)
    publishedid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    profileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    resourcename = Column(String(100), nullable=False)
    action = Column(String(1), nullable=False)
    status = Column(String(1), nullable=False)
    publishjobid = Column(Numeric(19, 0, asdecimal=False))
    dashboardid = Column(Numeric(19, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    orgid = Column(Numeric(19, 0, asdecimal=False))
    studentid = Column(Numeric(19, 0, asdecimal=False))
    usersdcid = Column(Numeric(19, 0, asdecimal=False))
    compositekeys = Column(String(300))
    supportingkeys = Column(String(300))
    origcreated = Column(DateTime)
    whocreated = Column(String(100), server_default=text("USER "))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP "))
    whomodified = Column(String(100), server_default=text("USER "))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP "))


class CstPubRecon(Base):
    __tablename__ = 'cst_pub_recon'
    __table_args__ = (
        Index('cst_pub_recon_u1', 'profileid', 'schoolyear', 'resourcename', 'externalrefid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUB_RECON_SQ"."NEXTVAL""))
    profileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    schoolyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    externalrefid = Column(String(300), nullable=False)
    resourcename = Column(String(100), nullable=False)
    eduorgid = Column(String(19))
    uniqueid = Column(String(30))
    is_published = Column(String(1), server_default=text("'N'"))
    cst_subdistrictsid = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))
    payload = Column(NullType)
    reviewed = Column(String(1), server_default=text("'N'"))
    dashboardid = Column(Numeric(19, 0, asdecimal=False), server_default=text("0"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubaudit(Base):
    __tablename__ = 'cst_pubaudit'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBAUDIT_SQ"."NEXTVAL""))
    tablename = Column(String(30), nullable=False)
    psid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    transtype = Column(String(1), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubauditattendance(Base):
    __tablename__ = 'cst_pubauditattendance'
    __table_args__ = (
        Index('cst_pubauditattendance_u1', 'attdcid', 'transtype', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBAUDITATTENDANCE_SQ"."NEXTVAL""))
    attdcid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    transtype = Column(String(1), nullable=False)
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubauditchangedfield(Base):
    __tablename__ = 'cst_pubauditchangedfield'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBAUDITCHANGEDFIELD_SQ"."NEXTVAL""))
    cst_pubauditid = Column(ForeignKey('cst_pubaudit.id'), nullable=False)
    fieldname = Column(String(30), nullable=False)
    oldvalue = Column(String(4000))
    newvalue = Column(String(4000))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubaudit = relationship('CstPubaudit')


class CstPubauditgradebook(Base):
    __tablename__ = 'cst_pubauditgradebook'
    __table_args__ = (
        Index('cst_pubauditgradebook_u1', 'psmtable', 'psmid', 'transtype', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBAUDITGRADEBOOK_SQ"."NEXTVAL""))
    psmtable = Column(Numeric(5, 0, asdecimal=False), nullable=False)
    psmid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    transtype = Column(String(1), nullable=False)
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubauditgrade(Base):
    __tablename__ = 'cst_pubauditgrades'
    __table_args__ = (
        Index('cst_pubauditgrades_u1', 'storedgradesdcid', 'transtype', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBAUDITGRADES_SQ"."NEXTVAL""))
    storedgradesdcid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    transtype = Column(String(1), nullable=False)
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubcodemapping(Base):
    __tablename__ = 'cst_pubcodemapping'
    __table_args__ = (
        Index('cst_pubcodemapping_u1', 'cst_pubcodevalueid', 'schoolid', 'localcode', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCODEMAPPING_SQ"."NEXTVAL""))
    cst_pubcodevalueid = Column(ForeignKey('cst_pubcodevalue.id'), nullable=False)
    schoolid = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    localcode = Column(String(30), server_default=text("'NULL'"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubcodevalue = relationship('CstPubcodevalue')


class CstPubcodemappingmisc(Base):
    __tablename__ = 'cst_pubcodemappingmisc'
    __table_args__ = (
        Index('cst_pubcodemappingmisc_u1', 'cst_pubcodesetmiscid', 'schoolid', 'schoolyear', 'localcode', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCODEMAPPINGMISC_SQ"."NEXTVAL""))
    cst_pubcodesetmiscid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    schoolid = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    schoolyear = Column(Numeric(4, 0, asdecimal=False))
    localcode = Column(String(50), server_default=text("'NULL'"))
    externalcode = Column(String(300), server_default=text("'NULL'"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubcodeset(Base):
    __tablename__ = 'cst_pubcodeset'
    __table_args__ = (
        Index('cst_pubcodeset_u1', 'resourcename', 'cst_pubprofileid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCODESET_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    resourcename = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    status = Column(String(1), nullable=False, server_default=text("'I'"))
    func = Column(String(30))
    description = Column(String(500), nullable=False)
    namespace = Column(String(300))
    basecodetagname = Column(String(100))
    usagequery = Column(String(4000))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubcodesetmisc(Base):
    __tablename__ = 'cst_pubcodesetmisc'
    __table_args__ = (
        Index('cst_pubcodesetmisc_u1', 'displayname', 'cst_pubprofileid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCODESETMISC_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    displayname = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    localcodequery = Column(String(4000))
    externalcodequery = Column(String(4000))
    usagedescription = Column(String(200))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubcodevalue(Base):
    __tablename__ = 'cst_pubcodevalue'
    __table_args__ = (
        Index('cst_pubcodevalue_u1', 'cst_pubcodesetid', 'codevalue', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCODEVALUE_SQ"."NEXTVAL""))
    cst_pubcodesetid = Column(ForeignKey('cst_pubcodeset.id'), nullable=False)
    codevalue = Column(String(300))
    shortdescription = Column(String(200))
    effectivebegindate = Column(DateTime, index=True)
    effectiveenddate = Column(DateTime)
    version = Column(String(32))
    description = Column(String(500))
    alternateid = Column(Numeric(19, 0, asdecimal=False))
    prioralternateid = Column(Numeric(19, 0, asdecimal=False))
    basecodevalue = Column(String(300))
    externalrefid = Column(String(300))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubcodeset = relationship('CstPubcodeset')


class CstPubconfig(Base):
    __tablename__ = 'cst_pubconfig'
    __table_args__ = (
        Index('cst_pubconfig_u1', 'settingname', 'cst_pubprofileid', 'cst_subdistrictsid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCONFIG_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    settingname = Column(String(50), nullable=False)
    settingvalue = Column(String(300))
    defaultvalue = Column(String(300))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    cst_subdistrictsid = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0"))


class CstPubconfigEduorg(Base):
    __tablename__ = 'cst_pubconfig_eduorg'
    __table_args__ = (
        Index('cst_pubconfig_eduorg_u1', 'cst_pubprofileid', 'eduorgid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCONFIG_EDUORG_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    eduorgid = Column(String(19), nullable=False)
    enabled_status = Column(Numeric(5, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubconfigResEduorg(Base):
    __tablename__ = 'cst_pubconfig_res_eduorg'
    __table_args__ = (
        Index('cst_pubconfig_res_eduorg_u1', 'cst_pubprofileid', 'cst_pubentitytypeid', 'eduorgid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCONFIG_RES_EDUORG_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    cst_pubentitytypeid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    eduorgid = Column(String(19), nullable=False)
    enabled_status = Column(Numeric(5, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubconfigResource(Base):
    __tablename__ = 'cst_pubconfig_resource'
    __table_args__ = (
        Index('cst_pubconfig_resource_u1', 'cst_pubprofileid', 'cst_pubentitytypeid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCONFIG_RESOURCE_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    cst_pubentitytypeid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    enabled_status = Column(Numeric(5, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubconfigfile(Base):
    __tablename__ = 'cst_pubconfigfiles'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCONFIGFILES_SQ"."NEXTVAL""))
    filename = Column(String(500), nullable=False)
    filedatetime = Column(DateTime)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


t_cst_pubconfigjobs = Table(
    'cst_pubconfigjobs', metadata,
    Column('jobname', String(100), nullable=False, unique=True),
    Column('mininterval', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('maxinterval', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('intervalsetting', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('defaultintervalsetting', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('frequency', String(100), nullable=False),
    Column('programaction', String(100), nullable=False),
    Column('jobenabled', String(1), nullable=False),
    Column('comments', String(1000)),
    Column('whocreated', String(100), server_default=text("USER")),
    Column('whencreated', DateTime, server_default=text("SYSTIMESTAMP")),
    Column('whomodified', String(100), server_default=text("USER")),
    Column('whenmodified', DateTime, server_default=text("""\
SYSTIMESTAMP
				"""))
)


class CstPubcourse(Base):
    __tablename__ = 'cst_pubcourse'
    __table_args__ = (
        Index('cst_pubcourse_u1', 'code', 'eduorgid', 'schoolyear', 'cst_pubprofileid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBCOURSE_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    schoolyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    eduorgid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    code = Column(String(60), nullable=False)
    title = Column(String(60), nullable=False)
    numberofparts = Column(Numeric(3, 0, asdecimal=False))
    academicsubjectdesc = Column(String(60))
    description = Column(String(300))
    hscourserequirement = Column(Numeric(3, 0, asdecimal=False))
    gpaapplicabilitytype = Column(String(60))
    externalrefid = Column(String(32))
    version = Column(String(32))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubprofile = relationship('CstPubprofile')


t_cst_pubdlmapnvl = Table(
    'cst_pubdlmapnvl', metadata,
    Column('cst_pubdlresourceid', ForeignKey('cst_pubdlresource.id')),
    Column('cst_pubdltablemapid', ForeignKey('cst_pubdltablemap.id')),
    Column('nvlseq', Numeric(19, 0, asdecimal=False)),
    Column('elementpath', String(1000)),
    Column('seeddata', String(1), server_default=text("'N'")),
    Column('whocreated', String(100), server_default=text("USER")),
    Column('whencreated', DateTime, server_default=text("SYSTIMESTAMP")),
    Column('whomodified', String(100), server_default=text("USER")),
    Column('whenmodified', DateTime, server_default=text("""\
SYSTIMESTAMP
						""")),
    Index('cst_pubdlmapnvl_u1', 'cst_pubdlresourceid', 'cst_pubdltablemapid', 'elementpath', unique=True)
)


t_cst_pubdlmapovr = Table(
    'cst_pubdlmapovr', metadata,
    Column('cst_pubdlresourceid', ForeignKey('cst_pubdlresource.id')),
    Column('cst_pubdltablemapid', ForeignKey('cst_pubdltablemap.id')),
    Column('elementpath', String(1000)),
    Column('seeddata', String(1), server_default=text("'N'")),
    Column('whocreated', String(100), server_default=text("USER")),
    Column('whencreated', DateTime, server_default=text("SYSTIMESTAMP")),
    Column('whomodified', String(100), server_default=text("USER")),
    Column('whenmodified', DateTime, server_default=text("""\
SYSTIMESTAMP						  
						""")),
    Index('cst_pubdlmapovr_u1', 'cst_pubdlresourceid', 'cst_pubdltablemapid', 'elementpath', unique=True)
)


class CstPubdlresource(Base):
    __tablename__ = 'cst_pubdlresource'
    __table_args__ = (
        Index('cst_pubdlresource_u1', 'cst_pubdltableid', 'mappinggroupnum', 'resourcename', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBDLRESOURCE_SQ"."NEXTVAL""))
    cst_pubdltableid = Column(ForeignKey('cst_pubdltable.id'), nullable=False)
    mappinggroupnum = Column(Numeric(19, 0, asdecimal=False))
    xmlnamespaces = Column(String(1000))
    resourcename = Column(String(500))
    resourcexmlpath = Column(String(500))
    resourceprocessingproc = Column(String(100))
    resourceprocseq = Column(Numeric(19, 0, asdecimal=False))
    seeddata = Column(String(1), server_default=text("'N'"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    recon_xml = Column(String(1), server_default=text("'N'"))

    cst_pubdltable = relationship('CstPubdltable')


class CstPubdltable(Base):
    __tablename__ = 'cst_pubdltable'
    __table_args__ = (
        Index('cst_pubdltable_u1', 'profileid', 'mergetablename', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBDLMERGETABLE_SQ"."NEXTVAL""))
    profileid = Column(Numeric(19, 0, asdecimal=False))
    mergetablename = Column(String(32))
    seeddata = Column(String(1), server_default=text("'N'"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


t_cst_pubdltablekeys = Table(
    'cst_pubdltablekeys', metadata,
    Column('cst_pubdltableid', ForeignKey('cst_pubdltable.id'), nullable=False),
    Column('mergekeyname', String(32)),
    Column('seeddata', String(1), server_default=text("'N'")),
    Column('whocreated', String(100), server_default=text("USER")),
    Column('whencreated', DateTime, server_default=text("SYSTIMESTAMP")),
    Column('whomodified', String(100), server_default=text("USER")),
    Column('whenmodified', DateTime, server_default=text("""\
SYSTIMESTAMP
						""")),
    Index('cst_pubdltablekeys_u1', 'cst_pubdltableid', 'mergekeyname', unique=True)
)


class CstPubdltablemap(Base):
    __tablename__ = 'cst_pubdltablemap'
    __table_args__ = (
        Index('cst_pubdltablemap_idx1', 'cst_pubdltableid', 'mappinggroupnum', 'elementname', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBDLTABLEMAP_SQ"."NEXTVAL""))
    cst_pubdltableid = Column(ForeignKey('cst_pubdltable.id'))
    mappinggroupnum = Column(Numeric(19, 0, asdecimal=False))
    elementname = Column(String(500))
    elementpath = Column(String(1000))
    elementdatatype = Column(String(200))
    elementsize = Column(Numeric(asdecimal=False))
    elementprocessingproc = Column(String(100))
    elementprocseq = Column(Numeric(19, 0, asdecimal=False))
    seeddata = Column(String(1), server_default=text("'N' "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubdltable = relationship('CstPubdltable')


class CstPubdownloadjob(Base):
    __tablename__ = 'cst_pubdownloadjob'
    __table_args__ = (
        Index('cst_pubdownloadjob_n1', 'resourcename', 'status', 'schoolyear', 'cst_pubprofileid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBDOWNLOADJOB_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    cst_publogid = Column(Numeric(19, 0, asdecimal=False))
    schoolyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    resourcename = Column(String(100), nullable=False)
    status = Column(String(1), nullable=False)
    params = Column(String(300))
    downloadeddata = Column(NullType)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    cst_subdistrictsid = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0"))
    nodeid = Column(String(50))
    headers = Column(String(4000))
    dashboardid = Column(Numeric(19, 0, asdecimal=False), server_default=text("0"))
    progressstatus = Column(String(255))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubentitytype(Base):
    __tablename__ = 'cst_pubentitytype'
    __table_args__ = (
        Index('cst_pubentitytype_u1', 'name', 'cst_pubprofileid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBENTITYTYPE_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    resourcename = Column(String(100), nullable=False)
    name = Column(String(50))
    status = Column(String(1), nullable=False, server_default=text("'I'"))
    func = Column(String(30))
    lastsync = Column(DateTime)
    validationgroup = Column(String(30))
    description = Column(String(200), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubfeederschool(Base):
    __tablename__ = 'cst_pubfeederschool'
    __table_args__ = (
        Index('cst_pubfeederschool_u1', 'feederschoolorgid', 'receivingschoolorgid', 'schoolyear', 'cst_pubprofileid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBFEEDERSCHOOL_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    schoolyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    feederschoolorgid = Column(String(60), nullable=False)
    receivingschoolorgid = Column(String(60), nullable=False)
    begindate = Column(DateTime, nullable=False)
    enddate = Column(DateTime)
    externalrefid = Column(String(32))
    version = Column(String(32))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubfieldrule(Base):
    __tablename__ = 'cst_pubfieldrule'
    __table_args__ = (
        Index('cst_pubfieldrule_u1', 'pstablename', 'cst_pubprofileid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBFIELDRULE_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    pstablename = Column(String(30), nullable=False)
    identitycolumnname = Column(String(30), nullable=False)
    transprocpackage = Column(String(30), nullable=False)
    transproc = Column(String(30), nullable=False)
    active = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubinterx(Base):
    __tablename__ = 'cst_pubinterx'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBINTERX_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    name = Column(String(50), nullable=False)
    annotationnamespace = Column(String(100), nullable=False)
    namespace = Column(String(100), nullable=False)
    xsinamespace = Column(String(100), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubinterxentity(Base):
    __tablename__ = 'cst_pubinterxentity'
    __table_args__ = (
        Index('cst_pubinterxentity_u1', 'cst_pubinterxid', 'cst_pubentitytypeid', 'publishorder', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBINTERXENTITY_SQ"."NEXTVAL""))
    cst_pubinterxid = Column(ForeignKey('cst_pubinterx.id'), nullable=False)
    cst_pubentitytypeid = Column(ForeignKey('cst_pubentitytype.id'), nullable=False)
    publishorder = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    publishdirection = Column(String(1), nullable=False)
    active = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubentitytype = relationship('CstPubentitytype')
    cst_pubinterx = relationship('CstPubinterx')


class CstPublog(Base):
    __tablename__ = 'cst_publog'
    __table_args__ = (
        Index('cst_publog_n1', 'severitylevel', 'servicetype', 'cst_pubprofileid', 'dashboardid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBLOG_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    severitylevel = Column(String(10), nullable=False)
    code = Column(String(50))
    servicetype = Column(String(1), server_default=text("'G'"))
    servicesubtype = Column(String(50))
    keyvalue = Column(String(20))
    dashboardid = Column(Numeric(19, 0, asdecimal=False))
    location = Column(String(100))
    resourcename = Column(String(100))
    displaymessage = Column(String(2000))
    techmessage = Column(String(2000))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubnodeproc(Base):
    __tablename__ = 'cst_pubnodeproc'
    __table_args__ = (
        Index('cst_pubnodeproc_u1', 'cst_pubprofileid', 'nodeid', 'proctype', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBNODEPROC_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    nodeid = Column(String(50))
    nodename = Column(String(50), nullable=False)
    nodetype = Column(String(20))
    proctype = Column(String(1), server_default=text("'G'"))
    lastactive = Column(DateTime, nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPuborganization(Base):
    __tablename__ = 'cst_puborganization'
    __table_args__ = (
        Index('cst_puborganization_u1', 'eduorgid', 'stateorgid', 'schoolyear', 'cst_pubprofileid', unique=True),
        Index('cst_puborganization_n1', 'schoolyear', 'institutiontype', 'eduorgid', 'stateorgid', 'cst_pubprofileid')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBORGANIZATION_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    schoolyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    eduorgid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    stateorgid = Column(String(60), nullable=False)
    institutiontype = Column(String(10), nullable=False)
    nameofinstitution = Column(String(75), nullable=False)
    shortname = Column(String(75))
    operationalstatus = Column(String(200))
    website = Column(String(255))
    localeducationagencyid = Column(Numeric(19, 0, asdecimal=False))
    stateeducationagencyid = Column(Numeric(19, 0, asdecimal=False))
    educationservicecenterid = Column(Numeric(19, 0, asdecimal=False))
    categorytype = Column(String(200))
    schooltype = Column(String(200))
    titleipartatype = Column(String(200))
    magnetspecialprogramtype = Column(String(200))
    adminfundingcontroldesc = Column(String(50))
    alternateid = Column(String(60))
    externalrefid = Column(String(32))
    version = Column(String(32))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubprofile(Base):
    __tablename__ = 'cst_pubprofile'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBPROFILE_SQ"."NEXTVAL""))
    profilecode = Column(String(10), nullable=False, unique=True)
    profilename = Column(String(100), nullable=False)
    profiletypecode = Column(String(30), nullable=False)
    profiletypeversion = Column(String(10), nullable=False)
    packagename = Column(String(30), nullable=False)
    uniqueidpackagename = Column(String(30))
    downloadpackagename = Column(String(30))
    version = Column(String(10), nullable=False)
    active = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubprofilediag(Base):
    __tablename__ = 'cst_pubprofilediag'
    __table_args__ = (
        Index('cst_pubprofilediag_u1', 'diagnosticname', 'cst_pubprofileid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBPROFILEDIAG_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    diagnosticname = Column(String(50), nullable=False)
    diagnosticvalue = Column(String(300))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubprogram(Base):
    __tablename__ = 'cst_pubprogram'
    __table_args__ = (
        Index('cst_pubprogram_u1', 'name', 'eduorgid', 'schoolyear', 'cst_pubprofileid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBPROGRAM_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    schoolyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    eduorgid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    type = Column(String(60), nullable=False)
    name = Column(String(60), nullable=False)
    programid = Column(String(60))
    sponsortype = Column(String(60))
    externalrefid = Column(String(32))
    version = Column(String(32))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubpublished(Base):
    __tablename__ = 'cst_pubpublished'
    __table_args__ = (
        Index('cst_pubpublished_n5', 'usersdcid', 'cst_pubentitytypeid'),
        Index('cst_pubpublished_u1', 'dashboardid', 'cst_pubentitytypeid', 'cst_pubprofileid', 'compositekeys', unique=True),
        Index('cst_pubpublished_n1', 'dashboardid', 'publishstatus', 'validatestatus', 'publishready', 'lastpublishdate'),
        Index('cst_pubpublished_n4', 'studentid', 'cst_pubentitytypeid')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBPUBLISHED_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    cst_pubentitytypeid = Column(ForeignKey('cst_pubentitytype.id'), nullable=False)
    cst_pubpublishmessageid = Column(Numeric(19, 0, asdecimal=False))
    dashboardid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    studentid = Column(Numeric(19, 0, asdecimal=False))
    usersdcid = Column(Numeric(19, 0, asdecimal=False))
    compositekeys = Column(String(300), nullable=False)
    supportingkeys = Column(String(300))
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    orgid = Column(String(19), nullable=False, index=True)
    validatestatus = Column(String(1), server_default=text("'V'"))
    publishready = Column(Numeric(10, 0, asdecimal=False), server_default=text("1"))
    publishstatus = Column(String(1), server_default=text("'S'"))
    publishjobid = Column(Numeric(19, 0, asdecimal=False), index=True, server_default=text("NULL"))
    lastpublishdate = Column(DateTime)
    externalrefid = Column(String(300))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    dependencyreason = Column(String(200))

    cst_pubentitytype = relationship('CstPubentitytype')
    cst_pubprofile = relationship('CstPubprofile')


class CstPubpublishjob(Base):
    __tablename__ = 'cst_pubpublishjob'
    __table_args__ = (
        Index('cst_pubpublishjob_n1', 'status', 'jobtype', 'cst_pubprofileid'),
        Index('cst_pubpublishjob_n2', 'status', 'whenmodified')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBPUBLISHJOB_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    cst_pubinterxid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    cst_publogid = Column(Numeric(19, 0, asdecimal=False))
    dashboardid = Column(Numeric(19, 0, asdecimal=False))
    status = Column(String(1), server_default=text("'P'"))
    schoolyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    resourcename = Column(String(100), nullable=False)
    publishtype = Column(String(1), nullable=False)
    jobtype = Column(String(1), nullable=False)
    bulkoperationid = Column(String(40))
    inprocessstatus = Column(Numeric(4, 0, asdecimal=False))
    publishdata = Column(Text)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    cst_subdistrictsid = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0"))
    nodeid = Column(String(50))
    headers = Column(String(4000))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubpublishmessage(Base):
    __tablename__ = 'cst_pubpublishmessage'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBPUBLISHMESSAGE_SQ"."NEXTVAL""))
    cst_pubpublishjobid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    messagetype = Column(String(100), nullable=False)
    message = Column(String(4000), nullable=False)
    messagereference = Column(String(4000))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubpublishrequest(Base):
    __tablename__ = 'cst_pubpublishrequests'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBPUBLISHREQUESTS_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    dashboardid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    requestoption = Column(String(20))
    inprocessstatus = Column(Numeric(5, 0, asdecimal=False), server_default=text("0"))
    afterhoursonly = Column(String(1), server_default=text("'N'"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))


class CstPubuniqueidparent(Base):
    __tablename__ = 'cst_pubuniqueidparent'
    __table_args__ = (
        Index('cst_pubuniqueidparent_u1', 'psid', 'cst_pubprofileid', unique=True),
        Index('cst_pubuniqueidparent_n2', 'psid', 'uniqueid', 'cst_pubprofileid', 'status', 'updateflag')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBUNIQUEIDPARENT_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    cst_publogid = Column(Numeric(19, 0, asdecimal=False))
    psid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    status = Column(String(1), nullable=False)
    updateflag = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    uniqueid = Column(String(32), index=True)
    prioruniqueid = Column(String(32))
    externalrefid = Column(String(32))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    nodeid = Column(String(50))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubuniqueidstaff(Base):
    __tablename__ = 'cst_pubuniqueidstaff'
    __table_args__ = (
        Index('cst_pubuniqueidstaff_u1', 'psid', 'cst_pubprofileid', unique=True),
        Index('cst_pubuniqueidstaff_n2', 'psid', 'uniqueid', 'cst_pubprofileid', 'status', 'updateflag')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBUNIQUEIDSTAFF_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    cst_publogid = Column(Numeric(19, 0, asdecimal=False))
    psid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    status = Column(String(1), nullable=False)
    updateflag = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    uniqueid = Column(String(32), index=True)
    prioruniqueid = Column(String(32))
    externalrefid = Column(String(32))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    nodeid = Column(String(50))

    cst_pubprofile = relationship('CstPubprofile')


class CstPubuniqueidstudent(Base):
    __tablename__ = 'cst_pubuniqueidstudent'
    __table_args__ = (
        Index('cst_pubuniqueidstudent_n2', 'psid', 'uniqueid', 'cst_pubprofileid', 'status', 'updateflag'),
        Index('cst_pubuniqueidstudent_u1', 'psid', 'cst_pubprofileid', unique=True)
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text(""PS"."CST_PUBUNIQUEIDSTUDENT_SQ"."NEXTVAL""))
    cst_pubprofileid = Column(ForeignKey('cst_pubprofile.id'), nullable=False)
    cst_publogid = Column(Numeric(19, 0, asdecimal=False))
    psid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    status = Column(String(1), nullable=False)
    updateflag = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    uniqueid = Column(String(32), index=True)
    prioruniqueid = Column(String(32))
    externalrefid = Column(String(32))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSTIMESTAMP"))
    nodeid = Column(String(50))

    cst_pubprofile = relationship('CstPubprofile')


class CstQuery(Base):
    __tablename__ = 'cst_query'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportconfigid = Column(ForeignKey('cst_reportconfig.id'))
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    phasetype = Column(Numeric(6, 0, asdecimal=False))
    queryclass = Column(String(255))
    queryname = Column(String(50))
    querytype = Column(String(20))
    isdatabasespecific = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    querysequence = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    exitallqueriesondepfail = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))

    cst_reportconfig = relationship('CstReportconfig')


class CstQuerydependency(Base):
    __tablename__ = 'cst_querydependency'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    queryid = Column(ForeignKey('cst_query.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    paramname = Column(String(50))
    value = Column(String(200))
    sortorder = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_query = relationship('CstQuery')


class CstQueryresult(Base):
    __tablename__ = 'cst_queryresult'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    queryid = Column(ForeignKey('cst_query.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    resultname = Column(String(255))
    sortorder = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_query = relationship('CstQuery')


class CstQueryresultcolumn(Base):
    __tablename__ = 'cst_queryresultcolumn'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    queryresultid = Column(ForeignKey('cst_queryresult.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    columnname = Column(String(50))
    sortorder = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_queryresult = relationship('CstQueryresult')


class CstQueryresulttable(Base):
    __tablename__ = 'cst_queryresulttable'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    queryid = Column(ForeignKey('cst_query.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    resulttablenamepattern = Column(String(50))
    paramname = Column(String(50))
    sortorder = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_query = relationship('CstQuery')


class CstRenderexpression(Base):
    __tablename__ = 'cst_renderexpression'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportconfigid = Column(ForeignKey('cst_reportconfig.id'), index=True)
    name = Column(String(100))
    sortorder = Column(Numeric(6, 0, asdecimal=False))
    outputtype = Column(String(10))
    outputfilename = Column(String(1000))
    outputfileextension = Column(String(10))
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_reportconfig = relationship('CstReportconfig')


class CstRenderexpressionitem(Base):
    __tablename__ = 'cst_renderexpressionitem'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    renderexpressionid = Column(ForeignKey('cst_renderexpression.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    type = Column(String(50))
    templatefilename = Column(String(50))
    paramname = Column(String(50))
    sortorder = Column(Numeric(19, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_renderexpression = relationship('CstRenderexpression')


class CstRenderexpressionoption(Base):
    __tablename__ = 'cst_renderexpressionoption'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    renderexpressionitemid = Column(ForeignKey('cst_renderexpressionitem.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    value = Column(String(50))
    subrenderexpressionid = Column(ForeignKey('cst_renderexpression.id'), index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_renderexpressionitem = relationship('CstRenderexpressionitem')
    cst_renderexpression = relationship('CstRenderexpression')


class CstReportconfig(Base):
    __tablename__ = 'cst_reportconfig'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    statecode = Column(String(10), nullable=False, index=True)
    reportname = Column(String(100), nullable=False, index=True)
    description = Column(String(4000))
    paramentryurl = Column(String(255))
    resulttablenamepattern = Column(String(50))
    reportoutputtype = Column(String(10))
    partitionntype = Column(String(20))
    partitioncollparam = Column(String(50))
    partitionunitparam = Column(String(50))
    category = Column(String(100))
    sortorder = Column(Numeric(19, 0, asdecimal=False))
    reportversion = Column(String(1000))
    reportoutputfilename = Column(String(1000))
    reportdelimiter = Column(String(50))
    detaileddescription = Column(Text)
    comments = Column(Text)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    configfileid = Column(ForeignKey('cst_configfile.id'), index=True)
    reportoutputfileextension = Column(String(10))
    renderclass = Column(String(255))
    reportdistrictschool = Column(Numeric(10, 0, asdecimal=False))
    reportexcludedschool = Column(Numeric(10, 0, asdecimal=False))
    recorddelimiter = Column(String(50))
    isteachersafe = Column(Numeric(1, 0, asdecimal=False))
    disableemptyresultsmsg = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    quotefields = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    isexternallinkonly = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    tabname = Column(String(100))
    preconditionqueryname = Column(String(300))
    minappversion = Column(String(50))
    maxappversion = Column(String(50))
    postsubmitaction = Column(String(300))
    reportqueuedesc = Column(String(1000))
    disablereportlistsubmit = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))

    cst_configfile = relationship('CstConfigfile')


class CstReportproces(Base):
    __tablename__ = 'cst_reportprocess'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportname = Column(String(100))
    statecode = Column(String(20))
    partitiontype = Column(String(50))
    resulttablename = Column(String(50))
    statusdesc = Column(String(50))
    creationtime = Column(DateTime)
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    fileoutputpath = Column(String(500))
    fileoutputdata = Column(LargeBinary)
    status = Column(Numeric(19, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    erroroutput = Column(LargeBinary)
    isemptyrecordset = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    exitallqueries = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    hostaddress = Column(String(100))


class CstReportprocesstable(Base):
    __tablename__ = 'cst_reportprocesstable'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportprocessid = Column(ForeignKey('cst_reportprocess.id'), index=True)
    reportsubprocessid = Column(ForeignKey('cst_reportsubprocess.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    tablename = Column(String(50))
    creationtime = Column(DateTime)
    retain = Column(Numeric(1, 0, asdecimal=False))
    deleted = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    tablenamepattern = Column(String(100))

    cst_reportproces = relationship('CstReportproces')
    cst_reportsubproces = relationship('CstReportsubproces')


class CstReportsubproces(Base):
    __tablename__ = 'cst_reportsubprocess'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportprocessid = Column(ForeignKey('cst_reportprocess.id'), index=True)
    partitionid = Column(String(50))
    subprocresulttablename = Column(String(50))
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    statusdesc = Column(String(50))
    creationtime = Column(DateTime)
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    erroroutput = Column(LargeBinary)
    status = Column(Numeric(19, 0, asdecimal=False))

    cst_reportproces = relationship('CstReportproces')


class CstResult(Base):
    __tablename__ = 'cst_result'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    reportconfigid = Column(ForeignKey('cst_reportconfig.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    resultname = Column(String(255))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    excludefromemptyresultscalc = Column(Numeric(1, 0, asdecimal=False))

    cst_reportconfig = relationship('CstReportconfig')


class CstSchoolsubdistrict(Base):
    __tablename__ = 'cst_schoolsubdistricts'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    subdistrictid = Column(Numeric(10, 0, asdecimal=False), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("current_date"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("current_date"))


class CstSqlmapfile(Base):
    __tablename__ = 'cst_sqlmapfiles'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    filename = Column(String(50), index=True)
    filedata = Column(LargeBinary)
    lastmodifiedtime = Column(Numeric(19, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    statecode = Column(String(20))
    configfileid = Column(ForeignKey('cst_configfile.id'), index=True)
    dependencyorder = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))

    cst_configfile = relationship('CstConfigfile')


class CstSubdistrict(Base):
    __tablename__ = 'cst_subdistricts'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    subdistrict_number = Column(String(10), nullable=False)
    subdistrict_name = Column(String(100), nullable=False)
    subdistrict_abbr = Column(String(20))
    subdistrict_address = Column(String(200))
    subdistrict_city = Column(String(100))
    subdistrict_state = Column(String(2))
    subdistrict_zipcode = Column(String(10))
    subdistrict_phone = Column(String(20))
    subdistrict_fax = Column(String(20))
    subdistrict_superintendent = Column(String(100))
    subdistrict_superintendent_phn = Column(String(20))
    subdistrict_superintendent_fax = Column(String(20))
    subdistrict_superintendent_eml = Column(String(50))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("current_date"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("current_date"))


class SSbdCrdcX(CstSubdistrict):
    __tablename__ = 's_sbd_crdc_x'

    cst_subdistrictsid = Column(ForeignKey('cst_subdistricts.id'), primary_key=True)
    coordinatordisability_yn = Column(String(1))
    coordinatordisabilityemail = Column(String(254))
    coordinatordisabilityfirstname = Column(String(35))
    coordinatordisabilitylastname = Column(String(35))
    coordinatordisabilityphone = Column(String(20))
    coordinatorgender_yn = Column(String(1))
    coordinatorgenderemail = Column(String(254))
    coordinatorgenderfirstname = Column(String(35))
    coordinatorgenderlastname = Column(String(35))
    coordinatorgenderphone = Column(String(20))
    coordinatorrace_yn = Column(String(1))
    coordinatorraceemail = Column(String(254))
    coordinatorracefirstname = Column(String(35))
    coordinatorracelastname = Column(String(35))
    coordinatorracephone = Column(String(20))
    desegorderorplan_yn = Column(String(1))
    distanceedenrolled_yn = Column(String(1))
    gedprepprogram_yn = Column(String(1))
    harassmentbullyingpolicy_yn = Column(String(1))
    harassmentbullyingpolicyurl = Column(String(2000))
    harassmentbullyingpolicyurl_yn = Column(String(1))
    kgfulldaycost = Column(String(10))
    kgpartdaycost = Column(String(10))
    lea_id = Column(String(10))
    prekgage0to2_yn = Column(String(1))
    prekgage3to5_yn = Column(String(1))
    prekgagenonidea0to2_yn = Column(String(1))
    prekgagenonidea3_yn = Column(String(1))
    prekgagenonidea4_yn = Column(String(1))
    prekgagenonidea5_yn = Column(String(1))
    prekgeligall_yn = Column(String(1))
    prekgeligidea_yn = Column(String(1))
    prekgeliglowincome_yn = Column(String(1))
    prekgeligtitlei_yn = Column(String(1))
    prekgfulldaycost = Column(String(10))
    prekgpartdaycost = Column(String(10))
    provideskgany_yn = Column(String(1))
    provideskgfullday_yn = Column(String(1))
    provideskgpartday_yn = Column(String(1))
    providesprekgfullday_yn = Column(String(1))
    providesprekgpartday_yn = Column(String(1))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class CstTemplate(Base):
    __tablename__ = 'cst_template'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportconfigid = Column(ForeignKey('cst_reportconfig.id'), index=True)
    sortindex = Column(Numeric(6, 0, asdecimal=False))
    filename = Column(String(50))
    filedata = Column(LargeBinary)
    lastmodifiedtime = Column(Numeric(19, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_reportconfig = relationship('CstReportconfig')


class CstUpdatecyclelock(Base):
    __tablename__ = 'cst_updatecyclelock'

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    counter = Column(Numeric(20, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    srpdelta = Column(Numeric(20, 0, asdecimal=False), server_default=text("0"))
    vlddelta = Column(Numeric(20, 0, asdecimal=False), server_default=text("0"))


class CstVldconfigfile(Base):
    __tablename__ = 'cst_vldconfigfile'
    __table_args__ = (
        Index('cst_vldconfigfile_u2', 'filename', 'configtype', 'statecode', unique=True),
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    filename = Column(String(100), nullable=False)
    configtype = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    statecode = Column(String(20), nullable=False)
    filepath = Column(String(1000), nullable=False)
    lastmodifiedtime = Column(Numeric(20, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class CstVldgroup(Base):
    __tablename__ = 'cst_vldgroup'

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldconfigfileid = Column(ForeignKey('cst_vldconfigfile.id'), nullable=False, index=True)
    groupcode = Column(String(30), nullable=False, unique=True)
    groupname = Column(String(100))
    description = Column(String(1000))
    version = Column(String(20))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldconfigfile = relationship('CstVldconfigfile')


class CstVldgrouprule(Base):
    __tablename__ = 'cst_vldgrouprule'
    __table_args__ = (
        Index('cst_vldgrouprule_u2', 'cst_vldgroupid', 'cst_vldruleid'),
        Index('cst_vldgrouprule_u3', 'cst_vldgroupid', 'sortorder')
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldgroupid = Column(ForeignKey('cst_vldgroup.id'), nullable=False, index=True)
    cst_vldruleid = Column(ForeignKey('cst_vldrule.id'), nullable=False, index=True)
    sortorder = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    listindex = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldgroup = relationship('CstVldgroup')
    cst_vldrule = relationship('CstVldrule')


class CstVldparam(Base):
    __tablename__ = 'cst_vldparam'
    __table_args__ = (
        Index('cst_vldparam_u2', 'cst_vldgroupid', 'paramname'),
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldgroupid = Column(ForeignKey('cst_vldgroup.id'), nullable=False, index=True)
    paramname = Column(String(100), nullable=False)
    paramtype = Column(String(100), nullable=False)
    defaultvalue = Column(String(1000))
    description = Column(String(1000))
    listindex = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldgroup = relationship('CstVldgroup')


class CstVldparamval(Base):
    __tablename__ = 'cst_vldparamval'
    __table_args__ = (
        Index('cst_vldparamval_u2', 'cst_vldresultbygroupid', 'paramname', unique=True),
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldresultbygroupid = Column(ForeignKey('cst_vldresultbygroup.id'), nullable=False, index=True)
    paramname = Column(String(100), nullable=False)
    paramvalue = Column(String(1000))
    defaulted = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldresultbygroup = relationship('CstVldresultbygroup')


class CstVldquery(Base):
    __tablename__ = 'cst_vldquery'
    __table_args__ = (
        Index('cst_vldquery_u2', 'cst_vldruleid', 'queryname'),
        Index('cst_vldquery_u3', 'cst_vldruleid', 'sortorder')
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldruleid = Column(ForeignKey('cst_vldrule.id'), nullable=False, index=True)
    queryname = Column(String(100), nullable=False)
    sortorder = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    schoolcontext = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    querysqlcode = Column(Text, nullable=False)
    description = Column(String(1000))
    listindex = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldrule = relationship('CstVldrule')


class CstVldquerycol(Base):
    __tablename__ = 'cst_vldquerycol'
    __table_args__ = (
        Index('cst_vldquerycol_u2', 'cst_vldqueryid', 'columnname'),
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldqueryid = Column(ForeignKey('cst_vldquery.id'), nullable=False, index=True)
    columnname = Column(String(100), nullable=False)
    columnentitytype = Column(String(100))
    columnidtype = Column(String(100))
    isdeleted = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldquery = relationship('CstVldquery')


class CstVldrecord(Base):
    __tablename__ = 'cst_vldrecord'
    __table_args__ = (
        Index('cst_vldrecord_u2', 'cst_vldresultbyruleid', 'recordnumber', unique=True),
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldresultbyruleid = Column(ForeignKey('cst_vldresultbyrule.id'), nullable=False, index=True)
    recordnumber = Column(Numeric(20, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldresultbyrule = relationship('CstVldresultbyrule')


class CstVldrecordval(Base):
    __tablename__ = 'cst_vldrecordval'
    __table_args__ = (
        Index('cst_vldrecordval_u2', 'cst_vldrecordid', 'columnname', unique=True),
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldrecordid = Column(ForeignKey('cst_vldrecord.id'), nullable=False, index=True)
    columnname = Column(String(100), nullable=False)
    columnvalue = Column(String(100))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    cst_vldquerycolid = Column(Numeric(20, 0, asdecimal=False))

    cst_vldrecord = relationship('CstVldrecord')


class CstVldresultbygroup(Base):
    __tablename__ = 'cst_vldresultbygroup'
    __table_args__ = (
        Index('cst_vldresultbygroup_u2', 'groupcode', 'externalinstanceid'),
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    groupcode = Column(String(30), nullable=False)
    externalinstanceid = Column(Numeric(20, 0, asdecimal=False), nullable=False)
    status = Column(String(50))
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    totaltime = Column(Numeric(20, 0, asdecimal=False))
    errordetail = Column(String(1000))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class CstVldresultbyrule(Base):
    __tablename__ = 'cst_vldresultbyrule'
    __table_args__ = (
        Index('cst_vldresultbyrule_u3', 'cst_vldresultbygroupid', 'sortorder', unique=True),
        Index('cst_vldresultbyrule_u2', 'cst_vldresultbygroupid', 'rulecode', unique=True)
    )

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldresultbygroupid = Column(ForeignKey('cst_vldresultbygroup.id'), nullable=False, index=True)
    rulecode = Column(String(30), nullable=False)
    sortorder = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    status = Column(String(50))
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    totaltime = Column(Numeric(20, 0, asdecimal=False))
    recordcount = Column(Numeric(10, 0, asdecimal=False))
    querylog = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldresultbygroup = relationship('CstVldresultbygroup')


class CstVldrule(Base):
    __tablename__ = 'cst_vldrule'

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldconfigfileid = Column(ForeignKey('cst_vldconfigfile.id'), nullable=False, index=True)
    cst_vldseverityid = Column(ForeignKey('cst_vldseverity.id'), nullable=False, index=True)
    rulecode = Column(String(30), nullable=False, unique=True)
    rulename = Column(String(100))
    description = Column(String(1000))
    recommendedaction = Column(String(1000))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldconfigfile = relationship('CstVldconfigfile')
    cst_vldseverity = relationship('CstVldseverity')


class CstVldseverity(Base):
    __tablename__ = 'cst_vldseverity'

    id = Column(Numeric(20, 0, asdecimal=False), primary_key=True)
    cst_vldconfigfileid = Column(ForeignKey('cst_vldconfigfile.id'), nullable=False, index=True)
    severitycode = Column(String(30), nullable=False, unique=True)
    severityname = Column(String(100))
    description = Column(String(1000))
    rank = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cst_vldconfigfile = relationship('CstVldconfigfile')


class Customdate(Base):
    __tablename__ = 'customdates'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fieldno = Column(Numeric(10, 0, asdecimal=False), index=True)
    keyno = Column(Numeric(10, 0, asdecimal=False), index=True)
    value = Column(DateTime, index=True)


class Customfieldmap(Base):
    __tablename__ = 'customfieldmap'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    canonicalfieldlistid = Column(ForeignKey('canonicalfieldlist.id'), nullable=False, unique=True)
    fieldstabledcid = Column(ForeignKey('fieldstable.dcid'), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    canonicalfieldlist = relationship('Canonicalfieldlist')
    fieldstable = relationship('Fieldstable')


class Customfieldmigrationhistory(Base):
    __tablename__ = 'customfieldmigrationhistory'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    fieldsetname = Column(String(256), nullable=False, unique=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Custominteger(Base):
    __tablename__ = 'customintegers'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fieldno = Column(Numeric(10, 0, asdecimal=False), index=True)
    keyno = Column(Numeric(10, 0, asdecimal=False), index=True)
    value = Column(Numeric(10, 0, asdecimal=False), index=True)


class Customreal(Base):
    __tablename__ = 'customreals'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fieldno = Column(Numeric(10, 0, asdecimal=False), index=True)
    keyno = Column(Numeric(10, 0, asdecimal=False), index=True)
    value = Column(Float, index=True)


class Customtext(Base):
    __tablename__ = 'customtext'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fieldno = Column(Numeric(10, 0, asdecimal=False), index=True)
    keyno = Column(Numeric(10, 0, asdecimal=False), index=True)
    value = Column(Text)


class Customtime(Base):
    __tablename__ = 'customtimes'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fieldno = Column(Numeric(10, 0, asdecimal=False), index=True)
    keyno = Column(Numeric(10, 0, asdecimal=False), index=True)
    value = Column(Numeric(10, 0, asdecimal=False), index=True)


class Customvarchar(Base):
    __tablename__ = 'customvarchars'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fieldno = Column(Numeric(10, 0, asdecimal=False), index=True)
    keyno = Column(Numeric(10, 0, asdecimal=False), index=True)
    value = Column(String(1024), index=True)


class CycleDay(Base):
    __tablename__ = 'cycle_day'
    __table_args__ = (
        Index('cycle_day_n5', 'year_id', 'letter', 'schoolid'),
        Index('cycle_day_n4', 'id', 'letter'),
        Index('cycle_day_u2', 'id', 'dcid', unique=True)
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    year_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    letter = Column(String(2))
    day_number = Column(Numeric(10, 0, asdecimal=False))
    abbreviation = Column(String(3))
    day_name = Column(String(30))
    sortorder = Column(Numeric(10, 0, asdecimal=False), index=True)
    psguid = Column(String(50), unique=True)


class Dailyattendance(Base):
    __tablename__ = 'dailyattendance'
    __table_args__ = (
        Index('dailyattendance_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    attendance_date = Column(DateTime, index=True)
    time_in = Column(Numeric(10, 0, asdecimal=False))
    time_out = Column(Numeric(10, 0, asdecimal=False))
    time_returned = Column(Numeric(10, 0, asdecimal=False))
    attendance_code = Column(String(2))
    comment_value = Column(Text)
    attendance_minutes = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)


class DalxSemaphore(Base):
    __tablename__ = 'dalx_semaphore'

    semaphorename = Column(String(80), primary_key=True)
    server_instanceid = Column(Numeric(scale=0, asdecimal=False))
    dalx_moduleid = Column(Numeric(scale=0, asdecimal=False))


t_dalx_sets = Table(
    'dalx_sets', metadata,
    Column('dalx_moduleid', Numeric(10, 0, asdecimal=False)),
    Column('dalx_selectionname', String(255)),
    Column('dalx_scope', Numeric(10, 0, asdecimal=False)),
    Column('dalx_setobject', LargeBinary)
)


class Datacollevent(Base):
    __tablename__ = 'datacollevent'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(128), nullable=False)
    site_id = Column(String(30), nullable=False)
    server_instance = Column(String(20), nullable=False)
    event_id = Column(String(50), nullable=False, index=True)
    type = Column(String(20), nullable=False)
    aggregated_ts = Column(DateTime)
    description = Column(Text)
    url = Column(String(200))
    params = Column(String(200))
    data = Column(Text)
    school_id = Column(Numeric(scale=0, asdecimal=False))
    severity = Column(String(10), nullable=False)
    exception = Column(Text)
    server_id = Column(String(30))
    version = Column(String(20))
    host_name = Column(String(256))
    ip_address = Column(String(16))
    screenshot = Column(Text)
    created_by = Column(Numeric(scale=0, asdecimal=False))
    created_ts = Column(DateTime)
    user_name = Column(String(30))
    user_email = Column(String(50))
    log_excerpt = Column(Text)


class Dataexporttemplate(Base):
    __tablename__ = 'dataexporttemplate'
    __table_args__ = (
        Index('dataexporttemplate_n1', 'modulename', 'teachersdcid', 'templatename'),
    )

    dataexporttemplateid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    modulename = Column(String(100), nullable=False)
    teachersdcid = Column(ForeignKey('schoolstaff.dcid'))
    templatename = Column(String(110), nullable=False)
    description = Column(String(500))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    issystem = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    schoolstaff = relationship('Schoolstaff')


class Dataexporttemplatefield(Base):
    __tablename__ = 'dataexporttemplatefield'
    __table_args__ = (
        Index('dataexporttemplatefield_u1', 'dataexporttemplateid', 'groupname', 'fieldname', 'label', 'fieldorder', unique=True),
    )

    dataexporttemplatefieldid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dataexporttemplateid = Column(ForeignKey('dataexporttemplate.dataexporttemplateid'), nullable=False, index=True)
    groupname = Column(String(150), nullable=False)
    fieldname = Column(String(150), nullable=False)
    label = Column(String(150), nullable=False)
    fieldorder = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    dataexporttemplate = relationship('Dataexporttemplate')


class Dataexporttemplatefilter(Base):
    __tablename__ = 'dataexporttemplatefilter'

    dataexporttemplatefilterid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dataexporttemplateid = Column(ForeignKey('dataexporttemplate.dataexporttemplateid'), nullable=False, index=True)
    filtername = Column(String(100), nullable=False)
    filtervalue = Column(String(4000))
    filteroperator = Column(String(10), nullable=False)
    isbuiltinfilter = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    dataexporttemplate = relationship('Dataexporttemplate')


class Dataexporttemplateoption(Base):
    __tablename__ = 'dataexporttemplateoption'

    dataexporttemplateoptionid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dataexporttemplateid = Column(ForeignKey('dataexporttemplate.dataexporttemplateid'), nullable=False, index=True)
    option_type = Column(String(20), nullable=False)
    option_name = Column(String(100), nullable=False)
    option_value = Column(String(2000))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    dataexporttemplate = relationship('Dataexporttemplate')


class Dataexporttemplateschedule(Base):
    __tablename__ = 'dataexporttemplateschedule'

    dataexporttemplatescheduleid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dataexporttemplateid = Column(ForeignKey('dataexporttemplate.dataexporttemplateid'), nullable=False, index=True)
    school_number = Column(ForeignKey('schools.school_number'), index=True)
    scheduledaysofweek = Column(String(100), nullable=False)
    scheduletime = Column(DateTime, nullable=False)
    isactive = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0  "))
    isdistrict = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0  "))
    scheduleoutput = Column(String(500), nullable=False)
    scheduleoutputpath = Column(String(500))
    scheduleemail = Column(String(4000))
    schedulestatus = Column(String(100))
    schedulelastruntime = Column(DateTime)
    pluginurlendpointid = Column(ForeignKey('pluginurlendpoint.pluginurlendpointid'), index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    dataexporttemplate = relationship('Dataexporttemplate')
    pluginurlendpoint = relationship('Pluginurlendpoint')
    school = relationship('School')


class Datafailedrecord(Base):
    __tablename__ = 'datafailedrecord'

    datafailedrecordid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dataimportid = Column(ForeignKey('dataimport.dataimportid'), nullable=False, index=True)
    failedrecorddata = Column(LargeBinary)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    dataimport = relationship('Dataimport')


class Dataimport(Base):
    __tablename__ = 'dataimport'

    dataimportid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    modulename = Column(String(100), nullable=False)
    teachersdcid = Column(ForeignKey('schoolstaff.dcid'), index=True)
    school_number = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    filename = Column(String(256), nullable=False)
    totalrecords = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    successrecordcount = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    failurerecordcount = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    statuscode = Column(String(256))
    resultdata = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    schoolstaff = relationship('Schoolstaff')


class Dataimporttemplate(Base):
    __tablename__ = 'dataimporttemplate'
    __table_args__ = (
        Index('dataimporttemplate_u1', 'modulename', 'teachersdcid', 'templatename', unique=True),
    )

    dataimporttemplateid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    modulename = Column(String(100), nullable=False)
    teachersdcid = Column(ForeignKey('schoolstaff.dcid'), nullable=False)
    templatename = Column(String(100), nullable=False)
    description = Column(String(500))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    schoolstaff = relationship('Schoolstaff')


class Dataimporttemplatecolumn(Base):
    __tablename__ = 'dataimporttemplatecolumn'
    __table_args__ = (
        Index('dataimporttemplatecolumn_u1', 'dataimporttemplateid', 'mappedtablename', 'mappedcolumnname', 'columnorder', unique=True),
    )

    dataimporttemplatecolumnid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dataimporttemplateid = Column(ForeignKey('dataimporttemplate.dataimporttemplateid'), nullable=False, index=True)
    mappedtablename = Column(String(150), nullable=False)
    mappedcolumnname = Column(String(150), nullable=False)
    columnorder = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    dataimporttemplate = relationship('Dataimporttemplate')


class Daypart(Base):
    __tablename__ = 'daypart'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(40), nullable=False)
    description = Column(String(256))
    isenabled = Column(Numeric(3, 0, asdecimal=False), server_default=text("1"))
    isvaliddaypart = Column(Numeric(3, 0, asdecimal=False), server_default=text("1"))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class DbObject(Base):
    __tablename__ = 'db_object'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    parent_dbobjectid = Column(Numeric(10, 0, asdecimal=False), index=True)
    audit_yn = Column(Numeric(10, 0, asdecimal=False))
    object_type = Column(String(10))
    object_internal_num = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(40))
    cleanup_freq = Column(String(10))
    write_to_file_yn = Column(Numeric(10, 0, asdecimal=False))
    unused = Column(DateTime)
    unused2 = Column(Numeric(10, 0, asdecimal=False))
    unused3 = Column(String(20))


class DbVersion(Base):
    __tablename__ = 'db_version'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    version = Column(String(16))
    majorversion = Column(String(4))
    minorversion = Column(String(12))
    createddt = Column(DateTime)
    createdby = Column(String(32))


class Dblog(Base):
    __tablename__ = 'dblog'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    type = Column(Numeric(10, 0, asdecimal=False))
    date_value = Column(DateTime, index=True)
    time = Column(Numeric(10, 0, asdecimal=False))
    userid = Column(Numeric(10, 0, asdecimal=False))
    ipaddress = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    tdata = Column(Text)
    code = Column(String(79))
    server_instanceid = Column(Numeric(10, 0, asdecimal=False), index=True)


class Dcfapplication(Base):
    __tablename__ = 'dcfapplication'

    dcfapplicationid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    applicationname = Column(String(2000), nullable=False)
    dataversioncolumn = Column(String(30), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    plugindef = relationship('Plugindef')


class Dcfcolumnmap(Base):
    __tablename__ = 'dcfcolumnmap'

    dcfcolumnmapid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dcftableid = Column(ForeignKey('dcftable.dcftableid'), nullable=False, index=True)
    corecolumn = Column(String(30), nullable=False)
    dcfcolumn = Column(String(28), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    dcftable = relationship('Dcftable')


class Dcftable(Base):
    __tablename__ = 'dcftable'

    dcftableid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    coretable = Column(String(30), nullable=False, unique=True)
    inserttrigger = Column(String(30))
    updatetrigger = Column(String(30))
    deletetrigger = Column(String(30))
    lgtable = Column(String(30))
    lgsequence = Column(String(30))
    lgindexpk = Column(String(30))
    autable = Column(String(30))
    ausequence = Column(String(30))
    auindexpk = Column(String(30))
    auindexfk = Column(String(30))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    dqtable = Column(String(30))
    dqpkcolumn = Column(String(30))
    dqindexcolumn = Column(String(30))


class Demographic(Base):
    __tablename__ = 'demographic'
    __table_args__ = (
        Index('demographic_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    birth_dt = Column(DateTime)
    birth_certificate_num = Column(String(40))
    birth_city = Column(String(80))
    birth_state_cd = Column(String(10))
    birth_country_cd = Column(String(10))
    birth_cert_verify_dt = Column(DateTime)
    citizenship_cd = Column(String(10))
    primary_lang_cd = Column(String(10))
    home_lang_cd = Column(String(10))
    gifted_yn = Column(Numeric(10, 0, asdecimal=False))
    homeless_yn = Column(Numeric(10, 0, asdecimal=False))
    home_schooled_yn = Column(Numeric(10, 0, asdecimal=False))
    migrant_yn = Column(Numeric(10, 0, asdecimal=False))
    single_parent_yn = Column(Numeric(10, 0, asdecimal=False))
    transient_yn = Column(Numeric(10, 0, asdecimal=False))
    ward_of_state_yn = Column(Numeric(10, 0, asdecimal=False))
    immigrant_yn = Column(Numeric(10, 0, asdecimal=False))
    lim_eng_prof = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))
    econom_disadvantaged = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))


class Department(Base):
    __tablename__ = 'department'
    __table_args__ = (
        Index('department_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    description = Column(String(30))
    psguid = Column(String(50), unique=True)


class Dictionarycolumn(Base):
    __tablename__ = 'dictionarycolumn'
    __table_args__ = (
        Index('dictionarycolumn_u2', 'tablename', 'columnname', unique=True),
    )

    dictionarycolumnid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    tableschema = Column(String(30), nullable=False, server_default=text("'PS'    "))
    tablename = Column(ForeignKey('dictionaryobject.objectname'), nullable=False, index=True)
    columnname = Column(String(30), nullable=False, index=True)
    displayname = Column(String(80))
    columndatatype = Column(String(30))
    columnversion = Column(String(30))
    columndescription = Column(String(4000), nullable=False)
    isnolongerused = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    dictionaryobject = relationship('Dictionaryobject')


class Dictionaryobject(Base):
    __tablename__ = 'dictionaryobject'

    dictionaryobjectid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    objectorigin = Column(String(30), nullable=False, server_default=text("'Core'     "))
    objectschema = Column(String(30), nullable=False, server_default=text("'PS'       "))
    objecttype = Column(String(30), nullable=False, server_default=text("'Table'    "))
    objectname = Column(String(30), nullable=False, unique=True)
    displayname = Column(String(80))
    objectnumber = Column(Numeric(6, 0, asdecimal=False))
    objectversion = Column(String(30))
    objectdescription = Column(String(4000), nullable=False)
    isnolongerused = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0            "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER         "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE      "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER         "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE      "))


class Districtbellschedule(Base):
    __tablename__ = 'districtbellschedule'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(30), nullable=False)
    year = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Districtcalendar(Base):
    __tablename__ = 'districtcalendar'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    calendarname = Column(String(50), nullable=False)
    description = Column(String(512), nullable=False)
    calendaryear = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    startdate = Column(DateTime, nullable=False)
    enddate = Column(DateTime, nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Districtcalendarday(Base):
    __tablename__ = 'districtcalendarday'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    districtcalendarid = Column(ForeignKey('districtcalendar.id'), nullable=False, index=True)
    datevalue = Column(DateTime, nullable=False)
    a = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    b = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    c = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    d = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    e = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    f = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    insession = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    membershipvalue = Column(Float, nullable=False)
    note = Column(String(50))
    type = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    districtcycledayid = Column(ForeignKey('districtcycleday.id'), index=True)
    districtbellscheduleid = Column(ForeignKey('districtbellschedule.id'), index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    districtbellschedule = relationship('Districtbellschedule')
    districtcalendar = relationship('Districtcalendar')
    districtcycleday = relationship('Districtcycleday')


class Districtcategory(Base):
    __tablename__ = 'districtcategory'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    isdeleted = Column(Numeric(1, 0, asdecimal=False), index=True, server_default=text("0"))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    isvisible = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))


class Districtcycleday(Base):
    __tablename__ = 'districtcycleday'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    abbreviation = Column(String(3), nullable=False)
    letter = Column(String(2), nullable=False)
    name = Column(String(30), nullable=False)
    year = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


t_districtschoolview = Table(
    'districtschoolview', metadata,
    Column('dcid', Numeric(asdecimal=False)),
    Column('id', Numeric(asdecimal=False)),
    Column('name', String(60)),
    Column('address', Text),
    Column('district_number', Numeric(asdecimal=False)),
    Column('school_number', Numeric(asdecimal=False)),
    Column('pscomm_path', Text),
    Column('low_grade', Numeric(asdecimal=False)),
    Column('high_grade', Numeric(asdecimal=False)),
    Column('sortorder', Numeric(asdecimal=False)),
    Column('abbreviation', String(20)),
    Column('schoolgroup', Numeric(asdecimal=False)),
    Column('custom', Text),
    Column('activecrslist', Text),
    Column('bulletinemail', Text),
    Column('sysemailfrom', Text),
    Column('hist_low_grade', Numeric(asdecimal=False)),
    Column('hist_high_grade', Numeric(asdecimal=False)),
    Column('tchrlogentrto', Text),
    Column('dfltnextschool', Numeric(asdecimal=False)),
    Column('portalid', String(20)),
    Column('view_in_portal', Numeric(asdecimal=False)),
    Column('state_excludefromreporting', Numeric(asdecimal=False)),
    Column('alternate_school_number', Numeric(asdecimal=False)),
    Column('schooladdress', String(79)),
    Column('schoolcity', String(79)),
    Column('schoolstate', String(79)),
    Column('schoolzip', String(79)),
    Column('schoolphone', String(31)),
    Column('schoolfax', String(31)),
    Column('schoolcountry', String(79)),
    Column('principal', String(79)),
    Column('principalphone', String(31)),
    Column('principalemail', String(79)),
    Column('asstprincipalphone', String(31)),
    Column('asstprincipalemail', String(79)),
    Column('countyname', String(79)),
    Column('countynbr', String(79)),
    Column('asstprincipal', String(79)),
    Column('schedulewhichschool', String(10)),
    Column('fee_exemption_status', Numeric(asdecimal=False)),
    Column('schoolinfo_guid', String(32)),
    Column('sif_stateprid', String(32)),
    Column('issummerschool', Numeric(asdecimal=False))
)


class Districtteachercategory(Base):
    __tablename__ = 'districtteachercategory'

    districtteachercategoryid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(4000))
    color = Column(String(30), nullable=False)
    isinfinalgrades = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    isactive = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    isusermodifiable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    displayposition = Column(Numeric(6, 0, asdecimal=False), nullable=False, server_default=text("9999     "))
    defaultscoreentrypoints = Column(Numeric(18, 6))
    defaultextracreditpoints = Column(Numeric(18, 6))
    defaultweight = Column(Numeric(18, 6))
    defaulttotalvalue = Column(Numeric(18, 6))
    defaultpublishstate = Column(String(30))
    defaultpublishoption = Column(String(30))
    isdefaultpublishscores = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    defaultscoretype = Column(String(30))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    defaultdaysbeforedue = Column(Numeric(3, 0, asdecimal=False))


class DmCurrentgrade(Base):
    __tablename__ = 'dm_currentgrade'
    __table_args__ = (
        Index('dm_currentgrade_n1', 'studentid', 'schoolid', 'yearid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    pgfinalgradesdcid = Column(Numeric(10, 0, asdecimal=False))
    gradescaleid = Column(Numeric(10, 0, asdecimal=False))
    gradescaleitemdcid = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False))
    course_number = Column(String(12))
    termsdcid = Column(Numeric(10, 0, asdecimal=False))
    termid = Column(Numeric(10, 0, asdecimal=False))
    storecode = Column(String(10))
    teacherid = Column(Numeric(10, 0, asdecimal=False))
    ccid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))


class DmHistoricalgrade(Base):
    __tablename__ = 'dm_historicalgrade'
    __table_args__ = (
        Index('dm_historicalgrade_n1', 'studentid', 'schoolid', 'yearid'),
        Index('dm_historicalgrade_n2', 'termbinsdcid', 'termsdcid')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    storecode = Column(String(10))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    termid = Column(Numeric(10, 0, asdecimal=False))
    storedgradesdcid = Column(Numeric(10, 0, asdecimal=False))
    termbinsdcid = Column(Numeric(10, 0, asdecimal=False))
    termsdcid = Column(Numeric(10, 0, asdecimal=False))


class DmSchoolenrollment(Base):
    __tablename__ = 'dm_schoolenrollment'
    __table_args__ = (
        Index('dm_schoolenrollment_n1', 'studentid', 'schoolid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sourceid = Column(Numeric(10, 0, asdecimal=False))
    sourcedcid = Column(Numeric(10, 0, asdecimal=False))
    sourcetable = Column(String(13))
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    entrydate = Column(DateTime)
    entrycode = Column(String(20))
    exitdate = Column(DateTime)
    exitcode = Column(String(60))
    grade_level = Column(Numeric(10, 0, asdecimal=False))
    termsdcid = Column(Numeric(10, 0, asdecimal=False))


class DmStandardgrade(Base):
    __tablename__ = 'dm_standardgrade'
    __table_args__ = (
        Index('dm_standardgrade_n1', 'studentid', 'schoolid', 'yearid'),
        Index('dm_standardgrade_n2', 'studentid', 'schoolid', 'yearid')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    psmsectionenrollmentid = Column(Numeric(19, 0, asdecimal=False))
    psmreportcarditemcommentid = Column(Numeric(19, 0, asdecimal=False))
    psmreportcarditemgradeid = Column(Numeric(19, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False))
    section_number = Column(String(10))
    termid = Column(Numeric(10, 0, asdecimal=False))
    psmtermid = Column(Numeric(19, 0, asdecimal=False))
    psmgradescaleid = Column(Numeric(19, 0, asdecimal=False))
    psmstandardid = Column(Numeric(19, 0, asdecimal=False))
    psmparentstandardid = Column(Numeric(19, 0, asdecimal=False))
    psmparentstandardidentifier = Column(String(20))
    standardid = Column(Numeric(10, 0, asdecimal=False))
    standardidentifier = Column(String(20))
    psmreportingtermid = Column(Numeric(19, 0, asdecimal=False))
    storecode = Column(String(30))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    psmsubjectareaid = Column(Numeric(19, 0, asdecimal=False))
    teacherid = Column(Numeric(10, 0, asdecimal=False))
    course_number = Column(String(11))


class Dnldqueue(Base):
    __tablename__ = 'dnldqueue'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    cmdno = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    data = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Docdistrict(Base):
    __tablename__ = 'docdistrict'

    districtid = Column(String(12), primary_key=True)
    quota = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    quotaused = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    rebuildstatus = Column(String(1024))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    perstudentquota = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("10485760 "))
    perdocumentquota = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("1048576 "))
    isperstudentlimitset = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    isperdocumentlimitset = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))


class Docmetadatum(Base):
    __tablename__ = 'docmetadata'
    __table_args__ = (
        Index('docmetadata_n2', 'studentsdcid', 'name'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    docdistrictid = Column(ForeignKey('docdistrict.districtid'), nullable=False, index=True)
    metadata = Column(Text, nullable=False)
    s3path = Column(String(2000), nullable=False, index=True)
    docsize = Column(Numeric(19, 0, asdecimal=False), server_default=text("0"))
    docuid = Column(String(128), nullable=False)
    entitytype = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    studentsdcid = Column(ForeignKey('students.dcid'))
    name = Column(String(2000), nullable=False)
    alias = Column(String(2000))
    uploadstatus = Column(String(30), nullable=False)
    whenuploaded = Column(DateTime, nullable=False, index=True, server_default=text("SYSDATE "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    pluginidentifier = Column(ForeignKey('pluginbackupdata.pluginidentifier'), index=True)

    docdistrict = relationship('Docdistrict')
    pluginbackupdatum = relationship('Pluginbackupdatum')
    student = relationship('Student')


class Docmetadatadistrictcategory(Base):
    __tablename__ = 'docmetadatadistrictcategory'
    __table_args__ = (
        Index('docmetadatadistrictcategory_u1', 'docmetadataid', 'districtcategoryid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    docmetadataid = Column(ForeignKey('docmetadata.id'), nullable=False)
    districtcategoryid = Column(ForeignKey('districtcategory.id'), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    districtcategory = relationship('Districtcategory')
    docmetadatum = relationship('Docmetadatum')


class D(Base):
    __tablename__ = 'ds'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    unused2 = Column(Numeric(10, 0, asdecimal=False))
    lastupdate = Column(DateTime)
    tdata1 = Column(Text)
    tdata2 = Column(Text)
    unused3 = Column(Numeric(10, 0, asdecimal=False))


class DvField(Base):
    __tablename__ = 'dv_fields'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    fldkey = Column(String(256), nullable=False, unique=True)
    fldtable = Column(String(30), nullable=False)
    fldcolumn = Column(String(50), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class DvRule(Base):
    __tablename__ = 'dv_rules'
    __table_args__ = (
        Index('dvrules_u2', 'dvfieldsid', 'dvruletypesid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dvfieldsid = Column(ForeignKey('dv_fields.id'), nullable=False, index=True)
    dvruletypesid = Column(ForeignKey('dv_ruletypes.id'), nullable=False, index=True)
    dvvalue = Column(String(256), nullable=False)
    isdynamic = Column(String(1), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    dv_field = relationship('DvField')
    dv_ruletype = relationship('DvRuletype')


class DvRuletype(Base):
    __tablename__ = 'dv_ruletypes'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    ruletype = Column(String(30), nullable=False, unique=True)
    allowablevalue = Column(String(30), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class DvTextmask(Base):
    __tablename__ = 'dv_textmasks'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    setid = Column(ForeignKey('dv_textmasksets.id'), nullable=False, index=True)
    mask = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    dv_textmaskset = relationship('DvTextmaskset')


class DvTextmaskset(Base):
    __tablename__ = 'dv_textmasksets'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(100), nullable=False)
    message_format = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Emailconfig(Base):
    __tablename__ = 'emailconfig'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    emailqueueid = Column(ForeignKey('emailqueue.id'), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    value = Column(String(256))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    emailqueue = relationship('Emailqueue')


class Emailqueue(Base):
    __tablename__ = 'emailqueue'
    __table_args__ = (
        Index('emailqueue_n3', 'whencreated', 'id'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    componentname = Column(ForeignKey('applicationcomponent.componentname'), index=True)
    emailbody = Column(Text)
    jobstatusid = Column(ForeignKey('jobstatus.id'), index=True)
    emailsubject = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    applicationcomponent = relationship('Applicationcomponent')
    jobstatu = relationship('Jobstatu')


class Emailrecipient(Base):
    __tablename__ = 'emailrecipient'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    emailaddress = Column(Text, nullable=False)
    emaildisplayname = Column(Text)
    emailqueueid = Column(ForeignKey('emailqueue.id'), nullable=False, index=True)
    recipienttype = Column(Numeric(3, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    emailqueue = relationship('Emailqueue')


class Emailsystemconfig(Base):
    __tablename__ = 'emailsystemconfig'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    componentname = Column(ForeignKey('applicationcomponent.componentname'))
    name = Column(String(50), nullable=False)
    value = Column(String(256))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    applicationcomponent = relationship('Applicationcomponent')


class Enterprisereportpage(Base):
    __tablename__ = 'enterprisereportpage'
    __table_args__ = (
        Index('enterprisereportpage_u1', 'apexapplicationid', 'apexpageid', unique=True),
    )

    enterprisereportpageid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(250))
    categorycode = Column(String(50), nullable=False)
    publish = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    apexapplicationid = Column(Numeric(16, 0, asdecimal=False), nullable=False)
    apexpageid = Column(Numeric(16, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))


class Ethnicity(Base):
    __tablename__ = 'ethnicity'
    __table_args__ = (
        Index('ethnicity_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    ethnicity_cd = Column(String(10))
    proportion = Column(Float)
    unused = Column(Numeric(10, 0, asdecimal=False))
    unused2 = Column(String(40))
    unused3 = Column(String(10))
    unused4 = Column(Numeric(10, 0, asdecimal=False))


class Evaluationfactor(Base):
    __tablename__ = 'evaluationfactors'

    studentid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    schoolid = Column(ForeignKey('schools.school_number'), nullable=False, index=True)
    gradeindex = Column(Numeric(5, 2))
    attendanceindex = Column(Numeric(5, 2))
    evaluationindex = Column(Numeric(5, 2))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))

    school = relationship('School')


class Evaluationlevel(Base):
    __tablename__ = 'evaluationlevels'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False)
    pointvalue = Column(Numeric(5, 2), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER      "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER      "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))


class Evaluationmethod(Base):
    __tablename__ = 'evaluationmethods'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False)
    method = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER      "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER      "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))


class Evaluationschoolconfig(Base):
    __tablename__ = 'evaluationschoolconfig'
    __table_args__ = (
        Index('evaluationschoolconfig_u1', 'schoolid', 'evaluationmethodsid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    schoolid = Column(ForeignKey('schools.school_number'), nullable=False)
    evaluationmethodsid = Column(ForeignKey('evaluationmethods.id'), nullable=False)
    interval = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    active = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL"))
    runstatus = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL"))
    rundate = Column(DateTime, server_default=text("NULL"))
    whocreated = Column(String(100), nullable=False, server_default=text("USER      "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER      "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))

    evaluationmethod = relationship('Evaluationmethod')
    school = relationship('School')


class Extschemacustomremap(Base):
    __tablename__ = 'extschemacustomremap'

    coretable = Column(String(32), primary_key=True, nullable=False)
    custname = Column(String(100), primary_key=True, nullable=False)
    exttable = Column(String(32), nullable=False)
    extcolumn = Column(String(32), nullable=False)
    extension = Column(String(256))
    alternatekey = Column(String(30))
    alternatecoretable = Column(String(30))


class Extschemadef(Base):
    __tablename__ = 'extschemadef'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    type = Column(String(1), nullable=False)
    name = Column(String(42), nullable=False, unique=True)
    active = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    version = Column(DateTime)
    source = Column(String(1), server_default=text("'F'"))
    whocreated = Column(String(30))
    whencreated = Column(DateTime)
    whomodified = Column(String(30))
    whenmodified = Column(DateTime)


class Extschemadefasset(Base):
    __tablename__ = 'extschemadefasset'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    extschemadef_id = Column(ForeignKey('extschemadef.id'), nullable=False, index=True)
    psm_asset_id = Column(ForeignKey('psm_asset.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    extschemadef = relationship('Extschemadef')
    psm_asset = relationship('PsmAsset')


class Extschemadeffield(Base):
    __tablename__ = 'extschemadeffield'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    extschematable_id = Column(ForeignKey('extschemadeftable.id'), nullable=False, index=True)
    type = Column(String(1), nullable=False)
    name = Column(String(30), nullable=False)
    length = Column(Numeric(10, 0, asdecimal=False))
    populatefrom = Column(String(100))
    remaps = Column(String(100))
    commentvalue = Column(String(256))
    defaultvalue = Column(String(1000))
    indexed = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(30))
    whencreated = Column(DateTime)
    whomodified = Column(String(30))
    whenmodified = Column(DateTime)
    alternatekey = Column(String(30))
    alternatecoretable = Column(String(30))

    extschematable = relationship('Extschemadeftable')


class Extschemadefforeignkey(Base):
    __tablename__ = 'extschemadefforeignkey'

    id = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    extschemadeftable_id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    constraintname = Column(String(30), primary_key=True, nullable=False)
    fieldname = Column(String(30), primary_key=True, nullable=False)
    parenttable = Column(String(30), nullable=False)
    parentfield = Column(String(30), nullable=False)
    ondeletecascade = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    whocreated = Column(String(30), server_default=text("user"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(30), server_default=text("user"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Extschemadefindex(Base):
    __tablename__ = 'extschemadefindex'

    id = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    extschemadeftable_id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    indexname = Column(String(30), primary_key=True, nullable=False)
    fieldname = Column(String(30), primary_key=True, nullable=False)
    whocreated = Column(String(30), server_default=text("user"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(30), server_default=text("user"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Extschemadeftable(Base):
    __tablename__ = 'extschemadeftable'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    extschemadef_id = Column(ForeignKey('extschemadef.id'), nullable=False, index=True)
    type = Column(String(1), nullable=False)
    coretable = Column(String(30))
    childname = Column(String(30))
    dbtablename = Column(String(30), nullable=False, unique=True)
    foreignkey = Column(String(30))
    coretablepk = Column(String(30))
    commentvalue = Column(String(256))
    whocreated = Column(String(30))
    whencreated = Column(DateTime)
    whomodified = Column(String(30))
    whenmodified = Column(DateTime)
    virtualtablename = Column(String(30))

    extschemadef = relationship('Extschemadef')


class Extschemamigrationissue(Base):
    __tablename__ = 'extschemamigrationissue'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    coretable = Column(String(32), nullable=False)
    coreid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    extension = Column(String(40), nullable=False)
    extcolumn = Column(String(32), nullable=False)
    issuecategory = Column(String(20), nullable=False)
    statusvalue = Column(String(20), nullable=False)
    message = Column(Text)
    sourcedata = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    fieldsetname = Column(String(100))
    issuestate = Column(String(30))


class Facility(Base):
    __tablename__ = 'facility'
    __table_args__ = (
        Index('facility_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    description = Column(String(30))
    roomtype_guid = Column(String(32), index=True)


class Fee(Base):
    __tablename__ = 'fee'
    __table_args__ = (
        Index('fee_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    course_number = Column(String(11), index=True)
    schoolfee_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fee_type_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fee_type_name = Column(String(79))
    creationdate = Column(DateTime)
    modificationdate = Column(DateTime)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    fee_amount = Column(Float)
    fee_balance = Column(Float)
    fee_paid = Column(Float)
    course_name = Column(String(79))
    pro_rated = Column(Numeric(10, 0, asdecimal=False))
    originalfee = Column(Float)
    priority = Column(Numeric(10, 0, asdecimal=False))
    department_name = Column(String(79))
    description = Column(String(79))
    custom = Column(Text)
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    date_value = Column(DateTime)
    time = Column(Numeric(10, 0, asdecimal=False))
    datetime = Column(String(15))
    fee_category_name = Column(String(21))
    system_user_id = Column(Numeric(10, 0, asdecimal=False))
    group_transaction_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    termid = Column(Numeric(10, 0, asdecimal=False))
    internal_info_for_trigger = Column(Numeric(10, 0, asdecimal=False))
    adjustment = Column(Float)
    feecharged = Column(Float)


class FeeBalance(Base):
    __tablename__ = 'fee_balance'
    __table_args__ = (
        Index('fee_balance_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    debit = Column(Float)
    credit = Column(Float)
    balance = Column(Float)


class FeeTransaction(Base):
    __tablename__ = 'fee_transaction'
    __table_args__ = (
        Index('fee_transaction_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    feeid = Column(Numeric(10, 0, asdecimal=False), index=True)
    date_value = Column(DateTime)
    time = Column(Numeric(10, 0, asdecimal=False))
    datetime = Column(String(15))
    amount = Column(Float)
    starting_balance = Column(Float)
    neteffect = Column(Float)
    payment_method = Column(String(11))
    system_user_id = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    description = Column(String(79))
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    payment_ref_nbr = Column(String(79))
    group_transaction_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    receipt_nbr = Column(String(79))
    transaction_type = Column(String(13))
    global_starting_balance = Column(Float)
    global_neteffect = Column(Float)
    internal_info_for_trigger = Column(Numeric(10, 0, asdecimal=False))


class FeeType(Base):
    __tablename__ = 'fee_type'
    __table_args__ = (
        Index('fee_type_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(50))
    fee_category_name = Column(String(50))
    priority = Column(Numeric(10, 0, asdecimal=False))
    description = Column(Text)
    custom = Column(Text)
    creationdate = Column(DateTime)
    modificationdate = Column(DateTime)


class Fee(Base):
    __tablename__ = 'fees'
    __table_args__ = (
        Index('fees_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    feestype = Column(String(20), index=True)
    date_value = Column(DateTime, index=True)
    description = Column(Text)
    time = Column(Numeric(10, 0, asdecimal=False))
    enteredby = Column(Numeric(10, 0, asdecimal=False))
    credit = Column(Float)
    debit = Column(Float)
    neteffect = Column(Float)
    cash = Column(Float)
    course_number = Column(String(11))
    yearid = Column(Numeric(10, 0, asdecimal=False))


class Fieldlevelsecurity(Base):
    __tablename__ = 'fieldlevelsecurity'

    fieldlevelsecurityid = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text("0 "))
    fieldname = Column(String(30), nullable=False)
    tablename = Column(String(30), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    isextension = Column(Numeric(1, 0, asdecimal=False))
    useinpages = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))


class Fieldstable(Base):
    __tablename__ = 'fieldstable'
    __table_args__ = (
        Index('fieldstable_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    fileno = Column(Numeric(10, 0, asdecimal=False), index=True)
    fieldno = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(50))
    type = Column(Numeric(10, 0, asdecimal=False))
    minval = Column(String(20))
    maxval = Column(String(20))
    minlen = Column(Numeric(10, 0, asdecimal=False))
    maxlen = Column(Numeric(10, 0, asdecimal=False))
    data = Column(Text)
    required = Column(Numeric(10, 0, asdecimal=False))
    cols = Column(Numeric(10, 0, asdecimal=False))
    rowsvalue = Column(Numeric(10, 0, asdecimal=False))
    defaultvalue = Column(String(50))
    dispname = Column(String(40))
    dataindex = Column(Numeric(10, 0, asdecimal=False))
    datalen = Column(Numeric(10, 0, asdecimal=False))
    html = Column(Text)
    formatstring = Column(String(20))
    inuse = Column(Numeric(10, 0, asdecimal=False))
    howdisp = Column(Numeric(10, 0, asdecimal=False))
    help = Column(Text)
    colno = Column(Numeric(10, 0, asdecimal=False), index=True)
    description = Column(Text)
    inputfilter = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    syncstatus = Column(Numeric(10, 0, asdecimal=False))


class Fieldtypechangerequest(Base):
    __tablename__ = 'fieldtypechangerequest'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    field_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    requestdate = Column(DateTime)
    requesttype = Column(Numeric(10, 0, asdecimal=False))
    implementationdate = Column(DateTime, index=True)
    minlen = Column(Numeric(10, 0, asdecimal=False))
    maxlen = Column(Numeric(10, 0, asdecimal=False))
    minval = Column(String(10))
    maxval = Column(String(20))
    who_created = Column(String(30))
    when_created = Column(DateTime)
    who_modified = Column(String(30))
    when_modified = Column(DateTime)


class Finalgradeattrib(Base):
    __tablename__ = 'finalgradeattrib'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    earnedvarcreditvalue = Column(Numeric(18, 6))
    pgfinalgradesdcid = Column(ForeignKey('pgfinalgrades.dcid'), nullable=False, unique=True)
    potentialvarcreditvalue = Column(Numeric(18, 6))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    pgfinalgrade = relationship('Pgfinalgrade')


class Fte(Base):
    __tablename__ = 'fte'
    __table_args__ = (
        Index('fte_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    fte_value = Column(Float)
    name = Column(String(80))
    description = Column(Text)
    dflt_att_mode_code = Column(String(13))
    dflt_conversion_mode_code = Column(String(11))


class FteGrade(Base):
    __tablename__ = 'fte_grade'
    __table_args__ = (
        Index('fte_grade_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    fteid = Column(Numeric(10, 0, asdecimal=False), index=True)
    grade_level = Column(Numeric(10, 0, asdecimal=False), index=True)


class Gen(Base):
    __tablename__ = 'gen'
    __table_args__ = (
        Index('gen_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    cat = Column(String(15), index=True)
    name = Column(String(50), index=True)
    value = Column(String(40))
    valuet = Column(Text)
    value2 = Column(String(40))
    valueli = Column(Numeric(10, 0, asdecimal=False))
    valueli2 = Column(Numeric(10, 0, asdecimal=False))
    valuer = Column(Float)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    valuet2 = Column(Text)
    custom = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    powerlink = Column(String(40))
    powerlinkspan = Column(String(60))
    valueli3 = Column(Numeric(10, 0, asdecimal=False))
    valuer2 = Column(Float)
    date_value = Column(DateTime)
    date2 = Column(DateTime)
    time1 = Column(Numeric(10, 0, asdecimal=False))
    time2 = Column(Numeric(10, 0, asdecimal=False))
    spedindicator = Column(Numeric(10, 0, asdecimal=False))
    log = Column(Text)
    valueli4 = Column(Numeric(10, 0, asdecimal=False))
    value_x = Column(LargeBinary)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    psguid = Column(String(50), unique=True)


class SGenNceaX(Gen):
    __tablename__ = 's_gen_ncea_x'

    gendcid = Column(ForeignKey('gen.dcid'), primary_key=True)
    racecodemap = Column(String(5))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


t_gen_tt_10422 = Table(
    'gen_tt_10422', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('cat', String(15)),
    Column('name', String(50)),
    Column('value', String(40)),
    Column('valuet', Text),
    Column('value2', String(40)),
    Column('valueli', Numeric(10, 0, asdecimal=False)),
    Column('valueli2', Numeric(10, 0, asdecimal=False)),
    Column('valuer', Float),
    Column('sortorder', Numeric(10, 0, asdecimal=False)),
    Column('valuet2', Text),
    Column('custom', Text),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('powerlink', String(40)),
    Column('powerlinkspan', String(60)),
    Column('valueli3', Numeric(10, 0, asdecimal=False)),
    Column('valuer2', Float),
    Column('date_value', DateTime),
    Column('date2', DateTime),
    Column('time1', Numeric(10, 0, asdecimal=False)),
    Column('time2', Numeric(10, 0, asdecimal=False)),
    Column('spedindicator', Numeric(10, 0, asdecimal=False)),
    Column('log', Text),
    Column('valueli4', Numeric(10, 0, asdecimal=False)),
    Column('value_x', LargeBinary),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('psguid', String(50))
)


class Gldetail(Base):
    __tablename__ = 'gldetail'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    date_value = Column(DateTime, index=True)
    time = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(80))
    debit = Column(Float)
    credit = Column(Float)
    transtype = Column(String(20), index=True)
    enteredby = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    cash = Column(Float)
    neteffect = Column(Float)
    mealprice = Column(Float)
    batch = Column(Numeric(10, 0, asdecimal=False), index=True)
    alacarte = Column(Float)


class Gpexpectation(Base):
    __tablename__ = 'gpexpectation'
    __table_args__ = (
        Index('gpexpectation_uk1', 'gradplanid', 'yearstograd', 'name', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gradplanid = Column(ForeignKey('gradplan.id'), nullable=False)
    yearstograd = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    name = Column(String(80), nullable=False)

    gradplan = relationship('Gradplan')


class Gpexpectationitem(Base):
    __tablename__ = 'gpexpectationitem'
    __table_args__ = (
        Index('gpexpectationitem_uk1', 'gpexpectationid', 'gpnodeid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gpexpectationid = Column(ForeignKey('gpexpectation.id'), nullable=False)
    gpnodeid = Column(ForeignKey('gpnode.id'), nullable=False)
    expectation = Column(Numeric(10, 4), nullable=False)

    gpexpectation = relationship('Gpexpectation')
    gpnode = relationship('Gpnode')


class Gpnode(Base):
    __tablename__ = 'gpnode'
    __table_args__ = (
        Index('gpnode_uk_name', 'gpversionid', 'parentid', 'name', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gpversionid = Column(ForeignKey('gpversion.id'), nullable=False)
    parentid = Column(ForeignKey('gpnode.id'))
    name = Column(String(80), nullable=False)
    sortorder = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    creditcapacity = Column(Numeric(15, 10))
    ishidden = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    allowwaiver = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    allowanyof = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    gpversion = relationship('Gpversion')
    parent = relationship('Gpnode', remote_side=[id])


class Gpprogresssubject(Base):
    __tablename__ = 'gpprogresssubject'
    __table_args__ = (
        Index('gpprogresssubject_u1', 'studentsdcid', 'gpnodeid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False)
    gpnodeid = Column(ForeignKey('gpnode.id'), nullable=False, index=True)
    requestedcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    enrolledcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    earnedcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    waivedcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    appliedwaivedcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    requiredcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gpnode = relationship('Gpnode')
    student = relationship('Student')


class Gpprogresssubjectearned(Base):
    __tablename__ = 'gpprogresssubjectearned'
    __table_args__ = (
        Index('gpprogresssubjectearned_u1', 'storedgradesdcid', 'gpprogresssubjectid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gpprogresssubjectid = Column(ForeignKey('gpprogresssubject.id'), nullable=False, index=True)
    storedgradesdcid = Column(ForeignKey('storedgrades.dcid'), nullable=False)
    coursenumber = Column(String(11))
    earnedcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    lettergrade = Column(String(7))
    percentgrade = Column(Float)
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gpprogresssubject = relationship('Gpprogresssubject')
    storedgrade = relationship('Storedgrade')


class Gpprogresssubjectenrolled(Base):
    __tablename__ = 'gpprogresssubjectenrolled'
    __table_args__ = (
        Index('gpprogresssubjectenrolled_u1', 'ccdcid', 'gpprogresssubjectid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gpprogresssubjectid = Column(ForeignKey('gpprogresssubject.id'), nullable=False, index=True)
    ccdcid = Column(ForeignKey('cc.dcid'), nullable=False)
    coursenumber = Column(String(11))
    enrolledcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    cc = relationship('Cc')
    gpprogresssubject = relationship('Gpprogresssubject')


class Gpprogresssubjectrequested(Base):
    __tablename__ = 'gpprogresssubjectrequested'
    __table_args__ = (
        Index('gpprogresssubjectrequested_u1', 'schedulerequestsdcid', 'gpprogresssubjectid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gpprogresssubjectid = Column(ForeignKey('gpprogresssubject.id'), nullable=False, index=True)
    schedulerequestsdcid = Column(ForeignKey('schedulerequests.dcid'), nullable=False)
    coursenumber = Column(String(11))
    requestedcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gpprogresssubject = relationship('Gpprogresssubject')
    schedulerequest = relationship('Schedulerequest')


class Gpprogresssubjectwaived(Base):
    __tablename__ = 'gpprogresssubjectwaived'
    __table_args__ = (
        Index('gpprogresssubjectwaived_u1', 'gpstudentwaiverid', 'gpprogresssubjectid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gpprogresssubjectid = Column(ForeignKey('gpprogresssubject.id'), nullable=False, index=True)
    gpstudentwaiverid = Column(ForeignKey('gpstudentwaiver.id'), nullable=False)
    waivedcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gpprogresssubject = relationship('Gpprogresssubject')
    gpstudentwaiver = relationship('Gpstudentwaiver')


class Gpprogresssubjwaivedapplied(Base):
    __tablename__ = 'gpprogresssubjwaivedapplied'
    __table_args__ = (
        Index('gpprogresssubjwaivedapplied_u1', 'gpstudentwaiverid', 'gpprogresssubjectid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gpprogresssubjectid = Column(ForeignKey('gpprogresssubject.id'), nullable=False, index=True)
    gpstudentwaiverid = Column(ForeignKey('gpstudentwaiver.id'), nullable=False)
    appliedcredits = Column(Numeric(15, 10), server_default=text("""\
0
          """))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gpprogresssubject = relationship('Gpprogresssubject')
    gpstudentwaiver = relationship('Gpstudentwaiver')


class Gpprogresstest(Base):
    __tablename__ = 'gpprogresstest'
    __table_args__ = (
        Index('gpprogresstest_u1', 'gptestconfigid', 'studentsdcid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    gptestconfigid = Column(ForeignKey('gptestconfig.id'), nullable=False)
    gpstudenttestwaiverid = Column(ForeignKey('gpstudenttestwaiver.id'), index=True)
    status = Column(Numeric(5, 0, asdecimal=False), server_default=text("""\
0
          """))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gpstudenttestwaiver = relationship('Gpstudenttestwaiver')
    gptestconfig = relationship('Gptestconfig')
    student = relationship('Student')


class Gpselectedcr(Base):
    __tablename__ = 'gpselectedcrs'
    __table_args__ = (
        Index('gpselectedcrs_uk_crit_course', 'gpselectorid', 'coursenumber', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gpselectorid = Column(ForeignKey('gpselector.id'), nullable=False)
    coursenumber = Column(String(20), nullable=False)

    gpselector = relationship('Gpselector')


class Gpselectedcrtype(Base):
    __tablename__ = 'gpselectedcrtype'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gpselectorid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    credittype = Column(String(20), nullable=False)


class Gpselector(Base):
    __tablename__ = 'gpselector'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gpversionid = Column(ForeignKey('gpversion.id'), nullable=False, index=True)
    description = Column(String(80))
    sortorder = Column(Numeric(10, 0, asdecimal=False), nullable=False)

    gpversion = relationship('Gpversion')


class Gpstudentplan(Base):
    __tablename__ = 'gpstudentplan'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    gpversionid = Column(ForeignKey('gpversion.id'), nullable=False, index=True)
    sortorder = Column(Numeric(4, 0, asdecimal=False), nullable=False)

    gpversion = relationship('Gpversion')


class Gpstudenttestwaiver(Base):
    __tablename__ = 'gpstudenttestwaiver'
    __table_args__ = (
        Index('gpstudenttestwaiver_u1', 'studentsdcid', 'gptestconfigid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False)
    gptestconfigid = Column(ForeignKey('gptestconfig.id'), nullable=False, index=True)
    gpwaiverconfigidfortype = Column(ForeignKey('gpwaiverconfig.id'), nullable=False, index=True)
    gpwaiverconfigidforsource = Column(Numeric(19, 0, asdecimal=False), index=True)
    gpwaiverconfigidforreason = Column(Numeric(19, 0, asdecimal=False), index=True)
    waiveddate = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    authorizedby = Column(String(100))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gptestconfig = relationship('Gptestconfig')
    gpwaiverconfig = relationship('Gpwaiverconfig')
    student = relationship('Student')


class Gpstudentwaiver(Base):
    __tablename__ = 'gpstudentwaiver'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    gpnodeidforwaived = Column(ForeignKey('gpnode.id'), nullable=False, index=True)
    gpnodeidforelective = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    gpwaiverconfigidfortype = Column(ForeignKey('gpwaiverconfig.id'), nullable=False, index=True)
    gpwaiverconfigidforsource = Column(Numeric(19, 0, asdecimal=False), index=True)
    gpwaiverconfigidforreason = Column(Numeric(19, 0, asdecimal=False), index=True)
    credithourswaived = Column(Numeric(15, 10), nullable=False)
    waiveddate = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    authorizedby = Column(String(100))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gpnode = relationship('Gpnode')
    gpwaiverconfig = relationship('Gpwaiverconfig')


class Gptarget(Base):
    __tablename__ = 'gptarget'
    __table_args__ = (
        Index('gptarget_uk2', 'gpselectorid', 'gpnodeid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gpselectorid = Column(ForeignKey('gpselector.id'), nullable=False)
    sortorder = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    gpnodeid = Column(ForeignKey('gpnode.id'), nullable=False)

    gpnode = relationship('Gpnode')
    gpselector = relationship('Gpselector')


class Gptestconfig(Base):
    __tablename__ = 'gptestconfig'
    __table_args__ = (
        Index('gptestconfig_u1', 'testdcid', 'gpversionid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    testdcid = Column(ForeignKey('test.dcid'), nullable=False)
    gpversionid = Column(ForeignKey('gpversion.id'), nullable=False, index=True)
    allowwaiver = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gpversion = relationship('Gpversion')
    test = relationship('Test')


class Gptestscoreconfig(Base):
    __tablename__ = 'gptestscoreconfig'
    __table_args__ = (
        Index('gptestscoreconfig_u1', 'gptestconfigid', 'testscoredcid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gptestconfigid = Column(ForeignKey('gptestconfig.id'), nullable=False)
    testscoredcid = Column(ForeignKey('testscore.dcid'), nullable=False, index=True)
    passnumscore = Column(Float)
    passpercentscore = Column(Float)
    passalphascore = Column(String(20))
    numscoreop = Column(Numeric(1, 0, asdecimal=False))
    percentscoreop = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gptestconfig = relationship('Gptestconfig')
    testscore = relationship('Testscore')


class Gpversion(Base):
    __tablename__ = 'gpversion'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gradplanid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    startyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    endyear = Column(Numeric(4, 0, asdecimal=False), nullable=False)


class Gpwaiverconfig(Base):
    __tablename__ = 'gpwaiverconfig'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    code = Column(String(100))
    name = Column(String(100))
    description = Column(String(512))
    allowreport = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    type = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Gradecalcdroplowscore(Base):
    __tablename__ = 'gradecalcdroplowscore'

    gradecalcdroplowscoreid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    gradecalculationtypeid = Column(ForeignKey('gradecalculationtype.gradecalculationtypeid'), nullable=False, index=True)
    teachercategoryid = Column(ForeignKey('teachercategory.teachercategoryid'), index=True)
    districtteachercategoryid = Column(ForeignKey('districtteachercategory.districtteachercategoryid'), index=True)
    droplowscorecount = Column(Numeric(3, 0, asdecimal=False), server_default=text("1            "))
    groupindicator = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    districtteachercategory = relationship('Districtteachercategory')
    gradecalculationtype = relationship('Gradecalculationtype')
    teachercategory = relationship('Teachercategory')


class Gradecalcformulaweight(Base):
    __tablename__ = 'gradecalcformulaweight'

    gradecalcformulaweightid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    gradecalculationtypeid = Column(ForeignKey('gradecalculationtype.gradecalculationtypeid'), nullable=False, index=True)
    storecode = Column(String(10))
    teachercategoryid = Column(ForeignKey('teachercategory.teachercategoryid'), index=True)
    districtteachercategoryid = Column(ForeignKey('districtteachercategory.districtteachercategoryid'), index=True)
    assignmentid = Column(ForeignKey('assignment.assignmentid'), index=True)
    weight = Column(Numeric(10, 4), server_default=text("1.0          "))
    type = Column(String(30), server_default=text("'Total_Points' "))
    stndcalculationmetric = Column(String(30), server_default=text("NULL         "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    assignment = relationship('Assignment')
    districtteachercategory = relationship('Districtteachercategory')
    gradecalculationtype = relationship('Gradecalculationtype')
    teachercategory = relationship('Teachercategory')


class Gradecalcschoolassoc(Base):
    __tablename__ = 'gradecalcschoolassoc'
    __table_args__ = (
        Index('gradecalcschoolassoc_u1', 'gradecalculationtypeid', 'schoolsdcid', unique=True),
    )

    gradecalcschoolassocid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    gradecalculationtypeid = Column(ForeignKey('gradecalculationtype.gradecalculationtypeid'), nullable=False, index=True)
    schoolsdcid = Column(ForeignKey('schools.dcid'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradecalculationtype = relationship('Gradecalculationtype')
    school = relationship('School')


class Gradecalculationtype(Base):
    __tablename__ = 'gradecalculationtype'
    __table_args__ = (
        Index('gradecalculationtype_n2', 'gradeformulasetid', 'abbreviation', 'yearid'),
    )

    gradecalculationtypeid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    gradeformulasetid = Column(ForeignKey('gradeformulaset.gradeformulasetid'), nullable=False, index=True)
    abbreviation = Column(String(6), nullable=False)
    storecode = Column(String(10), nullable=False)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    type = Column(String(30), server_default=text("'Total_Points'     "))
    isnograde = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isdroplowstudentfavor = Column(Numeric(1, 0, asdecimal=False), server_default=text("0            "))
    isalternatepointsused = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    droplowscoreoption = Column(String(30), server_default=text("'None'     "))
    iscalcformulaeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    isdropscoreeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradeformulaset = relationship('Gradeformulaset')


class Gradecourseconfig(Base):
    __tablename__ = 'gradecourseconfig'

    gradecourseconfigid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    coursesdcid = Column(ForeignKey('courses.dcid'), nullable=False, index=True)
    gradeformulasetid = Column(ForeignKey('gradeformulaset.gradeformulasetid'), index=True)
    defaultdecimalcount = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    defaultroundingrule = Column(String(30), server_default=text("NULL         "))
    iscalcformulaeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    isdropscoreeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    iscalcprecisioneditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    stndcalculationmetric = Column(String(30), server_default=text("NULL         "))
    isstndcalcmeteditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    recentscoreweightlist = Column(String(400), server_default=text("NULL         "))
    isstndrcntscoreeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    ishigherstndautocalc = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    ishigherstndcalceditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    higherlevelstndmetric = Column(String(30), server_default=text("NULL         "))
    ishigherlvlstndeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    calcmetriccoursefromstnd = Column(String(30), server_default=text("NULL         "))
    iscalccrsfrmstndeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    course = relationship('Course')
    gradeformulaset = relationship('Gradeformulaset')


class Gradeformulaset(Base):
    __tablename__ = 'gradeformulaset'
    __table_args__ = (
        Index('gradeformulaset_u1', 'sectionsdcid', 'yearid', unique=True),
    )

    gradeformulasetid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    name = Column(String(30), nullable=False)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    description = Column(String(4000))
    iscoursegradecalculated = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    isavailgeneraluse = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isavailgenasdefault = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isavailgenanycourse = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isavailspecstndcourse = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isreporttermsetupsame = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    sectionsdcid = Column(ForeignKey('sections.dcid'))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    section = relationship('Section')


class Gradepolicystorecode(Base):
    __tablename__ = 'gradepolicystorecodes'
    __table_args__ = (
        Index('gradepolicystorecodes_u1', 'gradereplacementpolicyid', 'storecode', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gradereplacementpolicyid = Column(ForeignKey('gradereplacementpolicy.id'), nullable=False)
    storecode = Column(String(20), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gradereplacementpolicy = relationship('Gradereplacementpolicy')


class Gradereplacementpolicy(Base):
    __tablename__ = 'gradereplacementpolicy'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(256))
    allowsuppressioninsameterm = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    lowthreshold = Column(Float)
    highthreshold = Column(Float)
    includeaddedvalue = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    replace_excludefromtranscripts = Column(Numeric(1, 0, asdecimal=False))
    replace_excludefromgpa = Column(Numeric(1, 0, asdecimal=False))
    replace_excludefromclassrank = Column(Numeric(1, 0, asdecimal=False))
    replace_excludefromhonorroll = Column(Numeric(1, 0, asdecimal=False))
    maxcr_excludefromtranscripts = Column(Numeric(1, 0, asdecimal=False))
    maxcr_excludefromgpa = Column(Numeric(1, 0, asdecimal=False))
    maxcr_excludefromclassrank = Column(Numeric(1, 0, asdecimal=False))
    maxcr_excludefromhonorroll = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Gradescaleitem(Base):
    __tablename__ = 'gradescaleitem'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    gradescaleid = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(50))
    description = Column(String(4000))
    gradescaletype = Column(String(30), nullable=False)
    isforcoursegrade = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    isforstandards = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    isgpashown = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    countsingpa = Column(Numeric(10, 0, asdecimal=False))
    displayposition = Column(Numeric(6, 0, asdecimal=False))
    grade_points = Column(Float)
    addedvalue = Column(Numeric(10, 0, asdecimal=False))
    graduationcredit = Column(Numeric(10, 0, asdecimal=False))
    teacherscale = Column(Numeric(10, 0, asdecimal=False))
    cutoffpercentage = Column(Float)
    value = Column(Float)
    colorlevels = Column(Numeric(6, 0, asdecimal=False))
    color = Column(String(30))
    isproficient = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    isscorecodeonassignments = Column(Numeric(1, 0, asdecimal=False))
    modify_code = Column(Numeric(10, 0, asdecimal=False))
    numericmin = Column(Numeric(10, 0, asdecimal=False))
    numericmax = Column(Numeric(10, 0, asdecimal=False))
    numericextras = Column(String(30))
    numericdecimals = Column(Numeric(10, 0, asdecimal=False))
    numericcutoff = Column(Numeric(18, 6))
    numericvalue = Column(Numeric(18, 6))
    conversiontonumeric = Column(String(30))
    hasspecialgrades = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    specialgradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    hasrelatedscales = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    altconvertgradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    altfinalnumericcutoff = Column(Numeric(18, 6))
    altfinalnumericrange = Column(String(30))
    istermweightingshown = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    alt_grade_points = Column(Float)
    cutoffpoints = Column(Float)
    excludefromafg = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50))
    grade_replacement_policy = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    parent = relationship('Gradescaleitem', remote_side=[dcid], primaryjoin='Gradescaleitem.altconvertgradescaledcid == Gradescaleitem.dcid')
    parent1 = relationship('Gradescaleitem', remote_side=[dcid], primaryjoin='Gradescaleitem.specialgradescaledcid == Gradescaleitem.dcid')


class GradescaleitemBackup(Base):
    __tablename__ = 'gradescaleitem_backup'
    __table_args__ = (
        Index('gradescaleitem_u2_bk', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    gradescaleid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(50))
    description = Column(Text)
    countsingpa = Column(Numeric(10, 0, asdecimal=False))
    graduationcredit = Column(Numeric(10, 0, asdecimal=False))
    teacherscale = Column(Numeric(10, 0, asdecimal=False))
    cutoffpercentage = Column(Float)
    powerlink = Column(String(40))
    powerlinkspanish = Column(String(40))
    grade_points = Column(Float)
    value = Column(Float)
    addedvalue = Column(Numeric(10, 0, asdecimal=False))
    modify_code = Column(Numeric(10, 0, asdecimal=False))
    excludefromafg = Column(Numeric(10, 0, asdecimal=False))
    alt_grade_points = Column(Float)
    cutoffpoints = Column(Float)
    psguid = Column(String(50), unique=True)
    grade_replacement_policy = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))


class Gradescalerelated(Base):
    __tablename__ = 'gradescalerelated'

    gradescalerelatedid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    maingradescaleitemdcid = Column(ForeignKey('gradescaleitem.dcid'), nullable=False, index=True)
    relatedgradescaleitemdcid = Column(ForeignKey('gradescaleitem.dcid'), nullable=False, index=True)
    isusedforassignments = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isusedforspecificstudent = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    isaltcutoffpercentdisplayed = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradescaleitem = relationship('Gradescaleitem', primaryjoin='Gradescalerelated.maingradescaleitemdcid == Gradescaleitem.dcid')
    gradescaleitem1 = relationship('Gradescaleitem', primaryjoin='Gradescalerelated.relatedgradescaleitemdcid == Gradescaleitem.dcid')


class Gradescalescorecode(Base):
    __tablename__ = 'gradescalescorecode'

    gradescalescorecodeid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(4000))
    gradescaleitemdcid = Column(ForeignKey('gradescaleitem.dcid'), nullable=False, index=True)
    islate = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    iscollected = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    isexempt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    ismissing = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    isabsent = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    isincomplete = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    percentvalue = Column(Numeric(18, 6))
    numerictype = Column(String(30))
    numericvalue = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradescaleitem = relationship('Gradescaleitem')


class Gradescalesectionstudent(Base):
    __tablename__ = 'gradescalesectionstudent'

    gradescalesectionstudentid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    sectionsdcid = Column(ForeignKey('sections.dcid'), nullable=False, index=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    gradescaleitemdcid = Column(ForeignKey('gradescaleitem.dcid'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradescaleitem = relationship('Gradescaleitem')
    section = relationship('Section')
    student = relationship('Student')


class Gradeschoolconfig(Base):
    __tablename__ = 'gradeschoolconfig'
    __table_args__ = (
        Index('gradeschoolconfig_u2', 'schoolsdcid', 'yearid', unique=True),
    )

    gradeschoolconfigid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    schoolsdcid = Column(ForeignKey('schools.dcid'), nullable=False, index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    gradecalcpreferenceorder = Column(String(30), nullable=False, server_default=text("'School'       "))
    defaultdecimalcount = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0                "))
    defaultroundingrule = Column(String(30), nullable=False, server_default=text("'Round'        "))
    iscalcformulaeditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    isdropscoreeditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    iscalcprecisioneditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    calculationmetric = Column(String(30), nullable=False, server_default=text("'Most_Recent'  "))
    iscalcmetriceditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    isrecentscoreeditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    ishigherstndautocalc = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0                "))
    ishigherstndcalceditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    higherlevelstndmetric = Column(String(30), nullable=False, server_default=text("'Mean'         "))
    ishighstandardeditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    recentscoreweightlist = Column(String(400), nullable=False, server_default=text("'1,1,1'        "))
    calcmetricschoolfromstd = Column(String(30), nullable=False, server_default=text("'Mean'         "))
    iscalcmetricschooledit = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    sectionnames = Column(String(30), nullable=False, server_default=text("'PeriodAndDay' "))
    isstandardsshown = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    isstandardsshownonasgmt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    istraditionalgradeshown = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    standardtraditionalorder = Column(String(30), nullable=False, server_default=text("'TraditionalFirst' "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER             "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE          "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER             "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE          "))
    iscitizenshipdisplayed = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    school = relationship('School')


class Gradeschoolformulaassoc(Base):
    __tablename__ = 'gradeschoolformulaassoc'
    __table_args__ = (
        Index('gradeschoolformulaassoc_u2', 'gradeformulasetid', 'gradeschoolconfigid', unique=True),
    )

    gradeschoolformulaassocid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    gradeformulasetid = Column(ForeignKey('gradeformulaset.gradeformulasetid'), nullable=False, index=True)
    gradeschoolconfigid = Column(ForeignKey('gradeschoolconfig.gradeschoolconfigid'), nullable=False, index=True)
    isdefaultformulaset = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradeformulaset = relationship('Gradeformulaset')
    gradeschoolconfig = relationship('Gradeschoolconfig')


class Gradesectionconfig(Base):
    __tablename__ = 'gradesectionconfig'
    __table_args__ = (
        Index('gradesectionconfig_u2', 'sectionsdcid', 'type', unique=True),
    )

    gradesectionconfigid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    sectionsdcid = Column(ForeignKey('sections.dcid'), nullable=False, index=True)
    gradeformulasetid = Column(ForeignKey('gradeformulaset.gradeformulasetid'), index=True)
    type = Column(String(30), nullable=False)
    defaultdecimalcount = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    defaultroundingrule = Column(String(30), server_default=text("NULL         "))
    iscalcformulaeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    isdropscoreeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    iscalcprecisioneditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    stndcalculationmetric = Column(String(30), server_default=text("NULL         "))
    isstndcalcmeteditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    recentscoreweightlist = Column(String(400), server_default=text("NULL         "))
    isstndrcntscoreeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    higherlevelstndmetric = Column(String(30), server_default=text("NULL         "))
    ishigherlvlstndeditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    ishigherstndautocalc = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    ishigherstndcalceditable = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    calcmetricsectionfromstnd = Column(String(30), server_default=text("NULL         "))
    iscalcsectionfromstndedit = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL         "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradeformulaset = relationship('Gradeformulaset')
    section = relationship('Section')


class Gradplan(Base):
    __tablename__ = 'gradplan'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    plantype = Column(Numeric(2, 0, asdecimal=False), nullable=False, server_default=text("0 "))


class Gradreq(Base):
    __tablename__ = 'gradreq'
    __table_args__ = (
        Index('gradreq_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(80))
    description = Column(Text)
    type = Column(String(20))
    reqforgrad = Column(Numeric(10, 0, asdecimal=False))
    appliesto = Column(String(20))
    appliestodata = Column(String(80))
    courselistt = Column(Text)
    courselisthtml = Column(Text)
    courselistcheck = Column(Text)
    reqcrhrs = Column(Float)
    overallcrhrs = Column(Float)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    fieldname = Column(String(40))
    fieldcomparator = Column(String(10))
    fieldmatchvalue = Column(String(40))
    appliestodisp = Column(String(60))
    appliestodatali = Column(Numeric(10, 0, asdecimal=False))
    grade_level = Column(Numeric(10, 0, asdecimal=False), index=True)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    itemtype = Column(String(20))
    how2dispcourses = Column(String(20))
    courselistorder = Column(String(20))
    minimummessage = Column(Text)
    coursegroup = Column(String(40))
    coursedesig = Column(String(30))
    entryboxwidth = Column(Numeric(10, 0, asdecimal=False))
    entryboxheight = Column(Numeric(10, 0, asdecimal=False))
    listboxheight = Column(Numeric(10, 0, asdecimal=False))
    minnoofcourses = Column(Numeric(10, 0, asdecimal=False))
    maxnoofcourses = Column(Numeric(10, 0, asdecimal=False))
    countinreqtots = Column(Numeric(10, 0, asdecimal=False))
    firstitem = Column(String(40))
    classification = Column(String(30))
    subtype = Column(String(20))
    credittype = Column(String(20))
    coursesource = Column(String(20), index=True)
    subjectarea = Column(String(30))
    requesttype = Column(String(20))
    multiterm = Column(String(20))
    schedpriority = Column(Numeric(10, 0, asdecimal=False))
    reqterms = Column(String(20))
    gradreqsetid = Column(Numeric(10, 0, asdecimal=False), index=True)


class Gradreqset(Base):
    __tablename__ = 'gradreqsets'
    __table_args__ = (
        Index('gradreqsets_u2', 'gradreqsetid', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gradreqsetid = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(40))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)


class Guardian(Base):
    __tablename__ = 'guardian'

    guardianid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    firstname = Column(String(30), nullable=False)
    middlename = Column(String(30))
    lastname = Column(String(30), nullable=False)
    email = Column(String(256), nullable=False)
    accountidentifier = Column(ForeignKey('pcas_account.pcas_accounttoken'), unique=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)
    state_guardiannumber = Column(String(32))

    pcas_account = relationship('PcasAccount')


class Guardiannotificationemail(Base):
    __tablename__ = 'guardiannotificationemail'

    guardiannotificationemailid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    guardianstudentid = Column(ForeignKey('guardianstudent.guardianstudentid'), nullable=False, index=True)
    notificationemail = Column(String(100), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    guardianstudent = relationship('Guardianstudent')


class Guardianrelationshiptype(Base):
    __tablename__ = 'guardianrelationshiptype'

    guardianrelationshiptypeid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sifrelationtostudent = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    displayorder = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Guardian(Base):
    __tablename__ = 'guardians'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    familyid = Column(Numeric(10, 0, asdecimal=False))
    first_name = Column(String(15))
    last_name = Column(String(20))
    middle_name = Column(String(20))
    classification = Column(String(20))
    relationship = Column(String(20))
    day_phone = Column(String(30))
    evening_phone = Column(String(30))
    fax = Column(String(30))
    email = Column(String(80))
    lastfirst = Column(String(35))
    tier = Column(String(20))
    rolevalue = Column(String(20))
    status = Column(Numeric(10, 0, asdecimal=False))
    allowwebaccess = Column(Numeric(10, 0, asdecimal=False))
    web_id = Column(String(20))
    webpassword = Column(String(20))
    webemail = Column(String(20))
    webmailpassword = Column(String(20))
    alias = Column(String(20))


class Guardianstudent(Base):
    __tablename__ = 'guardianstudent'

    guardianstudentid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    guardianid = Column(ForeignKey('guardian.guardianid'), nullable=False, index=True)
    guardianrelationshiptypeid = Column(ForeignKey('guardianrelationshiptype.guardianrelationshiptypeid'), nullable=False, index=True)
    autosend_summary = Column(Numeric(1, 0, asdecimal=False))
    autosend_attendancedetail = Column(Numeric(1, 0, asdecimal=False))
    autosend_gradedetail = Column(Numeric(1, 0, asdecimal=False))
    autosend_schoolannouncements = Column(Numeric(1, 0, asdecimal=False))
    autosend_balancealert = Column(Numeric(1, 0, asdecimal=False))
    autosend_howoften = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    guardian = relationship('Guardian')
    guardianrelationshiptype = relationship('Guardianrelationshiptype')
    student = relationship('Student')


class Guardianstudrestrictionmap(Base):
    __tablename__ = 'guardianstudrestrictionmap'
    __table_args__ = (
        Index('guardianstudrestrictionmap_u1', 'guardianstudentid', 'plugindefid', unique=True),
    )

    guardianstudrestrictionmapid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    guardianstudentid = Column(ForeignKey('guardianstudent.guardianstudentid'), nullable=False, index=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    isrestricted = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    guardianstudent = relationship('Guardianstudent')
    plugindef = relationship('Plugindef')


t_guid_setupmetadata = Table(
    'guid_setupmetadata', metadata,
    Column('tablename', String(30), nullable=False),
    Column('uniqueconstraintname', String(30)),
    Column('inserttriggername', String(30)),
    Column('updatetriggername', String(30)),
    Column('status', Numeric(1, 0, asdecimal=False), server_default=text("0")),
    Column('whocreated', String(100), nullable=False, server_default=text("USER ")),
    Column('whencreated', DateTime, nullable=False, server_default=text("sysdate ")),
    Column('whomodified', String(100), nullable=False, server_default=text("USER ")),
    Column('whenmodified', DateTime, nullable=False, server_default=text("sysdate "))
)


class Healthgradelevel(Base):
    __tablename__ = 'healthgradelevel'

    healthgradelevelid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gradelevel = Column(String(30), nullable=False, unique=True)
    iscertifiablegrade = Column(Numeric(1, 0, asdecimal=False), server_default=text("'0'"))
    gradeleveldesc = Column(String(512))
    displayorder = Column(Numeric(10, 0, asdecimal=False))
    stateofrecord = Column(String(30), nullable=False, server_default=text("'Active' "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)
    isactive = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))


class Healthimmexempt(Base):
    __tablename__ = 'healthimmexempt'

    healthimmexemptid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    immunizationexemptioncode = Column(String(30), nullable=False, unique=True)
    immunizationexemptionname = Column(String(50), nullable=False)
    exemptexpireindays = Column(Numeric(10, 0, asdecimal=False))
    statereportcode = Column(String(30))
    statereportname = Column(String(50))
    stateofrecord = Column(String(30), nullable=False, server_default=text("'Active' "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)


class Healthimmsource(Base):
    __tablename__ = 'healthimmsource'

    healthimmsourceid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    immunizationsourcecode = Column(String(30), nullable=False, unique=True)
    immunizationsourcename = Column(String(50), nullable=False)
    statereportcode = Column(String(30))
    statereportname = Column(String(50))
    stateofrecord = Column(String(30), nullable=False, server_default=text("'Active' "))
    isdefaultsource = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("'0' "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)


class Healthmainstudrec(Base):
    __tablename__ = 'healthmainstudrec'
    __table_args__ = (
        Index('healthmainstudrec_u1', 'schoolnumber', 'studentid', unique=True),
    )

    healthmainstudrecid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    schoolnumber = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)


class Healthofficevisit(Base):
    __tablename__ = 'healthofficevisit'
    __table_args__ = (
        Index('healthofficevisit_u1', 'healthofficevisitid', 'healthmainstudrecid', 'visitdate'),
    )

    healthofficevisitid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False)
    visitdate = Column(DateTime, nullable=False)
    screenername = Column(String(30))
    visittypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    officevisitscreenertypeluid = Column(Numeric(19, 0, asdecimal=False))
    visittimein = Column(DateTime)
    visittimeout = Column(DateTime)
    isguardiancontacted = Column(Numeric(1, 0, asdecimal=False))
    visitreasondesc = Column(String(512))
    assessment = Column(String(512))
    actions = Column(String(512))
    visitoutcomeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthmainstudrec = relationship('Healthmainstudrec')
    healthscreenlookup = relationship('Healthscreenlookup', primaryjoin='Healthofficevisit.visitoutcomeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup1 = relationship('Healthscreenlookup', primaryjoin='Healthofficevisit.visittypeluid == Healthscreenlookup.healthscreenlookupid')


class Healthscreenchngdetail(Base):
    __tablename__ = 'healthscreenchngdetail'

    healthscreenchngdetailid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False, index=True)
    healthstudchngrsnid = Column(ForeignKey('healthstudchngrsn.healthstudchngrsnid'), nullable=False, index=True)
    healthstudoralid = Column(ForeignKey('healthstudoral.healthstudoralid'), index=True)
    healthstudhearingid = Column(ForeignKey('healthstudhearing.healthstudhearingid'), index=True)
    healthvitalsignsid = Column(ForeignKey('healthvitalsigns.healthvitalsignsid'), index=True)
    healthstudvisionid = Column(ForeignKey('healthstudvision.healthstudvisionid'), index=True)
    healthstudtbid = Column(ForeignKey('healthstudtb.healthstudtbid'), index=True)
    healthstudscolioid = Column(ForeignKey('healthstudscolio.healthstudscolioid'), index=True)
    healthofficvisitid = Column(ForeignKey('healthofficevisit.healthofficevisitid'), index=True)
    whocreated = Column(String(100))
    whencreated = Column(DateTime)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    psguid = Column(String(50), unique=True)

    healthmainstudrec = relationship('Healthmainstudrec')
    healthofficevisit = relationship('Healthofficevisit')
    healthstudchngrsn = relationship('Healthstudchngrsn')
    healthstudhearing = relationship('Healthstudhearing')
    healthstudoral = relationship('Healthstudoral')
    healthstudscolio = relationship('Healthstudscolio')
    healthstudtb = relationship('Healthstudtb')
    healthstudvision = relationship('Healthstudvision')
    healthvitalsign = relationship('Healthvitalsign')


class Healthscreenlookup(Base):
    __tablename__ = 'healthscreenlookup'
    __table_args__ = (
        Index('healthscreenlookup_u1', 'codetype', 'healthcategory', unique=True),
    )

    healthscreenlookupid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    codetype = Column(String(30), nullable=False)
    healthcategory = Column(String(50), nullable=False)
    stateofrecord = Column(String(30), nullable=False, server_default=text("'Active' "))
    statereportcode = Column(String(30))
    statereportname = Column(String(50))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)
    displayorder = Column(Numeric(10, 0, asdecimal=False))
    isactive = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    defaultvalue = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))


class Healthscreenwaiver(Base):
    __tablename__ = 'healthscreenwaiver'

    healthscreenwaiverid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False, index=True)
    waiverdate = Column(DateTime, nullable=False)
    guardianname = Column(String(30))
    gradelevelatwaiver = Column(String(6))
    waivertype = Column(String(30), nullable=False)
    waiverreasonluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), nullable=False, index=True)
    waivercomment = Column(String(512))
    whocreated = Column(String(100))
    whencreated = Column(DateTime)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    psguid = Column(String(50), unique=True)

    healthmainstudrec = relationship('Healthmainstudrec')
    healthscreenlookup = relationship('Healthscreenlookup')


class Healthstudchngdetail(Base):
    __tablename__ = 'healthstudchngdetail'
    __table_args__ = (
        Index('healthstudchngdetail_n1', 'healthstudimmrecid', 'healthstudchngrsnid'),
    )

    healthstudchngdetailid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthstudimmrecid = Column(Numeric(19, 0, asdecimal=False))
    healthstudchngrsnid = Column(ForeignKey('healthstudchngrsn.healthstudchngrsnid'), nullable=False, index=True)
    healthvaccineid = Column(Numeric(19, 0, asdecimal=False))
    healthstuddoserecid = Column(Numeric(19, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthstudchngrsn = relationship('Healthstudchngrsn')


class Healthstudchngrsn(Base):
    __tablename__ = 'healthstudchngrsn'

    healthstudchngrsnid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    chngrsndesc = Column(String(2048))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)


class Healthstuddoserec(Base):
    __tablename__ = 'healthstuddoserec'

    healthstuddoserecid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    healthvaccineid = Column(ForeignKey('healthvaccine.healthvaccineid'), nullable=False, index=True)
    healthstudimmrecid = Column(ForeignKey('healthstudimmrec.healthstudimmrecid'), nullable=False, index=True)
    healthimmsourceid = Column(ForeignKey('healthimmsource.healthimmsourceid'), index=True)
    dose = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    dateadministered = Column(DateTime)
    dosecompliancystatement = Column(String(100))
    compliancystatus = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthimmsource = relationship('Healthimmsource')
    healthstudimmrec = relationship('Healthstudimmrec')
    healthvaccine = relationship('Healthvaccine')


class Healthstudgradelevel(Base):
    __tablename__ = 'healthstudgradelevel'
    __table_args__ = (
        Index('healthstudgradelevel_u1', 'healthgradelevelid', 'studentid', unique=True),
    )

    healthstudgradelevelid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthgradelevelid = Column(ForeignKey('healthgradelevel.healthgradelevelid'), nullable=False)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    certificationdate = Column(DateTime)
    certificationstatusluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), nullable=False, index=True)
    certificationfirstname = Column(String(30), nullable=False)
    certificationmiddlename = Column(String(30))
    certificationlastname = Column(String(30), nullable=False)
    certificationcomment = Column(String(512))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthscreenlookup = relationship('Healthscreenlookup')
    healthgradelevel = relationship('Healthgradelevel')


class Healthstudhearing(Base):
    __tablename__ = 'healthstudhearing'
    __table_args__ = (
        Index('healthstudhearing_u1', 'healthmainstudrecid', 'screendate', unique=True),
    )

    healthstudhearingid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False)
    screendate = Column(DateTime, nullable=False)
    screenername = Column(String(30))
    hearingscreenertypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    gradelevelatscreen = Column(String(6))
    righteartestluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    lefteartestluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    referraldate = Column(DateTime)
    hearingaid = Column(String(256))
    istestconductedlate = Column(Numeric(1, 0, asdecimal=False), server_default=text("'0'"))
    isimpairedtestconducted = Column(Numeric(1, 0, asdecimal=False), server_default=text("'0'"))
    examtypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    hearingscreenoutcomeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    screencomment = Column(String(512))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthscreenlookup = relationship('Healthscreenlookup', primaryjoin='Healthstudhearing.examtypeluid == Healthscreenlookup.healthscreenlookupid')
    healthmainstudrec = relationship('Healthmainstudrec')
    healthscreenlookup1 = relationship('Healthscreenlookup', primaryjoin='Healthstudhearing.hearingscreenertypeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup2 = relationship('Healthscreenlookup', primaryjoin='Healthstudhearing.hearingscreenoutcomeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup3 = relationship('Healthscreenlookup', primaryjoin='Healthstudhearing.lefteartestluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup4 = relationship('Healthscreenlookup', primaryjoin='Healthstudhearing.righteartestluid == Healthscreenlookup.healthscreenlookupid')


class Healthstudimmrec(Base):
    __tablename__ = 'healthstudimmrec'

    healthstudimmrecid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    healthvaccineid = Column(ForeignKey('healthvaccine.healthvaccineid'), nullable=False, index=True)
    healthimmexemptid = Column(ForeignKey('healthimmexempt.healthimmexemptid'), index=True)
    nextdose = Column(Numeric(10, 0, asdecimal=False))
    nextdoseduedate = Column(DateTime)
    compliancystatus = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    exemptiondate = Column(DateTime)
    exemptionexpirydate = Column(DateTime)
    exemptioncomment = Column(String(512))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)
    compliancystatement = Column(String(512))

    healthimmexempt = relationship('Healthimmexempt')
    healthvaccine = relationship('Healthvaccine')


class Healthstudoral(Base):
    __tablename__ = 'healthstudoral'
    __table_args__ = (
        Index('healthstudoral_u1', 'healthmainstudrecid', 'screendate', unique=True),
    )

    healthstudoralid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False)
    screendate = Column(DateTime, nullable=False)
    screenername = Column(String(30))
    oralscreenertypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    gradelevelatscreen = Column(String(6))
    isdentalsealantpresent = Column(Numeric(1, 0, asdecimal=False), server_default=text("'2'"))
    ismalocclusionpresent = Column(Numeric(1, 0, asdecimal=False), server_default=text("'2'"))
    ishistorycariespresent = Column(Numeric(1, 0, asdecimal=False), server_default=text("'2'"))
    isuntreatedcariespresent = Column(Numeric(1, 0, asdecimal=False), server_default=text("'2'"))
    oralscreenoutcomeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    treaturgencyluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    screencomment = Column(String(512))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthmainstudrec = relationship('Healthmainstudrec')
    healthscreenlookup = relationship('Healthscreenlookup', primaryjoin='Healthstudoral.oralscreenertypeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup1 = relationship('Healthscreenlookup', primaryjoin='Healthstudoral.oralscreenoutcomeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup2 = relationship('Healthscreenlookup', primaryjoin='Healthstudoral.treaturgencyluid == Healthscreenlookup.healthscreenlookupid')


class Healthstudscolio(Base):
    __tablename__ = 'healthstudscolio'
    __table_args__ = (
        Index('healthstudscolio_u1', 'healthmainstudrecid', 'screendate', unique=True),
    )

    healthstudscolioid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False)
    screendate = Column(DateTime, nullable=False)
    screenername = Column(String(30))
    scolioscreenertypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    gradelevelatscreen = Column(String(6))
    xrayfilmdate = Column(DateTime)
    xrayfilmimpresluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    scolioscreenoutcomeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    screencomment = Column(String(512))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthmainstudrec = relationship('Healthmainstudrec')
    healthscreenlookup = relationship('Healthscreenlookup', primaryjoin='Healthstudscolio.scolioscreenertypeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup1 = relationship('Healthscreenlookup', primaryjoin='Healthstudscolio.scolioscreenoutcomeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup2 = relationship('Healthscreenlookup', primaryjoin='Healthstudscolio.xrayfilmimpresluid == Healthscreenlookup.healthscreenlookupid')


class Healthstudtb(Base):
    __tablename__ = 'healthstudtb'
    __table_args__ = (
        Index('healthstudtb_u1', 'healthmainstudrecid', 'screendate'),
    )

    healthstudtbid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False)
    screendate = Column(DateTime, nullable=False)
    screenername = Column(String(30))
    tbscreenertypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    gradelevelatscreen = Column(String(6))
    skintesttypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    skintestgivendate = Column(DateTime)
    skintestreaddate = Column(DateTime)
    indurationsize = Column(Numeric(12, 2))
    impressionresultluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    chestxrayfilmdate = Column(DateTime)
    chestxrayimpresluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    tbscreenoutcomeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    screencomment = Column(String(512))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthscreenlookup = relationship('Healthscreenlookup', primaryjoin='Healthstudtb.chestxrayimpresluid == Healthscreenlookup.healthscreenlookupid')
    healthmainstudrec = relationship('Healthmainstudrec')
    healthscreenlookup1 = relationship('Healthscreenlookup', primaryjoin='Healthstudtb.impressionresultluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup2 = relationship('Healthscreenlookup', primaryjoin='Healthstudtb.skintesttypeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup3 = relationship('Healthscreenlookup', primaryjoin='Healthstudtb.tbscreenertypeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup4 = relationship('Healthscreenlookup', primaryjoin='Healthstudtb.tbscreenoutcomeluid == Healthscreenlookup.healthscreenlookupid')


class Healthstudvision(Base):
    __tablename__ = 'healthstudvision'
    __table_args__ = (
        Index('healthstudvision_u1', 'healthmainstudrecid', 'screendate', unique=True),
    )

    healthstudvisionid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False)
    screendate = Column(DateTime, nullable=False)
    screenername = Column(String(30))
    visionscreenertypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    gradelevelatscreen = Column(String(6))
    visionaid = Column(String(256))
    referraldate = Column(DateTime)
    colorblindtestluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    istestconductedlate = Column(Numeric(1, 0, asdecimal=False), server_default=text("'0'"))
    righteyetestluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    lefteyetestluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    visionscreenoutcomeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    screencomment = Column(String(512))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthscreenlookup = relationship('Healthscreenlookup', primaryjoin='Healthstudvision.colorblindtestluid == Healthscreenlookup.healthscreenlookupid')
    healthmainstudrec = relationship('Healthmainstudrec')
    healthscreenlookup1 = relationship('Healthscreenlookup', primaryjoin='Healthstudvision.lefteyetestluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup2 = relationship('Healthscreenlookup', primaryjoin='Healthstudvision.righteyetestluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup3 = relationship('Healthscreenlookup', primaryjoin='Healthstudvision.visionscreenertypeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup4 = relationship('Healthscreenlookup', primaryjoin='Healthstudvision.visionscreenoutcomeluid == Healthscreenlookup.healthscreenlookupid')


class Healthvaccine(Base):
    __tablename__ = 'healthvaccine'

    healthvaccineid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    vaccinecode = Column(String(30), nullable=False, unique=True)
    vaccinedesc = Column(String(512))
    vaccinename = Column(String(50), nullable=False)
    numberofdoses = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    statereportcode = Column(String(30))
    statereportname = Column(String(50))
    stateofrecord = Column(String(30), nullable=False, server_default=text("'Active' "))
    displayorder = Column(Numeric(10, 0, asdecimal=False))
    ismandatory = Column(Numeric(1, 0, asdecimal=False), server_default=text("'0'"))
    isrulesready = Column(Numeric(1, 0, asdecimal=False), server_default=text("'0'"))
    isusedbyruleengine = Column(Numeric(1, 0, asdecimal=False), server_default=text("'0'"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    healthvaccineruleid = Column(ForeignKey('healthvaccinerule.healthvaccineruleid'), index=True)
    psguid = Column(String(50), unique=True)

    healthvaccinerule = relationship('Healthvaccinerule')


class Healthvaccinerule(Base):
    __tablename__ = 'healthvaccinerule'

    healthvaccineruleid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthvacrulename = Column(String(30))
    healthvacrulecode = Column(String(30))
    isinusebyrule = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)


class Healthvitalsign(Base):
    __tablename__ = 'healthvitalsigns'
    __table_args__ = (
        Index('healthvitalsigns_u1', 'healthmainstudrecid', 'screendate', unique=True),
    )

    healthvitalsignsid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    healthmainstudrecid = Column(ForeignKey('healthmainstudrec.healthmainstudrecid'), nullable=False)
    screendate = Column(DateTime, nullable=False)
    screenername = Column(String(30))
    vitalscreenertypeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    gradelevelatscreen = Column(String(6))
    height = Column(Numeric(12, 2))
    heightpercentile = Column(String(6))
    weight = Column(Numeric(12, 2))
    weightpercentile = Column(String(6))
    weightstatusluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    bmi = Column(Numeric(12, 2))
    systolicbloodpressure = Column(String(6))
    diastolicbloodpressure = Column(String(6))
    temperature = Column(String(6))
    restingheartrate = Column(String(6))
    vitalscreenoutcomeluid = Column(ForeignKey('healthscreenlookup.healthscreenlookupid'), index=True)
    screencomment = Column(String(512))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    psguid = Column(String(50), unique=True)

    healthmainstudrec = relationship('Healthmainstudrec')
    healthscreenlookup = relationship('Healthscreenlookup', primaryjoin='Healthvitalsign.vitalscreenertypeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup1 = relationship('Healthscreenlookup', primaryjoin='Healthvitalsign.vitalscreenoutcomeluid == Healthscreenlookup.healthscreenlookupid')
    healthscreenlookup2 = relationship('Healthscreenlookup', primaryjoin='Healthvitalsign.weightstatusluid == Healthscreenlookup.healthscreenlookupid')


class Help(Base):
    __tablename__ = 'help'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    topicid = Column(String(30), index=True)
    title = Column(String(80))
    keywords = Column(String(80))
    searchtext = Column(Text)
    body = Column(Text)
    filesize = Column(Numeric(10, 0, asdecimal=False))
    modtime = Column(Numeric(10, 0, asdecimal=False))
    relpath = Column(Text)
    level1 = Column(String(80), index=True)
    level2 = Column(String(80))
    level3 = Column(String(80))
    level4 = Column(String(20))
    level5 = Column(String(20))
    numlevels = Column(Numeric(10, 0, asdecimal=False))
    moddate = Column(DateTime)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    searchtext2 = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class HleLog(Base):
    __tablename__ = 'hle_log'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    parentid = Column(ForeignKey('hle_log.id'), index=True)
    name = Column(String(20), nullable=False)
    fullpath = Column(String(400), nullable=False)
    paramsjson = Column(Text)
    tableparam = Column(String(40))
    colslistparam = Column(Text)
    startedts = Column(DateTime, nullable=False, server_default=text("SYSTIMESTAMP "))
    endedts = Column(DateTime)
    serverinstanceid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    userid = Column(Numeric(10, 0, asdecimal=False))
    usertype = Column(String(1))
    ipaddress = Column(String(20))

    parent = relationship('HleLog', remote_side=[id])


t_hle_log_no_lle = Table(
    'hle_log_no_lle', metadata,
    Column('hle_log_id', ForeignKey('hle_log.id'), nullable=False, index=True),
    Column('no_log_table', String(30), nullable=False)
)


class Honorroll(Base):
    __tablename__ = 'honorroll'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    schoolname = Column(String(60))
    storecode = Column(String(10))
    grade_level = Column(Numeric(10, 0, asdecimal=False))
    method = Column(String(50))
    levelvalue = Column(String(50))
    message = Column(Text)
    log = Column(Text)
    gpa = Column(String(80))
    datestored = Column(DateTime)


class Idpcontext(Base):
    __tablename__ = 'idpcontext'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    contextname = Column(String(100), nullable=False)
    sitetype = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Idpmetadatum(Base):
    __tablename__ = 'idpmetadata'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    idpcontextid = Column(ForeignKey('idpcontext.id'), nullable=False, unique=True)
    metadatacategory = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(String(256), nullable=False)
    attributetype = Column(String(100))
    encodertype = Column(String(100))
    dependencyref = Column(String(100))
    nameformat = Column(String(100))
    friendlyname = Column(String(100))
    binding = Column(String(100))
    location = Column(String(100))
    localentity = Column(String(100))
    localfield = Column(String(100))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    idpcontext = relationship('Idpcontext')


class Idpmetadatamap(Base):
    __tablename__ = 'idpmetadatamap'
    __table_args__ = (
        Index('idpmetadatamap_u2', 'idpmetadataid', 'idprelyingpartyid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    idpmetadataid = Column(ForeignKey('idpmetadata.id'), nullable=False, index=True)
    idprelyingpartyid = Column(ForeignKey('idprelyingparty.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    externalfield = Column(String(100))
    externalvalue = Column(String(256))

    idpmetadatum = relationship('Idpmetadatum')
    idprelyingparty = relationship('Idprelyingparty')


class Idprelyingparty(Base):
    __tablename__ = 'idprelyingparty'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(64), nullable=False)
    isenabled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    spmetadataurl = Column(String(256))
    spmetadatacache = Column(LargeBinary)
    relyingpartyentityname = Column(String(256))
    providerentityname = Column(String(256), nullable=False)
    adapterclass = Column(String(256), nullable=False)
    keystorealiasname = Column(String(256))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    idpmetadatacache = Column(LargeBinary)
    idpmetadataurl = Column(String(256))
    spbaseurl = Column(String(256))
    idpname = Column(String(40))
    plugindefid = Column(Numeric(10, 0, asdecimal=False))
    isserviceprovider = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))


class Idpservice(Base):
    __tablename__ = 'idpservice'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    idprelyingpartyid = Column(ForeignKey('idprelyingparty.id'), nullable=False, index=True)
    servicename = Column(String(100), nullable=False)
    description = Column(String(100))
    servicepath = Column(String(256), nullable=False)
    tableentity = Column(String(30))
    tablefield = Column(String(30))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    idprelyingparty = relationship('Idprelyingparty')


class Idpservicemap(Base):
    __tablename__ = 'idpservicemap'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    idpserviceid = Column(ForeignKey('idpservice.id'), nullable=False, index=True)
    idpserviceparamid = Column(ForeignKey('idpserviceparam.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    idpservice = relationship('Idpservice')
    idpserviceparam = relationship('Idpserviceparam')


class Idpserviceparam(Base):
    __tablename__ = 'idpserviceparam'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    paramname = Column(String(30), nullable=False)
    paramtype = Column(String(30), nullable=False)
    description = Column(String(100))
    defaultvalue = Column(String(256))
    relatedentity = Column(String(30))
    relatedfield = Column(String(250))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Importlocalizationresult(Base):
    __tablename__ = 'importlocalizationresults'

    importlocalizationresultsid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    importlocalizationstatusid = Column(ForeignKey('importlocalizationstatus.importlocalizationstatusid'), nullable=False, index=True)
    importstatus = Column(String(32), nullable=False)
    item = Column(String(256))
    messagetext = Column(Text)
    reason = Column(String(256), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    importlocalizationstatu = relationship('Importlocalizationstatu')


class Importlocalizationstatu(Base):
    __tablename__ = 'importlocalizationstatus'

    importlocalizationstatusid = Column(Numeric(10, 0, asdecimal=False), primary_key=True, server_default=text("0 "))
    importtype = Column(String(100), nullable=False)
    filename = Column(String(256), nullable=False, index=True)
    starttime = Column(DateTime, nullable=False)
    endtime = Column(DateTime)
    importstatus = Column(String(256), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Incident(Base):
    __tablename__ = 'incident'

    incident_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    school_number = Column(Numeric(10, 0, asdecimal=False), index=True)
    incident_title = Column(String(80))
    incident_detail_desc = Column(Text)
    entry_author = Column(String(50))
    incident_ts = Column(DateTime)
    financial_impact = Column(Numeric(10, 0, asdecimal=False))
    incident_reference_value = Column(String(30))
    location_details = Column(String(256))
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)


class IncidentAction(Base):
    __tablename__ = 'incident_action'

    incident_action_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_id = Column(ForeignKey('incident.incident_id'), nullable=False, index=True)
    action_plan_begin_dt = Column(DateTime)
    action_plan_end_dt = Column(DateTime)
    action_actual_resolved_dt = Column(DateTime)
    action_resolved_desc = Column(String(256))
    duration_assigned = Column(Numeric(10, 2))
    duration_actual = Column(Numeric(10, 2))
    duration_notes = Column(String(256))
    action_change_reason = Column(String(256))
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    action_incident_detail_id = Column(ForeignKey('incident_detail.incident_detail_id'), nullable=False, index=True)
    duration_incident_detail_id = Column(ForeignKey('incident_detail.incident_detail_id'), index=True)
    chng_rsn_incident_detail_id = Column(ForeignKey('incident_detail.incident_detail_id'), index=True)
    psguid = Column(String(50), unique=True)

    action_incident_detail = relationship('IncidentDetail', primaryjoin='IncidentAction.action_incident_detail_id == IncidentDetail.incident_detail_id')
    chng_rsn_incident_detail = relationship('IncidentDetail', primaryjoin='IncidentAction.chng_rsn_incident_detail_id == IncidentDetail.incident_detail_id')
    duration_incident_detail = relationship('IncidentDetail', primaryjoin='IncidentAction.duration_incident_detail_id == IncidentDetail.incident_detail_id')
    incident = relationship('Incident')


class IncidentActionAttribute(Base):
    __tablename__ = 'incident_action_attribute'

    incident_action_attribute_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_id = Column(ForeignKey('incident.incident_id'), nullable=False, index=True)
    incident_action_id = Column(ForeignKey('incident_action.incident_action_id'), nullable=False, index=True)
    incident_detail_id = Column(ForeignKey('incident_detail.incident_detail_id'), nullable=False, index=True)
    text_attribute = Column(String(2000))
    is_yes1_no0_attribute = Column(Numeric(1, 0, asdecimal=False))
    number_attribute = Column(Numeric(12, 2))
    date_attribute = Column(DateTime)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)

    incident_action = relationship('IncidentAction')
    incident_detail = relationship('IncidentDetail')
    incident = relationship('Incident')


class IncidentChangeRsnDesc(Base):
    __tablename__ = 'incident_change_rsn_desc'

    change_rsn_desc_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_id = Column(ForeignKey('incident.incident_id'), nullable=False, index=True)
    description = Column(String(2048), nullable=False)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)

    incident = relationship('Incident')


class IncidentDetail(Base):
    __tablename__ = 'incident_detail'
    __table_args__ = (
        Index('incident_detail_n2', 'incident_id', 'lu_sub_code_id'),
        Index('incident_detail_n1', 'incident_id', 'lu_code_id')
    )

    incident_detail_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_id = Column(ForeignKey('incident.incident_id'), nullable=False, index=True)
    lu_code_id = Column(ForeignKey('incident_lu_code.lu_code_id'), nullable=False, index=True)
    lu_sub_code_id = Column(ForeignKey('incident_lu_sub_code.lu_sub_code_id'), nullable=False, index=True)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    lookup_code_desc = Column(String(512))
    primary_indicator = Column(String(30), server_default=text("' '"))
    psguid = Column(String(50), unique=True)

    incident = relationship('Incident')
    lu_code = relationship('IncidentLuCode')
    lu_sub_code = relationship('IncidentLuSubCode')


class IncidentLuCode(Base):
    __tablename__ = 'incident_lu_code'
    __table_args__ = (
        Index('incdnt_sk02_indx', 'code_type', 'incident_category'),
    )

    lu_code_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    code_type = Column(String(50), nullable=False, index=True)
    incident_category = Column(String(50), nullable=False)
    state_aggregate_rpt_code = Column(String(20))
    application_display_order = Column(Numeric(10, 0, asdecimal=False))
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)


class IncidentLuSubCode(Base):
    __tablename__ = 'incident_lu_sub_code'

    lu_sub_code_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    sub_category = Column(String(50), nullable=False)
    lu_code_id = Column(ForeignKey('incident_lu_code.lu_code_id'), nullable=False, index=True)
    severity = Column(Numeric(12, 2))
    is_state_reportable_flg = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    is_police_reportable_flg = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    state_detail_report_code = Column(String(20))
    application_display_order = Column(Numeric(10, 0, asdecimal=False))
    short_desc = Column(String(80))
    long_desc = Column(String(256))
    effective_begin_dt = Column(DateTime, nullable=False)
    effective_end_dt = Column(DateTime)
    status = Column(String(30), nullable=False)
    restricted = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    comment_enable_state = Column(String(30), server_default=text("'Disabled'"))
    parent_lu_sub_code_id = Column(ForeignKey('incident_lu_sub_code.lu_sub_code_id'), index=True)
    datatype_attribute = Column(String(30))
    psguid = Column(String(50), unique=True)
    policy_desc = Column(String(1000))
    is_affects_attendance_flg = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    lu_code = relationship('IncidentLuCode')
    parent_lu_sub_code = relationship('IncidentLuSubCode', remote_side=[lu_sub_code_id])


class IncidentObject(Base):
    __tablename__ = 'incident_object'

    incident_object_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    object_desc = Column(String(2048))
    incident_id = Column(ForeignKey('incident.incident_id'), nullable=False, index=True)
    object_quanity = Column(Numeric(10, 0, asdecimal=False))
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    object_incident_detail_id = Column(ForeignKey('incident_detail.incident_detail_id'), nullable=False, index=True)
    psguid = Column(String(50), unique=True)

    incident = relationship('Incident')
    object_incident_detail = relationship('IncidentDetail')


class IncidentObjectPerson(Base):
    __tablename__ = 'incident_object_person'

    incident_object_person_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_object_id = Column(ForeignKey('incident_object.incident_object_id'), nullable=False, index=True)
    incident_person_role_id = Column(ForeignKey('incident_person_role.incident_person_role_id'), nullable=False, index=True)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)

    incident_object = relationship('IncidentObject')
    incident_person_role = relationship('IncidentPersonRole')


class IncidentOtherPerson(Base):
    __tablename__ = 'incident_other_person'

    incident_other_person_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    first_name = Column(String(30))
    middle_name = Column(String(30))
    last_name = Column(String(30))
    position = Column(String(30))
    age = Column(Numeric(6, 0, asdecimal=False))
    gender = Column(String(10))
    is_unknown = Column(Numeric(1, 0, asdecimal=False))
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)


class IncidentPersonAction(Base):
    __tablename__ = 'incident_person_action'

    incident_person_action_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_action_id = Column(ForeignKey('incident_action.incident_action_id'), nullable=False, index=True)
    incident_person_detail_id = Column(ForeignKey('incident_person_detail.incident_person_detail_id'), index=True)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)

    incident_action = relationship('IncidentAction')
    incident_person_detail = relationship('IncidentPersonDetail')


class IncidentPersonDetail(Base):
    __tablename__ = 'incident_person_detail'

    incident_person_detail_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_person_role_id = Column(ForeignKey('incident_person_role.incident_person_role_id'), nullable=False, index=True)
    incident_detail_id = Column(ForeignKey('incident_detail.incident_detail_id'), index=True)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)

    incident_detail = relationship('IncidentDetail')
    incident_person_role = relationship('IncidentPersonRole')


class IncidentPersonRole(Base):
    __tablename__ = 'incident_person_role'
    __table_args__ = (
        Index('incident_person_role_n2', 'incident_id', 'teacherid'),
        Index('incident_person_role_n1', 'incident_id', 'studentid')
    )

    incident_person_role_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    person_desc = Column(String(2048))
    incident_id = Column(ForeignKey('incident.incident_id'), nullable=False, index=True)
    teacherid = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    incident_other_person_id = Column(ForeignKey('incident_other_person.incident_other_person_id'), index=True)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    role_incident_detail_id = Column(ForeignKey('incident_detail.incident_detail_id'), nullable=False, index=True)
    psguid = Column(String(50), unique=True)

    incident = relationship('Incident')
    incident_other_person = relationship('IncidentOtherPerson')
    role_incident_detail = relationship('IncidentDetail')


class IncidentPersonal(Base):
    __tablename__ = 'incident_personal'

    incident_personal_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_id = Column(ForeignKey('incident.incident_id'), nullable=False, index=True)
    personal_incident_detail_id = Column(ForeignKey('incident_detail.incident_detail_id'), nullable=False, index=True)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)

    incident = relationship('Incident')
    personal_incident_detail = relationship('IncidentDetail')


class IncidentPersonalDetail(Base):
    __tablename__ = 'incident_personal_detail'

    incident_personal_detail_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    incident_personal_id = Column(ForeignKey('incident_personal.incident_personal_id'), nullable=False, index=True)
    incident_person_role_id = Column(ForeignKey('incident_person_role.incident_person_role_id'), nullable=False, index=True)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)

    incident_person_role = relationship('IncidentPersonRole')
    incident_personal = relationship('IncidentPersonal')


class IncidentSecurityGroup(Base):
    __tablename__ = 'incident_security_group'

    incident_security_group_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    lu_sub_code_id = Column(ForeignKey('incident_lu_sub_code.lu_sub_code_id'), nullable=False, index=True)
    gen_dcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    created_by = Column(String(30))
    created_ts = Column(DateTime)
    last_modified_by = Column(String(30))
    last_modified_ts = Column(DateTime)
    psguid = Column(String(50), unique=True)

    lu_sub_code = relationship('IncidentLuSubCode')


class Institution(Base):
    __tablename__ = 'institution'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    institutioncodeid = Column(ForeignKey('institutioncodelist.id'), index=True)
    institutionnumber = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    institutioncodelist = relationship('Institutioncodelist')


class Institutioncodelist(Base):
    __tablename__ = 'institutioncodelist'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    idprelyingpartyid = Column(ForeignKey('idprelyingparty.id'), nullable=False, index=True)
    institutioncode = Column(String(20), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    idprelyingparty = relationship('Idprelyingparty')


t_ir_schools = Table(
    'ir_schools', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('school_number', Numeric(10, 0, asdecimal=False)),
    Column('name', String(60))
)


class Jobstatu(Base):
    __tablename__ = 'jobstatus'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    jobname = Column(String(200))
    jobgroup = Column(String(200))
    endts = Column(DateTime)
    jobtype = Column(String(30), nullable=False)
    scheduledts = Column(DateTime)
    startts = Column(DateTime)
    status = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Keystore(Base):
    __tablename__ = 'keystore'

    keystoreid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    aliasname = Column(String(256), nullable=False, unique=True)
    entrytype = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    key = Column(LargeBinary)
    certificatechain = Column(LargeBinary)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class Languageisocodelu(Base):
    __tablename__ = 'languageisocodelu'

    languageisocode = Column(String(3), primary_key=True)
    displaylabel = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


t_lg_attendance = Table(
    'lg_attendance', metadata,
    Column('log_seq', Numeric(19, 0, asdecimal=False), nullable=False, unique=True),
    Column('transaction_date', DateTime, nullable=False),
    Column('dml_type', String(1), nullable=False),
    Column('hle_log_id', Numeric(10, 0, asdecimal=False)),
    Column('dcid', Numeric(10, 0, asdecimal=False)),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('ccid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('periodid', Numeric(10, 0, asdecimal=False)),
    Column('o_attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('n_attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('ip_address', String(39)),
    Column('whomodifiedid', Numeric(10, 0, asdecimal=False)),
    Column('whomodifiedtype', String(1)),
    Column('changed_columns', String(4000))
)


t_lg_pgfinalgrades = Table(
    'lg_pgfinalgrades', metadata,
    Column('log_seq', Numeric(19, 0, asdecimal=False), nullable=False, unique=True),
    Column('transaction_date', DateTime, nullable=False),
    Column('dml_type', String(1), nullable=False),
    Column('hle_log_id', Numeric(10, 0, asdecimal=False)),
    Column('dcid', Numeric(10, 0, asdecimal=False)),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('finalgradename', String(8)),
    Column('o_grade', String(7)),
    Column('n_grade', String(7)),
    Column('ip_address', String(39)),
    Column('whomodifiedid', Numeric(10, 0, asdecimal=False)),
    Column('whomodifiedtype', String(1)),
    Column('changed_columns', String(4000))
)


t_lg_roledefteachersmap = Table(
    'lg_roledefteachersmap', metadata,
    Column('log_seq', Numeric(19, 0, asdecimal=False), nullable=False, unique=True),
    Column('transaction_date', DateTime, nullable=False),
    Column('dml_type', String(1), nullable=False),
    Column('hle_log_id', Numeric(10, 0, asdecimal=False)),
    Column('teachersdcid', Numeric(19, 0, asdecimal=False)),
    Column('o_isenabled', Numeric(3, 0, asdecimal=False)),
    Column('n_isenabled', Numeric(3, 0, asdecimal=False)),
    Column('o_schoolid', Numeric(10, 0, asdecimal=False)),
    Column('n_schoolid', Numeric(10, 0, asdecimal=False)),
    Column('o_isdistrict', Numeric(3, 0, asdecimal=False)),
    Column('n_isdistrict', Numeric(3, 0, asdecimal=False)),
    Column('o_roledefid', Numeric(19, 0, asdecimal=False)),
    Column('n_roledefid', Numeric(19, 0, asdecimal=False)),
    Column('ip_address', String(39)),
    Column('whomodifiedid', Numeric(10, 0, asdecimal=False)),
    Column('whomodifiedtype', String(1)),
    Column('changed_columns', String(4000))
)


class Locale(Base):
    __tablename__ = 'locale'
    __table_args__ = (
        Index('localecountryisocodei1', 'countryisocode', 'languageisocode', unique=True),
    )

    localeid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    displaylabel = Column(String(20), nullable=False)
    countryisocode = Column(ForeignKey('countryisocodelu.countryisocode'), nullable=False)
    languageisocode = Column(ForeignKey('languageisocodelu.languageisocode'), nullable=False, index=True)
    localedateformatid = Column(ForeignKey('localedateformat.localedateformatid'), nullable=False, index=True)
    localetimeformatid = Column(ForeignKey('localetimeformat.localetimeformatid'), nullable=False, index=True)
    localenumericformatid = Column(ForeignKey('localenumcurrformatlu.localenumcurrid'), index=True)
    localecurrencyformatid = Column(ForeignKey('localenumcurrformatlu.localenumcurrid'), index=True)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    countryisocodelu = relationship('Countryisocodelu')
    languageisocodelu = relationship('Languageisocodelu')
    localenumcurrformatlu = relationship('Localenumcurrformatlu', primaryjoin='Locale.localecurrencyformatid == Localenumcurrformatlu.localenumcurrid')
    localedateformat = relationship('Localedateformat')
    localenumcurrformatlu1 = relationship('Localenumcurrformatlu', primaryjoin='Locale.localenumericformatid == Localenumcurrformatlu.localenumcurrid')
    localetimeformat = relationship('Localetimeformat')


class Localedateformat(Base):
    __tablename__ = 'localedateformat'

    localedateformatid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    displaylabel = Column(String(100), nullable=False)
    dateformat = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Localenumcurrformatlu(Base):
    __tablename__ = 'localenumcurrformatlu'

    localenumcurrid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    localenumcurrformat = Column(String(100), nullable=False)
    displaylabel = Column(String(100), nullable=False)
    groupseparator = Column(ForeignKey('localeseparatorlu.localeseparatorcode'), nullable=False, index=True)
    decimalseparator = Column(ForeignKey('localeseparatorlu.localeseparatorcode'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    localeseparatorlu = relationship('Localeseparatorlu', primaryjoin='Localenumcurrformatlu.decimalseparator == Localeseparatorlu.localeseparatorcode')
    localeseparatorlu1 = relationship('Localeseparatorlu', primaryjoin='Localenumcurrformatlu.groupseparator == Localeseparatorlu.localeseparatorcode')


class Localeseparatorlu(Base):
    __tablename__ = 'localeseparatorlu'

    localeseparatorcode = Column(String(1), primary_key=True)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Localetimeformat(Base):
    __tablename__ = 'localetimeformat'

    localetimeformatid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    displaylabel = Column(String(100), nullable=False)
    timeformat = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Log(Base):
    __tablename__ = 'log'
    __table_args__ = (
        Index('log_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    entry_author = Column(String(30))
    entry_date = Column(DateTime, index=True)
    entry_time = Column(Numeric(10, 0, asdecimal=False))
    category = Column(Numeric(10, 0, asdecimal=False), index=True)
    subject = Column(String(40))
    entry = Column(Text)
    custom = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    logtypeid = Column(Numeric(10, 0, asdecimal=False))
    subtype = Column(String(20))
    consequence = Column(String(20))
    student_number = Column(Float)
    discipline_incidenttype = Column(String(79))
    incidenttypecategory = Column(String(79))
    discipline_incidenttypedetail = Column(String(79))
    discipline_incidentdate = Column(DateTime)
    discipline_incidentcontext = Column(String(79))
    discipline_incidentlocation = Column(String(79))
    discipline_incidentlocdetail = Column(String(79))
    discipline_offender = Column(String(79))
    discipline_reporter = Column(String(79))
    discipline_reporterid = Column(String(79))
    discipline_victimtype = Column(String(79))
    discipline_felonyflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_likelyinjuryflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_schoolrulesvioflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_policeinvolvedflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_hearingofficerflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_gangrelatedflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_hatecrimeflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_alcoholrelatedflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_drugrelatedflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_drugtypedetail = Column(String(79))
    discipline_weaponrelatedflag = Column(Numeric(10, 0, asdecimal=False))
    discipline_weapontype = Column(String(79))
    discipline_weapontypenotes = Column(String(79))
    discipline_moneylossvalue = Column(Float)
    discipline_actiondate = Column(DateTime)
    discipline_actiontaken = Column(String(79))
    discipline_actiontakendetail = Column(String(79))
    discipline_durationassigned = Column(Float)
    discipline_durationactual = Column(Float)
    durationchangesource = Column(String(79))
    discipline_durationnotes = Column(String(79))
    discipline_sequence = Column(Numeric(10, 0, asdecimal=False))
    discipline_administratorid = Column(String(79))
    discipline_actiontakenenddate = Column(DateTime)
    psguid = Column(String(50), unique=True)


class Log2(Base):
    __tablename__ = 'log2'
    __table_args__ = (
        Index('log2_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(60))
    description = Column(Text)
    date_value = Column(DateTime)
    time = Column(Numeric(10, 0, asdecimal=False))
    ticks = Column(Numeric(10, 0, asdecimal=False))
    server_instanceid = Column(Numeric(10, 0, asdecimal=False), index=True)


t_logbackup_esc7251 = Table(
    'logbackup_esc7251', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('teacherid', Numeric(10, 0, asdecimal=False)),
    Column('entry_author', String(30)),
    Column('entry_date', DateTime),
    Column('entry_time', Numeric(10, 0, asdecimal=False)),
    Column('category', Numeric(10, 0, asdecimal=False)),
    Column('subject', String(40)),
    Column('entry', Text),
    Column('custom', Text),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('logtypeid', Numeric(10, 0, asdecimal=False)),
    Column('subtype', String(20)),
    Column('consequence', String(20)),
    Column('student_number', Float),
    Column('discipline_incidenttype', String(79)),
    Column('incidenttypecategory', String(79)),
    Column('discipline_incidenttypedetail', String(79)),
    Column('discipline_incidentdate', DateTime),
    Column('discipline_incidentcontext', String(79)),
    Column('discipline_incidentlocation', String(79)),
    Column('discipline_incidentlocdetail', String(79)),
    Column('discipline_offender', String(79)),
    Column('discipline_reporter', String(79)),
    Column('discipline_reporterid', String(79)),
    Column('discipline_victimtype', String(79)),
    Column('discipline_felonyflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_likelyinjuryflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_schoolrulesvioflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_policeinvolvedflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_hearingofficerflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_gangrelatedflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_hatecrimeflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_alcoholrelatedflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_drugrelatedflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_drugtypedetail', String(79)),
    Column('discipline_weaponrelatedflag', Numeric(10, 0, asdecimal=False)),
    Column('discipline_weapontype', String(79)),
    Column('discipline_weapontypenotes', String(79)),
    Column('discipline_moneylossvalue', Float),
    Column('discipline_actiondate', DateTime),
    Column('discipline_actiontaken', String(79)),
    Column('discipline_actiontakendetail', String(79)),
    Column('discipline_durationassigned', Float),
    Column('discipline_durationactual', Float),
    Column('durationchangesource', String(79)),
    Column('discipline_durationnotes', String(79)),
    Column('discipline_sequence', Numeric(10, 0, asdecimal=False)),
    Column('discipline_administratorid', String(79)),
    Column('discipline_actiontakenenddate', DateTime)
)


class Login(Base):
    __tablename__ = 'logins'
    __table_args__ = (
        Index('logins_n6', 'psid', 'logindate'),
        Index('logins_u2', 'id', 'dcid', unique=True)
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    userid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(20))
    pw = Column(String(20))
    psid = Column(String(80))
    ipaddr = Column(Numeric(10, 0, asdecimal=False))
    loginticks = Column(Numeric(10, 0, asdecimal=False))
    logindate = Column(DateTime, index=True)
    logintime = Column(Numeric(10, 0, asdecimal=False))
    logoutdate = Column(DateTime)
    logouttime = Column(Numeric(10, 0, asdecimal=False))
    logoutstatus = Column(Numeric(10, 0, asdecimal=False))
    usertype = Column(Numeric(10, 0, asdecimal=False), index=True)
    hits = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    minutesonline = Column(Float)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    pageviews = Column(Numeric(10, 0, asdecimal=False))
    platform = Column(Numeric(10, 0, asdecimal=False))
    useragent = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    server_instance_id = Column(Numeric(10, 0, asdecimal=False))
    untrustedforwardedfor = Column(String(4000))


class Messagekeymap(Base):
    __tablename__ = 'messagekeymap'
    __table_args__ = (
        Index('messagekeymapu2', 'countryisocode', 'languageisocode', 'messagekey', 'identifier', unique=True),
    )

    messagekeymapid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    countryisocode = Column(ForeignKey('countryisocodelu.countryisocode'), nullable=False, index=True)
    languageisocode = Column(ForeignKey('languageisocodelu.languageisocode'), nullable=False, index=True)
    messagekey = Column(String(256), nullable=False)
    messagetext = Column(Text, nullable=False)
    schoolid = Column(Numeric(asdecimal=False))
    yearid = Column(Numeric(asdecimal=False))
    identifier = Column(String(128))
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    defaulttext = Column(Text)
    mergetext = Column(Text)
    messagesource = Column(String(32), server_default=text("'manual'"))

    countryisocodelu = relationship('Countryisocodelu')
    languageisocodelu = relationship('Languageisocodelu')


class Messagerequestsummary(Base):
    __tablename__ = 'messagerequestsummary'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    inboundrequests = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    inboundrecords = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    pendingoutboundrequests = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    rejectedoutboundrequests = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    pendingoutboundrecords = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    rejectedoutboundrecords = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    schoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Messagestaging(Base):
    __tablename__ = 'messagestaging'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    importstatus = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    institutionnumber = Column(String(30))
    messagedata = Column(Text, nullable=False)
    messageinpdf = Column(LargeBinary)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    solicitflag = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    attachmentcount = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    providerschoolname = Column(String(64))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    requestorid = Column(Numeric(10, 0, asdecimal=False))


t_messageupdaterejected = Table(
    'messageupdaterejected', metadata,
    Column('messageupdaterejectedid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('countryisocode', ForeignKey('countryisocodelu.countryisocode'), nullable=False, index=True),
    Column('languageisocode', ForeignKey('languageisocodelu.languageisocode'), nullable=False, index=True),
    Column('messagekey', String(256), nullable=False),
    Column('messagetext', Text),
    Column('defaulttext', Text),
    Column('whocreated', String(100), nullable=False),
    Column('whencreated', DateTime, nullable=False),
    Column('whomodified', String(100)),
    Column('whenmodified', DateTime)
)


class Metaphone(Base):
    __tablename__ = 'metaphone'

    last_name = Column(String(100), primary_key=True)
    dominant = Column(String(5), nullable=False)
    alternate = Column(String(5))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Mimetype(Base):
    __tablename__ = 'mimetypes'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    suffix = Column(String(20), index=True)
    mime = Column(String(30))


t_mv_pssr_district = Table(
    'mv_pssr_district', metadata,
    Column('districtname', String(250)),
    Column('districtnumber', String(250)),
    Column('districtaddress', String(250)),
    Column('districtcity', String(250)),
    Column('districtstate', String(250)),
    Column('districtzip', String(250)),
    Column('districtcountry', String(250)),
    Column('districtphone', String(250)),
    Column('districtfax', String(250)),
    Column('superintendent', String(250)),
    Column('superintendentphone', String(250)),
    Column('superintendentfax', String(250)),
    Column('superintendentemail', String(250)),
    Column('districttechemail', String(250)),
    Column('districttechphone', String(250)),
    Column('districttechurl', String(250))
)


class Oauthaccesstoken(Base):
    __tablename__ = 'oauthaccesstoken'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    accesstoken = Column(String(64), nullable=False)
    expiresinseconds = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    issuedtime = Column(DateTime, nullable=False)
    pluginconfoauthproviderid = Column(ForeignKey('pluginconfoauthprovider.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    pluginconfoauthprovider = relationship('Pluginconfoauthprovider')


class Oidserverassociationstore(Base):
    __tablename__ = 'oidserverassociationstore'

    handle = Column(String(256), primary_key=True)
    type = Column(String(32))
    mackey = Column(String(256))
    expdate = Column(DateTime)


class Page(Base):
    __tablename__ = 'pages'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    filename = Column(String(60))
    directory = Column(Text)
    security = Column(String(500))
    moddate = Column(DateTime)
    modtime = Column(Numeric(10, 0, asdecimal=False))
    modsecs = Column(Numeric(10, 0, asdecimal=False))
    modifycode = Column(Numeric(10, 0, asdecimal=False))
    path = Column(String(1000))


t_pbcatcol = Table(
    'pbcatcol', metadata,
    Column('pbc_tnam', String(30), nullable=False),
    Column('pbc_tid', Numeric(scale=0, asdecimal=False)),
    Column('pbc_ownr', String(30), nullable=False),
    Column('pbc_cnam', String(30), nullable=False),
    Column('pbc_cid', Numeric(scale=0, asdecimal=False)),
    Column('pbc_labl', String(254)),
    Column('pbc_lpos', Numeric(scale=0, asdecimal=False)),
    Column('pbc_hdr', String(254)),
    Column('pbc_hpos', Numeric(scale=0, asdecimal=False)),
    Column('pbc_jtfy', Numeric(scale=0, asdecimal=False)),
    Column('pbc_mask', String(31)),
    Column('pbc_case', Numeric(scale=0, asdecimal=False)),
    Column('pbc_hght', Numeric(scale=0, asdecimal=False)),
    Column('pbc_wdth', Numeric(scale=0, asdecimal=False)),
    Column('pbc_ptrn', String(31)),
    Column('pbc_bmap', String(1)),
    Column('pbc_init', String(254)),
    Column('pbc_cmnt', String(254)),
    Column('pbc_edit', String(31)),
    Column('pbc_tag', String(254)),
    Index('pbsyscatcoldict_idx', 'pbc_tnam', 'pbc_ownr', 'pbc_cnam', unique=True)
)


t_pbcatedt = Table(
    'pbcatedt', metadata,
    Column('pbe_name', String(30)),
    Column('pbe_edit', String(254)),
    Column('pbe_type', Numeric(scale=0, asdecimal=False)),
    Column('pbe_cntr', Numeric(scale=0, asdecimal=False)),
    Column('pbe_seqn', Numeric(scale=0, asdecimal=False)),
    Column('pbe_flag', Numeric(scale=0, asdecimal=False)),
    Column('pbe_work', String(32)),
    Index('pbsyspbe_idx', 'pbe_name', 'pbe_seqn', unique=True)
)


t_pbcatfmt = Table(
    'pbcatfmt', metadata,
    Column('pbf_name', String(30), unique=True),
    Column('pbf_frmt', String(254)),
    Column('pbf_type', Numeric(scale=0, asdecimal=False), nullable=False),
    Column('pbf_cntr', Numeric(scale=0, asdecimal=False))
)


t_pbcattbl = Table(
    'pbcattbl', metadata,
    Column('pbt_tnam', String(30), nullable=False),
    Column('pbt_tid', Numeric(scale=0, asdecimal=False)),
    Column('pbt_ownr', String(30), nullable=False),
    Column('pbd_fhgt', Numeric(scale=0, asdecimal=False)),
    Column('pbd_fwgt', Numeric(scale=0, asdecimal=False)),
    Column('pbd_fitl', String(1)),
    Column('pbd_funl', String(1)),
    Column('pbd_fchr', Numeric(scale=0, asdecimal=False)),
    Column('pbd_fptc', Numeric(scale=0, asdecimal=False)),
    Column('pbd_ffce', String(18)),
    Column('pbh_fhgt', Numeric(scale=0, asdecimal=False)),
    Column('pbh_fwgt', Numeric(scale=0, asdecimal=False)),
    Column('pbh_fitl', String(1)),
    Column('pbh_funl', String(1)),
    Column('pbh_fchr', Numeric(scale=0, asdecimal=False)),
    Column('pbh_fptc', Numeric(scale=0, asdecimal=False)),
    Column('pbh_ffce', String(18)),
    Column('pbl_fhgt', Numeric(scale=0, asdecimal=False)),
    Column('pbl_fwgt', Numeric(scale=0, asdecimal=False)),
    Column('pbl_fitl', String(1)),
    Column('pbl_funl', String(1)),
    Column('pbl_fchr', Numeric(scale=0, asdecimal=False)),
    Column('pbl_fptc', Numeric(scale=0, asdecimal=False)),
    Column('pbl_ffce', String(18)),
    Column('pbt_cmnt', String(254)),
    Index('pbsyscatpbt_idx', 'pbt_tnam', 'pbt_ownr', unique=True)
)


t_pbcatvld = Table(
    'pbcatvld', metadata,
    Column('pbv_name', String(30), unique=True),
    Column('pbv_vald', String(254)),
    Column('pbv_type', Numeric(scale=0, asdecimal=False)),
    Column('pbv_cntr', Numeric(scale=0, asdecimal=False)),
    Column('pbv_msg', String(254))
)


class PcasAccount(Base):
    __tablename__ = 'pcas_account'

    pcas_accountid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pcas_credentialtypeid = Column(ForeignKey('pcas_credentialtype.pcas_credentialtypeid'), nullable=False, index=True)
    pcas_serviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), nullable=False, unique=True)
    pcas_accounttoken = Column(String(32), nullable=False, unique=True)
    username = Column(String(64), nullable=False)
    credential = Column(String(64))
    isenabled = Column(Numeric(1, 0, asdecimal=False))
    encryptionmode = Column(Numeric(2, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    credentialchangeddate = Column(DateTime, nullable=False, server_default=text("sysdate "))
    islockedout = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    lockedoutreason = Column(String(256))

    pcas_credentialtype = relationship('PcasCredentialtype')
    pcas_service = relationship('PcasService')


class PcasAccountaccesshist(Base):
    __tablename__ = 'pcas_accountaccesshist'

    pcas_accountaccesshistid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    isinvalidusername = Column(Numeric(1, 0, asdecimal=False), nullable=False, index=True, server_default=text("0 "))
    pcas_serviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), nullable=False, index=True)
    usernameattempted = Column(String(64), nullable=False)
    pcas_accountid = Column(ForeignKey('pcas_account.pcas_accountid'), index=True)
    loginattemptdate = Column(DateTime, nullable=False, server_default=text("sysdate "))
    logindelay = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    loginipsource = Column(String(30), nullable=False, index=True, server_default=text("'0.0.0.0' "))
    httpforwardedfor = Column(String(30), nullable=False, server_default=text("'0.0.0.0' "))
    isloginsuccessful = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    isapprovedtodelete = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_account = relationship('PcasAccount')
    pcas_service = relationship('PcasService')


class PcasAccountservicepref(Base):
    __tablename__ = 'pcas_accountservicepref'

    pcas_accountserviceprefid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pcas_accountid = Column(ForeignKey('pcas_account.pcas_accountid'), nullable=False, unique=True)
    name = Column(String(256), nullable=False)
    value = Column(String(256))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_account = relationship('PcasAccount')


class PcasAccountservicerel(Base):
    __tablename__ = 'pcas_accountservicerel'

    pcas_accountid = Column(ForeignKey('pcas_account.pcas_accountid'), primary_key=True, nullable=False)
    pcas_serviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), primary_key=True, nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_account = relationship('PcasAccount')
    pcas_service = relationship('PcasService')


class PcasAccountsession(Base):
    __tablename__ = 'pcas_accountsession'

    pcas_accountsessionid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    loginserviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), index=True)
    logoutserviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), index=True)
    pcas_accountid = Column(ForeignKey('pcas_account.pcas_accountid'), nullable=False, index=True)
    userticket = Column(String(128), nullable=False, unique=True)
    ipaddress = Column(String(32))
    sessionstatus = Column(String(24))
    logintime = Column(DateTime)
    logouttime = Column(DateTime)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_service = relationship('PcasService', primaryjoin='PcasAccountsession.loginserviceid == PcasService.pcas_serviceid')
    pcas_service1 = relationship('PcasService', primaryjoin='PcasAccountsession.logoutserviceid == PcasService.pcas_serviceid')
    pcas_account = relationship('PcasAccount')


class PcasApplicationusertype(Base):
    __tablename__ = 'pcas_applicationusertype'

    pcas_applicationusertypeid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    applicationusertype = Column(String(30), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))


class PcasConfiguration(Base):
    __tablename__ = 'pcas_configuration'

    pcas_configurationid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    configurationname = Column(String(100))
    configurationvalue = Column(String(100))
    pcas_serviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_service = relationship('PcasService')


class PcasCredentialcomplexity(Base):
    __tablename__ = 'pcas_credentialcomplexity'

    pcas_credentialcomplexityid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pcas_serviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), nullable=False, index=True)
    isresetruleenabled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    ismixofcasereq = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    islettersandnumreq = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    isspecialcharacterreq = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    passwordreusecyclenum = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("5 "))
    passwordexpiredays = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("60 "))
    reqcharactercnt = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("7 "))
    expirationwarningdays = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("3 "))
    ishardlockoutenabled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    hardlockoutthreshold = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("5 "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_service = relationship('PcasService')


class PcasCredentialrecoverytoken(Base):
    __tablename__ = 'pcas_credentialrecoverytoken'

    pcas_credentialrecoverytokenid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pcas_accountid = Column(ForeignKey('pcas_account.pcas_accountid'), nullable=False, index=True)
    token = Column(String(30), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_account = relationship('PcasAccount')


class PcasCredentialreuse(Base):
    __tablename__ = 'pcas_credentialreuse'

    pcas_credentialreuseid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pcas_accountid = Column(ForeignKey('pcas_account.pcas_accountid'), nullable=False, index=True)
    credential = Column(String(64))
    credentialchangedate = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_account = relationship('PcasAccount')


class PcasCredentialtype(Base):
    __tablename__ = 'pcas_credentialtype'

    pcas_credentialtypeid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    credentialtypename = Column(String(64), nullable=False, unique=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class PcasDevicetoken(Base):
    __tablename__ = 'pcas_devicetoken'

    pcas_devicetokenid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pcas_accountid = Column(ForeignKey('pcas_account.pcas_accountid'), nullable=False, index=True)
    pcas_serviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), nullable=False, index=True)
    devicetoken = Column(String(64), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    pcas_account = relationship('PcasAccount')
    pcas_service = relationship('PcasService')


class PcasEmailcontact(Base):
    __tablename__ = 'pcas_emailcontact'
    __table_args__ = (
        Index('pcas_emailcontact_n1', 'pcas_accountid', 'pcas_serviceid'),
    )

    pcas_emailcontactid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pcas_serviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), nullable=False, index=True)
    pcas_accountid = Column(ForeignKey('pcas_account.pcas_accountid'), index=True)
    emailaddress = Column(String(256), nullable=False, unique=True, server_default=text("'Invalid Email Address' "))
    externalident = Column(String(32))
    whocreated = Column(String(100))
    whencreated = Column(DateTime)
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    pcas_account = relationship('PcasAccount')
    pcas_service = relationship('PcasService')


class PcasExternalaccountmap(Base):
    __tablename__ = 'pcas_externalaccountmap'

    pcas_externalaccountmapid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    openiduseraccountid = Column(Numeric(20, 0, asdecimal=False), nullable=False)
    applicationusertype = Column(ForeignKey('pcas_applicationusertype.applicationusertype'), nullable=False, index=True)
    pcas_accounttoken = Column(ForeignKey('pcas_account.pcas_accounttoken'), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    pcas_applicationusertype = relationship('PcasApplicationusertype')
    pcas_account = relationship('PcasAccount')


class PcasKeylocator(Base):
    __tablename__ = 'pcas_keylocator'

    pcas_keylocatorid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    locator = Column(String(32), nullable=False, unique=True)
    keytype = Column(String(20), nullable=False)
    keyid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class PcasKeyuserpassword(Base):
    __tablename__ = 'pcas_keyuserpassword'

    pcas_keyuserpasswordid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    username = Column(String(256), nullable=False)
    salt = Column(String(20), nullable=False)
    password = Column(Text, nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class PcasService(Base):
    __tablename__ = 'pcas_service'

    pcas_serviceid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    servicename = Column(String(64), nullable=False, unique=True)
    isenabled = Column(Numeric(1, 0, asdecimal=False))
    isenabledsso = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class PcasServiceticket(Base):
    __tablename__ = 'pcas_serviceticket'

    pcas_serviceticketid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pcas_accountsessionid = Column(ForeignKey('pcas_accountsession.pcas_accountsessionid'), index=True)
    pcas_serviceid = Column(ForeignKey('pcas_service.pcas_serviceid'), nullable=False, index=True)
    serviceticket = Column(String(128), nullable=False, unique=True)
    isenabled = Column(Numeric(1, 0, asdecimal=False))
    ticketcreated = Column(DateTime)
    ticketvalidated = Column(DateTime)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    pcas_accountsession = relationship('PcasAccountsession')
    pcas_service = relationship('PcasService')


class Period(Base):
    __tablename__ = 'period'
    __table_args__ = (
        Index('period_u2', 'id', 'dcid', unique=True),
        Index('period_n4', 'schoolid', 'year_id', 'period_number', 'id')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    year_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    period_number = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(80))
    abbreviation = Column(String(3))
    sort_order = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)


class Permissiongrouplabel(Base):
    __tablename__ = 'permissiongrouplabel'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    applicationcomponentid = Column(ForeignKey('applicationcomponent.id'), nullable=False, index=True)
    label = Column(String(255))
    type = Column(String(255))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    applicationcomponent = relationship('Applicationcomponent')


class Permissiongroupvalue(Base):
    __tablename__ = 'permissiongroupvalue'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    permissiongrouplabelid = Column(ForeignKey('permissiongrouplabel.id'), nullable=False, index=True)
    gendcid = Column(Numeric(asdecimal=False), nullable=False)
    value = Column(String(4000))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    permissiongrouplabel = relationship('Permissiongrouplabel')


class Person(Base):
    __tablename__ = 'person'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)


class Pgassignment(Base):
    __tablename__ = 'pgassignments'
    __table_args__ = (
        Index('pgassignments_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    assignmentid = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(50))
    abbreviation = Column(String(15))
    pgcategoriesid = Column(Numeric(10, 0, asdecimal=False), index=True)
    datedue = Column(DateTime)
    pointspossible = Column(Float)
    weight = Column(Float)
    description = Column(Text)
    type = Column(Numeric(10, 0, asdecimal=False))
    publishstate = Column(Numeric(10, 0, asdecimal=False))
    publishonspecificdate = Column(DateTime)
    publishdaysbeforedue = Column(Numeric(10, 0, asdecimal=False))
    publishscores = Column(Numeric(10, 0, asdecimal=False))
    includeinfinalgrades = Column(Numeric(10, 0, asdecimal=False))
    gradebooktype = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)


class Pgassignmentstandard(Base):
    __tablename__ = 'pgassignmentstandards'
    __table_args__ = (
        Index('pgassignmentstandards_u2', 'pgassignmentsid', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    pgassignmentsid = Column(Numeric(10, 0, asdecimal=False))
    standardsid = Column(Numeric(10, 0, asdecimal=False), index=True)


class Pgcategory(Base):
    __tablename__ = 'pgcategories'
    __table_args__ = (
        Index('pgcategories_u2', 'id', 'dcid', unique=True),
        Index('pgcategories_n1', 'sectionid', 'name')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(50))
    abbreviation = Column(String(15))
    defaultptsposs = Column(Float)
    description = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Pgcommentbank(Base):
    __tablename__ = 'pgcommentbank'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    code = Column(String(10), index=True)
    category = Column(String(30))
    comment_value = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Pgfinalgrade(Base):
    __tablename__ = 'pgfinalgrades'
    __table_args__ = (
        Index('pgfinalgrades_u2', 'studentid', 'sectionid', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    finalgradename = Column(String(8))
    grade = Column(String(7))
    citizenship = Column(String(7))
    percent = Column(Float)
    points = Column(Float)
    pointspossible = Column(Float)
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    comment_value = Column(Text)
    lastgradeupdate = Column(DateTime)
    varcredit = Column(Float, server_default=text("(0)"))
    overridefg = Column(String(2))
    gradebooktype = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))
    calculatedgrade = Column(String(7))
    calculatedpercent = Column(Float)
    isincomplete = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    isexempt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))


class Pgfinalgradessetup(Base):
    __tablename__ = 'pgfinalgradessetup'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    abbreviation = Column(String(7))
    begindate = Column(DateTime)
    changegradeto = Column(String(20))
    citizenshipasmtname = Column(String(50))
    currentgrade = Column(Numeric(10, 0, asdecimal=False))
    displayonspreadsheet = Column(Numeric(10, 0, asdecimal=False))
    duedate = Column(DateTime)
    enddate = Column(DateTime)
    excludedmarks = Column(String(40))
    factorinfos = Column(LargeBinary)
    factornumscorestodrop = Column(LargeBinary)
    factortypes = Column(LargeBinary)
    factorweights = Column(LargeBinary)
    fromserver = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(7))
    numattpoints = Column(Float)
    numfactors = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    serverid = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)


class Pggradescale(Base):
    __tablename__ = 'pggradescales'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    modifycode = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)


class Pggradescalesmark(Base):
    __tablename__ = 'pggradescalesmark'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    cutoff = Column(Float)
    description = Column(String(50))
    pggradescaleid = Column(Numeric(10, 0, asdecimal=False), index=True)
    mark = Column(String(6))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    value = Column(Float)


class Pgincomingqueue(Base):
    __tablename__ = 'pgincomingqueue'
    __table_args__ = (
        Index('pgincomingqueue_n5', 'command', 'server_instanceid', 'createdt', 'createtm', 'timereceived'),
        Index('pgincomingqueue_n4', 'command', 'processnum', 'sectionid'),
        Index('pgincomingqueue_n2', 'createdt', 'createtm'),
        Index('pgincomingqueue_idx1', 'processnum', 'sectionid')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    pgversion = Column(Numeric(10, 0, asdecimal=False))
    teacherid = Column(Numeric(10, 0, asdecimal=False))
    command = Column(String(80))
    timereceived = Column(Numeric(10, 0, asdecimal=False))
    data = Column(Text)
    blobdata = Column(LargeBinary)
    createtm = Column(Numeric(10, 0, asdecimal=False))
    createdt = Column(DateTime)
    server_instanceid = Column(Numeric(10, 0, asdecimal=False), index=True)
    processnum = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False))


class Pgnotification(Base):
    __tablename__ = 'pgnotification'
    __table_args__ = (
        Index('pgnotification_u2', 'teacherid', 'sectionid', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    category = Column(String(30), index=True)
    identifier = Column(String(80))
    ntf_value = Column(String(50))
    teacherid = Column(Numeric(10, 0, asdecimal=False))


class Pgpreference(Base):
    __tablename__ = 'pgpreferences'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    textdata = Column(LargeBinary)
    textfield = Column(LargeBinary)
    longintdata = Column(LargeBinary)
    longintfield = Column(LargeBinary)
    datedata = Column(LargeBinary)
    datefield = Column(LargeBinary)
    booleandata = Column(LargeBinary)
    booleanfield = Column(LargeBinary)
    blobfield = Column(LargeBinary)
    blobdata = Column(LargeBinary)
    id = Column(Numeric(10, 0, asdecimal=False))


class Pgscore(Base):
    __tablename__ = 'pgscores'
    __table_args__ = (
        Index('pgscores_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    pgassignmentsid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    percent = Column(Float, index=True)
    percentstr = Column(String(7), index=True)
    score = Column(Float)
    scorestr = Column(String(7))
    grade = Column(String(7))
    comment_value = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Pgsection(Base):
    __tablename__ = 'pgsections'
    __table_args__ = (
        Index('pgsections_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    custfieldname1 = Column(String(80))
    custfieldname2 = Column(String(80))
    custfieldname3 = Column(String(80))
    custfieldname4 = Column(String(80))
    custfieldname5 = Column(String(80))
    id = Column(Numeric(10, 0, asdecimal=False))


class Pgstudent(Base):
    __tablename__ = 'pgstudents'
    __table_args__ = (
        Index('pgstudents_n1', 'studentid', 'sectionid', 'schoolid', 'yearid'),
        Index('pgstudents_u2', 'id', 'dcid', unique=True)
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    custfield1 = Column(String(40))
    custfield2 = Column(String(40))
    custfield3 = Column(String(40))
    custfield4 = Column(String(40))
    custfield5 = Column(String(40))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False))
    id = Column(Numeric(10, 0, asdecimal=False))


class Phonelog(Base):
    __tablename__ = 'phonelog'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    date_value = Column(DateTime, index=True)
    starttime = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    optionschosen = Column(String(40))
    entrytype = Column(Numeric(10, 0, asdecimal=False))
    duration = Column(Float)
    startticks = Column(Numeric(10, 0, asdecimal=False))
    logtype = Column(Numeric(10, 0, asdecimal=False))


class PisaSession(Base):
    __tablename__ = 'pisa_session'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    conversationcredentials = Column(String(255))
    sessiontimestamp = Column(DateTime)


class Plannedrequest(Base):
    __tablename__ = 'plannedrequest'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    coursenumber = Column(String(20), nullable=False)
    gradelevel = Column(Numeric(4, 0, asdecimal=False), nullable=False)
    registreqid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    studentcomment = Column(String(1000))


class Pluginbackupdatum(Base):
    __tablename__ = 'pluginbackupdata'

    pluginbackupdataid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pluginname = Column(String(40), nullable=False)
    pluginidentifier = Column(String(256), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER      "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER      "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))


class Pluginconfigdefault(Base):
    __tablename__ = 'pluginconfigdefaults'
    __table_args__ = (
        Index('pluginconfigdefaults_uk1', 'plugindefid', 'plugindefinterfacemapid', 'name', 'regioncode', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    plugindefinterfacemapid = Column(ForeignKey('plugindefinterfacemap.id'), index=True)
    name = Column(String(40), nullable=False)
    ispsadminreadonly = Column(Numeric(3, 0, asdecimal=False))
    isvaluerequired = Column(Numeric(3, 0, asdecimal=False))
    value = Column(Text)
    propertytype = Column(String(100))
    propertyresolver = Column(String(256))
    regioncode = Column(String(20), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    plugindef = relationship('Plugindef')
    plugindefinterfacemap = relationship('Plugindefinterfacemap')


class Pluginconfigoidprovider(Base):
    __tablename__ = 'pluginconfigoidprovider'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    relyingpartyname = Column(String(40), nullable=False, unique=True)
    relyingpartyhost = Column(String(256), nullable=False)
    relyingpartyport = Column(Numeric(5, 0, asdecimal=False), nullable=False)
    relyingpartypath = Column(String(256))
    whocreated = Column(String(30), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(30), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    isrelyingpartypathrequired = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("1 "))

    plugindef = relationship('Plugindef')


class Pluginconfigwstrustbridge(Base):
    __tablename__ = 'pluginconfigwstrustbridge'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, unique=True)
    securityattributename = Column(String(40))
    realm = Column(String(256))
    passiveaddress = Column(String(256))
    idpsigningcert = Column(String(256))
    encryptioncert = Column(String(256))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    plugindef = relationship('Plugindef')


class Pluginconfoauthconsumer(Base):
    __tablename__ = 'pluginconfoauthconsumer'
    __table_args__ = (
        Index('pluginconfoauthconsumer_u1', 'plugindefid', 'clientid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False)
    clientid = Column(String(100))
    clientsecret = Column(String(100))
    accesstokenurl = Column(String(100))
    ispersisted = Column(Numeric(3, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    credentialtype = Column(String(30))
    privatekeyjson = Column(Text)
    privatekeyp12 = Column(LargeBinary)
    credentialuser = Column(String(250))

    plugindef = relationship('Plugindef')


class Pluginconfoauthprovider(Base):
    __tablename__ = 'pluginconfoauthprovider'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    accountidentifier = Column(ForeignKey('pcas_account.pcas_accounttoken'), nullable=False, unique=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    pcas_account = relationship('PcasAccount')
    plugindef = relationship('Plugindef')


class Pluginconfwebcustompage(Base):
    __tablename__ = 'pluginconfwebcustompage'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, unique=True)
    pagename = Column(String(40), nullable=False)
    pagepath = Column(String(256), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    plugindef = relationship('Plugindef')


class Pluginconfwssoapclient(Base):
    __tablename__ = 'pluginconfwssoapclient'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    pluginconfwssoapproviderid = Column(ForeignKey('pluginconfwssoapprovider.id'), nullable=False, unique=True)
    clientcertificatealias = Column(String(256))
    clientname = Column(String(256))
    clientaddress = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    pluginconfwssoapprovider = relationship('Pluginconfwssoapprovider')


class Pluginconfwssoapconsumer(Base):
    __tablename__ = 'pluginconfwssoapconsumer'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, unique=True)
    consumername = Column(String(40), nullable=False)
    consumercertificatealias = Column(String(256))
    serverurl = Column(String(256), nullable=False)
    servercertificatealias = Column(String(256))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    plugindef = relationship('Plugindef')


class Pluginconfwssoapprovider(Base):
    __tablename__ = 'pluginconfwssoapprovider'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    providername = Column(String(40), nullable=False)
    publishedport = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    plugindef = relationship('Plugindef')


class Plugindef(Base):
    __tablename__ = 'plugindef'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    classname = Column(String(256), nullable=False)
    description = Column(String(256))
    version = Column(String(20))
    minrequiredpsversion = Column(String(20))
    isenabled = Column(Numeric(3, 0, asdecimal=False))
    isdeletable = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    isstaterestricted = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    resetflag = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    isdistrictrestricted = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    isschoolrestricted = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    islinkdetaildisplayed = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    pluginregistrationid = Column(ForeignKey('pluginregistration.id'), index=True)
    ishidden = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    pluginidentifier = Column(String(256), unique=True)
    isguardianrestrictionallowed = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    pluginregistration = relationship('Pluginregistration')


class Plugindefaccessrequest(Base):
    __tablename__ = 'plugindefaccessrequest'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    reqtype = Column(String(1), nullable=False)
    target = Column(String(256), nullable=False)
    accesslevel = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    status = Column(String(1), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    plugindef = relationship('Plugindef')


class Plugindefasset(Base):
    __tablename__ = 'plugindefasset'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    type = Column(String(128))
    assetid = Column(ForeignKey('psm_asset.id'), nullable=False, index=True)
    whocreated = Column(String(30), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("CURRENT_DATE"))
    whomodified = Column(String(30))
    whenmodified = Column(DateTime)

    psm_asset = relationship('PsmAsset')
    plugindef = relationship('Plugindef')


class Plugindefentityattribmap(Base):
    __tablename__ = 'plugindefentityattribmap'
    __table_args__ = (
        Index('plugindefentityattribmap_u1', 'plugindefid', 'pluginentityattribid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False)
    pluginentityattribid = Column(ForeignKey('pluginentityattrib.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    plugindef = relationship('Plugindef')
    pluginentityattrib = relationship('Pluginentityattrib')


class Plugindefinlineusertypemap(Base):
    __tablename__ = 'plugindefinlineusertypemap'
    __table_args__ = (
        Index('plugindefinlineusertypemap_u1', 'plugindefid', 'pluginusertypeid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False)
    pluginusertypeid = Column(ForeignKey('plugininlineusertype.id'), nullable=False)
    inlineauthnewwindow = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    plugindef = relationship('Plugindef')
    plugininlineusertype = relationship('Plugininlineusertype')


class Plugindefinterfacemap(Base):
    __tablename__ = 'plugindefinterfacemap'
    __table_args__ = (
        Index('plugindefinterfacemap_u2', 'plugindefid', 'plugininterfaceid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False)
    plugininterfaceid = Column(ForeignKey('plugininterface.id'), nullable=False, index=True)
    sortorder = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    isoptional = Column(Numeric(3, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    plugindef = relationship('Plugindef')
    plugininterface = relationship('Plugininterface')


class Plugindefrole(Base):
    __tablename__ = 'plugindefrole'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, unique=True)
    roledefid = Column(ForeignKey('roledef.id'), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    plugindef = relationship('Plugindef')
    roledef = relationship('Roledef')


class Plugindefschoolsmap(Base):
    __tablename__ = 'plugindefschoolsmap'
    __table_args__ = (
        Index('plugindefschoolsmap_u1', 'serviceid_usertype', 'schoolid', 'plugindefid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, index=True)
    schoolid = Column(ForeignKey('schools.school_number'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    serviceid_usertype = Column(ForeignKey('pcas_service.pcas_serviceid'))

    plugindef = relationship('Plugindef')
    school = relationship('School')
    pcas_service = relationship('PcasService')


class Plugindefstatesmap(Base):
    __tablename__ = 'plugindefstatesmap'
    __table_args__ = (
        Index('plugindefstatesmap_u2', 'plugindefid', 'statesid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False)
    statesid = Column(ForeignKey('states.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    plugindef = relationship('Plugindef')
    state = relationship('State')


class Pluginentity(Base):
    __tablename__ = 'pluginentity'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Pluginentityattrib(Base):
    __tablename__ = 'pluginentityattrib'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    pluginentityid = Column(ForeignKey('pluginentity.id'), nullable=False, unique=True)
    identitybuilderclass = Column(String(256), nullable=False)
    isdefault = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    name = Column(String(256), nullable=False)
    restapiidtype = Column(String(256))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    pluginentity = relationship('Pluginentity')


class Plugineventsubscriber(Base):
    __tablename__ = 'plugineventsubscriber'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    authtype = Column(String(100), nullable=False)
    secretkey = Column(String(1000))
    url = Column(String(500), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    isselfnotificationincluded = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    plugindef = relationship('Plugindef')


class Plugineventtype(Base):
    __tablename__ = 'plugineventtype'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    entityname = Column(String(100), nullable=False)
    eventtype = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Plugininlineusertype(Base):
    __tablename__ = 'plugininlineusertype'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    usertype = Column(String(50), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Plugininterface(Base):
    __tablename__ = 'plugininterface'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    type = Column(String(40), nullable=False)
    description = Column(String(256))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Pluginknownhost(Base):
    __tablename__ = 'pluginknownhost'

    pluginknownhostid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    institutionid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    host = Column(String(80), nullable=False, unique=True)
    hostkey = Column(LargeBinary)
    hostkeytype = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Pluginlink(Base):
    __tablename__ = 'pluginlink'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    title = Column(String(256))
    linktext = Column(String(100), nullable=False)
    path = Column(String(1000), nullable=False)
    plugindefinterfacemapid = Column(ForeignKey('plugindefinterfacemap.id'), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    isrolerequired = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    errorpath = Column(String(1000))

    plugindefinterfacemap = relationship('Plugindefinterfacemap')


class Pluginlinkcontext(Base):
    __tablename__ = 'pluginlinkcontext'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    contextname = Column(String(20))
    location = Column(String(256), nullable=False)
    pluginlinkid = Column(ForeignKey('pluginlink.id'), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    type = Column(String(20), server_default=text("'external' "))

    pluginlink = relationship('Pluginlink')


class Pluginlinkrolecapmap(Base):
    __tablename__ = 'pluginlinkrolecapmap'
    __table_args__ = (
        Index('pluginlinkrolecapmap_u1', 'pluginlinkid', 'roleavailablecapabilityid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pluginlinkid = Column(ForeignKey('pluginlink.id'), nullable=False)
    roleavailablecapabilityid = Column(ForeignKey('roleavailablecapability.id'), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    pluginlink = relationship('Pluginlink')
    roleavailablecapability = relationship('Roleavailablecapability')


class Pluginpublisher(Base):
    __tablename__ = 'pluginpublisher'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    plugindefid = Column(ForeignKey('plugindef.id'), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    email = Column(String(40), nullable=False)
    whocreated = Column(String(30), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(30), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    publisheridentifier = Column(String(256))

    plugindef = relationship('Plugindef')


class Pluginregistration(Base):
    __tablename__ = 'pluginregistration'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    registrationurl = Column(String(1000))
    callbackdata = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    isregisteratstartup = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))


class Pluginregistrationparam(Base):
    __tablename__ = 'pluginregistrationparam'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    pluginregistrationid = Column(ForeignKey('pluginregistration.id'), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    value = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    pluginregistration = relationship('Pluginregistration')


class Pluginresourceentity(Base):
    __tablename__ = 'pluginresourceentity'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    resourcepath = Column(String(100), nullable=False)
    entityname = Column(String(100), nullable=False)
    fields = Column(String(1000), nullable=False)
    ispriorstate = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(30), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(30), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Pluginsubscribereventtype(Base):
    __tablename__ = 'pluginsubscribereventtype'
    __table_args__ = (
        Index('pluginsubscribereventtype_u1', 'plugineventsubscriberid', 'plugineventtypeid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    plugineventsubscriberid = Column(ForeignKey('plugineventsubscriber.id'), nullable=False)
    plugineventtypeid = Column(ForeignKey('plugineventtype.id'), nullable=False, index=True)
    filter = Column(String(500))
    subscriptionresourcepath = Column(String(1000), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    plugineventsubscriber = relationship('Plugineventsubscriber')
    plugineventtype = relationship('Plugineventtype')


class Pluginurlendpoint(Base):
    __tablename__ = 'pluginurlendpoint'

    pluginurlendpointid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    institutionid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(1000))
    protocol = Column(String(5), nullable=False)
    server = Column(String(80), nullable=False)
    port = Column(Numeric(6, 0, asdecimal=False))
    path = Column(String(256))
    keylocator = Column(ForeignKey('pcas_keylocator.locator'), nullable=False, index=True)
    isinput = Column(Numeric(1, 0, asdecimal=False))
    isoutput = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    pcas_keylocator = relationship('PcasKeylocator')


class Postsecondary(Base):
    __tablename__ = 'postsecondary'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    post_status = Column(String(50))
    completion_type = Column(String(40))
    completion_dt = Column(DateTime)
    post_hs_plan = Column(String(50))
    post_hs_actual = Column(String(50))
    college_type = Column(String(20))
    graduation_yr = Column(Numeric(10, 0, asdecimal=False))
    sched_graduation_yr = Column(Numeric(10, 0, asdecimal=False))
    class_of = Column(Numeric(10, 0, asdecimal=False))
    grad_school_name = Column(String(60))
    graduated_rank = Column(Numeric(10, 0, asdecimal=False))
    diploma_type = Column(String(2))


class Pref(Base):
    __tablename__ = 'prefs'
    __table_args__ = (
        Index('prefs_n6', 'schoolid', 'yearid'),
        Index('prefs_u2', 'id', 'dcid', unique=True)
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), index=True)
    value = Column(Text)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    userid = Column(Numeric(10, 0, asdecimal=False), index=True)
    psguid = Column(String(50), unique=True)


class Program(Base):
    __tablename__ = 'program'
    __table_args__ = (
        Index('program_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(32))
    description = Column(Text)
    effective_start_dt = Column(DateTime)
    effective_end_dt = Column(DateTime)
    program_num = Column(String(32))


t_ps_adaadm_daily_ctod = Table(
    'ps_adaadm_daily_ctod', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_daily_ttod = Table(
    'ps_adaadm_daily_ttod', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_defaults_all = Table(
    'ps_adaadm_defaults_all', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_interval_ttod = Table(
    'ps_adaadm_interval_ttod', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_meeting_ptod = Table(
    'ps_adaadm_meeting_ptod', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('periodcount', Numeric(asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_meeting_ptop = Table(
    'ps_adaadm_meeting_ptop', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('daypartname', String(40)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('periodcount', Numeric(asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_meeting_ptop_curyear = Table(
    'ps_adaadm_meeting_ptop_curyear', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('daypartname', String(40)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('periodcount', Numeric(asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_meeting_ptop_prevyr = Table(
    'ps_adaadm_meeting_ptop_prevyr', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('daypartname', String(40)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('periodcount', Numeric(asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_meeting_ttod = Table(
    'ps_adaadm_meeting_ttod', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_meeting_ttop = Table(
    'ps_adaadm_meeting_ttop', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('daypartname', String(40)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_meeting_ttop_curyear = Table(
    'ps_adaadm_meeting_ttop_curyear', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('daypartname', String(40)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_meeting_ttop_prevyr = Table(
    'ps_adaadm_meeting_ttop_prevyr', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('daypartname', String(40)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_time_ttod = Table(
    'ps_adaadm_time_ttod', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_adaadm_timeinter_ttod = Table(
    'ps_adaadm_timeinter_ttod', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('total_minutes', Numeric(asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_ps_attendance_daily = Table(
    'ps_attendance_daily', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float),
    Column('count_for_adm', Numeric(10, 0, asdecimal=False))
)


t_ps_attendance_interval = Table(
    'ps_attendance_interval', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('att_interval', Numeric(10, 0, asdecimal=False)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('ccid', Numeric(10, 0, asdecimal=False)),
    Column('cc_schoolid', Numeric(10, 0, asdecimal=False)),
    Column('dropped', Numeric(asdecimal=False)),
    Column('periodid', Numeric(10, 0, asdecimal=False)),
    Column('period_abbreviation', String(3)),
    Column('period_number', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('section_number', String(10)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_ps_attendance_meeting = Table(
    'ps_attendance_meeting', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('att_interval', Numeric(10, 0, asdecimal=False)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('ccid', Numeric(10, 0, asdecimal=False)),
    Column('cc_schoolid', Numeric(10, 0, asdecimal=False)),
    Column('dropped', Numeric(asdecimal=False)),
    Column('periodid', Numeric(10, 0, asdecimal=False)),
    Column('period_abbreviation', String(3)),
    Column('period_number', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('section_number', String(10)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float),
    Column('course_credit_points', Float)
)


t_ps_attendance_meetinter = Table(
    'ps_attendance_meetinter', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('att_interval', Numeric(10, 0, asdecimal=False)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('ccid', Numeric(10, 0, asdecimal=False)),
    Column('cc_schoolid', Numeric(10, 0, asdecimal=False)),
    Column('dropped', Numeric(asdecimal=False)),
    Column('periodid', Numeric(10, 0, asdecimal=False)),
    Column('period_abbreviation', String(3)),
    Column('period_number', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('section_number', String(10)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_ps_attendance_summary = Table(
    'ps_attendance_summary', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('presence_status_cd', String(10)),
    Column('qty', Numeric(asdecimal=False))
)


t_ps_attendance_time = Table(
    'ps_attendance_time', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_ps_attendance_timeinter = Table(
    'ps_attendance_timeinter', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('att_interval', Numeric(10, 0, asdecimal=False)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('ccid', Numeric(10, 0, asdecimal=False)),
    Column('cc_schoolid', Numeric(asdecimal=False)),
    Column('periodid', Numeric(asdecimal=False)),
    Column('period_abbreviation', String(3)),
    Column('period_number', Numeric(asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_ps_calendar_day = Table(
    'ps_calendar_day', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('date_value', DateTime),
    Column('a', Numeric(10, 0, asdecimal=False)),
    Column('b', Numeric(10, 0, asdecimal=False)),
    Column('c', Numeric(10, 0, asdecimal=False)),
    Column('d', Numeric(10, 0, asdecimal=False)),
    Column('e', Numeric(10, 0, asdecimal=False)),
    Column('f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('membershipvalue', Float),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('scheduleid', String(20)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(7)),
    Column('interval_duration', Text)
)


t_ps_class_meeting = Table(
    'ps_class_meeting', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('termid', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('course_number', String(11)),
    Column('dateenrolled', DateTime),
    Column('dateleft', DateTime),
    Column('date_value', DateTime),
    Column('periodid', Numeric(10, 0, asdecimal=False)),
    Column('period_number', Numeric(10, 0, asdecimal=False)),
    Column('section_number', String(10)),
    Column('attendance_type_code', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('start_time', Numeric(10, 0, asdecimal=False)),
    Column('end_time', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_letter', String(2)),
    Column('dropped', Numeric(asdecimal=False)),
    Column('take_attendance', Numeric(asdecimal=False)),
    Column('attendance_code_id', Numeric(asdecimal=False)),
    Column('att_code', String(10)),
    Column('course_credit_points', Numeric(asdecimal=False))
)


class PsCommonCode(Base):
    __tablename__ = 'ps_common_code'
    __table_args__ = (
        Index('pscmcd_fk01_indx', 'ps_common_code_id', 'ps_group', 'category'),
    )

    ps_common_code_id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    ps_group = Column(String(30), nullable=False)
    category = Column(String(50), nullable=False)
    code = Column(String(30), nullable=False)
    description = Column(String(400))
    effective_startdate = Column(DateTime, server_default=text("sysdate"))
    effective_enddate = Column(DateTime, server_default=text("to_date('09-Sep-9999', 'DD-Mon-YYYY')"))
    sortorder = Column(Numeric(4, 0, asdecimal=False))
    alt_report_code = Column(String(50))
    created_by = Column(String(30), nullable=False)
    created_ts = Column(DateTime, nullable=False)
    last_modified_by = Column(String(30), nullable=False)
    last_modified_ts = Column(DateTime, nullable=False)
    default_value = Column(Numeric(2, 0, asdecimal=False))
    parentcategoryid = Column(Numeric(11, 0, asdecimal=False))


t_ps_daily_att = Table(
    'ps_daily_att', metadata,
    Column('districtnumber', Text),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('insession', String(1)),
    Column('attendance_type', String(1)),
    Column('potential_periods', String(0)),
    Column('periods_present', String(0)),
    Column('daily_att', String(10)),
    Column('entrydate', DateTime),
    Column('exitdate', DateTime),
    Column('year_id', Numeric(10, 0, asdecimal=False))
)


t_ps_enrollment = Table(
    'ps_enrollment', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('track', String(20)),
    Column('entrydate', DateTime),
    Column('exitdate', DateTime)
)


t_ps_enrollment_all = Table(
    'ps_enrollment_all', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('entrydate', DateTime),
    Column('entrycode', String(20)),
    Column('exitdate', DateTime),
    Column('exitcode', String(20)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(asdecimal=False)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('membershipshare', Float),
    Column('track', String(20)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('yearid', Numeric(asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(4000))
)


t_ps_enrollment_prog = Table(
    'ps_enrollment_prog', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('entrydate', DateTime),
    Column('entrycode', String(0)),
    Column('exitdate', DateTime),
    Column('exitcode', String(15)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False))
)


t_ps_enrollment_reg = Table(
    'ps_enrollment_reg', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('entrydate', DateTime),
    Column('entrycode', String(20)),
    Column('exitdate', DateTime),
    Column('exitcode', String(20)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('membershipshare', Float),
    Column('track', String(20)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('yearid', Numeric(asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(4000))
)


t_ps_enrollment_sif = Table(
    'ps_enrollment_sif', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(asdecimal=False)),
    Column('entrydate', DateTime),
    Column('exitdate', DateTime),
    Column('leavedate', DateTime),
    Column('entrycode', String(20)),
    Column('exitcode', String(20)),
    Column('noshow', Numeric(asdecimal=False))
)


t_ps_membership_defaults = Table(
    'ps_membership_defaults', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('studentmembership', Float),
    Column('calendarmembership', Float),
    Column('student_track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(30)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('potential_periods_present', Numeric(10, 0, asdecimal=False)),
    Column('potential_minutes_present', Numeric(10, 0, asdecimal=False)),
    Column('periods_absent', Numeric(10, 0, asdecimal=False)),
    Column('minutes_absent', Numeric(10, 0, asdecimal=False)),
    Index('ps_membership_defaultsidx2', 'schoolid', 'calendardate'),
    Index('ps_membership_defaultsidx3', 'studentid', 'schoolid', 'calendardate')
)


t_ps_membership_prog = Table(
    'ps_membership_prog', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('studentmembership', Numeric(asdecimal=False)),
    Column('calendarmembership', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(4000)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False))
)


t_ps_membership_reg = Table(
    'ps_membership_reg', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('studentmembership', Numeric(asdecimal=False)),
    Column('calendarmembership', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(4000)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(asdecimal=False))
)


t_ps_period_att = Table(
    'ps_period_att', metadata,
    Column('districtnumber', Text),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('date_value', DateTime),
    Column('insession', String(1)),
    Column('attendance_type', String(1)),
    Column('potential_periods', Numeric(asdecimal=False)),
    Column('periods_absent', Numeric(asdecimal=False)),
    Column('daily_att', String(0)),
    Column('entrydate', DateTime),
    Column('exitdate', DateTime),
    Column('year_id', Numeric(10, 0, asdecimal=False))
)


t_ps_schoolenrollment = Table(
    'ps_schoolenrollment', metadata,
    Column('id', Numeric(asdecimal=False)),
    Column('sourceid', Numeric(10, 0, asdecimal=False)),
    Column('sourcedcid', Numeric(10, 0, asdecimal=False)),
    Column('sourcetable', String(13)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('schoolname', String(60)),
    Column('entrydate', DateTime),
    Column('entrycode', String(20)),
    Column('exitdate', DateTime),
    Column('exitcode', String(20)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(asdecimal=False)),
    Column('schooladdress', String(79)),
    Column('schoolcity', String(79)),
    Column('schoolcountry', String(79)),
    Column('schoolfax', String(31)),
    Column('schoolphone', String(31)),
    Column('schoolstate', String(79)),
    Column('schoolzip', String(79)),
    Column('countyname', String(79)),
    Column('principal', String(79)),
    Column('principalphone', String(31)),
    Column('principalemail', String(79)),
    Column('asstprincipal', String(79)),
    Column('asstprincipalphone', String(31)),
    Column('asstprincipalemail', String(79))
)


t_ps_userdefaultgroup = Table(
    'ps_userdefaultgroup', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('groupvalue', Numeric(10, 0, asdecimal=False))
)


t_ps_usergroup = Table(
    'ps_usergroup', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('groupvalue', Numeric(asdecimal=False))
)


t_ps_userschoolgroup = Table(
    'ps_userschoolgroup', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('groupvalue', Numeric(asdecimal=False))
)


class PsWritebackaudittrail(Base):
    __tablename__ = 'ps_writebackaudittrail'
    __table_args__ = (
        Index('ps_writebackaudittrail_n1', 'transactionsource', 'sourcetransactiontype', 'sourcetransactionident'),
        Index('ps_writebackaudittrail_n2', 'updatedtablename', 'updatedcolumnname')
    )

    ps_writebackaudittrailid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    transactionsource = Column(String(32), nullable=False, server_default=text("'Invalid Source' "))
    sourcetransactiontype = Column(String(30), nullable=False, server_default=text("'Invalid Type' "))
    sourcetransactionident = Column(String(32), nullable=False, server_default=text("'Invalid Transaction ID' "))
    sourceobjectident = Column(String(32), nullable=False, server_default=text("'No Related External Object' "))
    sourceobjecttypeid = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    school_number = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    dmlactiontype = Column(String(30), nullable=False, server_default=text("'UPDATE' "))
    updatedtablename = Column(String(30), nullable=False)
    updatedcolumnname = Column(String(50), nullable=False)
    updatedclobpairname = Column(String(50))
    updatedrowprimarykey = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    updatedrowsecondarykey = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    previousnumberval = Column(Numeric(19, 0, asdecimal=False))
    previouscharval = Column(String(4000))
    previousclobval = Column(Text)
    previoustimestampval = Column(DateTime)
    newnumberval = Column(Numeric(19, 0, asdecimal=False))
    newcharval = Column(String(4000))
    newclobval = Column(Text)
    newtimestampval = Column(DateTime)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class PsmAccount(Base):
    __tablename__ = 'psm_account'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))
    isenabled = Column(Numeric(1, 0, asdecimal=False))
    islocked = Column(Numeric(1, 0, asdecimal=False))
    passwordlastchanged = Column(DateTime)
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(500))
    phone = Column(String(30))
    accountidentifier = Column(String(32), index=True)


class PsmAccountdistrictassoc(Base):
    __tablename__ = 'psm_accountdistrictassoc'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    accountid = Column(ForeignKey('psm_account.id'), index=True)
    districtid = Column(ForeignKey('psm_district.id'), index=True)

    psm_account = relationship('PsmAccount')
    psm_district = relationship('PsmDistrict')


class PsmAccountlegacyteacher(Base):
    __tablename__ = 'psm_accountlegacyteacher'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    teachersdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    accountid = Column(ForeignKey('psm_account.id'), nullable=False, unique=True)

    psm_account = relationship('PsmAccount')


class PsmAccountpermissionrole(Base):
    __tablename__ = 'psm_accountpermissionrole'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    accountid = Column(ForeignKey('psm_account.id'), index=True)
    permissionroleid = Column(ForeignKey('psm_permissionrole.id'), index=True)

    psm_account = relationship('PsmAccount')
    psm_permissionrole = relationship('PsmPermissionrole')


class PsmAccountschoolassoc(Base):
    __tablename__ = 'psm_accountschoolassoc'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    accountid = Column(ForeignKey('psm_account.id'), index=True)
    schoolid = Column(ForeignKey('psm_school.id'), index=True)

    psm_account = relationship('PsmAccount')
    psm_school = relationship('PsmSchool')


class PsmAccountsecurityquestion(Base):
    __tablename__ = 'psm_accountsecurityquestion'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    question = Column(String(256))
    answer = Column(String(256))
    accountid = Column(ForeignKey('psm_account.id'), index=True)

    psm_account = relationship('PsmAccount')


class PsmAccountsession(Base):
    __tablename__ = 'psm_accountsession'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    conversationcredentials = Column(String(256))
    lastactivetimestamp = Column(DateTime, index=True)
    accountid = Column(ForeignKey('psm_account.id'), index=True)
    applicationcode = Column(Numeric(19, 0, asdecimal=False), server_default=text("0"))
    teacherid = Column(ForeignKey('psm_teacher.id'), index=True, server_default=text("0"))

    psm_account = relationship('PsmAccount')
    psm_teacher = relationship('PsmTeacher')


class PsmAccountsubjectassoc(Base):
    __tablename__ = 'psm_accountsubjectassoc'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    subjectareaid = Column(ForeignKey('psm_subjectarea.id'), index=True)
    accountid = Column(ForeignKey('psm_account.id'), index=True)

    psm_account = relationship('PsmAccount')
    psm_subjectarea = relationship('PsmSubjectarea')


class PsmAsset(Base):
    __tablename__ = 'psm_asset'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    assetfolder_id = Column(ForeignKey('psm_assetfolder.id'), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    mime_type = Column(String(50))
    is_binary = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    lastmodified_by = Column(String(64), nullable=False)
    lastmodified_ts = Column(DateTime, nullable=False)
    created_by = Column(String(64), nullable=False)
    created_ts = Column(DateTime, nullable=False)

    assetfolder = relationship('PsmAssetfolder')


class PsmAssetcontent(Base):
    __tablename__ = 'psm_assetcontent'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    asset_id = Column(ForeignKey('psm_asset.id'), nullable=False, index=True)
    status = Column(String(1), nullable=False)
    blob_content = Column(LargeBinary)
    clob_content = Column(Text)
    lastmodified_by = Column(String(64), nullable=False)
    lastmodified_ts = Column(DateTime, nullable=False)
    created_by = Column(String(64), nullable=False)
    created_ts = Column(DateTime, nullable=False)

    asset = relationship('PsmAsset')


class PsmAssetcontentarchive(Base):
    __tablename__ = 'psm_assetcontentarchive'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    asset_id = Column(ForeignKey('psm_asset.id'), nullable=False, index=True)
    blob_content = Column(LargeBinary)
    clob_content = Column(Text)
    lastmodified_by = Column(String(64), nullable=False)
    lastmodified_ts = Column(DateTime, nullable=False)
    created_by = Column(String(64), nullable=False)
    created_ts = Column(DateTime, nullable=False)

    asset = relationship('PsmAsset')


class PsmAssetfolder(Base):
    __tablename__ = 'psm_assetfolder'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(255), nullable=False)
    parentassetfolder_id = Column(ForeignKey('psm_assetfolder.id'), index=True)
    lastmodified_by = Column(String(64), nullable=False)
    lastmodified_ts = Column(DateTime, nullable=False)
    created_by = Column(String(64), nullable=False)
    created_ts = Column(DateTime, nullable=False)

    parentassetfolder = relationship('PsmAssetfolder', remote_side=[id])


class PsmAssignment(Base):
    __tablename__ = 'psm_assignment'
    __table_args__ = (
        Index('psm_assignment1', 'contentgroupid', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False)
    abbreviation = Column(String(30))
    description = Column(String(4000))
    pointspossible = Column(Numeric(10, 0, asdecimal=False))
    scoringtype = Column(Numeric(10, 0, asdecimal=False))
    isfinalscorecalculated = Column(Numeric(3, 0, asdecimal=False))
    weight = Column(Numeric(18, 6))
    assignmentcategoryid = Column(ForeignKey('psm_assignmentcategory.id'), index=True)
    contentgroupid = Column(ForeignKey('psm_contentgroup.id'), nullable=False)
    extracreditpoints = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    createdbyplugin = Column(ForeignKey('plugindef.name'), index=True)

    psm_assignmentcategory = relationship('PsmAssignmentcategory')
    psm_contentgroup = relationship('PsmContentgroup')
    plugindef = relationship('Plugindef')


class PsmAssignmentcategory(Base):
    __tablename__ = 'psm_assignmentcategory'
    __table_args__ = (
        Index('psm_assignmentcategory1', 'contentgroupid', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False)
    abbreviation = Column(String(30))
    description = Column(String(4000))
    defaultpoints = Column(Numeric(10, 0, asdecimal=False))
    defaultscoretype = Column(Numeric(10, 0, asdecimal=False))
    includeinfinalgrades = Column(Numeric(3, 0, asdecimal=False))
    contentgroupid = Column(ForeignKey('psm_contentgroup.id'), nullable=False)
    defaultextracreditpoints = Column(Numeric(10, 0, asdecimal=False))

    psm_contentgroup = relationship('PsmContentgroup')


class PsmAssignmentscore(Base):
    __tablename__ = 'psm_assignmentscore'
    __table_args__ = (
        Index('assignscore2', 'sectionassignmentid', 'sectionenrollmentid', unique=True),
        Index('psm_assignmentscore1', 'sectionenrollmentid', 'sectionassignmentid', unique=True)
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    turnedinlate = Column(Numeric(3, 0, asdecimal=False))
    turnedin = Column(Numeric(3, 0, asdecimal=False))
    exempt = Column(Numeric(3, 0, asdecimal=False))
    score = Column(Numeric(18, 6))
    lettergrade = Column(String(10))
    actualscoreentered = Column(String(30))
    commentvalue = Column(String(4000))
    ismissing = Column(Numeric(3, 0, asdecimal=False), server_default=text("(0)"))
    sectionenrollmentid = Column(ForeignKey('psm_sectionenrollment.id'), nullable=False)
    sectionassignmentid = Column(ForeignKey('psm_sectionassignment.id'), nullable=False)
    scoretype = Column(Numeric(3, 0, asdecimal=False), server_default=text("0"))

    psm_sectionassignment = relationship('PsmSectionassignment')
    psm_sectionenrollment = relationship('PsmSectionenrollment')


class PsmAssignmentstandard(Base):
    __tablename__ = 'psm_assignmentstandard'
    __table_args__ = (
        Index('psm_assignmentstandard_u2', 'sectionassignmentid', 'standardid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sectionassignmentid = Column(ForeignKey('psm_sectionassignment.id'), nullable=False)
    standardid = Column(ForeignKey('psm_standard.id'), nullable=False, index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    psm_sectionassignment = relationship('PsmSectionassignment')
    psm_standard = relationship('PsmStandard')


class PsmAssignmentstandardscore(Base):
    __tablename__ = 'psm_assignmentstandardscore'
    __table_args__ = (
        Index('psm_assignmentstandardscore_u2', 'assignmentstandardid', 'sectionenrollmentid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    turnedin = Column(Numeric(3, 0, asdecimal=False))
    turnedinlate = Column(Numeric(3, 0, asdecimal=False))
    exempt = Column(Numeric(3, 0, asdecimal=False))
    ismissing = Column(Numeric(3, 0, asdecimal=False))
    actualscoreentered = Column(String(30))
    score = Column(Numeric(18, 6))
    assignmentstandardid = Column(ForeignKey('psm_assignmentstandard.id'), nullable=False)
    sectionenrollmentid = Column(ForeignKey('psm_sectionenrollment.id'), nullable=False, index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    scoretype = Column(Numeric(3, 0, asdecimal=False), server_default=text("0"))

    psm_assignmentstandard = relationship('PsmAssignmentstandard')
    psm_sectionenrollment = relationship('PsmSectionenrollment')


class PsmAuthenticationattempt(Base):
    __tablename__ = 'psm_authenticationattempt'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    username = Column(String(30))
    password = Column(String(30))
    ipaddress = Column(String(256))
    platform = Column(String(30))
    useragent = Column(String(256))
    attempttimestamp = Column(DateTime)
    issuccessfullogin = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    accountid = Column(ForeignKey('psm_account.id'), index=True)

    psm_account = relationship('PsmAccount')


class PsmCategorymetaattribute(Base):
    __tablename__ = 'psm_categorymetaattributes'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    colorcode = Column(Numeric(10, 0, asdecimal=False))
    assignmentcategoryid = Column(ForeignKey('psm_assignmentcategory.id'), nullable=False, unique=True)
    publishstate = Column(Numeric(10, 0, asdecimal=False))
    publishonspecificdate = Column(DateTime)
    publishdaysbeforedue = Column(Numeric(10, 0, asdecimal=False))
    publishscores = Column(Numeric(3, 0, asdecimal=False), server_default=text("1"))
    pushassignmentscores = Column(Numeric(3, 0, asdecimal=False))

    psm_assignmentcategory = relationship('PsmAssignmentcategory')


class PsmChartlayout(Base):
    __tablename__ = 'psm_chartlayout'

    psm_chartlayoutid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    layoutname = Column(String(30), nullable=False)
    layoutdescription = Column(String(2048))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class PsmChartlayoutpreference(Base):
    __tablename__ = 'psm_chartlayoutpreference'

    psm_chartlayoutpreferenceid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    psm_chartlayoutid = Column(ForeignKey('psm_chartlayout.psm_chartlayoutid'), nullable=False, index=True)
    psm_teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False, index=True)
    displaysizeratio = Column(Numeric(10, 3), nullable=False, server_default=text("1 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_chartlayout = relationship('PsmChartlayout')
    psm_teacher = relationship('PsmTeacher')


class PsmChartobject(Base):
    __tablename__ = 'psm_chartobject'

    psm_chartobjectid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    psm_chartlayoutid = Column(ForeignKey('psm_chartlayout.psm_chartlayoutid'), nullable=False, index=True)
    psm_studentid = Column(ForeignKey('psm_student.id'), index=True)
    chartobjecttype = Column(String(30), nullable=False)
    displayname = Column(String(30))
    coordinate_x = Column(Numeric(10, 0, asdecimal=False))
    coordinate_y = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_chartlayout = relationship('PsmChartlayout')
    psm_student = relationship('PsmStudent')


class PsmChartsection(Base):
    __tablename__ = 'psm_chartsection'

    psm_chartsectionid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    psm_chartlayoutid = Column(ForeignKey('psm_chartlayout.psm_chartlayoutid'), nullable=False, index=True)
    psm_sectionid = Column(ForeignKey('psm_section.id'), nullable=False, index=True)
    isoriginatingsection = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_chartlayout = relationship('PsmChartlayout')
    psm_section = relationship('PsmSection')


class PsmChartteachersection(Base):
    __tablename__ = 'psm_chartteachersection'

    psm_chartteachersectionid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    psm_chartlayoutid = Column(ForeignKey('psm_chartlayout.psm_chartlayoutid'), nullable=False, index=True)
    psm_teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False, index=True)
    psm_sectionid = Column(ForeignKey('psm_section.id'), nullable=False, index=True)
    isdefaultlayout = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_chartlayout = relationship('PsmChartlayout')
    psm_section = relationship('PsmSection')
    psm_teacher = relationship('PsmTeacher')


class PsmCommentbank(Base):
    __tablename__ = 'psm_commentbank'
    __table_args__ = (
        Index('psm_commentbanki2', 'schoolid', 'districtid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    code = Column(String(30))
    category = Column(String(256))
    commentvalue = Column(String(4000))
    schoolid = Column(ForeignKey('psm_school.id'))
    districtid = Column(ForeignKey('psm_district.id'), nullable=False, index=True)

    psm_district = relationship('PsmDistrict')
    psm_school = relationship('PsmSchool')


class PsmConfiguration(Base):
    __tablename__ = 'psm_configuration'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), unique=True)
    configvalue = Column(String(256))


class PsmContentgroup(Base):
    __tablename__ = 'psm_contentgroup'
    __table_args__ = (
        Index('psm_contentgroup1', 'parentcontentgroupid', 'ownerid', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False)
    fullyqualifiedns = Column(String(4000))
    ownerid = Column(ForeignKey('psm_teacher.id'), index=True)
    parentcontentgroupid = Column(ForeignKey('psm_contentgroup.id'))

    psm_teacher = relationship('PsmTeacher')
    parent = relationship('PsmContentgroup', remote_side=[id])


class PsmCourse(Base):
    __tablename__ = 'psm_course'
    __table_args__ = (
        Index('psm_course1', 'districtid', 'districtcoursecode', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    title = Column(String(60), nullable=False)
    abbreviation = Column(String(30))
    districtcoursecode = Column(String(30), index=True)
    description = Column(String(4000))
    coursecode = Column(String(30))
    districtid = Column(ForeignKey('psm_district.id'), nullable=False)
    subjectid = Column(ForeignKey('psm_subjectarea.id'), index=True)

    psm_district = relationship('PsmDistrict')
    psm_subjectarea = relationship('PsmSubjectarea')


class PsmCoursestandard(Base):
    __tablename__ = 'psm_coursestandard'
    __table_args__ = (
        Index('psm_coursestandard_u2', 'courseid', 'standardid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    courseid = Column(ForeignKey('psm_course.id'))
    standardid = Column(ForeignKey('psm_standard.id'), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    psm_course = relationship('PsmCourse')
    psm_standard = relationship('PsmStandard')


class PsmCycleday(Base):
    __tablename__ = 'psm_cycleday'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    schoolyear = Column(Numeric(10, 0, asdecimal=False))
    letter = Column(String(10))
    daynumber = Column(Numeric(10, 0, asdecimal=False))
    abbreviation = Column(String(10))
    dayname = Column(String(30))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(ForeignKey('psm_school.id'), index=True)

    psm_school = relationship('PsmSchool')


class PsmDistrict(Base):
    __tablename__ = 'psm_district'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    abbreviation = Column(String(30))
    url = Column(String(256))
    districtnumber = Column(String(30), nullable=False, unique=True)


class PsmExportError(Base):
    __tablename__ = 'psm_export_error'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    rowidentifier = Column(String(255))
    description = Column(String(4000))
    exportjobid = Column(ForeignKey('psm_export_job.id'), nullable=False, index=True)

    psm_export_job = relationship('PsmExportJob')


class PsmExportJob(Base):
    __tablename__ = 'psm_export_job'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    created = Column(DateTime, nullable=False)
    starttime = Column(DateTime)
    percentcomplete = Column(Numeric(10, 0, asdecimal=False))
    status = Column(Numeric(5, 0, asdecimal=False), nullable=False)


class PsmFinalgradesetup(Base):
    __tablename__ = 'psm_finalgradesetup'
    __table_args__ = (
        Index('psm_finalgradesetup_u2', 'sectionid', 'reportingtermid', 'contentgroupid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    finalgradesetuptype = Column(String(255), nullable=False)
    sectionid = Column(ForeignKey('psm_section.id'), index=True)
    contentgroupid = Column(ForeignKey('psm_contentgroup.id'), nullable=False, index=True)
    reportingtermid = Column(ForeignKey('psm_reportingterm.id'), nullable=False, index=True)
    gradingformulaid = Column(ForeignKey('psm_gradingformula.id'), index=True)
    lowscorestodiscard = Column(Numeric(10, 0, asdecimal=False))

    psm_contentgroup = relationship('PsmContentgroup')
    psm_gradingformula = relationship('PsmGradingformula')
    psm_reportingterm = relationship('PsmReportingterm')
    psm_section = relationship('PsmSection')


class PsmFinalscore(Base):
    __tablename__ = 'psm_finalscore'
    __table_args__ = (
        Index('psm_finalscore1', 'sectionenrollmentid', 'reportingtermid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    manualoverride = Column(Numeric(3, 0, asdecimal=False))
    pointsearned = Column(Numeric(18, 6))
    pointspossible = Column(Numeric(18, 6))
    outofdate = Column(Numeric(3, 0, asdecimal=False))
    score = Column(Numeric(18, 6))
    lettergrade = Column(String(10))
    actualscoreentered = Column(String(30))
    commentcode = Column(String(30))
    commentvalue = Column(String(4000))
    sectionenrollmentid = Column(ForeignKey('psm_sectionenrollment.id'), nullable=False, index=True)
    reportingtermid = Column(ForeignKey('psm_reportingterm.id'), nullable=False, index=True)
    lastupdated = Column(DateTime)
    variablecreditvalue = Column(Numeric(18, 6))
    potentialvarcreditvalue = Column(Numeric(18, 6))

    psm_reportingterm = relationship('PsmReportingterm')
    psm_sectionenrollment = relationship('PsmSectionenrollment')


class PsmGrade(Base):
    __tablename__ = 'psm_grade'
    __table_args__ = (
        Index('psm_grade1', 'gradescaleid', 'gradelabel', unique=True),
        Index('psm_grade_n1', 'gradescaleid', 'cutoffpercent', 'defaultzerocutoff', 'adminuseonly')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gradelabel = Column(String(30), nullable=False)
    pointsvalue = Column(Numeric(18, 6))
    percentvalue = Column(Numeric(18, 6))
    cutoffpercent = Column(Numeric(18, 6))
    description = Column(String(4000))
    adminuseonly = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    defaultzerocutoff = Column(Numeric(3, 0, asdecimal=False))
    gradescaleid = Column(ForeignKey('psm_gradescale.id'), nullable=False)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    isspecial = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    psm_gradescale = relationship('PsmGradescale')


class PsmGradescale(Base):
    __tablename__ = 'psm_gradescale'
    __table_args__ = (
        Index('psm_gradescalei2', 'teacherid', 'name', 'schoolid', 'contentgroupid', 'parentgradescaleid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(4000))
    isdistrictdefault = Column(Numeric(3, 0, asdecimal=False))
    contentgroupid = Column(ForeignKey('psm_contentgroup.id'), nullable=False, index=True)
    isnumeric = Column(Numeric(5, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    numericscale = Column(Numeric(10, 0, asdecimal=False))
    gradingscale = Column(Numeric(10, 0, asdecimal=False))
    numericprecision = Column(Numeric(10, 0, asdecimal=False))
    numericmin = Column(Numeric(10, 0, asdecimal=False))
    numericmax = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(ForeignKey('psm_school.id'), index=True)
    canmodify = Column(Numeric(1, 0, asdecimal=False))
    teacherid = Column(ForeignKey('psm_teacher.id'))
    parentgradescaleid = Column(ForeignKey('psm_gradescale.id'), index=True)

    psm_contentgroup = relationship('PsmContentgroup')
    parent = relationship('PsmGradescale', remote_side=[id])
    psm_school = relationship('PsmSchool')
    psm_teacher = relationship('PsmTeacher')


class PsmGradingformula(Base):
    __tablename__ = 'psm_gradingformula'
    __table_args__ = (
        Index('psm_gradingformula1', 'contentgroupid', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False)
    gradescaleid = Column(ForeignKey('psm_gradescale.id'), index=True)
    contentgroupid = Column(ForeignKey('psm_contentgroup.id'), nullable=False)

    psm_contentgroup = relationship('PsmContentgroup')
    psm_gradescale = relationship('PsmGradescale')


class PsmGradingformulaweighting(Base):
    __tablename__ = 'psm_gradingformulaweighting'
    __table_args__ = (
        Index('psm_gradingformulaweighting_n2', 'reportcarditemid', 'reportingtermid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    gradingformulaweightingtype = Column(String(255), nullable=False)
    weighting = Column(Numeric(18, 6), nullable=False)
    parentgradingformulaid = Column(ForeignKey('psm_gradingformula.id'), nullable=False, index=True)
    assignmentid = Column(ForeignKey('psm_assignment.id'), index=True)
    lowscorestodiscard = Column(Numeric(10, 0, asdecimal=False))
    assignmentcategoryid = Column(ForeignKey('psm_assignmentcategory.id'), index=True)
    reportingtermid = Column(ForeignKey('psm_reportingterm.id'), index=True)
    reportcarditemid = Column(ForeignKey('psm_reportcarditem.id'), index=True)

    psm_assignmentcategory = relationship('PsmAssignmentcategory')
    psm_assignment = relationship('PsmAssignment')
    psm_gradingformula = relationship('PsmGradingformula')
    psm_reportcarditem = relationship('PsmReportcarditem')
    psm_reportingterm = relationship('PsmReportingterm')


class PsmGradingpreference(Base):
    __tablename__ = 'psm_gradingpreference'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    approximationmethod = Column(Numeric(10, 0, asdecimal=False))
    accuracy = Column(Numeric(10, 0, asdecimal=False))
    contentgroupid = Column(ForeignKey('psm_contentgroup.id'), nullable=False, unique=True)

    psm_contentgroup = relationship('PsmContentgroup')


class PsmGrantedpermission(Base):
    __tablename__ = 'psm_grantedpermission'
    __table_args__ = (
        Index('psm_grantedpermissioni2', 'permissionroleid', 'permissionid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    permissionmask = Column(Numeric(10, 0, asdecimal=False))
    permissionroleid = Column(ForeignKey('psm_permissionrole.id'))
    permissionid = Column(ForeignKey('psm_permission.id'), index=True)

    psm_permission = relationship('PsmPermission')
    psm_permissionrole = relationship('PsmPermissionrole')


class PsmGroupquery(Base):
    __tablename__ = 'psm_groupquery'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256))
    description = Column(String(4000))
    entitytype = Column(String(256), index=True)
    querydata = Column(LargeBinary)
    accountid = Column(ForeignKey('psm_account.id'), index=True)

    psm_account = relationship('PsmAccount')


class PsmImportError(Base):
    __tablename__ = 'psm_import_error'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    rowidentifier = Column(String(255))
    description = Column(String(4000))
    importjobid = Column(ForeignKey('psm_import_job.id'), nullable=False, index=True)

    psm_import_job = relationship('PsmImportJob')


class PsmImportJob(Base):
    __tablename__ = 'psm_import_job'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    created = Column(DateTime, nullable=False)
    starttime = Column(DateTime)
    percentcomplete = Column(Numeric(10, 0, asdecimal=False))
    status = Column(Numeric(5, 0, asdecimal=False), nullable=False)


class PsmJobqueuecurrent(Base):
    __tablename__ = 'psm_jobqueuecurrent'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    status = Column(String(80))
    starttimestamp = Column(DateTime)
    endtimestamp = Column(DateTime)
    creationtimestamp = Column(DateTime)
    priority = Column(Numeric(10, 0, asdecimal=False))
    scheduletimestamp = Column(DateTime)
    outputfile = Column(String(4000))
    activeflag = Column(Numeric(3, 0, asdecimal=False))
    errorcode = Column(Numeric(10, 0, asdecimal=False))
    errormessage = Column(LargeBinary)
    reportgenuserid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    reportruntimerequestid = Column(ForeignKey('psm_reportruntimerequest.id'), nullable=False, index=True)
    reportapplicationid = Column(ForeignKey('psm_reportapplication.id'), nullable=False, index=True)
    downloadfilename = Column(String(512))
    downloadfileextension = Column(String(50))

    psm_reportapplication = relationship('PsmReportapplication')
    psm_reportruntimerequest = relationship('PsmReportruntimerequest')


t_psm_jobqueuecurrentview = Table(
    'psm_jobqueuecurrentview', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('status', String(80)),
    Column('starttimestamp', DateTime),
    Column('endtimestamp', DateTime),
    Column('creationtimestamp', DateTime),
    Column('priority', Numeric(10, 0, asdecimal=False)),
    Column('scheduletimestamp', DateTime),
    Column('outputfile', String(4000)),
    Column('activeflag', Numeric(3, 0, asdecimal=False)),
    Column('errorcode', Numeric(10, 0, asdecimal=False)),
    Column('errormessage', LargeBinary),
    Column('reportgenuserid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('reportruntimerequestid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('reportapplicationid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('downloadfilename', String(512)),
    Column('downloadfileextension', String(50)),
    Column('isparent', Numeric(1, 0, asdecimal=False)),
    Column('parent_schedulestarttimestamp', DateTime),
    Column('parent_endtimestamp', DateTime)
)


class PsmLink(Base):
    __tablename__ = 'psm_link'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    title = Column(String(50))
    description = Column(String(4000))
    url = Column(String(4000))
    linktype = Column(Numeric(10, 0, asdecimal=False))
    preferredorder = Column(Numeric(10, 0, asdecimal=False))
    accountid = Column(ForeignKey('psm_account.id'), index=True)
    linkgroupid = Column(ForeignKey('psm_linkgroup.id'), index=True)

    psm_account = relationship('PsmAccount')
    psm_linkgroup = relationship('PsmLinkgroup')


class PsmLinkgroup(Base):
    __tablename__ = 'psm_linkgroup'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    title = Column(String(50))
    description = Column(String(4000))
    lastmodificationdate = Column(DateTime)
    accountid = Column(ForeignKey('psm_account.id'), index=True)

    psm_account = relationship('PsmAccount')


class PsmLinkpush(Base):
    __tablename__ = 'psm_linkpush'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pushtimestamp = Column(DateTime)
    accountid = Column(ForeignKey('psm_account.id'), index=True)

    psm_account = relationship('PsmAccount')


class PsmLinkpushlink(Base):
    __tablename__ = 'psm_linkpushlink'
    __table_args__ = (
        Index('psm_linkpushlinki2', 'linkpushid', 'linkid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    linkid = Column(ForeignKey('psm_link.id'), index=True)
    linkpushid = Column(ForeignKey('psm_linkpush.id'))

    psm_link = relationship('PsmLink')
    psm_linkpush = relationship('PsmLinkpush')


class PsmLinkpushsearchgroup(Base):
    __tablename__ = 'psm_linkpushsearchgroup'
    __table_args__ = (
        Index('psm_linkpushsearchgroupi2', 'linkpushid', 'groupqueryid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    linkpushid = Column(ForeignKey('psm_linkpush.id'))
    groupqueryid = Column(ForeignKey('psm_groupquery.id'), index=True)

    psm_groupquery = relationship('PsmGroupquery')
    psm_linkpush = relationship('PsmLinkpush')


class PsmMeeting(Base):
    __tablename__ = 'psm_meeting'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    schoolyear = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(ForeignKey('psm_school.id'), index=True)
    sectionid = Column(ForeignKey('psm_section.id'), index=True)
    cycledayid = Column(ForeignKey('psm_cycleday.id'), index=True)
    periodid = Column(ForeignKey('psm_period.id'), index=True)

    psm_cycleday = relationship('PsmCycleday')
    psm_period = relationship('PsmPeriod')
    psm_school = relationship('PsmSchool')
    psm_section = relationship('PsmSection')


class PsmParamprojectpubassoc(Base):
    __tablename__ = 'psm_paramprojectpubassoc'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    overridelabel = Column(String(32))
    overridedesc = Column(String(4000))
    reportprojectid = Column(ForeignKey('psm_reportproject.id'), index=True)
    reportpubid = Column(ForeignKey('psm_reportpub.id'), index=True)
    reportparametername = Column(String(256))

    psm_reportproject = relationship('PsmReportproject')
    psm_reportpub = relationship('PsmReportpub')


class PsmPeriod(Base):
    __tablename__ = 'psm_period'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    schoolyear = Column(Numeric(10, 0, asdecimal=False))
    periodnumber = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(256))
    abbreviation = Column(String(10))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(ForeignKey('psm_school.id'), index=True)

    psm_school = relationship('PsmSchool')


class PsmPermission(Base):
    __tablename__ = 'psm_permission'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(4000))
    displayname = Column(String(256))


class PsmPermissionrole(Base):
    __tablename__ = 'psm_permissionrole'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(4000))
    displayname = Column(String(256))


class PsmPhoto(Base):
    __tablename__ = 'psm_photo'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    mimetype = Column(String(50), nullable=False)
    imagedata = Column(LargeBinary)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class PsmReportappcatassoc(Base):
    __tablename__ = 'psm_reportappcatassoc'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportapplicationid = Column(ForeignKey('psm_reportapplication.id'), index=True)
    reportcategoryid = Column(Numeric(19, 0, asdecimal=False))
    categoryname = Column(String(256))
    categorydescription = Column(String(4000))
    categorydisplayname = Column(String(256))
    sortorder = Column(Numeric(10, 0, asdecimal=False))

    psm_reportapplication = relationship('PsmReportapplication')


class PsmReportapplication(Base):
    __tablename__ = 'psm_reportapplication'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(String(4000))
    displayname = Column(String(256))


class PsmReportcarditem(Base):
    __tablename__ = 'psm_reportcarditem'
    __table_args__ = (
        Index('psm_reportcarditem_u2', 'sectionid', 'reportingtermid', 'standardid', 'parentreportcarditemid', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(400), nullable=False)
    description = Column(String(4000))
    itemtype = Column(Numeric(5, 0, asdecimal=False))
    itemlevel = Column(Numeric(5, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    isoptional = Column(Numeric(5, 0, asdecimal=False))
    colorcode = Column(Numeric(10, 0, asdecimal=False))
    scoretype = Column(String(20))
    pointpossible = Column(Numeric(10, 0, asdecimal=False))
    prepopulationvalue = Column(String(20))
    includestandardcomment = Column(Numeric(5, 0, asdecimal=False), nullable=False)
    maxstandardcomments = Column(Numeric(10, 0, asdecimal=False))
    includenarrativecomment = Column(Numeric(5, 0, asdecimal=False), nullable=False)
    maxnarrativelength = Column(Numeric(10, 0, asdecimal=False))
    exportpercentgrade = Column(Numeric(3, 0, asdecimal=False))
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False)
    reportingtermid = Column(ForeignKey('psm_reportingterm.id'), nullable=False, index=True)
    gradescaleid = Column(ForeignKey('psm_gradescale.id'), index=True)
    parentreportcarditemid = Column(ForeignKey('psm_reportcarditem.id'), index=True)
    standardid = Column(ForeignKey('psm_standard.id'), index=True)

    psm_gradescale = relationship('PsmGradescale')
    parent = relationship('PsmReportcarditem', remote_side=[id])
    psm_reportingterm = relationship('PsmReportingterm')
    psm_section = relationship('PsmSection')
    psm_standard = relationship('PsmStandard')


class PsmReportcarditemcomment(Base):
    __tablename__ = 'psm_reportcarditemcomment'
    __table_args__ = (
        Index('psm_reportcarditemcommenti2', 'reportcarditemid', 'sectionenrollmentid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    type = Column(String(20), nullable=False)
    commenttext = Column(String(4000))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    lastupdated = Column(DateTime)
    reportcarditemid = Column(ForeignKey('psm_reportcarditem.id'), nullable=False)
    commentbankid = Column(ForeignKey('psm_commentbank.id'), index=True)
    sectionenrollmentid = Column(ForeignKey('psm_sectionenrollment.id'), nullable=False, index=True)

    psm_commentbank = relationship('PsmCommentbank')
    psm_reportcarditem = relationship('PsmReportcarditem')
    psm_sectionenrollment = relationship('PsmSectionenrollment')


class PsmReportcarditemgrade(Base):
    __tablename__ = 'psm_reportcarditemgrade'
    __table_args__ = (
        Index('psm_reportcarditemgradei2', 'reportcarditemid', 'sectionenrollmentid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    actualgradeentered = Column(String(8))
    ismissing = Column(Numeric(5, 0, asdecimal=False))
    isexempt = Column(Numeric(5, 0, asdecimal=False))
    islate = Column(Numeric(5, 0, asdecimal=False))
    lastupdated = Column(DateTime)
    reportcarditemid = Column(ForeignKey('psm_reportcarditem.id'), nullable=False)
    sectionenrollmentid = Column(ForeignKey('psm_sectionenrollment.id'), nullable=False, index=True)
    iscalculated = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    psm_reportcarditem = relationship('PsmReportcarditem')
    psm_sectionenrollment = relationship('PsmSectionenrollment')


class PsmReportclas(Base):
    __tablename__ = 'psm_reportclass'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256))
    javaclass = Column(String(256), unique=True)


class PsmReportcolumn(Base):
    __tablename__ = 'psm_reportcolumn'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256))
    javaclass = Column(String(256))
    mappingtype = Column(Numeric(10, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    isfilterable = Column(Numeric(3, 0, asdecimal=False))
    isreportparamable = Column(Numeric(3, 0, asdecimal=False))
    reportentityid = Column(ForeignKey('psm_reportentity.id'), index=True)
    defaultlayoutvalue = Column(String(256))
    defaultrendervalue = Column(String(256))
    reportmappingid = Column(Numeric(19, 0, asdecimal=False))
    mappedcolumnname = Column(String(256))
    functionclass = Column(String(256))

    psm_reportentity = relationship('PsmReportentity')


class PsmReportentity(Base):
    __tablename__ = 'psm_reportentity'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256))
    reportclassid = Column(ForeignKey('psm_reportclass.id'), nullable=False, unique=True)
    reportmodelid = Column(ForeignKey('psm_reportmodel.id'), index=True)
    layoutcolumnvalue = Column(String(256))
    rendercolumnvalue = Column(String(256))
    functionclass = Column(String(256))

    psm_reportclas = relationship('PsmReportclas')
    psm_reportmodel = relationship('PsmReportmodel')


t_psm_reportfunctiondependency = Table(
    'psm_reportfunctiondependency', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('reportcolumnid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('reportmappingid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('columnname', String(256), nullable=False),
    Column('javaclass', String(256), nullable=False)
)


t_psm_reportfunctionparameter = Table(
    'psm_reportfunctionparameter', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('reportcolumnid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('parametername', String(256), nullable=False),
    Column('valuesequence', Numeric(scale=0, asdecimal=False), nullable=False),
    Column('parametervalue', String(256), nullable=False)
)


t_psm_reportgenrole = Table(
    'psm_reportgenrole', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('name', String(50)),
    Column('schoolid', String(0))
)


t_psm_reportgenuser = Table(
    'psm_reportgenuser', metadata,
    Column('id', Numeric(asdecimal=False)),
    Column('lastname', String(20)),
    Column('firstname', String(20)),
    Column('middlename', String(20)),
    Column('lastfirst', String(40))
)


t_psm_reportgenuserrole = Table(
    'psm_reportgenuserrole', metadata,
    Column('id', Numeric(asdecimal=False)),
    Column('reportgenuserid', Numeric(asdecimal=False)),
    Column('reportgenroleid', Numeric(10, 0, asdecimal=False))
)


class PsmReportingterm(Base):
    __tablename__ = 'psm_reportingterm'
    __table_args__ = (
        Index('psm_reportingterm2', 'startdate', 'enddate'),
        Index('psm_reportingterm1', 'parentreportingtermid', 'termid', 'name', unique=True)
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(30), index=True)
    isbasedontermdates = Column(Numeric(3, 0, asdecimal=False))
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    termid = Column(ForeignKey('psm_term.id'), index=True)
    parentreportingtermid = Column(ForeignKey('psm_reportingterm.id'))

    parent = relationship('PsmReportingterm', remote_side=[id])
    psm_term = relationship('PsmTerm')


class PsmReportmapping(Base):
    __tablename__ = 'psm_reportmapping'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    tablename = Column(String(256), nullable=False)
    parentmappingid = Column(ForeignKey('psm_reportmapping.id'), index=True)
    parentlink = Column(String(512))
    name = Column(String(80))
    permissionquery = Column(String(4000))
    altparentlink = Column(String(512))

    parent = relationship('PsmReportmapping', remote_side=[id])


class PsmReportmodel(Base):
    __tablename__ = 'psm_reportmodel'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256))
    version = Column(Numeric(10, 0, asdecimal=False))


class PsmReportnode(Base):
    __tablename__ = 'psm_reportnode'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), unique=True)
    isindependanttree = Column(Numeric(3, 0, asdecimal=False))
    mappingtype = Column(Numeric(10, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    parenttreenodeid = Column(ForeignKey('psm_reportnode.id'), index=True)
    reportentityid = Column(ForeignKey('psm_reportentity.id'), index=True)
    reportmappingid = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    parent = relationship('PsmReportnode', remote_side=[id])
    psm_reportentity = relationship('PsmReportentity')


class PsmReportoutput(Base):
    __tablename__ = 'psm_reportoutput'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    outputtype = Column(String(256), nullable=False)
    outputbytes = Column(LargeBinary, nullable=False)
    jobqueuecurrentid = Column(ForeignKey('psm_jobqueuecurrent.id'), nullable=False, unique=True)

    psm_jobqueuecurrent = relationship('PsmJobqueuecurrent')


class PsmReportparameter(Base):
    __tablename__ = 'psm_reportparameter'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    paramname = Column(String(256), nullable=False, unique=True)
    description = Column(String(4000))
    typename = Column(String(60))
    label = Column(String(4000))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    isrequired = Column(Numeric(3, 0, asdecimal=False))
    datatextfield = Column(String(256))
    datasource = Column(String(500))
    datavaluefield = Column(String(256))
    dataisselectedfield = Column(String(256))
    datasortbystatement = Column(String(256))
    datawherestatement = Column(String(500))
    ismandatory = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))


class PsmReportparamoption(Base):
    __tablename__ = 'psm_reportparamoptions'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    optionvalue = Column(String(256))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    defaultvalue = Column(Numeric(3, 0, asdecimal=False))
    reportparameterid = Column(ForeignKey('psm_reportparameter.id'), nullable=False, index=True)
    optiontext = Column(String(500))
    filtersql = Column(String(4000))
    districtfiltersql = Column(String(4000))

    psm_reportparameter = relationship('PsmReportparameter')


class PsmReportpath(Base):
    __tablename__ = 'psm_reportpath'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    path = Column(String(4000), nullable=False)
    reportprojectid = Column(ForeignKey('psm_reportproject.id'), nullable=False, index=True)
    accountid = Column(ForeignKey('psm_account.id'), index=True)

    psm_account = relationship('PsmAccount')
    psm_reportproject = relationship('PsmReportproject')


class PsmReportproject(Base):
    __tablename__ = 'psm_reportproject'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(String(4000))
    templateobject = Column(LargeBinary)
    queryobject = Column(LargeBinary)
    runtimeparamobject = Column(LargeBinary)
    powerreportingversion = Column(String(256))
    createdby = Column(String(256), nullable=False)
    createdtimestamp = Column(DateTime)
    modifiedby = Column(String(256))
    modifiedtimestamp = Column(DateTime)
    activestate = Column(String(256), nullable=False)
    sharestate = Column(String(256), nullable=False)
    publishstate = Column(String(256), nullable=False)
    reportpubid = Column(ForeignKey('psm_reportpub.id'), index=True)
    accountid = Column(ForeignKey('psm_account.id'), index=True)
    projecttemplatestate = Column(String(256))
    reporttreename = Column(String(256))

    psm_account = relationship('PsmAccount')
    psm_reportpub = relationship('PsmReportpub')


class PsmReportpub(Base):
    __tablename__ = 'psm_reportpub'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), nullable=False)
    description = Column(String(4000))
    templateobject = Column(LargeBinary)
    queryobject = Column(LargeBinary)
    runtimeparamobject = Column(LargeBinary)
    modifiedtimestamp = Column(DateTime)
    publishedby = Column(String(256), nullable=False)
    publishedtimestamp = Column(DateTime)
    outputtype = Column(String(256), nullable=False)
    publicationscope = Column(String(256), nullable=False)
    custompagename = Column(String(4000))


class PsmReportpubappcat(Base):
    __tablename__ = 'psm_reportpubappcat'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportpubid = Column(ForeignKey('psm_reportpub.id'), nullable=False, index=True)
    reportappcatassocid = Column(ForeignKey('psm_reportappcatassoc.id'), index=True)

    psm_reportappcatassoc = relationship('PsmReportappcatassoc')
    psm_reportpub = relationship('PsmReportpub')


class PsmReportpubrole(Base):
    __tablename__ = 'psm_reportpubrole'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    reportgenroleid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    reportpubid = Column(ForeignKey('psm_reportpub.id'), nullable=False, index=True)

    psm_reportpub = relationship('PsmReportpub')


class PsmReportpubschool(Base):
    __tablename__ = 'psm_reportpubschool'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    schoolrelatedid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    reportpubid = Column(ForeignKey('psm_reportpub.id'), nullable=False, index=True)

    psm_reportpub = relationship('PsmReportpub')


class PsmReportruntimerequest(Base):
    __tablename__ = 'psm_reportruntimerequest'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    scheduletype = Column(String(20))
    schedulestarttimestamp = Column(DateTime)
    scheduleendtimestamp = Column(DateTime)
    repeatcount = Column(Numeric(10, 0, asdecimal=False))
    repeatinterval = Column(Numeric(19, 0, asdecimal=False))
    cronexpression = Column(String(255))
    isscheduled = Column(Numeric(3, 0, asdecimal=False), index=True)
    reportcontext = Column(LargeBinary)
    reportgenuserid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    reportpubid = Column(ForeignKey('psm_reportpub.id'), nullable=False, index=True)
    reportapplicationid = Column(ForeignKey('psm_reportapplication.id'), nullable=False, index=True)
    parentid = Column(Numeric(19, 0, asdecimal=False))
    isparent = Column(Numeric(1, 0, asdecimal=False))
    reportqueuedesc = Column(String(2000))
    schedulerequestid = Column(Numeric(19, 0, asdecimal=False))

    psm_reportapplication = relationship('PsmReportapplication')
    psm_reportpub = relationship('PsmReportpub')


t_psm_reportruntimerequestview = Table(
    'psm_reportruntimerequestview', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('scheduletype', String(20)),
    Column('schedulestarttimestamp', DateTime),
    Column('scheduleendtimestamp', DateTime),
    Column('repeatcount', Numeric(10, 0, asdecimal=False)),
    Column('repeatinterval', Numeric(19, 0, asdecimal=False)),
    Column('cronexpression', String(255)),
    Column('isscheduled', Numeric(3, 0, asdecimal=False)),
    Column('reportcontext', LargeBinary),
    Column('reportgenuserid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('reportpubid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('reportapplicationid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('parentid', Numeric(19, 0, asdecimal=False)),
    Column('isparent', Numeric(1, 0, asdecimal=False)),
    Column('parent_schedulestarttimestamp', DateTime),
    Column('reportqueuedesc', String(2000)),
    Column('schedulerequestid', Numeric(19, 0, asdecimal=False))
)


class PsmReporttree(Base):
    __tablename__ = 'psm_reporttree'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), unique=True)
    displayname = Column(String(256))
    version = Column(Numeric(10, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    reportmodelid = Column(ForeignKey('psm_reportmodel.id'), index=True)
    reportnodeid = Column(ForeignKey('psm_reportnode.id'), nullable=False, unique=True)
    defaultdatasetkey = Column(String(256))
    defaulthorizontalgroupkey = Column(String(256))
    defaulthorizontalgrouptext = Column(String(256))
    defaultverticalgroupkey = Column(String(256))
    defaultverticalgrouptext = Column(String(256))
    defaultsegmentsize = Column(Numeric(10, 0, asdecimal=False))
    isenabled = Column(Numeric(1, 0, asdecimal=False))
    isdistrictexcluded = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))

    psm_reportmodel = relationship('PsmReportmodel')
    psm_reportnode = relationship('PsmReportnode')


class PsmReporttreeparamassoc(Base):
    __tablename__ = 'psm_reporttreeparamassoc'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    reporttreeid = Column(ForeignKey('psm_reporttree.id'), nullable=False, index=True)
    reportparameterid = Column(ForeignKey('psm_reportparameter.id'), nullable=False, index=True)
    filtersql = Column(String(4000))
    districtfiltersql = Column(String(4000))
    filterdecision = Column(Numeric(3, 0, asdecimal=False), server_default=text("0"))

    psm_reportparameter = relationship('PsmReportparameter')
    psm_reporttree = relationship('PsmReporttree')


class PsmSchool(Base):
    __tablename__ = 'psm_school'
    __table_args__ = (
        Index('psm_school1', 'districtid', 'name', unique=True),
        Index('psm_school2', 'districtid', 'schoolnumber', unique=True)
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(60), nullable=False)
    address = Column(String(4000))
    abbreviation = Column(String(30))
    schoolnumber = Column(String(30))
    districtid = Column(ForeignKey('psm_district.id'), nullable=False)

    psm_district = relationship('PsmDistrict')


class PsmSchoolconfiguration(Base):
    __tablename__ = 'psm_schoolconfiguration'
    __table_args__ = (
        Index('psm_schoolconfiguration_u2', 'schoolid', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), nullable=False)
    configvalue = Column(String(256), nullable=False)
    schoolid = Column(ForeignKey('psm_school.id'))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    psm_school = relationship('PsmSchool')


class PsmSchoolcourse(Base):
    __tablename__ = 'psm_schoolcourse'
    __table_args__ = (
        Index('psm_schoolcourse1', 'schoolid', 'coursecode', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    coursecode = Column(String(30), nullable=False)
    schoolcoursetitle = Column(String(50))
    description = Column(String(4000))
    abbreviation = Column(String(30))
    schoolid = Column(ForeignKey('psm_school.id'), nullable=False)
    courseid = Column(ForeignKey('psm_course.id'), index=True)

    psm_course = relationship('PsmCourse')
    psm_school = relationship('PsmSchool')


class PsmSearchgroupmember(Base):
    __tablename__ = 'psm_searchgroupmember'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    memberid = Column(Numeric(19, 0, asdecimal=False))
    searchentitytype = Column(Numeric(10, 0, asdecimal=False))
    groupqueryid = Column(ForeignKey('psm_groupquery.id'), index=True)

    psm_groupquery = relationship('PsmGroupquery')


class PsmSection(Base):
    __tablename__ = 'psm_section'
    __table_args__ = (
        Index('psm_section1', 'schoolid', 'sectionidentifier', 'schoolcourseid', 'termid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sectionidentifier = Column(String(30))
    description = Column(String(4000))
    schoolid = Column(ForeignKey('psm_school.id'), nullable=False)
    termid = Column(ForeignKey('psm_term.id'), nullable=False, index=True)
    schoolcourseid = Column(ForeignKey('psm_schoolcourse.id'), index=True)
    meeting = Column(String(256))
    roomname = Column(String(10))
    isearnedvarcreditallowed = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    ispotentialvarcreditallowed = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    gradebooktype = Column(Numeric(10, 0, asdecimal=False))

    psm_schoolcourse = relationship('PsmSchoolcourse')
    psm_school = relationship('PsmSchool')
    psm_term = relationship('PsmTerm')


class PsmSectionassignment(Base):
    __tablename__ = 'psm_sectionassignment'
    __table_args__ = (
        Index('psm_sectionassignment1', 'sectionid', 'assignmentid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    dateassignedtosection = Column(DateTime)
    pointspossible = Column(Numeric(10, 0, asdecimal=False))
    dateassignmentdue = Column(DateTime)
    assignmentid = Column(ForeignKey('psm_assignment.id'), nullable=False, index=True)
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False)

    psm_assignment = relationship('PsmAssignment')
    psm_section = relationship('PsmSection')


class PsmSectionassignmetaattribute(Base):
    __tablename__ = 'psm_sectionassignmetaattribute'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    publishstate = Column(Numeric(10, 0, asdecimal=False))
    publishonspecificdate = Column(DateTime)
    publishdaysbeforedue = Column(Numeric(10, 0, asdecimal=False))
    publishscores = Column(Numeric(3, 0, asdecimal=False))
    sectionassignmentid = Column(ForeignKey('psm_sectionassignment.id'), nullable=False, unique=True)
    pushassignmentscores = Column(Numeric(3, 0, asdecimal=False))

    psm_sectionassignment = relationship('PsmSectionassignment')


class PsmSectionenrollment(Base):
    __tablename__ = 'psm_sectionenrollment'
    __table_args__ = (
        Index('psm_sectionenrollment1', 'sectionid', 'studentid', 'dateenrolled', 'dateleft', unique=True),
        Index('psm_sectionenrollment_n2', 'sectionid', 'studentid', 'sectionenrollmentstatus')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sectionenrollmentstatus = Column(Numeric(10, 0, asdecimal=False))
    dateenrolled = Column(DateTime)
    dateleft = Column(DateTime)
    studentid = Column(ForeignKey('psm_student.id'), nullable=False, index=True)
    gradescaleid = Column(ForeignKey('psm_gradescale.id'), index=True)
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False)
    teachernotifiedflag = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    psm_gradescale = relationship('PsmGradescale')
    psm_section = relationship('PsmSection')
    psm_student = relationship('PsmStudent')


class PsmSectiongradescale(Base):
    __tablename__ = 'psm_sectiongradescale'
    __table_args__ = (
        Index('psm_sectiongradescale1', 'sectionid', 'gradescaleid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    issectiondefault = Column(Numeric(3, 0, asdecimal=False))
    gradescaleid = Column(ForeignKey('psm_gradescale.id'), nullable=False, index=True)
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False)

    psm_gradescale = relationship('PsmGradescale')
    psm_section = relationship('PsmSection')


class PsmSectionreadines(Base):
    __tablename__ = 'psm_sectionreadiness'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    verifiedstatus = Column(Numeric(1, 0, asdecimal=False))
    verifieddate = Column(DateTime)
    verifiedcomment = Column(String(256))
    sectionid = Column(ForeignKey('psm_section.id'), index=True)
    reportingtermid = Column(ForeignKey('psm_reportingterm.id'), index=True)

    psm_reportingterm = relationship('PsmReportingterm')
    psm_section = relationship('PsmSection')


class PsmSectionspecfield(Base):
    __tablename__ = 'psm_sectionspecfield'
    __table_args__ = (
        Index('psm_sectionspecfield_u2', 'sectionid', 'fieldlabel', 'systemfieldtype', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    description = Column(String(100))
    fieldlabel = Column(String(30), nullable=False)
    fielddisplayorder = Column(Numeric(3, 0, asdecimal=False))
    fielddatatype = Column(Numeric(3, 0, asdecimal=False))
    systemfieldtype = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_section = relationship('PsmSection')


class PsmSectionstandardcalc(Base):
    __tablename__ = 'psm_sectionstandardcalc'
    __table_args__ = (
        Index('psm_sectionstandardcalc_u2', 'sectionid', 'reportingtermid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    calculationtype = Column(Numeric(10, 0, asdecimal=False))
    recencysetup = Column(String(255))
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False)
    reportingtermid = Column(ForeignKey('psm_reportingterm.id'), nullable=False, index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    topleveltype = Column(Numeric(10, 0, asdecimal=False))

    psm_reportingterm = relationship('PsmReportingterm')
    psm_section = relationship('PsmSection')


class PsmSectionstudentdatum(Base):
    __tablename__ = 'psm_sectionstudentdata'
    __table_args__ = (
        Index('psm_sectionstudentdata_u2', 'studentid', 'sectionspecfieldid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    fieldvalue = Column(String(4000))
    studentid = Column(ForeignKey('psm_student.id'), nullable=False)
    sectionspecfieldid = Column(ForeignKey('psm_sectionspecfield.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_sectionspecfield = relationship('PsmSectionspecfield')
    psm_student = relationship('PsmStudent')


class PsmSectionstudentgroup(Base):
    __tablename__ = 'psm_sectionstudentgroup'
    __table_args__ = (
        Index('psm_sectionstudentgroup1', 'studentgroupid', 'sectionid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False, index=True)
    studentgroupid = Column(ForeignKey('psm_studentgroup.id'), nullable=False)

    psm_section = relationship('PsmSection')
    psm_studentgroup = relationship('PsmStudentgroup')


class PsmSectionteacher(Base):
    __tablename__ = 'psm_sectionteacher'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    priorityorder = Column(Numeric(10, 0, asdecimal=False))
    sectionnickname = Column(String(50))
    teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False, index=True)
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    allocation = Column(Numeric(10, 2))
    roleid = Column(ForeignKey('roledef.id'), index=True)

    roledef = relationship('Roledef')
    psm_section = relationship('PsmSection')
    psm_teacher = relationship('PsmTeacher')


class PsmStandard(Base):
    __tablename__ = 'psm_standard'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(400), nullable=False)
    description = Column(String(4000), nullable=False)
    identifier = Column(String(20), nullable=False)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    allowscore = Column(Numeric(10, 0, asdecimal=False))
    includecomment = Column(Numeric(10, 0, asdecimal=False))
    parentstandardid = Column(ForeignKey('psm_standard.id'), index=True)
    subjectareaid = Column(ForeignKey('psm_subjectarea.id'), index=True)
    gradescaleid = Column(ForeignKey('psm_gradescale.id'), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    maxcommentlength = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("4000 "))

    psm_gradescale = relationship('PsmGradescale')
    parent = relationship('PsmStandard', remote_side=[id])
    psm_subjectarea = relationship('PsmSubjectarea')


class PsmStandardrecentsetup(Base):
    __tablename__ = 'psm_standardrecentsetup'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    assignmentorder = Column(Numeric(5, 0, asdecimal=False))
    assignmentweight = Column(Numeric(18, 6))
    teacherid = Column(ForeignKey('psm_teacher.id'), index=True)
    schoolid = Column(ForeignKey('psm_school.id'), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    psm_school = relationship('PsmSchool')
    psm_teacher = relationship('PsmTeacher')


class PsmStudent(Base):
    __tablename__ = 'psm_student'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    middlename = Column(String(30))
    studentidentifier = Column(String(30), unique=True)
    gender = Column(String(10))
    birthdate = Column(DateTime)
    primaryracecode = Column(String(10))
    citizenship = Column(String(30))
    primarylanguage = Column(String(30))
    correspondencelanguage = Column(String(30))
    nickname = Column(String(256))
    gradelevel = Column(String(30))
    homephone = Column(String(30))


class PsmStudentalert(Base):
    __tablename__ = 'psm_studentalert'
    __table_args__ = (
        Index('psm_studentalerti2', 'studentid', 'studentalertcategoryid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    description = Column(String(4000))
    dateexpires = Column(DateTime)
    studentid = Column(ForeignKey('psm_student.id'), nullable=False)
    studentalertcategoryid = Column(ForeignKey('psm_studentalertcategory.id'), index=True)

    psm_studentalertcategory = relationship('PsmStudentalertcategory')
    psm_student = relationship('PsmStudent')


class PsmStudentalertcategory(Base):
    __tablename__ = 'psm_studentalertcategory'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50))
    description = Column(String(4000))


class PsmStudentcontact(Base):
    __tablename__ = 'psm_studentcontact'
    __table_args__ = (
        Index('psm_studentcontacti2', 'studentid', 'studentcontacttypeid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    firstname = Column(String(60))
    lastname = Column(String(60))
    phone = Column(String(30))
    email = Column(String(256))
    studentid = Column(ForeignKey('psm_student.id'), nullable=False)
    studentcontacttypeid = Column(ForeignKey('psm_studentcontacttype.id'), index=True)

    psm_studentcontacttype = relationship('PsmStudentcontacttype')
    psm_student = relationship('PsmStudent')


class PsmStudentcontacttype(Base):
    __tablename__ = 'psm_studentcontacttype'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(30))
    description = Column(String(4000))


class PsmStudentgroup(Base):
    __tablename__ = 'psm_studentgroup'
    __table_args__ = (
        Index('psm_studentgroup1', 'parentstudentgroupid', 'contentgroupid', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50))
    isstudentgroupset = Column(Numeric(3, 0, asdecimal=False))
    contentgroupid = Column(ForeignKey('psm_contentgroup.id'), nullable=False, index=True)
    parentstudentgroupid = Column(ForeignKey('psm_studentgroup.id'))

    psm_contentgroup = relationship('PsmContentgroup')
    parent = relationship('PsmStudentgroup', remote_side=[id])


class PsmStudentgroupmembership(Base):
    __tablename__ = 'psm_studentgroupmembership'
    __table_args__ = (
        Index('psm_studentgroupmembership1', 'sectionenrollmentid', 'studentgroupid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sectionenrollmentid = Column(ForeignKey('psm_sectionenrollment.id'), nullable=False)
    studentgroupid = Column(ForeignKey('psm_studentgroup.id'), nullable=False, index=True)

    psm_sectionenrollment = relationship('PsmSectionenrollment')
    psm_studentgroup = relationship('PsmStudentgroup')


class PsmStudentphoto(Base):
    __tablename__ = 'psm_studentphoto'
    __table_args__ = (
        Index('psm_studentphoto_u2', 'studentid', 'photoid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    studentid = Column(ForeignKey('psm_student.id'), nullable=False)
    photoid = Column(ForeignKey('psm_photo.id'), nullable=False, index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    psm_photo = relationship('PsmPhoto')
    psm_student = relationship('PsmStudent')


class PsmSubjectarea(Base):
    __tablename__ = 'psm_subjectarea'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)


class PsmTeacher(Base):
    __tablename__ = 'psm_teacher'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(32))
    teacheridentifier = Column(String(30), nullable=False)
    ssn = Column(String(30))
    ethnicity = Column(String(30))
    salt = Column(String(10))
    email = Column(String(50))
    ldapenabled = Column(Numeric(3, 0, asdecimal=False))
    isaccessible = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))


class PsmTeachercode(Base):
    __tablename__ = 'psm_teachercode'
    __table_args__ = (
        Index('psm_teachercode_u2', 'teacherid', 'gradelabel', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    description = Column(String(30))
    gradelabel = Column(String(6), nullable=False)
    isexempt = Column(Numeric(3, 0, asdecimal=False))
    numerictype = Column(Numeric(5, 0, asdecimal=False), nullable=False)
    numericvalue = Column(Numeric(18, 6))
    percentvalue = Column(Numeric(18, 6))
    teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    psm_teacher = relationship('PsmTeacher')


class PsmTeachercommentbank(Base):
    __tablename__ = 'psm_teachercommentbank'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    code = Column(String(30))
    category = Column(String(256))
    commentvalue = Column(String(4000))
    teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_teacher = relationship('PsmTeacher')


class PsmTeachercoursestandard(Base):
    __tablename__ = 'psm_teachercoursestandard'
    __table_args__ = (
        Index('psm_teachercoursestandard_uf1', 'teacherid', 'courseid', 'standardid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    courseid = Column(ForeignKey('psm_course.id'), nullable=False)
    standardid = Column(ForeignKey('psm_standard.id'))
    teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_course = relationship('PsmCourse')
    psm_standard = relationship('PsmStandard')
    psm_teacher = relationship('PsmTeacher')


class PsmTeacherfavoritecomment(Base):
    __tablename__ = 'psm_teacherfavoritecomment'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False, index=True)
    commentbankid = Column(ForeignKey('psm_commentbank.id'), index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_commentbank = relationship('PsmCommentbank')
    psm_teacher = relationship('PsmTeacher')


class PsmTeacherlink(Base):
    __tablename__ = 'psm_teacherlink'
    __table_args__ = (
        Index('psm_teacherlinki2', 'teacherlinkgroupid', 'linkid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    title = Column(String(256))
    description = Column(String(4000))
    url = Column(String(4000))
    linktype = Column(Numeric(10, 0, asdecimal=False))
    preferredorder = Column(Numeric(10, 0, asdecimal=False))
    linkid = Column(ForeignKey('psm_link.id'), index=True)
    teacherlinkgroupid = Column(ForeignKey('psm_teacherlinkgroup.id'))
    teacherid = Column(ForeignKey('psm_teacher.id'), index=True)

    psm_link = relationship('PsmLink')
    psm_teacher = relationship('PsmTeacher')
    psm_teacherlinkgroup = relationship('PsmTeacherlinkgroup')


class PsmTeacherlinkgroup(Base):
    __tablename__ = 'psm_teacherlinkgroup'
    __table_args__ = (
        Index('psm_teacherlinkgroupi2', 'teacherid', 'linkgroupid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    title = Column(String(256))
    description = Column(String(4000))
    groupcolor = Column(Numeric(19, 0, asdecimal=False))
    teacherid = Column(ForeignKey('psm_teacher.id'))
    linkgroupid = Column(ForeignKey('psm_linkgroup.id'), index=True)

    psm_linkgroup = relationship('PsmLinkgroup')
    psm_teacher = relationship('PsmTeacher')


class PsmTeacherlinksource(Base):
    __tablename__ = 'psm_teacherlinksource'
    __table_args__ = (
        Index('psm_teacherlinksourcei2', 'teacherlinkid', 'courseid', 'schoolid', 'teacherid'),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    teacherlinkid = Column(ForeignKey('psm_teacherlink.id'))
    teacherid = Column(ForeignKey('psm_teacher.id'), index=True)
    schoolid = Column(ForeignKey('psm_school.id'), index=True)
    courseid = Column(ForeignKey('psm_course.id'), index=True)

    psm_course = relationship('PsmCourse')
    psm_school = relationship('PsmSchool')
    psm_teacher = relationship('PsmTeacher')
    psm_teacherlink = relationship('PsmTeacherlink')


class PsmTerm(Base):
    __tablename__ = 'psm_term'
    __table_args__ = (
        Index('psm_term4', 'startdate', 'enddate'),
        Index('psm_term1', 'schoolid', 'parenttermid', 'schoolyear', 'termcode', unique=True)
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    termcode = Column(String(30), nullable=False, index=True)
    schoolyear = Column(Numeric(10, 0, asdecimal=False), index=True)
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    description = Column(String(4000))
    portion = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(ForeignKey('psm_school.id'), nullable=False)
    parenttermid = Column(ForeignKey('psm_term.id'), index=True)

    parent = relationship('PsmTerm', remote_side=[id])
    psm_school = relationship('PsmSchool')


class PsmUsereventlog(Base):
    __tablename__ = 'psm_usereventlog'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    usertype = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    accountid = Column(ForeignKey('psm_account.id'), index=True)
    teacherid = Column(ForeignKey('psm_teacher.id'), index=True)
    eventtime = Column(DateTime, nullable=False)
    usereventtypeid = Column(ForeignKey('psm_usereventtype.id'), nullable=False, index=True)
    accountsessionid = Column(ForeignKey('psm_accountsession.id'), index=True)
    sourceip = Column(String(30), nullable=False)
    description = Column(String(256))
    accountusername = Column(String(50))
    accountfirstname = Column(String(50))
    accountlastname = Column(String(50))
    teacherusername = Column(String(50))
    teacherfirstname = Column(String(50))
    teacherlastname = Column(String(50))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))
    teachernotifiedflag = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))

    psm_account = relationship('PsmAccount')
    psm_accountsession = relationship('PsmAccountsession')
    psm_teacher = relationship('PsmTeacher')
    psm_usereventtype = relationship('PsmUsereventtype')


class PsmUsereventtype(Base):
    __tablename__ = 'psm_usereventtype'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    abbreviation = Column(String(30), nullable=False)
    description = Column(String(256))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))


class PsmUserpreference(Base):
    __tablename__ = 'psm_userpreference'
    __table_args__ = (
        Index('psm_userpreference_u2', 'teacherid', 'schoolid', 'name', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), nullable=False)
    value = Column(String(256))
    teacherid = Column(ForeignKey('psm_teacher.id'))
    schoolid = Column(ForeignKey('psm_school.id'), index=True)
    whocreated = Column(String(30), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("CURRENT_DATE"))
    whomodified = Column(String(30))
    whenmodified = Column(DateTime)

    psm_school = relationship('PsmSchool')
    psm_teacher = relationship('PsmTeacher')


class PsmUsersession(Base):
    __tablename__ = 'psm_usersession'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    conversationcredentials = Column(String(4000))
    timestampvalue = Column(DateTime)
    teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False, index=True)

    psm_teacher = relationship('PsmTeacher')


t_psrw_currentenrollment = Table(
    'psrw_currentenrollment', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('entrydate', DateTime),
    Column('entrycode', String(10)),
    Column('exitdate', DateTime),
    Column('exitcode', String(10)),
    Column('exitcomment', Text),
    Column('schoolentrydate', DateTime),
    Column('schoolentrygradelevel', Numeric(10, 0, asdecimal=False)),
    Column('track', String(20)),
    Column('team', String(10)),
    Column('building', String(10)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('schoolname', String(60)),
    Column('schooladdress', String(79)),
    Column('schoolstate', String(79)),
    Column('schoolzip', String(79)),
    Column('schoolcity', String(79)),
    Column('countyname', String(79)),
    Column('schoolphone', String(31)),
    Column('schoolfax', String(31)),
    Column('principal', String(79)),
    Column('principalphone', String(31)),
    Column('principalemail', String(79)),
    Column('asstprincipal', String(79)),
    Column('asstprincipalphone', String(31)),
    Column('asstprincipalemail', String(79)),
    Column('yearname', String(30)),
    Column('yearid', Numeric(10, 0, asdecimal=False))
)


t_psrw_currentgrade = Table(
    'psrw_currentgrade', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('course_number', String(12)),
    Column('storecode', String(10)),
    Column('grade', String(7)),
    Column('citizenship', String(7)),
    Column('percent', Numeric(asdecimal=False)),
    Column('points', Numeric(asdecimal=False)),
    Column('pointspossible', Numeric(asdecimal=False)),
    Column('startdate', DateTime),
    Column('enddate', DateTime),
    Column('comment_value', Text),
    Column('lastgradeupdate', DateTime),
    Column('varcredit', Numeric(asdecimal=False)),
    Column('overridefg', String(2)),
    Column('gradebooktype', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('termid', Numeric(10, 0, asdecimal=False)),
    Column('course_name', String(40)),
    Column('credit_hours', Numeric(asdecimal=False)),
    Column('corequisites', Text),
    Column('prerequisites', Text),
    Column('credittype', String(20)),
    Column('crhrweight', Numeric(asdecimal=False)),
    Column('sched_department', String(12)),
    Column('sched_do_not_print', Numeric(10, 0, asdecimal=False)),
    Column('sched_lunchcourse', Numeric(10, 0, asdecimal=False)),
    Column('section_number', String(10)),
    Column('section_comment_value', Text),
    Column('expression', String(80)),
    Column('no_of_students', Numeric(10, 0, asdecimal=False)),
    Column('gradescaleid', Numeric(10, 0, asdecimal=False)),
    Column('gradescalename', String(50)),
    Column('house', String(10)),
    Column('maxenrollment', Numeric(10, 0, asdecimal=False)),
    Column('original_expression', String(80)),
    Column('parent_section_id', Numeric(10, 0, asdecimal=False)),
    Column('remaining_available_seats', Numeric(asdecimal=False)),
    Column('roomnumber', String(10)),
    Column('exclude_ada', Numeric(10, 0, asdecimal=False)),
    Column('excludefromclassrank', Numeric(10, 0, asdecimal=False)),
    Column('excludefromgpa', Numeric(10, 0, asdecimal=False)),
    Column('excludefromhonorroll', Numeric(10, 0, asdecimal=False)),
    Column('teacherid', Numeric(10, 0, asdecimal=False)),
    Column('teachername', String(41)),
    Column('termabbreviation', String(6)),
    Column('termname', String(30)),
    Column('class_expression', String(80)),
    Column('course_start_date', DateTime),
    Column('course_end_date', DateTime),
    Column('schoolname', String(60)),
    Column('storecodestartdate', DateTime),
    Column('storecodeenddate', DateTime)
)


t_psrw_healthcertperm = Table(
    'psrw_healthcertperm', metadata,
    Column('userid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False))
)


t_psrw_healthgradelevel = Table(
    'psrw_healthgradelevel', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('certification_date', DateTime),
    Column('certification_status', String(50)),
    Column('certification_first_name', String(30), nullable=False),
    Column('certification_middle_name', String(30)),
    Column('certification_last_name', String(30), nullable=False),
    Column('certification_grade_level', String(30), nullable=False),
    Column('certification_description', String(512)),
    Column('certification_comment', String(512))
)


t_psrw_healthimmunization = Table(
    'psrw_healthimmunization', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('vaccine_id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('vaccine_name', String(50), nullable=False),
    Column('vaccine_sort_order', Numeric(10, 0, asdecimal=False)),
    Column('vaccine_code', String(30), nullable=False),
    Column('vaccine_dose_count', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('vaccine_description', String(512)),
    Column('vaccine_mandatoryoptional', Numeric(1, 0, asdecimal=False)),
    Column('vaccine_compliance_mode', Numeric(1, 0, asdecimal=False)),
    Column('vaccine_state_name', String(50)),
    Column('vaccine_state_code', String(30)),
    Column('compliance_status', Numeric(asdecimal=False)),
    Column('exemption_status', Numeric(asdecimal=False)),
    Column('exemption_reason', String(50)),
    Column('exemption_code', String(30)),
    Column('exemption_state_reason', String(50)),
    Column('exemption_state_code', String(30)),
    Column('immunization_comment', String(512)),
    Column('administered_dose_count', Numeric(asdecimal=False))
)


t_psrw_healthimmunizationdoses = Table(
    'psrw_healthimmunizationdoses', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('vaccine_id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('student_imm_record_id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('imm_source_id', Numeric(19, 0, asdecimal=False)),
    Column('dose_number', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('dose_date_administered', DateTime),
    Column('dose_date_recorded', DateTime),
    Column('compliancy_statement', String(100)),
    Column('compliancy_status', String(13)),
    Column('certificate_type_code', String(30)),
    Column('certificate_type_name', String(50)),
    Column('certificate_type_state_code', String(30)),
    Column('certificate_type_state_name', String(50)),
    Column('is_default_certificate_type', Numeric(1, 0, asdecimal=False)),
    Column('vaccine_name', String(50)),
    Column('vaccine_sort_order', Numeric(10, 0, asdecimal=False)),
    Column('vaccine_dose_count', Numeric(10, 0, asdecimal=False))
)


t_psrw_healthimmuperm = Table(
    'psrw_healthimmuperm', metadata,
    Column('userid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False))
)


t_psrw_healthmedical = Table(
    'psrw_healthmedical', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('custom', Text),
    Column('active_med_alert_indicator', Numeric(asdecimal=False)),
    Column('medical_alert_text', Text),
    Column('medical_alert_exp_date', DateTime),
    Column('immunization_status', Numeric(asdecimal=False))
)


t_psrw_healthofficevisits = Table(
    'psrw_healthofficevisits', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('visit_date', DateTime, nullable=False),
    Column('time_in', String(8)),
    Column('time_out', String(8)),
    Column('visit_type', String(50)),
    Column('visit_type_id', Numeric(19, 0, asdecimal=False)),
    Column('provider_name', String(30)),
    Column('provider_type', String(50)),
    Column('parentguardian_contact_ind', Numeric(1, 0, asdecimal=False)),
    Column('visit_reason', String(512)),
    Column('assessment', String(512)),
    Column('actions', String(512)),
    Column('outcome', String(50)),
    Column('outcome_id', Numeric(19, 0, asdecimal=False))
)


t_psrw_healthofficevisitsperm = Table(
    'psrw_healthofficevisitsperm', metadata,
    Column('userid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False))
)


t_psrw_healthscreeningtypes = Table(
    'psrw_healthscreeningtypes', metadata,
    Column('screeningtypeid', Numeric(asdecimal=False)),
    Column('screeningtypename', String(12))
)


t_psrw_healthscreeningwaiver = Table(
    'psrw_healthscreeningwaiver', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('waiver_date', DateTime, nullable=False),
    Column('parentguardian_name', String(30)),
    Column('grade_level', String(6)),
    Column('waiver_reason', String(50)),
    Column('comments', String(512))
)


t_psrw_healthscreenperm = Table(
    'psrw_healthscreenperm', metadata,
    Column('userid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False))
)


t_psrw_healthstudhearing = Table(
    'psrw_healthstudhearing', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('screeningtypeid', Numeric(asdecimal=False)),
    Column('screening_date', DateTime, nullable=False),
    Column('provider_name', String(30)),
    Column('provider_type', String(50)),
    Column('grade_level', String(6)),
    Column('left_ear_result', String(50)),
    Column('right_ear_result', String(50)),
    Column('test_type', String(50)),
    Column('referral_date', DateTime),
    Column('hearing_aid', String(256)),
    Column('late_test_indicator', Numeric(asdecimal=False)),
    Column('impaired_test_indicator', Numeric(asdecimal=False)),
    Column('outcome', String(50)),
    Column('comments', String(512))
)


t_psrw_healthstudoral = Table(
    'psrw_healthstudoral', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('screeningtypeid', Numeric(asdecimal=False)),
    Column('screening_date', DateTime, nullable=False),
    Column('provider_name', String(30)),
    Column('provider_type', String(50)),
    Column('grade_level', String(6)),
    Column('sealants', Numeric(1, 0, asdecimal=False)),
    Column('malocclusion', Numeric(1, 0, asdecimal=False)),
    Column('historyofcaries', Numeric(1, 0, asdecimal=False)),
    Column('untreatedcaries', Numeric(1, 0, asdecimal=False)),
    Column('treatmenturgency', String(50)),
    Column('outcome', String(50)),
    Column('comments', String(512))
)


t_psrw_healthstudscoliosis = Table(
    'psrw_healthstudscoliosis', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('screeningtypeid', Numeric(asdecimal=False)),
    Column('screening_date', DateTime, nullable=False),
    Column('provider_name', String(30)),
    Column('provider_type', String(50)),
    Column('grade_level', String(6)),
    Column('xray_film_date', DateTime),
    Column('xray_film_impression', String(50)),
    Column('outcome', String(50)),
    Column('comments', String(512))
)


t_psrw_healthstudtuberculosis = Table(
    'psrw_healthstudtuberculosis', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('screeningtypeid', Numeric(asdecimal=False)),
    Column('screening_date', DateTime, nullable=False),
    Column('provider_name', String(30)),
    Column('provider_type', String(50)),
    Column('grade_level', String(6)),
    Column('skin_test_given_date', DateTime),
    Column('skin_test_read_date', DateTime),
    Column('skin_test_type', String(50)),
    Column('skin_test_result', String(50)),
    Column('induration_size', Numeric(12, 2)),
    Column('xray_film_date', DateTime),
    Column('xray_film_impression', String(50)),
    Column('outcome', String(50)),
    Column('comments', String(512))
)


t_psrw_healthstudvision = Table(
    'psrw_healthstudvision', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('screeningtypeid', Numeric(asdecimal=False)),
    Column('screening_date', DateTime, nullable=False),
    Column('provider_name', String(30)),
    Column('provider_type', String(50)),
    Column('grade_level', String(6)),
    Column('referral_date', DateTime),
    Column('late_test_indicator', Numeric(asdecimal=False)),
    Column('left_eye_result', String(50)),
    Column('right_eye_result', String(50)),
    Column('color_blind_test_result', String(50)),
    Column('vision_aid', String(256)),
    Column('outcome', String(50)),
    Column('comments', String(512))
)


t_psrw_healthvitalsigns = Table(
    'psrw_healthvitalsigns', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('screeningtypeid', Numeric(asdecimal=False)),
    Column('screening_date', DateTime, nullable=False),
    Column('provider_name', String(30)),
    Column('provider_type', String(50)),
    Column('grade_level', String(6)),
    Column('height', String(10)),
    Column('height_percentile', String(6)),
    Column('weight', String(10)),
    Column('weight_percentile', String(6)),
    Column('weight_status', String(50)),
    Column('bmi', Numeric(asdecimal=False)),
    Column('systolic', String(6)),
    Column('diastolic', String(6)),
    Column('heart_rate', String(6)),
    Column('temperature', String(6)),
    Column('outcome', String(50)),
    Column('comments', String(512))
)


t_psrw_historicalgrade = Table(
    'psrw_historicalgrade', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('behavior', String(7)),
    Column('excludefromclassrank', Numeric(10, 0, asdecimal=False)),
    Column('course_name', String(40)),
    Column('course_number', String(11)),
    Column('credit_type', String(20)),
    Column('datestored', DateTime),
    Column('earnedcrhrs', Numeric(asdecimal=False)),
    Column('gpa_addedvalue', Numeric(asdecimal=False)),
    Column('excludefromgpa', Numeric(10, 0, asdecimal=False)),
    Column('gpa_points', Float),
    Column('grade', String(7)),
    Column('gradescale_name', String(50)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('excludefromhonorroll', Numeric(10, 0, asdecimal=False)),
    Column('percent', Numeric(asdecimal=False)),
    Column('potentialcrhrs', Numeric(asdecimal=False)),
    Column('schoolname', String(60)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('storecode', String(10)),
    Column('absences', Numeric(asdecimal=False)),
    Column('tardies', Numeric(asdecimal=False)),
    Column('comment_value', Text),
    Column('teacher_name', String(40)),
    Column('termid', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('log', Text),
    Column('termname', String(30)),
    Column('termabbreviation', String(6)),
    Column('schoolyear', String(30)),
    Column('storecodestartdate', DateTime),
    Column('storecodeenddate', DateTime),
    Column('storecodeportion', String(42))
)


t_psrw_incident = Table(
    'psrw_incident', metadata,
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('school_number', Numeric(asdecimal=False)),
    Column('school_name', String(60)),
    Column('incident_title', String(80)),
    Column('incident_detail_desc', Text),
    Column('entry_author', String(50)),
    Column('incident_ts', DateTime),
    Column('financial_impact', Numeric(10, 0, asdecimal=False)),
    Column('incident_reference_value', String(30)),
    Column('location_details', String(256)),
    Column('created_by', String(40)),
    Column('created_ts', DateTime),
    Column('last_modified_by', String(40)),
    Column('last_modified_ts', DateTime)
)


t_psrw_incidentaction = Table(
    'psrw_incidentaction', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('duration_incident_detail_id', Numeric(10, 0, asdecimal=False)),
    Column('chng_rsn_incident_detail_id', Numeric(10, 0, asdecimal=False)),
    Column('action_plan_begin_dt', DateTime),
    Column('incident_category', String(50), nullable=False),
    Column('action_change_reason', String(256)),
    Column('lookup_code_desc', String(512)),
    Column('app_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('created_by', String(40)),
    Column('created_ts', DateTime),
    Column('action_plan_end_dt', DateTime),
    Column('last_modified_by', String(40)),
    Column('last_modified_ts', DateTime),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_app_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('short_desc', String(80)),
    Column('action_resolved_desc', String(256)),
    Column('action_actual_resolved_dt', DateTime),
    Column('state_aggregate_rpt_code', String(20)),
    Column('duration_assigned', Numeric(10, 2)),
    Column('duration_actual', Numeric(10, 2)),
    Column('duration_notes', String(256))
)


t_psrw_incidentactionattribute = Table(
    'psrw_incidentactionattribute', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_action_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_detail_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('text_attribute', String(2000)),
    Column('is_yes1_no0_attribute', Numeric(1, 0, asdecimal=False)),
    Column('number_attribute', Numeric(12, 2)),
    Column('date_attribute', DateTime),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('sub_category', String(50)),
    Column('datatype_attribute', String(30)),
    Column('select_attribute', String(2000))
)


t_psrw_incidentactionchange = Table(
    'psrw_incidentactionchange', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('short_desc', String(80))
)


t_psrw_incidentattribute = Table(
    'psrw_incidentattribute', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('lu_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('lu_sub_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_incidentbehavior = Table(
    'psrw_incidentbehavior', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('app_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_report_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('is_state_report_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('severity', Numeric(12, 2)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category_1', String(50), nullable=False),
    Column('sub_app_display_order_1', Numeric(10, 0, asdecimal=False)),
    Column('long_desc_1', String(256)),
    Column('sub_is_police_report_flg_1', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('short_desc_1', String(80)),
    Column('sub_is_state_report_flg_1', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('sub_category_2', String(50)),
    Column('sub_app_display_order_2', Numeric(10, 0, asdecimal=False)),
    Column('long_desc_2', String(256)),
    Column('sub_is_police_report_flg_2', Numeric(1, 0, asdecimal=False)),
    Column('short_desc_2', String(80)),
    Column('sub_is_state_report_flg_2', Numeric(1, 0, asdecimal=False)),
    Column('sub_category_3', String(50)),
    Column('sub_app_display_order_3', Numeric(10, 0, asdecimal=False)),
    Column('long_desc_3', String(256)),
    Column('sub_is_police_report_flg_3', Numeric(1, 0, asdecimal=False)),
    Column('short_desc_3', String(80)),
    Column('sub_is_state_report_flg_3', Numeric(1, 0, asdecimal=False)),
    Column('sub_category_4', String(50)),
    Column('sub_app_display_order_4', Numeric(10, 0, asdecimal=False)),
    Column('long_desc_4', String(256)),
    Column('sub_is_police_report_flg_4', Numeric(1, 0, asdecimal=False)),
    Column('short_desc_4', String(80)),
    Column('sub_is_state_report_flg_4', Numeric(1, 0, asdecimal=False)),
    Column('primary_indicator', Numeric(asdecimal=False))
)


t_psrw_incidentchangehistory = Table(
    'psrw_incidentchangehistory', metadata,
    Column('change_rsn_desc_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('description', String(2048), nullable=False),
    Column('created_by', String(40)),
    Column('created_ts', DateTime),
    Column('last_modified_by', String(40)),
    Column('last_modified_ts', DateTime)
)


t_psrw_incidentcode = Table(
    'psrw_incidentcode', metadata,
    Column('lu_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('code_type', String(50), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('state_aggregate_rpt_code', String(20)),
    Column('lu_sub_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('sub_category', String(50), nullable=False),
    Column('severity', Numeric(12, 2)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('short_desc', String(80)),
    Column('long_desc', String(256))
)


t_psrw_incidentduration = Table(
    'psrw_incidentduration', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('short_desc', String(80))
)


t_psrw_incidentlocation = Table(
    'psrw_incidentlocation', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('code_app_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('lookup_code_desc', String(512)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_app_display_order', Numeric(asdecimal=False)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_incidentobject = Table(
    'psrw_incidentobject', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('object_desc', String(2048)),
    Column('object_quantity', Numeric(10, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False)),
    Column('created_by', String(40)),
    Column('created_ts', DateTime),
    Column('last_modified_by', String(40)),
    Column('last_modified_ts', DateTime)
)


t_psrw_incidentparticipant = Table(
    'psrw_incidentparticipant', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('incident_id', Numeric(10, 0, asdecimal=False)),
    Column('first_name', String(50)),
    Column('middle_name', String(30)),
    Column('last_name', String(50)),
    Column('gender', String(10)),
    Column('dob', DateTime),
    Column('age', Numeric(asdecimal=False)),
    Column('participant_number', String(21)),
    Column('role_code', String(50)),
    Column('role_subcode', String(50)),
    Column('participant_type', String(8)),
    Column('participant_title', String(40)),
    Column('created_by', String(40)),
    Column('created_ts', DateTime),
    Column('last_modified_by', String(40)),
    Column('last_modified_ts', DateTime),
    Column('unknown_indicator', Numeric(asdecimal=False)),
    Column('schoolid', Numeric(asdecimal=False)),
    Column('school_name', String(60)),
    Column('grade_level', Numeric(asdecimal=False))
)


t_psrw_incidentparticipantaction = Table(
    'psrw_incidentparticipantaction', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_action_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_person_role_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('duration_incident_detail_id', Numeric(10, 0, asdecimal=False)),
    Column('chng_rsn_incident_detail_id', Numeric(10, 0, asdecimal=False)),
    Column('action_plan_begin_dt', DateTime),
    Column('incident_category', String(50), nullable=False),
    Column('action_change_reason', String(256)),
    Column('lookup_code_desc', String(512)),
    Column('app_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('created_by', String(40)),
    Column('created_ts', DateTime),
    Column('action_plan_end_dt', DateTime),
    Column('last_modified_by', String(40)),
    Column('last_modified_ts', DateTime),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_app_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('short_desc', String(80)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False)),
    Column('action_resolved_desc', String(256)),
    Column('action_actual_resolved_dt', DateTime),
    Column('state_aggregate_rpt_code', String(20)),
    Column('duration_assigned', Numeric(10, 2)),
    Column('duration_actual', Numeric(10, 2)),
    Column('duration_notes', String(256))
)


t_psrw_incidentparticipantobject = Table(
    'psrw_incidentparticipantobject', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_person_role_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('object_desc', String(2048)),
    Column('object_quantity', Numeric(10, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False)),
    Column('created_by', String(40)),
    Column('created_ts', DateTime),
    Column('last_modified_by', String(40)),
    Column('last_modified_ts', DateTime)
)


t_psrw_incidenttimeframe = Table(
    'psrw_incidenttimeframe', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('lookup_code_desc', String(512)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_incidenttype = Table(
    'psrw_incidenttype', metadata,
    Column('id', Numeric(asdecimal=False)),
    Column('incident_detail_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('lu_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('lu_sub_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('code_type', String(50), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('state_aggregate_rpt_code', String(20)),
    Column('sub_category', String(50)),
    Column('severity', Numeric(12, 2)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('short_desc', String(80)),
    Column('long_desc', String(256))
)


t_psrw_incidenttypeforuser = Table(
    'psrw_incidenttypeforuser', metadata,
    Column('userid', Numeric(asdecimal=False)),
    Column('groupid', Numeric(asdecimal=False)),
    Column('incident_security_group_id', Numeric(asdecimal=False)),
    Column('lu_code_id', Numeric(10, 0, asdecimal=False)),
    Column('incident_category', String(50)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('lu_sub_code_id', Numeric(10, 0, asdecimal=False)),
    Column('sub_category', String(50)),
    Column('severity', Numeric(12, 2)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('short_desc', String(80)),
    Column('long_desc', String(256)),
    Column('schoolid', Numeric(asdecimal=False))
)


t_psrw_lucodeandsubcode = Table(
    'psrw_lucodeandsubcode', metadata,
    Column('lu_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('code_type', String(50), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('state_aggregate_rpt_code', String(20)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('created_by', String(30)),
    Column('created_ts', DateTime),
    Column('last_modified_by', String(30)),
    Column('last_modified_ts', DateTime),
    Column('lu_sub_code_id', Numeric(10, 0, asdecimal=False)),
    Column('sub_category', String(50)),
    Column('severity', Numeric(12, 2)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('short_desc', String(80)),
    Column('long_desc', String(256))
)


t_psrw_participantactionattr = Table(
    'psrw_participantactionattr', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_action_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_detail_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('text_attribute', String(2000)),
    Column('is_yes1_no0_attribute', Numeric(1, 0, asdecimal=False)),
    Column('number_attribute', Numeric(12, 2)),
    Column('date_attribute', DateTime),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False)),
    Column('datatype_attribute', String(30)),
    Column('select_attribute', String(2000))
)


t_psrw_participantactionchange = Table(
    'psrw_participantactionchange', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_participantactionduration = Table(
    'psrw_participantactionduration', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_participantattr = Table(
    'psrw_participantattr', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_person_role_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_participantbehactattr = Table(
    'psrw_participantbehactattr', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_action_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('sub_category', String(50)),
    Column('datatype_attribute', String(30)),
    Column('text_attribute', String(2000)),
    Column('is_yes1_no0_attribute', Numeric(1, 0, asdecimal=False)),
    Column('number_attribute', Numeric(12, 2)),
    Column('date_attribute', DateTime),
    Column('select_attribute', String(2000))
)


t_psrw_participantbehactchng = Table(
    'psrw_participantbehactchng', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_detail_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('action_change_reason', String(256)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_participantbehactdur = Table(
    'psrw_participantbehactdur', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_detail_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('duration_actual', Numeric(10, 2)),
    Column('duration_assigned', Numeric(10, 2)),
    Column('incident_category', String(50), nullable=False),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('lookup_code_desc', String(512)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('duration_notes', String(256)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_participantbehavior = Table(
    'psrw_participantbehavior', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_person_role_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False)),
    Column('severity', Numeric(12, 2)),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_lookup_code_desc', String(512)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False)),
    Column('primary_indicator', Numeric(asdecimal=False))
)


t_psrw_participantbehavioraction = Table(
    'psrw_participantbehavioraction', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('incident_action_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('incident_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('action_resolved_desc', String(256)),
    Column('action_actual_resolved_dt', DateTime),
    Column('action_plan_begin_dt', DateTime),
    Column('incident_category', String(50), nullable=False),
    Column('lookup_code_desc', String(512)),
    Column('application_display_order', Numeric(10, 0, asdecimal=False)),
    Column('is_police_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('is_state_reportable_flg', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('created_by', String(40)),
    Column('created_ts', DateTime),
    Column('action_plan_end_dt', DateTime),
    Column('last_modified_by', String(40)),
    Column('last_modified_ts', DateTime),
    Column('state_aggregate_rpt_code', String(20)),
    Column('state_detail_report_code', String(20)),
    Column('sub_category', String(50)),
    Column('sub_application_display_order', Numeric(asdecimal=False)),
    Column('long_desc', String(256)),
    Column('sub_is_police_reportable_flg', Numeric(asdecimal=False)),
    Column('short_desc', String(80)),
    Column('sub_is_state_reportable_flg', Numeric(asdecimal=False))
)


t_psrw_reportcard_changehistory = Table(
    'psrw_reportcard_changehistory', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('log', Text)
)


t_psrw_reportcard_classrank = Table(
    'psrw_reportcard_classrank', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('class_rank_gpa', String(80)),
    Column('dateranked', DateTime),
    Column('gpamethod', String(50)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('outof', Numeric(10, 0, asdecimal=False)),
    Column('rank', Numeric(10, 0, asdecimal=False)),
    Column('percentage', Numeric(asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('schoolname', String(60)),
    Column('yearid', Numeric(10, 0, asdecimal=False))
)


t_psrw_reportcard_honorroll = Table(
    'psrw_reportcard_honorroll', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('schoolname', String(60)),
    Column('storecode', String(10)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('method', String(50)),
    Column('levelvalue', String(50)),
    Column('message', Text),
    Column('gpa', String(80))
)


t_psrw_reportcard_termbins = Table(
    'psrw_reportcard_termbins', metadata,
    Column('storecode', String(90)),
    Column('yearid', Numeric(10, 0, asdecimal=False))
)


t_psrw_schoolenrollment = Table(
    'psrw_schoolenrollment', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('sourceid', Numeric(10, 0, asdecimal=False)),
    Column('sourcedcid', Numeric(10, 0, asdecimal=False)),
    Column('sourcetable', String(13)),
    Column('studentid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('schoolname', String(60)),
    Column('schoolyear', String(30)),
    Column('entrydate', DateTime),
    Column('entrycode', String(20)),
    Column('exitdate', DateTime),
    Column('exitcode', String(60)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('schooladdress', String(79)),
    Column('schoolcity', String(79)),
    Column('schoolcountry', String(79)),
    Column('schoolfax', String(31)),
    Column('schoolphone', String(31)),
    Column('schoolstate', String(79)),
    Column('schoolzip', String(79)),
    Column('countyname', String(79)),
    Column('principal', String(79)),
    Column('principalphone', String(31)),
    Column('principalemail', String(79)),
    Column('asstprincipal', String(79)),
    Column('asstprincipalphone', String(31)),
    Column('asstprincipalemail', String(79)),
    Column('enrollmenttype', String(7))
)


t_psrw_standardgrade = Table(
    'psrw_standardgrade', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('studentid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('course_number', String(11)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('termid', Numeric(10, 0, asdecimal=False)),
    Column('termcode', String(30), nullable=False),
    Column('subjectarea', String(50)),
    Column('schoolname', String(60)),
    Column('schoolyear', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('actualgradeentered', String(8)),
    Column('lastupdated', DateTime),
    Column('iscalculated', Numeric(3, 0, asdecimal=False)),
    Column('gradescaleid', Numeric(19, 0, asdecimal=False)),
    Column('gradescaledescription', String(4000)),
    Column('gradescalename', String(50)),
    Column('parentstandardid', Numeric(19, 0, asdecimal=False)),
    Column('parentstandardidentifier', String(20)),
    Column('sortorder', Numeric(10, 0, asdecimal=False)),
    Column('reportcarditemdescription', String(4000), nullable=False),
    Column('reportcarditemname', String(400), nullable=False),
    Column('standardid', Numeric(10, 0, asdecimal=False)),
    Column('standardidentifier', String(20)),
    Column('allowscore', Numeric(10, 0, asdecimal=False)),
    Column('storecode', String(30)),
    Column('reportcardcommenttext', String(4000)),
    Column('dateenrolled', DateTime),
    Column('dateleft', DateTime),
    Column('yearid', Numeric(asdecimal=False)),
    Column('expression', String(80)),
    Column('course_name', String(40)),
    Column('credit_hours', Numeric(asdecimal=False)),
    Column('corequisites', String(4000)),
    Column('prerequisites', String(4000)),
    Column('credittype', String(20)),
    Column('crhrweight', Numeric(asdecimal=False)),
    Column('sched_department', String(12)),
    Column('sched_do_not_print', Numeric(10, 0, asdecimal=False)),
    Column('sched_lunchcourse', Numeric(10, 0, asdecimal=False)),
    Column('section_number', String(10)),
    Column('no_of_students', Numeric(10, 0, asdecimal=False)),
    Column('house', String(10)),
    Column('maxenrollment', Numeric(10, 0, asdecimal=False)),
    Column('original_expression', String(80)),
    Column('parent_section_id', Numeric(10, 0, asdecimal=False)),
    Column('remaining_available_seats', Numeric(asdecimal=False)),
    Column('roomnumber', String(10)),
    Column('exclude_ada', Numeric(10, 0, asdecimal=False)),
    Column('excludefromclassrank', Numeric(10, 0, asdecimal=False)),
    Column('excludefromgpa', Numeric(10, 0, asdecimal=False)),
    Column('excludefromhonorroll', Numeric(10, 0, asdecimal=False)),
    Column('teacherid', Numeric(10, 0, asdecimal=False)),
    Column('teachername', String(41)),
    Column('termname', String(4000)),
    Column('storecodestartdate', DateTime),
    Column('storecodeenddate', DateTime)
)


t_psrw_standardhierarchy = Table(
    'psrw_standardhierarchy', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('identifier', String(20)),
    Column('description', String(4000)),
    Column('path', String(4000)),
    Column('sortorder', Numeric(10, 0, asdecimal=False)),
    Column('type', Numeric(asdecimal=False))
)


t_psrw_student_race = Table(
    'psrw_student_race', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('category_code', String(50)),
    Column('category_description', String(40)),
    Column('category_sort', Numeric(10, 0, asdecimal=False)),
    Column('code', String(50)),
    Column('description', String(255)),
    Column('alt_code', String(40)),
    Column('sort', Numeric(10, 0, asdecimal=False))
)


t_psrw_testscores = Table(
    'psrw_testscores', metadata,
    Column('id', Numeric(asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('test_date', DateTime),
    Column('testdescription', Text),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('testname', String(35)),
    Column('testscore_name', String(35)),
    Column('termid', Numeric(10, 0, asdecimal=False)),
    Column('test_type', String(8)),
    Column('alpahscore', String(20)),
    Column('testscoredescription', Text),
    Column('numscore', Float),
    Column('percentscore', Float),
    Column('termname', String(30)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('schoolyear', String(30))
)


t_pssis_adaadm_daily_ctod = Table(
    'pssis_adaadm_daily_ctod', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('attendance_school_abbreviation', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_pssis_adaadm_daily_ttod = Table(
    'pssis_adaadm_daily_ttod', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('attendance_school_abbreviation', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_pssis_adaadm_interval_ttod = Table(
    'pssis_adaadm_interval_ttod', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('attendance_school_abbreviation', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_pssis_adaadm_meeting_ptod = Table(
    'pssis_adaadm_meeting_ptod', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('attendance_school_abbreviation', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('periodcount', Numeric(asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_pssis_adaadm_meeting_ttod = Table(
    'pssis_adaadm_meeting_ttod', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('attendance_school_abbreviation', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_pssis_adaadm_time_ttod = Table(
    'pssis_adaadm_time_ttod', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('attendance_school_abbreviation', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_pssis_adaadm_timeinter_ttod = Table(
    'pssis_adaadm_timeinter_ttod', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('attendance_school_abbreviation', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('total_minutes', Numeric(asdecimal=False)),
    Column('attendancevalue', Numeric(asdecimal=False)),
    Column('membershipvalue', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('student_track', String(20)),
    Column('potential_attendancevalue', Numeric(asdecimal=False))
)


t_pssis_attendance_daily = Table(
    'pssis_attendance_daily', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('att_comment', Text),
    Column('program_name', String(50)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_pssis_attendance_interval = Table(
    'pssis_attendance_interval', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('att_interval', Numeric(10, 0, asdecimal=False)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('ccid', Numeric(10, 0, asdecimal=False)),
    Column('att_comment', Text),
    Column('cc_schoolid', Numeric(10, 0, asdecimal=False)),
    Column('dropped', Numeric(asdecimal=False)),
    Column('periodid', Numeric(10, 0, asdecimal=False)),
    Column('period_abbreviation', String(3)),
    Column('period_number', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('section_number', String(10)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('program_name', String(50)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_pssis_attendance_meeting = Table(
    'pssis_attendance_meeting', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('att_interval', Numeric(10, 0, asdecimal=False)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('ccid', Numeric(10, 0, asdecimal=False)),
    Column('att_comment', Text),
    Column('cc_schoolid', Numeric(10, 0, asdecimal=False)),
    Column('dropped', Numeric(asdecimal=False)),
    Column('periodid', Numeric(10, 0, asdecimal=False)),
    Column('period_abbreviation', String(3)),
    Column('period_number', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('section_number', String(10)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('program_name', String(50)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_pssis_attendance_time = Table(
    'pssis_attendance_time', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('att_comment', Text),
    Column('program_name', String(50)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_pssis_attendance_timeinter = Table(
    'pssis_attendance_timeinter', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('att_date', DateTime),
    Column('attendance_codeid', Numeric(10, 0, asdecimal=False)),
    Column('att_code', String(10)),
    Column('att_mode_code', String(20)),
    Column('att_interval', Numeric(10, 0, asdecimal=False)),
    Column('calendar_dayid', Numeric(10, 0, asdecimal=False)),
    Column('ccid', Numeric(10, 0, asdecimal=False)),
    Column('att_comment', String(4000)),
    Column('cc_schoolid', Numeric(asdecimal=False)),
    Column('periodid', Numeric(asdecimal=False)),
    Column('period_abbreviation', String(3)),
    Column('period_number', Numeric(asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('program_name', String(50)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('insession', Numeric(10, 0, asdecimal=False)),
    Column('count_for_ada', Numeric(10, 0, asdecimal=False)),
    Column('presence_status_cd', String(10)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_abbreviation', String(3)),
    Column('total_minutes', Float)
)


t_pssis_bus_routes = Table(
    'pssis_bus_routes', metadata,
    Column('route_number', String(79)),
    Column('bus_number', String(79)),
    Column('driver_name', String(79)),
    Column('number_students', Numeric(asdecimal=False))
)


t_pssis_enrollment_all = Table(
    'pssis_enrollment_all', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('entrydate', DateTime),
    Column('entrycode', String(20)),
    Column('exitdate', DateTime),
    Column('exitcode', String(20)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(asdecimal=False)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('membershipshare', Float),
    Column('track', String(20)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('yearid', Numeric(asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(4000))
)


t_pssis_membership_defaults = Table(
    'pssis_membership_defaults', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('studentmembership', Float),
    Column('calendarmembership', Float),
    Column('student_track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(30)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('potential_periods_present', Numeric(10, 0, asdecimal=False)),
    Column('potential_minutes_present', Numeric(10, 0, asdecimal=False)),
    Column('periods_absent', Numeric(10, 0, asdecimal=False)),
    Column('minutes_absent', Numeric(10, 0, asdecimal=False))
)


t_pssis_membership_prog = Table(
    'pssis_membership_prog', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('studentmembership', Float),
    Column('calendarmembership', Float),
    Column('track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(4000))
)


t_pssis_membership_reg = Table(
    'pssis_membership_reg', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('studentmembership', Float),
    Column('calendarmembership', Float),
    Column('student_track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(4000)),
    Column('ontrack', Numeric(asdecimal=False)),
    Column('offtrack', Numeric(asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(asdecimal=False))
)


t_pssis_nclb_fields = Table(
    'pssis_nclb_fields', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3))
)


t_pssis_special_pgm_enrollments = Table(
    'pssis_special_pgm_enrollments', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_school_abbreviation', String(20)),
    Column('grade', Numeric(10, 0, asdecimal=False)),
    Column('seop_code', String(15)),
    Column('seop_setting_code', String(15)),
    Column('comment_value', Text),
    Column('exit_reason', Text),
    Column('enter_date', DateTime),
    Column('exit_date', DateTime),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('program_name', String(50))
)


t_pssis_standards = Table(
    'pssis_standards', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('allowassignments', Numeric(1, 0, asdecimal=False)),
    Column('conversionscalename', String(50)),
    Column('conversionscaletext', Text),
    Column('conversionscalereal', Float),
    Column('courses', Text),
    Column('standarddescription', String(4000)),
    Column('identifier', String(20)),
    Column('includecomment', Numeric(10, 0, asdecimal=False)),
    Column('levelvalue', Numeric(asdecimal=False)),
    Column('listparent', String(20)),
    Column('name', String(400)),
    Column('subjectarea', String(40)),
    Column('type', String(6))
)


t_pssis_student_addresses = Table(
    'pssis_student_addresses', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('current_enroll_status', String(15)),
    Column('address_type', String(8)),
    Column('street', String(60)),
    Column('city', String(50)),
    Column('state', String(2)),
    Column('zip', String(10))
)


t_pssis_student_alerts = Table(
    'pssis_student_alerts', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_school_abbreviation', String(20)),
    Column('grade', Numeric(10, 0, asdecimal=False)),
    Column('alert_discipline', Text),
    Column('alert_disciplineexpires', DateTime),
    Column('alert_guardian', Text),
    Column('alert_guardianexpires', DateTime),
    Column('alert_medical', Text),
    Column('alert_medicalexpires', DateTime),
    Column('alert_other', Text),
    Column('alert_otherexpires', DateTime)
)


t_pssis_student_demographics = Table(
    'pssis_student_demographics', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('current_enroll_status', String(15)),
    Column('number_years_in_district', Numeric(asdecimal=False)),
    Column('middle_name', String(30)),
    Column('last_name', String(50)),
    Column('first_name', String(50)),
    Column('date_of_birth', DateTime),
    Column('classof', Numeric(10, 0, asdecimal=False)),
    Column('districtentrydate', DateTime),
    Column('districtentrygradelevel', Numeric(10, 0, asdecimal=False)),
    Column('districtofresidence', String(20)),
    Column('exclude_from_rank', String(3)),
    Column('family_ident', String(30)),
    Column('fee_exemption_status', String(33)),
    Column('graduation_req_set', String(40)),
    Column('home_phone', String(30)),
    Column('locker_combination', String(20)),
    Column('locker_number', String(15)),
    Column('photoflag', Numeric(10, 0, asdecimal=False)),
    Column('ssn', String(12)),
    Column('exclude_from_reporting', String(3)),
    Column('state_enrolled', String(3)),
    Column('state_student_number', String(32)),
    Column('allow_web_access', String(3)),
    Column('web_id', String(20)),
    Column('web_password', String(4000)),
    Column('membershipshare', Float)
)


t_pssis_student_discip_summary = Table(
    'pssis_student_discip_summary', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('log_type', String(50)),
    Column('incident_sub_type', String(20)),
    Column('incident_date', DateTime),
    Column('incident_type', String(79)),
    Column('incident_type_category', String(79)),
    Column('incident_context', String(79)),
    Column('incident_location', String(79)),
    Column('incident_offender', String(79)),
    Column('incident_reporter', String(79)),
    Column('incident_victim_type', String(79)),
    Column('incident_felony', Numeric(10, 0, asdecimal=False)),
    Column('incident_gang_related', Numeric(10, 0, asdecimal=False)),
    Column('incident_hate_crime', Numeric(10, 0, asdecimal=False)),
    Column('incident_alcohol', Numeric(10, 0, asdecimal=False)),
    Column('incident_drug', Numeric(10, 0, asdecimal=False)),
    Column('incident_weapon', Numeric(10, 0, asdecimal=False)),
    Column('incident_weapon_type', String(79)),
    Column('incident_action_taken', String(79)),
    Column('incident_money_loss', Float)
)


t_pssis_student_enrollments = Table(
    'pssis_student_enrollments', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_school_abbreviation', String(20)),
    Column('grade', Numeric(10, 0, asdecimal=False)),
    Column('current_enroll_status', String(15)),
    Column('enrollmentcode', Numeric(10, 0, asdecimal=False)),
    Column('enrollmenttype', String(2)),
    Column('full_time_equivalency', String(80)),
    Column('enrollment_transfer_date_pend', DateTime),
    Column('enrollment_transfer_info', RAW),
    Column('entry_code', String(20)),
    Column('entry_reason', String(4000)),
    Column('entry_date', DateTime),
    Column('exit_code', String(20)),
    Column('exit_reason', String(4000)),
    Column('exit_comment', String(4000)),
    Column('exit_date', DateTime),
    Column('graduated_rank', Numeric(10, 0, asdecimal=False)),
    Column('graduated_schoolname', String(60)),
    Column('log_notes', String(4000)),
    Column('transfer_comments', String(4000)),
    Column('withdrawal_reason', String(4000)),
    Column('lunch_portion_to_pay', String(11)),
    Column('membershipshare', Float),
    Column('tuitionpayer', String(16)),
    Column('track', String(20))
)


t_pssis_student_fees = Table(
    'pssis_student_fees', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_school_abbreviation', String(20)),
    Column('grade', Numeric(10, 0, asdecimal=False)),
    Column('mother_name', String(60)),
    Column('father_name', String(60)),
    Column('physical_address', Numeric(asdecimal=False)),
    Column('home_phone', String(30)),
    Column('lastmeal', String(20)),
    Column('lunch_portion_to_pay', String(3)),
    Column('lunch_id', Float),
    Column('tuitionpayer', String(16)),
    Column('fee_type_name', String(79)),
    Column('fee_category_name', String(21)),
    Column('description', String(79)),
    Column('creation_date', DateTime),
    Column('original_fee_amount', Float),
    Column('prorated_fee_amount', Float),
    Column('fee_balance', Float),
    Column('fee_paid', Float),
    Column('fee_term', String(6)),
    Column('fee_year', String(6)),
    Column('family_original_fee_amount', Numeric(asdecimal=False)),
    Column('family_prorated_fee_amount', Numeric(asdecimal=False)),
    Column('family_fee_paid', Numeric(asdecimal=False)),
    Column('family_fee_balance', Numeric(asdecimal=False))
)


t_pssis_student_relationships = Table(
    'pssis_student_relationships', metadata,
    Column('student_name', String(135)),
    Column('student_number', Float),
    Column('current_school_abbreviation', String(20)),
    Column('grade', Numeric(10, 0, asdecimal=False)),
    Column('type', String(9)),
    Column('full_name', String(60)),
    Column('phone', String(30)),
    Column('emergency_contact_order', String(1)),
    Column('web_id', String(20)),
    Column('web_password', String(4000))
)


t_pssis_student_sched_class_term = Table(
    'pssis_student_sched_class_term', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_school_abbreviation', String(20)),
    Column('grade', Numeric(10, 0, asdecimal=False)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('current_building', String(10)),
    Column('current_homeroom', String(60)),
    Column('current_house', String(10)),
    Column('current_next_school', Numeric(10, 0, asdecimal=False)),
    Column('locker_number', String(15)),
    Column('locker_combination', String(20)),
    Column('course_number', String(11)),
    Column('course_name', String(40)),
    Column('section_number', String(10)),
    Column('section_expression', String(80)),
    Column('teacher_name', String(40)),
    Column('room_number', String(10)),
    Column('term', String(6)),
    Column('term_first_day', DateTime),
    Column('term_last_day', DateTime),
    Column('section_school', String(20))
)


t_pssis_student_scheduling = Table(
    'pssis_student_scheduling', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_school_abbreviation', String(20)),
    Column('grade', Numeric(10, 0, asdecimal=False)),
    Column('current_building', String(10)),
    Column('current_homeroom', String(60)),
    Column('current_house', String(10)),
    Column('current_next_school', Numeric(10, 0, asdecimal=False)),
    Column('sched_lockstudentschedule', Numeric(10, 0, asdecimal=False)),
    Column('sched_nextyearbuilding', String(10)),
    Column('sched_nextyeargrade', Numeric(10, 0, asdecimal=False)),
    Column('sched_nextyearhouse', String(10)),
    Column('sched_nextyearteam', String(10)),
    Column('sched_priority', Numeric(10, 0, asdecimal=False)),
    Column('sched_scheduled', Numeric(10, 0, asdecimal=False)),
    Column('sched_yearofgraduation', Numeric(10, 0, asdecimal=False)),
    Column('current_team', String(10)),
    Column('track', String(20))
)


t_pssis_student_stored_standards = Table(
    'pssis_student_stored_standards', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('current_grade_level', Numeric(10, 0, asdecimal=False)),
    Column('current_school_abbreviation', String(20)),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('standard_identifier', String(20)),
    Column('standard_name', String(400)),
    Column('subject_area', String(40)),
    Column('standard_type', Numeric(asdecimal=False)),
    Column('conversion_scale_name', String(50)),
    Column('year', Numeric(10, 0, asdecimal=False)),
    Column('store_code', String(10)),
    Column('number_of_scores', Numeric(asdecimal=False)),
    Column('high_score', Float),
    Column('average_score', Float),
    Column('translated_average_score', String(50)),
    Column('translated_high_score', String(50)),
    Column('comment_value', Text)
)


t_pssis_student_test_scores = Table(
    'pssis_student_test_scores', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('gender', String(2)),
    Column('ethnicity_name', String(50)),
    Column('ethnicity_code', String(20)),
    Column('special_ed_student', String(3)),
    Column('test_name', String(35)),
    Column('test_date', DateTime),
    Column('test_subtest', String(35)),
    Column('num_score', Float),
    Column('alpha_score', String(20)),
    Column('percent_score', Float)
)


t_pssis_student_transportation = Table(
    'pssis_student_transportation', metadata,
    Column('name', String(135)),
    Column('student_number', Float),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('fromto', String(79)),
    Column('monday', Numeric(10, 0, asdecimal=False)),
    Column('tuesday', Numeric(10, 0, asdecimal=False)),
    Column('wednesday', Numeric(10, 0, asdecimal=False)),
    Column('thursday', Numeric(10, 0, asdecimal=False)),
    Column('friday', Numeric(10, 0, asdecimal=False)),
    Column('saturday', Numeric(10, 0, asdecimal=False)),
    Column('sunday', Numeric(10, 0, asdecimal=False)),
    Column('transportation_type', String(79)),
    Column('route_number', String(79)),
    Column('bus_number', String(79)),
    Column('departure_time', Numeric(10, 0, asdecimal=False)),
    Column('arrival_time', Numeric(10, 0, asdecimal=False)),
    Column('driver_name', String(79)),
    Column('student_emergency_phone', String(30)),
    Column('alert_medical', Text),
    Column('alert_guardian', Text),
    Column('trans_special_instructions', Text)
)


class PssrDataEventQueue(Base):
    __tablename__ = 'pssr_data_event_queue'

    pssr_data_event_queueid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    event_type = Column(Numeric(6, 0, asdecimal=False), nullable=False)
    event_table = Column(String(30), nullable=False)
    event_table_dcid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    event_category = Column(String(30))
    process_state = Column(Numeric(6, 0, asdecimal=False))
    processed_date = Column(DateTime)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    event_table_id = Column(Numeric(10, 0, asdecimal=False))
    state_studentnumber = Column(String(32))
    enrollmentid = Column(Numeric(10, 0, asdecimal=False))
    process_attempts = Column(Numeric(4, 0, asdecimal=False), server_default=text("0"))
    event_fields = Column(Text)
    created_user_id = Column(Numeric(10, 0, asdecimal=False))
    created_user_ip_address = Column(String(45))
    created_user_org_code = Column(Numeric(10, 0, asdecimal=False))


t_pssr_enrollment = Table(
    'pssr_enrollment', metadata,
    Column('source', String(1)),
    Column('dcid', Numeric(10, 0, asdecimal=False)),
    Column('recordid', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('track', String(20)),
    Column('entrydate', DateTime),
    Column('entrycode', String(20)),
    Column('exitdate', DateTime),
    Column('exitcode', String(20)),
    Column('exitcomment', String(4000)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('enrollmenttype', String(2))
)


t_pssr_im_code_map_status = Table(
    'pssr_im_code_map_status', metadata,
    Column('code_type', String(50), nullable=False, unique=True),
    Column('last_map_time', DateTime),
    Column('last_map_status', String(2000))
)


t_pssr_incident_code_map = Table(
    'pssr_incident_code_map', metadata,
    Column('lu_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('lu_sub_code_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('code_type', String(50), nullable=False),
    Column('incident_category', String(50), nullable=False),
    Column('sub_category', String(50), nullable=False),
    Column('new_lu_code_id', Numeric(10, 0, asdecimal=False)),
    Column('new_lu_sub_code_id', Numeric(10, 0, asdecimal=False)),
    Index('pssr_incident_code_map_u1', 'lu_code_id', 'lu_sub_code_id', unique=True)
)


t_pssr_sif_enrollment_refids = Table(
    'pssr_sif_enrollment_refids', metadata,
    Column('studentdcid', Numeric(10, 0, asdecimal=False)),
    Column('dcid', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schooldcid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('entrydate', DateTime),
    Column('exitdate', DateTime),
    Column('src', Numeric(asdecimal=False))
)


t_pssr_student_section_dates = Table(
    'pssr_student_section_dates', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('sectionid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('ps_dateenrolled', DateTime),
    Column('ps_dateleft', DateTime),
    Column('firstday', DateTime),
    Column('lastday', DateTime)
)


t_pssr_vaccinations = Table(
    'pssr_vaccinations', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('vaccinename', String(50), nullable=False),
    Column('vaccinecode', String(30), nullable=False),
    Column('reportname', String(50)),
    Column('reportcode', String(30)),
    Column('exempt', Numeric(asdecimal=False)),
    Column('exemptcode', String(30)),
    Column('compliant', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('recordsource', String(100)),
    Column('dose', Numeric(10, 0, asdecimal=False)),
    Column('dateadministered', DateTime),
    Column('displayorder', Numeric(asdecimal=False))
)


t_pt_enrollment_all = Table(
    'pt_enrollment_all', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False), index=True),
    Column('schoolid', Numeric(10, 0, asdecimal=False), index=True),
    Column('entrydate', DateTime),
    Column('entrycode', String(20)),
    Column('exitdate', DateTime),
    Column('exitcode', String(20)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('programid', Numeric(10, 0, asdecimal=False)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('membershipshare', Float),
    Column('track', String(20)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(30)),
    Index('pt_enrollment_allidx4', 'schoolid', 'entrydate'),
    Index('pt_enrollment_allidx3', 'studentid', 'schoolid', 'entrydate', 'exitdate')
)


t_pt_membership_defaults = Table(
    'pt_membership_defaults', metadata,
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('calendardate', DateTime),
    Column('studentmembership', Float),
    Column('calendarmembership', Float),
    Column('student_track', String(20)),
    Column('fteid', Numeric(10, 0, asdecimal=False)),
    Column('attendance_conversion_id', Numeric(10, 0, asdecimal=False)),
    Column('dflt_att_mode_code', String(13)),
    Column('dflt_conversion_mode_code', String(11)),
    Column('track_a', Numeric(10, 0, asdecimal=False)),
    Column('track_b', Numeric(10, 0, asdecimal=False)),
    Column('track_c', Numeric(10, 0, asdecimal=False)),
    Column('track_d', Numeric(10, 0, asdecimal=False)),
    Column('track_e', Numeric(10, 0, asdecimal=False)),
    Column('track_f', Numeric(10, 0, asdecimal=False)),
    Column('att_calccntpresentabsent', String(7)),
    Column('att_intervalduration', String(30)),
    Column('ontrack', Numeric(10, 0, asdecimal=False)),
    Column('offtrack', Numeric(10, 0, asdecimal=False)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('bell_schedule_id', Numeric(10, 0, asdecimal=False)),
    Column('cycle_day_id', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('potential_periods_present', Numeric(10, 0, asdecimal=False)),
    Column('potential_minutes_present', Numeric(10, 0, asdecimal=False)),
    Column('periods_absent', Numeric(10, 0, asdecimal=False)),
    Column('minutes_absent', Numeric(10, 0, asdecimal=False)),
    Index('pt_membership_defaultsidx3', 'studentid', 'schoolid', 'calendardate'),
    Index('pt_membership_defaultsidx2', 'schoolid', 'calendardate'),
    Index('pt_membership_defaultsidx1', 'schoolid', 'dflt_att_mode_code', 'dflt_conversion_mode_code')
)


class QrtzCalendar(Base):
    __tablename__ = 'qrtz_calendars'

    calendar_name = Column(String(200), primary_key=True, nullable=False)
    calendar = Column(LargeBinary, nullable=False)
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzFiredTrigger(Base):
    __tablename__ = 'qrtz_fired_triggers'
    __table_args__ = (
        Index('idx_qrtz_ft_jg', 'sched_name', 'job_group'),
        Index('idx_qrtz_ft_trig_inst_name', 'sched_name', 'instance_name'),
        Index('idx_qrtz_ft_inst_job_req_rcvry', 'sched_name', 'instance_name', 'requests_recovery'),
        Index('idx_qrtz_ft_j_g', 'sched_name', 'job_name', 'job_group'),
        Index('idx_qrtz_ft_trig_nm_gp', 'trigger_name', 'trigger_group'),
        Index('idx_qrtz_ft_tg', 'sched_name', 'trigger_group'),
        Index('idx_qrtz_ft_t_g', 'sched_name', 'trigger_name', 'trigger_group')
    )

    entry_id = Column(String(95), primary_key=True, nullable=False)
    trigger_name = Column(String(200), nullable=False, index=True)
    trigger_group = Column(String(200), nullable=False, index=True)
    instance_name = Column(String(200), nullable=False)
    fired_time = Column(Numeric(13, 0, asdecimal=False), nullable=False)
    priority = Column(Numeric(13, 0, asdecimal=False), nullable=False)
    state = Column(String(16), nullable=False)
    job_name = Column(String(200), index=True)
    job_group = Column(String(200), index=True)
    requests_recovery = Column(String(1), index=True)
    is_nonconcurrent = Column(String(1))
    is_update_data = Column(String(1))
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzJobDetail(Base):
    __tablename__ = 'qrtz_job_details'
    __table_args__ = (
        Index('idx_qrtz_j_req_recovery', 'sched_name', 'requests_recovery'),
        Index('idx_qrtz_j_grp', 'sched_name', 'job_group')
    )

    job_name = Column(String(200), primary_key=True, nullable=False)
    job_group = Column(String(200), primary_key=True, nullable=False)
    description = Column(String(250))
    job_class_name = Column(String(250), nullable=False)
    is_durable = Column(String(1), nullable=False)
    requests_recovery = Column(String(1), nullable=False)
    job_data = Column(LargeBinary)
    is_nonconcurrent = Column(String(1))
    is_update_data = Column(String(1))
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzLock(Base):
    __tablename__ = 'qrtz_locks'

    lock_name = Column(String(40), primary_key=True, nullable=False)
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzPausedTriggerGrp(Base):
    __tablename__ = 'qrtz_paused_trigger_grps'

    trigger_group = Column(String(200), primary_key=True, nullable=False)
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzSchedulerState(Base):
    __tablename__ = 'qrtz_scheduler_state'

    instance_name = Column(String(200), primary_key=True, nullable=False)
    last_checkin_time = Column(Numeric(13, 0, asdecimal=False), nullable=False)
    checkin_interval = Column(Numeric(13, 0, asdecimal=False), nullable=False)
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzTrigger(Base):
    __tablename__ = 'qrtz_triggers'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'job_name', 'job_group'], ['qrtz_job_details.sched_name', 'qrtz_job_details.job_name', 'qrtz_job_details.job_group']),
        Index('idx_qrtz_t_jg', 'sched_name', 'job_group'),
        Index('idx_qrtz_t_next_fire_time', 'sched_name', 'next_fire_time'),
        Index('idx_qrtz_t_nft_st', 'sched_name', 'trigger_state', 'next_fire_time'),
        Index('idx_qrtz_t_nft_st_misfire_grp', 'sched_name', 'misfire_instr', 'next_fire_time', 'trigger_group', 'trigger_state'),
        Index('idx_qrtz_t_n_g_state', 'sched_name', 'trigger_group', 'trigger_state'),
        Index('idx_qrtz_t_nft_misfire', 'sched_name', 'misfire_instr', 'next_fire_time'),
        Index('idx_qrtz_t_c', 'sched_name', 'calendar_name'),
        Index('idx_qrtz_t_j', 'sched_name', 'job_name', 'job_group'),
        Index('idx_qrtz_t_nft_st_misfire', 'sched_name', 'misfire_instr', 'next_fire_time', 'trigger_state'),
        Index('idx_qrtz_t_n_state', 'sched_name', 'trigger_name', 'trigger_group', 'trigger_state'),
        Index('idx_qrtz_t_g', 'sched_name', 'trigger_group'),
        Index('idx_qrtz_t_state', 'sched_name', 'trigger_state')
    )

    trigger_name = Column(String(200), primary_key=True, nullable=False)
    trigger_group = Column(String(200), primary_key=True, nullable=False)
    job_name = Column(String(200), nullable=False)
    job_group = Column(String(200), nullable=False)
    description = Column(String(250))
    next_fire_time = Column(Numeric(13, 0, asdecimal=False))
    prev_fire_time = Column(Numeric(13, 0, asdecimal=False))
    priority = Column(Numeric(13, 0, asdecimal=False))
    trigger_state = Column(String(16), nullable=False)
    trigger_type = Column(String(8), nullable=False)
    start_time = Column(Numeric(13, 0, asdecimal=False), nullable=False)
    end_time = Column(Numeric(13, 0, asdecimal=False))
    calendar_name = Column(String(200))
    misfire_instr = Column(Numeric(2, 0, asdecimal=False))
    job_data = Column(LargeBinary)
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))

    qrtz_job_detail = relationship('QrtzJobDetail')


class QrtzBlobTrigger(QrtzTrigger):
    __tablename__ = 'qrtz_blob_triggers'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'trigger_name', 'trigger_group'], ['qrtz_triggers.sched_name', 'qrtz_triggers.trigger_name', 'qrtz_triggers.trigger_group']),
    )

    trigger_name = Column(String(200), primary_key=True, nullable=False)
    trigger_group = Column(String(200), primary_key=True, nullable=False)
    blob_data = Column(LargeBinary)
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzCronTrigger(QrtzTrigger):
    __tablename__ = 'qrtz_cron_triggers'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'trigger_name', 'trigger_group'], ['qrtz_triggers.sched_name', 'qrtz_triggers.trigger_name', 'qrtz_triggers.trigger_group']),
    )

    trigger_name = Column(String(200), primary_key=True, nullable=False)
    trigger_group = Column(String(200), primary_key=True, nullable=False)
    cron_expression = Column(String(120), nullable=False)
    time_zone_id = Column(String(80))
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzSimpleTrigger(QrtzTrigger):
    __tablename__ = 'qrtz_simple_triggers'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'trigger_name', 'trigger_group'], ['qrtz_triggers.sched_name', 'qrtz_triggers.trigger_name', 'qrtz_triggers.trigger_group']),
    )

    trigger_name = Column(String(200), primary_key=True, nullable=False)
    trigger_group = Column(String(200), primary_key=True, nullable=False)
    repeat_count = Column(Numeric(7, 0, asdecimal=False), nullable=False)
    repeat_interval = Column(Numeric(12, 0, asdecimal=False), nullable=False)
    times_triggered = Column(Numeric(7, 0, asdecimal=False), nullable=False)
    sched_name = Column(String(120), primary_key=True, nullable=False, server_default=text("'ReportManager' "))


class QrtzSimpropTrigger(QrtzTrigger):
    __tablename__ = 'qrtz_simprop_triggers'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'trigger_name', 'trigger_group'], ['qrtz_triggers.sched_name', 'qrtz_triggers.trigger_name', 'qrtz_triggers.trigger_group']),
    )

    sched_name = Column(String(120), primary_key=True, nullable=False)
    trigger_name = Column(String(200), primary_key=True, nullable=False)
    trigger_group = Column(String(200), primary_key=True, nullable=False)
    str_prop_1 = Column(String(512))
    str_prop_2 = Column(String(512))
    str_prop_3 = Column(String(512))
    int_prop_1 = Column(Numeric(scale=0, asdecimal=False))
    int_prop_2 = Column(Numeric(scale=0, asdecimal=False))
    long_prop_1 = Column(Numeric(13, 0, asdecimal=False))
    long_prop_2 = Column(Numeric(13, 0, asdecimal=False))
    dec_prop_1 = Column(Numeric(13, 4))
    dec_prop_2 = Column(Numeric(13, 4))
    bool_prop_1 = Column(String(1))
    bool_prop_2 = Column(String(1))


class QueriesTable(Base):
    __tablename__ = 'queries_table'

    id = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    sqlquery = Column(String(4000), nullable=False)
    name = Column(String(64), nullable=False)
    nametodisplay = Column(String(40))
    description = Column(String(100))
    dataset = Column(String(100))
    sortorder = Column(Numeric(4, 0, asdecimal=False))
    active = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Queue(Base):
    __tablename__ = 'queue'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    type = Column(Numeric(10, 0, asdecimal=False), index=True)
    cmd = Column(Numeric(10, 0, asdecimal=False))
    tdata1 = Column(Text)
    tdata2 = Column(Text)
    tdata3 = Column(Text)
    tdata4 = Column(Text)
    tdata5 = Column(Text)
    date_value = Column(DateTime)
    time = Column(Numeric(10, 0, asdecimal=False))
    countvalue = Column(Numeric(10, 0, asdecimal=False))
    tryagainindex = Column(Numeric(10, 0, asdecimal=False), index=True)


class Reenrollment(Base):
    __tablename__ = 'reenrollments'
    __table_args__ = (
        Index('reenrollments_u2', 'studentid', 'dcid', unique=True),
        Index('reenrollments_n6', 'studentid', 'schoolid', 'entrydate', 'exitdate', 'track')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), unique=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    entrydate = Column(DateTime, index=True)
    entrycode = Column(String(20))
    entrycomment = Column(Text)
    exitdate = Column(DateTime, index=True)
    exitcode = Column(String(20))
    exitcomment = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    grade_level = Column(Numeric(10, 0, asdecimal=False))
    type = Column(Numeric(10, 0, asdecimal=False))
    track = Column(String(20))
    districtofresidence = Column(String(20))
    enrollmenttype = Column(String(2))
    enrollmentcode = Column(Numeric(10, 0, asdecimal=False))
    fulltimeequiv_obsolete = Column(Float)
    membershipshare = Column(Float)
    tuitionpayer = Column(Numeric(10, 0, asdecimal=False))
    lunchstatus = Column(String(11))
    custom = Column(Text)
    fteid = Column(Numeric(10, 0, asdecimal=False), index=True)
    withdrawal_reason_code = Column(String(3))
    studentschlenrl_guid = Column(String(32), index=True)
    psguid = Column(String(50), unique=True)


class CReenrollmentsoutofdistrict(Reenrollment):
    __tablename__ = 'c_reenrollmentsoutofdistrict'

    reenrollmentsdcid = Column(ForeignKey('reenrollments.dcid'), primary_key=True)
    districtname = Column(String(60))
    schoolname = Column(String(60))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whenmodified = Column(DateTime)
    whocreated = Column(String(100), server_default=text("'PS'"))
    whomodified = Column(String(100))


class Registreq(Base):
    __tablename__ = 'registreq'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(80))
    description = Column(Text)
    type = Column(String(20))
    reqforgrad = Column(Numeric(10, 0, asdecimal=False))
    appliesto = Column(String(20))
    appliestodata = Column(String(80))
    courselist = Column(Text)
    courselisthtml = Column(Text)
    courselistcheck = Column(Text)
    reqcrhrs = Column(Float)
    overallcrhrs = Column(Float)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    fieldname = Column(String(40))
    fieldcomparator = Column(String(10))
    fieldmatchvalue = Column(String(40))
    appliestodisp = Column(String(60))
    appliestodatali = Column(Numeric(10, 0, asdecimal=False))
    grade_level = Column(Numeric(10, 0, asdecimal=False), index=True)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    itemtype = Column(String(20))
    how2dispcourses = Column(String(20))
    courselistorder = Column(String(20))
    minimummessage = Column(Text)
    coursegroup = Column(String(40))
    coursedesig = Column(String(30))
    entryboxwidth = Column(Numeric(10, 0, asdecimal=False))
    entryboxheight = Column(Numeric(10, 0, asdecimal=False))
    listboxheight = Column(Numeric(10, 0, asdecimal=False))
    minnoofcourses = Column(Numeric(10, 0, asdecimal=False))
    maxnoofcourses = Column(Numeric(10, 0, asdecimal=False))
    countinreqtots = Column(Numeric(10, 0, asdecimal=False))
    firstitem = Column(String(40))
    classification = Column(String(30))
    subtype = Column(String(20))
    credittype = Column(String(20))
    coursesource = Column(String(20))
    subjectarea = Column(String(30))
    requesttype = Column(String(20))
    multiterm = Column(String(20))
    schedpriority = Column(Numeric(10, 0, asdecimal=False))
    reqterms = Column(String(20))
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)


class Relationship(Base):
    __tablename__ = 'relationship'
    __table_args__ = (
        Index('relationship_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    person_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    relatedperson_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    reciprocalrelationship_id = Column(Numeric(10, 0, asdecimal=False), index=True)


class Repobatchsetup(Base):
    __tablename__ = 'repobatchsetups'
    __table_args__ = (
        Index('repobatchsetups_u2', 'internal_id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    reportsetupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    creation_date = Column(DateTime)
    creation_time = Column(Numeric(10, 0, asdecimal=False))
    creation_timestamp = Column(String(15))
    status = Column(String(31), index=True)
    userid = Column(Numeric(10, 0, asdecimal=False), index=True)
    start_date = Column(DateTime)
    start_time = Column(Numeric(10, 0, asdecimal=False))
    start_timestamp = Column(String(15))
    end_date = Column(DateTime)
    end_time = Column(Numeric(10, 0, asdecimal=False))
    when_to_execute = Column(Numeric(10, 0, asdecimal=False))
    specific_date = Column(DateTime)
    specific_time = Column(Numeric(10, 0, asdecimal=False))
    zwhat_to_do_with_result = Column(Numeric(10, 0, asdecimal=False))
    merger_action = Column(String(21))
    setups = Column(String(21))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    destination = Column(String(21))
    user_variables_as_text = Column(Text)
    reportid = Column(String(79))
    external_filename = Column(Text)
    filename = Column(Text)
    use_current_selection = Column(Numeric(10, 0, asdecimal=False))
    current_selection_blob = Column(LargeBinary)
    resulting_error_code = Column(Numeric(10, 0, asdecimal=False))
    resulting_error_message = Column(Text)
    international_chars_option = Column(Numeric(10, 0, asdecimal=False))
    priority = Column(Numeric(10, 0, asdecimal=False))
    type = Column(Numeric(10, 0, asdecimal=False))
    tabletouse_name = Column(String(31))
    user_environment_blob = Column(LargeBinary)
    external_filesize = Column(Numeric(10, 0, asdecimal=False))
    checksum = Column(String(33), index=True)
    server_instanceid = Column(Numeric(10, 0, asdecimal=False), index=True)
    report_output = Column(LargeBinary)


class Repolookuptable(Base):
    __tablename__ = 'repolookuptables'
    __table_args__ = (
        Index('repolookuptables_u2', 'internal_id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    reportsetupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    table_name = Column(String(31))


class Repolookuptablescontentsitem(Base):
    __tablename__ = 'repolookuptablescontentsitems'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    lookuptablerecordid = Column(Numeric(10, 0, asdecimal=False), index=True)
    lookuptableid = Column(Numeric(10, 0, asdecimal=False))
    field_index = Column(Numeric(10, 0, asdecimal=False))
    value = Column(String(79))


class Repolookuptablescontrecord(Base):
    __tablename__ = 'repolookuptablescontrecords'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    lookuptableid = Column(Numeric(10, 0, asdecimal=False), index=True)
    record_index = Column(Numeric(10, 0, asdecimal=False))


class Repolookuptablesdefitem(Base):
    __tablename__ = 'repolookuptablesdefitems'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    lookuptableid = Column(Numeric(10, 0, asdecimal=False), index=True)
    field_index = Column(Numeric(10, 0, asdecimal=False))
    item_name = Column(String(31))
    value_type = Column(Numeric(10, 0, asdecimal=False))
    description = Column(Text)
    max_nbr_of_chars = Column(Numeric(10, 0, asdecimal=False))


class Report(Base):
    __tablename__ = 'reports'
    __table_args__ = (
        Index('reports_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(60), index=True)
    masterfile = Column(Numeric(10, 0, asdecimal=False), index=True)
    heading = Column(Text)
    footing = Column(Text)
    body = Column(Text)
    custom = Column(Text)
    type = Column(Numeric(10, 0, asdecimal=False), index=True)
    numcols = Column(Numeric(10, 0, asdecimal=False))
    columntitles = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    teacheraccess = Column(Numeric(10, 0, asdecimal=False))
    unused5 = Column(Numeric(10, 0, asdecimal=False))
    unused6 = Column(Numeric(10, 0, asdecimal=False))


class Reposetup(Base):
    __tablename__ = 'reposetups'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    creationdate = Column(DateTime)
    creationtime = Column(Numeric(10, 0, asdecimal=False))
    creationby = Column(String(79))
    modificationdate = Column(DateTime)
    modificationtime = Column(Numeric(10, 0, asdecimal=False))
    modificationby = Column(String(79))
    management_reportversion = Column(String(11))
    xml_formatversion = Column(String(11))
    dateofimport = Column(DateTime)
    reportid = Column(String(31))
    reportname = Column(Text)
    tabletouse = Column(Numeric(10, 0, asdecimal=False))
    fileformat = Column(String(5))
    fielddelimiter = Column(String(79))
    recorddelimiter = Column(String(79))
    doublequotesurrounded = Column(Numeric(10, 0, asdecimal=False))
    filenametemplate = Column(Text)
    filenamemaxlength = Column(Numeric(10, 0, asdecimal=False))
    description = Column(Text)
    encoding_type = Column(String(79))
    destination_file_path = Column(Text)
    header_export = Column(Numeric(10, 0, asdecimal=False))
    fixedlength_totalwidthinchars = Column(Numeric(10, 0, asdecimal=False))
    for_current_school = Column(Numeric(10, 0, asdecimal=False))
    loadedfrom_filepathonly = Column(Text)
    reporttype = Column(String(79))
    usermodifiable = Column(Numeric(10, 0, asdecimal=False))
    reportcategory = Column(String(31))
    columns_multi_order = Column(Numeric(10, 0, asdecimal=False))
    template = Column(Text)
    send_conf_to_email_address = Column(Text)
    send_error_to_email_address = Column(Text)
    state_id = Column(String(11))
    due_date = Column(Text)
    contact_name = Column(Text)
    contact_email = Column(Text)
    contact_phone = Column(Text)
    contact_url = Column(Text)
    columns_display_headers = Column(Numeric(10, 0, asdecimal=False))
    columns_export_headers = Column(Numeric(10, 0, asdecimal=False))
    columns_nbr_lines_per_page = Column(Numeric(10, 0, asdecimal=False))
    columns_nbr_items_per_line = Column(Numeric(10, 0, asdecimal=False))
    destination_type = Column(String(79))
    destination_email_dest_address = Column(Text)
    destination_email_subject = Column(Text)
    destination_email_send_attach = Column(Numeric(10, 0, asdecimal=False))
    destination_email_msg = Column(Text)
    destination_ftp_server_name = Column(Text)
    destination_ftp_path = Column(Text)
    destination_ftp_user_name = Column(String(79))
    destination_ftp_password = Column(String(79))
    general_owner_info = Column(Text)
    header_display = Column(Numeric(10, 0, asdecimal=False))
    header_text = Column(Text)
    header_repeat_at_breaks = Column(Numeric(10, 0, asdecimal=False))
    footer_display = Column(Numeric(10, 0, asdecimal=False))
    footer_export = Column(Numeric(10, 0, asdecimal=False))
    footer_text = Column(Text)
    footer_repeat_at_breaks = Column(Numeric(10, 0, asdecimal=False))
    columns_nbr_of_break_level = Column(Numeric(10, 0, asdecimal=False))
    columns_generate_total_line = Column(Numeric(10, 0, asdecimal=False))
    destination_web_mime_type = Column(String(79))
    list_of_values = Column(Text)
    contact_job_title = Column(String(79))
    filenametemplate_ = Column(Text)
    comments_to_user = Column(Text)
    loadedfrom_datestamp = Column(String(21))
    loadedfrom_filename = Column(String(79))
    value_type = Column(Numeric(10, 0, asdecimal=False))
    revision_date = Column(Text)
    merger_user_vars_action = Column(Numeric(10, 0, asdecimal=False))
    use_current_selection = Column(Numeric(10, 0, asdecimal=False))
    include_in_list = Column(Numeric(10, 0, asdecimal=False))
    programmer_comments = Column(Text)
    validation_expression = Column(Text)
    international_chars_option = Column(Numeric(10, 0, asdecimal=False))
    disable_use_current_sel_over = Column(Numeric(10, 0, asdecimal=False))
    disable_curr_school_only_over = Column(Numeric(10, 0, asdecimal=False))
    disable_destination_over = Column(Numeric(10, 0, asdecimal=False))
    disable_int_char_option_over = Column(Numeric(10, 0, asdecimal=False))
    disable_nbr_of_lines_per_page = Column(Numeric(10, 0, asdecimal=False))
    disable_nbr_of_items_per_line = Column(Numeric(10, 0, asdecimal=False))
    dont_reset_page_number = Column(Numeric(10, 0, asdecimal=False))
    tabletouse_name = Column(String(31))
    doublequote_removewhenempty = Column(Numeric(10, 0, asdecimal=False))
    param_att_modes = Column(Numeric(10, 0, asdecimal=False))
    param_schools = Column(Numeric(10, 0, asdecimal=False))
    param_schools_options = Column(Text)
    param_schools_script = Column(Text)
    param_source = Column(Numeric(10, 0, asdecimal=False))
    param_grades = Column(Numeric(10, 0, asdecimal=False))
    param_grades_options = Column(Text)
    param_grades_script = Column(Text)
    param_att_codes = Column(Numeric(10, 0, asdecimal=False))
    param_datetoscan = Column(Numeric(10, 0, asdecimal=False))
    param_rep_segments = Column(Numeric(10, 0, asdecimal=False))
    param_weeks = Column(Numeric(10, 0, asdecimal=False))
    param_weeks_options = Column(Text)
    param_teachers = Column(Numeric(10, 0, asdecimal=False))
    param_teachers_options = Column(Text)
    param_teachers_script = Column(Text)
    param_periods = Column(Numeric(10, 0, asdecimal=False))
    param_periods_options = Column(Text)
    param_lines_per_page = Column(Numeric(10, 0, asdecimal=False))
    param_items_per_line = Column(Numeric(10, 0, asdecimal=False))
    param_starting_page_nbr = Column(Numeric(10, 0, asdecimal=False))
    param_att_conv = Column(Numeric(10, 0, asdecimal=False))
    param_att_codes_categ = Column(Numeric(10, 0, asdecimal=False))
    param_prcs_options = Column(Numeric(10, 0, asdecimal=False))
    param_prcs_options_def = Column(Text)
    param_dest = Column(Numeric(10, 0, asdecimal=False))
    param_uservars_sel_script = Column(Text)
    param_misc = Column(Numeric(10, 0, asdecimal=False))
    param_misc_options = Column(Text)
    param_daterange = Column(Numeric(10, 0, asdecimal=False))
    param_att_codes_options = Column(Text)
    param_att_codes_categ_opt = Column(Text)
    param_javascript_toinsert = Column(Text)
    use_parameters_yn = Column(Numeric(10, 0, asdecimal=False))
    param_submit_button_code = Column(Text)
    param_update_script = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Reposetupsitem(Base):
    __tablename__ = 'reposetupsitems'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    reportsetupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    itemnbr = Column(Numeric(10, 0, asdecimal=False))
    titleheading = Column(Text)
    datatoexport = Column(Text)
    missingvaluesymbol = Column(String(79))
    fixedlength_startposition = Column(Numeric(10, 0, asdecimal=False))
    fixedlength_length = Column(Numeric(10, 0, asdecimal=False))
    fixedlength_fillchar = Column(String(11))
    fixedlength_justification = Column(Numeric(10, 0, asdecimal=False))
    conversiontable = Column(Text)
    user_modifiable = Column(Numeric(10, 0, asdecimal=False))
    display_format = Column(String(79))
    trim_start_at = Column(Numeric(10, 0, asdecimal=False))
    trim_nbr_of_chars = Column(Numeric(10, 0, asdecimal=False))
    nbr_of_decimals = Column(Numeric(10, 0, asdecimal=False))
    description = Column(Text)
    value_type = Column(Numeric(10, 0, asdecimal=False))
    conversion_table_def_value = Column(Text)
    user_info = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Reposetupsorderby(Base):
    __tablename__ = 'reposetupsorderby'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    reportsetupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    order_index = Column(Numeric(10, 0, asdecimal=False))
    table_number = Column(Numeric(10, 0, asdecimal=False))
    field_number = Column(Numeric(10, 0, asdecimal=False))
    formula_and_parameters = Column(Text)
    direction_up = Column(Numeric(10, 0, asdecimal=False))
    value_type = Column(Numeric(10, 0, asdecimal=False))
    break_generation = Column(String(21))
    break_gen_formula = Column(Text)
    formula_and_parameters_display = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Reposetupsquery(Base):
    __tablename__ = 'reposetupsqueries'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    reportsetupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    order_index = Column(Numeric(10, 0, asdecimal=False))
    type = Column(String(11))
    table_nbr = Column(Numeric(10, 0, asdecimal=False))
    simple_query = Column(Text)
    comments = Column(Text)
    table_name = Column(String(31))


class Reposetupsqueryitem(Base):
    __tablename__ = 'reposetupsqueryitems'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    queryid = Column(Numeric(10, 0, asdecimal=False), index=True)
    order_index = Column(Numeric(10, 0, asdecimal=False))
    table_number = Column(Numeric(10, 0, asdecimal=False))
    field_number = Column(Numeric(10, 0, asdecimal=False))
    value_type = Column(Numeric(10, 0, asdecimal=False))
    comparator = Column(Numeric(10, 0, asdecimal=False))
    value_as_string = Column(Text)
    conjunction = Column(Numeric(10, 0, asdecimal=False))
    formula_and_or_parameters = Column(Text)
    formula_and_or_parameters_ = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Reposetupsuserdatum(Base):
    __tablename__ = 'reposetupsuserdata'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    reportsetupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    order_index = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(79))
    description = Column(Text)
    defaultvalue = Column(Text)
    value_type = Column(Numeric(10, 0, asdecimal=False))
    required = Column(Numeric(10, 0, asdecimal=False))
    valid_lower_limit = Column(String(79))
    valid_upper_limit = Column(String(79))
    valid_min_nbr_of_chars = Column(Numeric(10, 0, asdecimal=False))
    valid_max_nbr_of_chars = Column(Numeric(10, 0, asdecimal=False))
    display_as = Column(String(11))
    display_as_info = Column(Text)
    to_update = Column(Numeric(10, 0, asdecimal=False))
    user_info = Column(Text)
    options = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Reposetupsuserdatadefault(Base):
    __tablename__ = 'reposetupsuserdatadefaults'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    reportsetupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    userdata_name = Column(String(79))
    defaultvalue = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Reposetupsvariable(Base):
    __tablename__ = 'reposetupsvariables'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    reportsetupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    order_index = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(31))
    description = Column(Text)
    value_type = Column(Numeric(10, 0, asdecimal=False))
    when_to_set = Column(Numeric(10, 0, asdecimal=False))
    value = Column(Text)
    missing_value_symbol = Column(Text)
    initialization_value = Column(Text)
    permanent_in_merger = Column(Numeric(10, 0, asdecimal=False))


class Robj(Base):
    __tablename__ = 'robj'
    __table_args__ = (
        Index('robj_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    reportid = Column(Numeric(10, 0, asdecimal=False), index=True)
    seq = Column(Numeric(10, 0, asdecimal=False))
    type = Column(String(40))
    text = Column(Text)
    custom = Column(Text)
    name = Column(Text)
    name2 = Column(Text)
    page = Column(String(3))
    layer = Column(Numeric(10, 0, asdecimal=False))
    label = Column(String(30))
    x1 = Column(Float)
    y1 = Column(Float)
    x2 = Column(Float)
    y2 = Column(Float)
    id = Column(Numeric(10, 0, asdecimal=False))


class Roleacces(Base):
    __tablename__ = 'roleaccess'
    __table_args__ = (
        Index('roleaccess_u2', 'roledefid', 'roleavailableaccessid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    roledefid = Column(ForeignKey('roledef.id'), nullable=False, index=True)
    roleavailableaccessid = Column(ForeignKey('roleavailableaccess.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    roleavailableacces = relationship('Roleavailableacces')
    roledef = relationship('Roledef')


class Roleattributegroup(Base):
    __tablename__ = 'roleattributegroup'

    roleattributegroupid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    rolemoduleid = Column(ForeignKey('rolemodule.id'), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    rolemodule = relationship('Rolemodule')


class Roleavailableacces(Base):
    __tablename__ = 'roleavailableaccess'
    __table_args__ = (
        Index('roleavailableaccess_u2', 'rolemoduleid', 'code', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(100), nullable=False)
    matrixvisible = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    iseditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    sortorder = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    rolemoduleid = Column(ForeignKey('rolemodule.id'), nullable=False, index=True)
    code = Column(String(100), nullable=False)
    description = Column(String(1024))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    roleattributegroupid = Column(Numeric(19, 0, asdecimal=False))

    rolemodule = relationship('Rolemodule')


class Roleavailablecapability(Base):
    __tablename__ = 'roleavailablecapability'
    __table_args__ = (
        Index('roleavailablecapability_u2', 'code', 'rolemoduleid', 'roleattributegroupid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(100), nullable=False)
    matrixvisible = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    iseditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    sortorder = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    rolemoduleid = Column(ForeignKey('rolemodule.id'), nullable=False, index=True)
    code = Column(String(100), nullable=False)
    description = Column(String(1024))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    roleattributegroupid = Column(ForeignKey('roleattributegroup.roleattributegroupid'), index=True)

    roleattributegroup = relationship('Roleattributegroup')
    rolemodule = relationship('Rolemodule')


class Roleavailabledatagroup(Base):
    __tablename__ = 'roleavailabledatagroup'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(256), nullable=False)
    sortorder = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    rolemoduleid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    typename = Column(String(256), nullable=False)
    description = Column(String(1000))
    matrixvisible = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    iseditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    roleattributegroupid = Column(Numeric(19, 0, asdecimal=False))


class Roleavailableidpcapability(Base):
    __tablename__ = 'roleavailableidpcapability'
    __table_args__ = (
        Index('roleavailableidpcapability_u1', 'idprelyingpartyid', 'roleavailablecapabilityid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    idprelyingpartyid = Column(ForeignKey('idprelyingparty.id'), nullable=False)
    roleavailablecapabilityid = Column(ForeignKey('roleavailablecapability.id'), nullable=False, index=True)
    value = Column(String(100))
    whocreated = Column(String(100), nullable=False)
    whencreated = Column(DateTime, nullable=False)
    whomodified = Column(String(100), nullable=False)
    whenmodified = Column(DateTime, nullable=False)

    idprelyingparty = relationship('Idprelyingparty')
    roleavailablecapability = relationship('Roleavailablecapability')


class Roleavailableproperty(Base):
    __tablename__ = 'roleavailableproperty'
    __table_args__ = (
        Index('roleavailableproperty_u2', 'rolemoduleid', 'propname', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(100), nullable=False)
    matrixvisible = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    iseditable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    sortorder = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    rolemoduleid = Column(ForeignKey('rolemodule.id'), nullable=False, index=True)
    propname = Column(String(1024), nullable=False)
    description = Column(String(1024))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    roleattributegroupid = Column(Numeric(19, 0, asdecimal=False))

    rolemodule = relationship('Rolemodule')


class Rolecapability(Base):
    __tablename__ = 'rolecapability'
    __table_args__ = (
        Index('rolecapability_u2', 'roledefid', 'roleavailablecapabilityid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    roledefid = Column(ForeignKey('roledef.id'), nullable=False, index=True)
    roleavailablecapabilityid = Column(ForeignKey('roleavailablecapability.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    roleavailablecapability = relationship('Roleavailablecapability')
    roledef = relationship('Roledef')


class Rolecategoryacces(Base):
    __tablename__ = 'rolecategoryaccess'
    __table_args__ = (
        Index('rolecategoryaccess_n1', 'districtcategoryid', 'roledefid', 'roleavailableaccessid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    districtcategoryid = Column(ForeignKey('districtcategory.id'), nullable=False)
    roledefid = Column(ForeignKey('roledef.id'), nullable=False, index=True)
    roleavailableaccessid = Column(ForeignKey('roleavailableaccess.id'), nullable=False, index=True)
    granted = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    districtcategory = relationship('Districtcategory')
    roleavailableacces = relationship('Roleavailableacces')
    roledef = relationship('Roledef')


t_rolecategorypermissions = Table(
    'rolecategorypermissions', metadata,
    Column('roledefid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('districtcategoryid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('iscategorydeleted', Numeric(1, 0, asdecimal=False)),
    Column('isdefault', Numeric(asdecimal=False)),
    Column('download', Numeric(asdecimal=False)),
    Column('edit', Numeric(asdecimal=False)),
    Column('del', Numeric(asdecimal=False))
)


class Roledatum(Base):
    __tablename__ = 'roledata'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    roledefid = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    roleavailabledatagroupid = Column(Numeric(19, 0, asdecimal=False))
    datakey = Column(String(256), nullable=False)
    sortorder = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    stringvalue = Column(String(1000))
    numbervalue = Column(Numeric(22, 6))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Roledef(Base):
    __tablename__ = 'roledef'
    __table_args__ = (
        Index('roledef_u2', 'rolemoduleid', 'name', unique=True),
        Index('roledef_u3', 'rolemoduleid', 'rolekey', unique=True)
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(100), nullable=False)
    rolekey = Column(String(500), nullable=False)
    rolemoduleid = Column(ForeignKey('rolemodule.id'), nullable=False, index=True)
    description = Column(String(1024))
    islocked = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    isvisible = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    isenabled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    sortorder = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    rolemodule = relationship('Rolemodule')


class Roledefteachersmap(Base):
    __tablename__ = 'roledefteachersmap'
    __table_args__ = (
        Index('roledefteachersmap_u2', 'teachersdcid', 'schoolid', 'roledefid', 'isdistrict', unique=True),
    )

    id = Column(Numeric(asdecimal=False), primary_key=True)
    roledefid = Column(ForeignKey('roledef.id'), nullable=False)
    teachersdcid = Column(ForeignKey('users.dcid'), nullable=False)
    isenabled = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    isdistrict = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    roledef = relationship('Roledef')
    user = relationship('User')


class Roleenterpriserptacces(Base):
    __tablename__ = 'roleenterpriserptaccess'

    roleenterpriserptaccessid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    roledefid = Column(ForeignKey('roledef.id'), nullable=False, index=True)
    rptcategorycode = Column(String(100), nullable=False)
    canviewflag = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    roledef = relationship('Roledef')


class Rolefieldacces(Base):
    __tablename__ = 'rolefieldaccess'
    __table_args__ = (
        Index('rolefieldaccess_u1', 'roledefid', 'fieldlevelsecurityid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True, server_default=text("0 "))
    roledefid = Column(ForeignKey('roledef.id'), nullable=False, server_default=text("0 "))
    fieldlevelsecurityid = Column(ForeignKey('fieldlevelsecurity.fieldlevelsecurityid'), nullable=False, server_default=text("0 "))
    accesslevel = Column(Numeric(3, 0, asdecimal=False), server_default=text("NULL"))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    fieldlevelsecurity = relationship('Fieldlevelsecurity')
    roledef = relationship('Roledef')


class Rolemassdataacces(Base):
    __tablename__ = 'rolemassdataaccess'

    rolemassdataaccessid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    roledefid = Column(ForeignKey('roledef.id'), nullable=False, index=True)
    datasourcename = Column(String(100), nullable=False)
    canexportflag = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    caneditflag = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    roledef = relationship('Roledef')


class Rolemodule(Base):
    __tablename__ = 'rolemodule'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    name = Column(String(300), nullable=False, unique=True)
    description = Column(String(1024), nullable=False, unique=True)
    isvisible = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    isenabled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    version = Column(Numeric(19, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Roleproperty(Base):
    __tablename__ = 'roleproperty'
    __table_args__ = (
        Index('roleproperty_u2', 'roledefid', 'roleavailablepropertyid', unique=True),
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    roledefid = Column(ForeignKey('roledef.id'), nullable=False, index=True)
    roleavailablepropertyid = Column(ForeignKey('roleavailableproperty.id'), nullable=False, index=True)
    propvalue = Column(String(1024))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    roleavailableproperty = relationship('Roleavailableproperty')
    roledef = relationship('Roledef')


class Room(Base):
    __tablename__ = 'room'
    __table_args__ = (
        Index('room_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    room_number = Column(String(10), index=True)
    name = Column(String(30))
    department = Column(String(12))
    building = Column(String(10))
    house = Column(String(10))
    facilities = Column(String(50))
    occupancy_maximum = Column(Numeric(10, 0, asdecimal=False))
    roominfo_guid = Column(String(32), index=True)


class SAcp(Base):
    __tablename__ = 's_acp_s'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    description = Column(String(200))
    name = Column(String(80), nullable=False)
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SCommonLocaldate(Base):
    __tablename__ = 's_common_localdates'

    localid = Column(Numeric(10, 0, asdecimal=False), primary_key=True, nullable=False)
    schoolid = Column(Numeric(10, 0, asdecimal=False), primary_key=True, nullable=False)
    yearid = Column(Numeric(10, 0, asdecimal=False), primary_key=True, nullable=False)
    localstartdate = Column(DateTime, nullable=False)
    localenddate = Column(DateTime, nullable=False)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class SContactRelationshipC(Base):
    __tablename__ = 's_contact_relationship_c'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    s_contacts_sid = Column(ForeignKey('s_contacts_s.id'), nullable=False, index=True)
    can_pickup = Column(Numeric(1, 0, asdecimal=False))
    contact_order = Column(Numeric(11, 0, asdecimal=False))
    emergency_contact = Column(Numeric(1, 0, asdecimal=False))
    end_date = Column(DateTime)
    has_custody = Column(Numeric(1, 0, asdecimal=False))
    legal_guardianship = Column(Numeric(1, 0, asdecimal=False))
    lives_with = Column(Numeric(1, 0, asdecimal=False))
    notes = Column(String(4000))
    primary_contact = Column(Numeric(1, 0, asdecimal=False))
    receive_mailing = Column(Numeric(1, 0, asdecimal=False))
    relationship = Column(String(100))
    start_date = Column(DateTime)
    students_dcid = Column(ForeignKey('students.dcid'))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    association = Column(String(100))
    secondary_contact = Column(Numeric(1, 0, asdecimal=False))

    s_contacts_ = relationship('SContacts')
    student = relationship('Student')


class SContacts(Base):
    __tablename__ = 's_contacts_s'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    cell_phone = Column(String(30))
    date_of_birth = Column(DateTime)
    employer = Column(String(100))
    employment_status = Column(String(30))
    first_name = Column(String(75))
    gender = Column(String(50))
    home_address_1 = Column(String(100))
    home_address_2 = Column(String(100))
    home_address_3 = Column(String(100))
    home_city = Column(String(100))
    home_country = Column(String(100))
    home_county = Column(String(100))
    home_phone = Column(String(30))
    home_postal_code = Column(String(17))
    home_state = Column(String(50))
    job_title = Column(String(100))
    last_name = Column(String(75))
    mailing_address_1 = Column(String(100))
    mailing_address_2 = Column(String(100))
    mailing_address_3 = Column(String(100))
    mailing_city = Column(String(100))
    mailing_country = Column(String(100))
    mailing_county = Column(String(100))
    mailing_postal_code = Column(String(17))
    mailing_state = Column(String(50))
    middle_name = Column(String(75))
    oral_language = Column(String(50))
    personal_email = Column(String(254))
    prefix = Column(String(20))
    state_contactnumber = Column(String(32))
    state_excludefromreporting = Column(Numeric(1, 0, asdecimal=False))
    suffix = Column(String(10))
    work_email = Column(String(254))
    work_phone = Column(String(30))
    written_language = Column(String(50))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SGradelevelAcpC(Base):
    __tablename__ = 's_gradelevel_acp_c'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    s_acp_sid = Column(ForeignKey('s_acp_s.id'), nullable=False, index=True)
    gradelevel = Column(Numeric(11, 0, asdecimal=False), nullable=False)
    name = Column(String(20))
    sortorder = Column(Numeric(11, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    s_acp_ = relationship('SAcp')


class SPremigrationAudit(Base):
    __tablename__ = 's_premigration_audit_s'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    fieldsetname = Column(String(4000))
    lastrunissuecount = Column(Numeric(11, 0, asdecimal=False))
    lastruntime = Column(DateTime)
    whenagreed = Column(DateTime)
    whoagreed = Column(String(100))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SPremigrationIssue(Base):
    __tablename__ = 's_premigration_issue_s'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    coredcid = Column(Numeric(25, 10))
    coretable = Column(String(32))
    dateformat001 = Column(String(50))
    destinationdatatype = Column(String(15))
    destinationfield = Column(String(32))
    destinationlength = Column(Numeric(11, 0, asdecimal=False))
    destinationvalue = Column(String(4000))
    errorcategory = Column(String(20))
    errormessage = Column(String(4000))
    exttable = Column(String(40))
    fieldsetname = Column(String(4000))
    sourcefield = Column(String(100))
    sourcevalue = Column(String(4000))
    statusvalue = Column(String(20))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SReportingSegments(Base):
    __tablename__ = 's_reporting_segments_s'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    enddate = Column(DateTime)
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    segmentname = Column(String(80))
    sortorder = Column(Numeric(11, 0, asdecimal=False))
    startdate = Column(DateTime)
    yearid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SScheduleService(Base):
    __tablename__ = 's_schedule_service_s'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    schedule_cron_expression = Column(String(200))
    schedule_description = Column(String(200))
    schedule_end_date = Column(DateTime)
    schedule_name = Column(String(200))
    schedule_service = Column(String(200))
    schedule_start_date = Column(DateTime)
    schedule_start_time = Column(String(20))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SSnapshotRun(Base):
    __tablename__ = 's_snapshot_run_s'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    disabledelete = Column(Numeric(1, 0, asdecimal=False))
    endtime = Column(DateTime)
    identitycolumn = Column(String(30))
    identitylabel = Column(String(250))
    identityvalue = Column(String(100))
    name = Column(String(250))
    runtimeparams = Column(Text)
    starttime = Column(DateTime)
    status = Column(String(20))
    storagetable = Column(String(30))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SStuAcp(Base):
    __tablename__ = 's_stu_acp_s'
    __table_args__ = (
        Index('s_stu_acp_s_unique', 'studentsdcid', 's_acp_sid', unique=True),
    )

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    primary_tf = Column(Numeric(1, 0, asdecimal=False))
    s_acp_sid = Column(ForeignKey('s_acp_s.id'), nullable=False)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False)
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    s_acp_ = relationship('SAcp')
    student = relationship('Student')


class SStuCrsAcpC(Base):
    __tablename__ = 's_stu_crs_acp_c'
    __table_args__ = (
        Index('s_stu_crs_acp_c_unique', 's_stu_acp_sid', 'coursesdcid', 's_subarea_acp_cid', 's_gradelevel_acp_cid', unique=True),
    )

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    s_stu_acp_sid = Column(ForeignKey('s_stu_acp_s.id'), nullable=False, index=True)
    coursesdcid = Column(ForeignKey('courses.dcid'), nullable=False)
    s_gradelevel_acp_cid = Column(ForeignKey('s_gradelevel_acp_c.id'), nullable=False)
    s_subarea_acp_cid = Column(ForeignKey('s_subarea_acp_c.id'), nullable=False)
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    course = relationship('Course')
    s_gradelevel_acp_c = relationship('SGradelevelAcpC')
    s_stu_acp_ = relationship('SStuAcp')
    s_subarea_acp_c = relationship('SSubareaAcpC')


class SSubareaAcpC(Base):
    __tablename__ = 's_subarea_acp_c'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    s_acp_sid = Column(ForeignKey('s_acp_s.id'), nullable=False, index=True)
    name = Column(String(50), nullable=False)
    sortorder = Column(Numeric(11, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    s_acp_ = relationship('SAcp')


t_saved_fieldstable = Table(
    'saved_fieldstable', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('fileno', Numeric(10, 0, asdecimal=False)),
    Column('fieldno', Numeric(10, 0, asdecimal=False)),
    Column('name', String(50)),
    Column('type', Numeric(10, 0, asdecimal=False)),
    Column('minval', String(20)),
    Column('maxval', String(20)),
    Column('minlen', Numeric(10, 0, asdecimal=False)),
    Column('maxlen', Numeric(10, 0, asdecimal=False)),
    Column('data', Text),
    Column('required', Numeric(10, 0, asdecimal=False)),
    Column('cols', Numeric(10, 0, asdecimal=False)),
    Column('rowsvalue', Numeric(10, 0, asdecimal=False)),
    Column('defaultvalue', String(50)),
    Column('dispname', String(40)),
    Column('dataindex', Numeric(10, 0, asdecimal=False)),
    Column('datalen', Numeric(10, 0, asdecimal=False)),
    Column('html', Text),
    Column('formatstring', String(20)),
    Column('inuse', Numeric(10, 0, asdecimal=False)),
    Column('howdisp', Numeric(10, 0, asdecimal=False)),
    Column('help', Text),
    Column('colno', Numeric(10, 0, asdecimal=False)),
    Column('description', Text),
    Column('inputfilter', Text),
    Column('unused1', Numeric(10, 0, asdecimal=False)),
    Column('syncstatus', Numeric(10, 0, asdecimal=False))
)


t_sc$_ps_audit_tbl = Table(
    'sc$_ps_audit_tbl', metadata,
    Column('logon_seq', Numeric(asdecimal=False)),
    Column('logon_time', DateTime),
    Column('terminal', String(18)),
    Column('sessionid', Numeric(asdecimal=False)),
    Column('instance', String(8)),
    Column('entryid', Numeric(asdecimal=False)),
    Column('isdba', String(5)),
    Column('current_user', String(30)),
    Column('session_user', String(30)),
    Column('session_userid', Numeric(asdecimal=False)),
    Column('proxy_user', String(30)),
    Column('proxy_userid', Numeric(asdecimal=False)),
    Column('db_name', String(8)),
    Column('host', String(20)),
    Column('os_user', String(20)),
    Column('external_name', String(20)),
    Column('ip_address', String(20)),
    Column('network_protocol', String(12)),
    Column('authentication_type', String(12)),
    Column('module', String(48)),
    Column('action', String(32)),
    Column('client_info', String(64)),
    Column('sql_exec_start', DateTime)
)


class ScedCodeMapping(Base):
    __tablename__ = 'sced_code_mapping'

    sced_code_mappingid = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    scedcode = Column(String(10), nullable=False)
    subjecttype = Column(String(30))
    aptype = Column(String(10))
    created_by = Column(String(30), nullable=False)
    created_ts = Column(DateTime, nullable=False)
    last_modified_by = Column(String(30), nullable=False)
    last_modified_ts = Column(DateTime, nullable=False)


class SchedDebug(Base):
    __tablename__ = 'sched_debug'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    debug = Column(Text)
    flag = Column(Numeric(10, 0, asdecimal=False))


class Schedcategorybalancing(Base):
    __tablename__ = 'schedcategorybalancing'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    gendcid = Column(ForeignKey('gen.dcid'), nullable=False, index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gen = relationship('Gen')


class Schedsectprogsetting(Base):
    __tablename__ = 'schedsectprogsettings'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    schedsections_dcid = Column(ForeignKey('schedulesections.dcid'), nullable=False, index=True)
    program_gendcid = Column(ForeignKey('gen.dcid'), nullable=False, index=True)
    operation = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gen = relationship('Gen')
    schedulesection = relationship('Schedulesection')


class Scheduleactivitystatu(Base):
    __tablename__ = 'scheduleactivitystatus'
    __table_args__ = (
        Index('scheduleactivitystatus_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Schedulebldsession(Base):
    __tablename__ = 'schedulebldsessions'
    __table_args__ = (
        Index('schedulebldsessions_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    callback_id = Column(Numeric(10, 0, asdecimal=False))
    userid = Column(Numeric(10, 0, asdecimal=False))
    results = Column(LargeBinary)
    success = Column(Numeric(10, 0, asdecimal=False))
    completed = Column(String(20))
    diags = Column(Text)
    started = Column(Numeric(10, 0, asdecimal=False))
    errorlog = Column(Text)
    enginepings = Column(Numeric(10, 0, asdecimal=False))
    engineip = Column(String(20))
    engineport = Column(Numeric(10, 0, asdecimal=False))
    dbfpath = Column(Text)
    buildid = Column(Numeric(10, 0, asdecimal=False))
    buildtype = Column(String(20))
    isbuild = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    reschedule = Column(Numeric(10, 0, asdecimal=False))
    reschedulestudentselection = Column(LargeBinary)
    comment_value = Column(Text)
    validateonly = Column(Numeric(10, 0, asdecimal=False))
    input = Column(Text)


class Schedulebuildcourserank(Base):
    __tablename__ = 'schedulebuildcourserank'
    __table_args__ = (
        Index('schedulebuildcourserank_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    buildid = Column(Numeric(10, 0, asdecimal=False), index=True)
    rank = Column(Numeric(10, 0, asdecimal=False), index=True)
    systemrank = Column(Numeric(10, 0, asdecimal=False))
    coursenumber = Column(String(10), index=True)
    sectionsoffered = Column(Numeric(10, 0, asdecimal=False))
    periodspercycle = Column(Numeric(10, 0, asdecimal=False))
    demand = Column(Numeric(10, 0, asdecimal=False))
    totalconflictstudents = Column(Numeric(10, 0, asdecimal=False))
    totalconflictcourses = Column(Numeric(10, 0, asdecimal=False))
    constrainedsections = Column(Numeric(10, 0, asdecimal=False))
    comments = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Schedulebuilddiagnostic(Base):
    __tablename__ = 'schedulebuilddiagnostics'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    bd_code = Column(String(25))
    bd_coursenumber = Column(String(12))
    bd_text = Column(Text)
    bd_value = Column(Numeric(10, 0, asdecimal=False))
    bd_buildid = Column(Numeric(10, 0, asdecimal=False))


class Schedulebuilding(Base):
    __tablename__ = 'schedulebuildings'
    __table_args__ = (
        Index('schedulebuildings_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Schedulebuild(Base):
    __tablename__ = 'schedulebuilds'
    __table_args__ = (
        Index('schedulebuilds_n3', 'schoolid', 'currentbuild', 'buildid'),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    buildid = Column(Numeric(10, 0, asdecimal=False), index=True)
    buildname = Column(String(25))
    datelastbuild = Column(DateTime)
    datelastload = Column(DateTime)
    studentswithrequests = Column(Numeric(10, 0, asdecimal=False))
    studentsscheduled = Column(Numeric(10, 0, asdecimal=False))
    totalrequests = Column(Numeric(10, 0, asdecimal=False))
    totalrequestssatisfied = Column(Numeric(10, 0, asdecimal=False))
    lastbuildlog = Column(Text)
    lastloadlog = Column(Text)
    wfconflict = Column(Numeric(10, 0, asdecimal=False))
    potentialconflictweight = Column(Numeric(10, 0, asdecimal=False))
    nonconflictweight = Column(Numeric(10, 0, asdecimal=False))
    wfbalance = Column(Numeric(10, 0, asdecimal=False))
    restrictedweightfactor = Column(Numeric(10, 0, asdecimal=False))
    comments = Column(Text)
    buildyear = Column(Numeric(10, 0, asdecimal=False))
    ppday = Column(Numeric(10, 0, asdecimal=False))
    blocksperday = Column(Numeric(10, 0, asdecimal=False))
    dpcycle = Column(Numeric(10, 0, asdecimal=False))
    nolunchperiods = Column(Numeric(10, 0, asdecimal=False))
    fixedcycleschedule = Column(Numeric(10, 0, asdecimal=False))
    dloadmax = Column(Numeric(10, 0, asdecimal=False))
    maintainintegrityofhouses = Column(Numeric(10, 0, asdecimal=False))
    usestudentpriorityforload = Column(Numeric(10, 0, asdecimal=False))
    userotation = Column(Numeric(10, 0, asdecimal=False))
    sterms = Column(Numeric(10, 0, asdecimal=False))
    loadpct = Column(Float)
    minimumschedulestoevaluate = Column(Numeric(10, 0, asdecimal=False))
    schdpct = Column(Float)
    minimumblockedcoursecombos = Column(Numeric(10, 0, asdecimal=False))
    loadmin = Column(Numeric(10, 0, asdecimal=False))
    schdmin = Column(Numeric(10, 0, asdecimal=False))
    loadsectionthreshold = Column(Numeric(10, 0, asdecimal=False))
    sectionlimitforfullload = Column(Numeric(10, 0, asdecimal=False))
    isthisaload = Column(Numeric(10, 0, asdecimal=False))
    verboselogfile = Column(Numeric(10, 0, asdecimal=False))
    closeroom = Column(Numeric(10, 0, asdecimal=False))
    rndseed = Column(Numeric(10, 0, asdecimal=False))
    currentbuild = Column(Numeric(10, 0, asdecimal=False))
    coursecatalogid = Column(Numeric(10, 0, asdecimal=False), index=True)
    termlevellist = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    showdebug = Column(Numeric(10, 0, asdecimal=False))
    dynamiccombos = Column(Numeric(10, 0, asdecimal=False))
    swaproomsalways = Column(Numeric(10, 0, asdecimal=False))
    swapall = Column(Numeric(10, 0, asdecimal=False))
    calcfutureassignments = Column(Numeric(10, 0, asdecimal=False))
    percenttocalculate = Column(Float)
    futuremaxtime = Column(Float)
    maxmemspedtable = Column(Numeric(10, 0, asdecimal=False))
    rotatedperiods = Column(Numeric(10, 0, asdecimal=False))
    secttype = Column(String(10))
    validperiods = Column(Text)
    usebldg = Column(Numeric(10, 0, asdecimal=False))
    usehouse = Column(Numeric(10, 0, asdecimal=False))
    loadusemax = Column(Numeric(10, 0, asdecimal=False))
    opthours = Column(Numeric(10, 0, asdecimal=False))
    optminutes = Column(Numeric(10, 0, asdecimal=False))
    optmaxrank = Column(Numeric(10, 0, asdecimal=False))
    maxscores = Column(Numeric(10, 0, asdecimal=False))
    debug = Column(Numeric(10, 0, asdecimal=False))
    sortrooms = Column(Numeric(10, 0, asdecimal=False))
    validateonly = Column(Numeric(10, 0, asdecimal=False))
    futureasgnscore = Column(Numeric(10, 0, asdecimal=False))
    futureasgneach = Column(Numeric(10, 0, asdecimal=False))
    verifyasgneach = Column(Numeric(10, 0, asdecimal=False))
    verifyasgnassgn = Column(Numeric(10, 0, asdecimal=False))
    msgmaxcount = Column(Numeric(10, 0, asdecimal=False))
    maxmemfortasgn = Column(Numeric(10, 0, asdecimal=False))
    maxtimeupfutasgn = Column(Numeric(10, 0, asdecimal=False))
    tchoversubfatal = Column(Numeric(10, 0, asdecimal=False))
    invoversubfatal = Column(Numeric(10, 0, asdecimal=False))
    optdebug = Column(Numeric(10, 0, asdecimal=False))
    maxsubstperstd = Column(Numeric(10, 0, asdecimal=False))
    maxsubstpercrs = Column(Numeric(10, 0, asdecimal=False))
    maxsubsatatime = Column(Numeric(10, 0, asdecimal=False))
    usesmallerroom = Column(Numeric(10, 0, asdecimal=False))
    maxmemfortsched = Column(Numeric(10, 0, asdecimal=False))
    invpreschdfatal = Column(Numeric(10, 0, asdecimal=False))
    maxcombofastasgn = Column(Numeric(10, 0, asdecimal=False))
    smaptype = Column(String(2))
    linestodisplay = Column(Numeric(10, 0, asdecimal=False))
    debugscores = Column(Numeric(10, 0, asdecimal=False))
    futureasgnpct = Column(Numeric(10, 0, asdecimal=False))
    tchsortmaxtime = Column(Float)
    rotateddays = Column(Numeric(10, 0, asdecimal=False))
    buildtype = Column(String(10))
    timelastbuild = Column(Numeric(10, 0, asdecimal=False))
    timelastload = Column(Numeric(10, 0, asdecimal=False))
    scenariotype = Column(String(10))


class Schedulecatalog(Base):
    __tablename__ = 'schedulecatalogs'
    __table_args__ = (
        Index('schedulecatalogs_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(80))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(40))
    currentvalue = Column(Numeric(10, 0, asdecimal=False))


class Schedulecc(Base):
    __tablename__ = 'schedulecc'
    __table_args__ = (
        Index('schedulecc_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    dateenrolled = Column(DateTime)
    dateleft = Column(DateTime)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    termid = Column(Numeric(10, 0, asdecimal=False))
    period = Column(String(7))
    teacherid = Column(Numeric(10, 0, asdecimal=False))
    section_number = Column(Numeric(10, 0, asdecimal=False))
    course_number = Column(String(11), index=True)
    studyear = Column(Numeric(10, 0, asdecimal=False))
    buildid = Column(Numeric(10, 0, asdecimal=False))
    bitmap = Column(LargeBinary)
    sectiontype = Column(String(2))
    expression = Column(String(80))
    loadlock = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))


class Scheduleconstraint(Base):
    __tablename__ = 'scheduleconstraints'
    __table_args__ = (
        Index('scheduleconstraints_u2', 'constraintkeyid', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    constraintkeyid = Column(Numeric(10, 0, asdecimal=False))
    constraintcode = Column(String(8))
    codeid = Column(String(15))
    other = Column(String(10))
    type = Column(String(8))
    priority = Column(Numeric(10, 0, asdecimal=False))
    coursenumber = Column(String(11), index=True)
    sectionnumber = Column(String(10))
    sectiontype = Column(String(2))
    term = Column(String(5))
    classroom = Column(String(10))
    coursenumber2 = Column(String(11), index=True)
    sectionnumber2 = Column(String(10))
    teacherid = Column(Numeric(10, 0, asdecimal=False))
    teacherid2 = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    preloadcount = Column(Numeric(10, 0, asdecimal=False))
    team = Column(String(10))
    maximumnumber = Column(Numeric(10, 0, asdecimal=False))
    minimumnumber = Column(Numeric(10, 0, asdecimal=False))
    percent = Column(Float)
    period = Column(String(7))
    period2 = Column(String(7))
    groupschedule = Column(String(12))
    constraintnumber = Column(Numeric(10, 0, asdecimal=False))
    constraintnumber2 = Column(Numeric(10, 0, asdecimal=False))
    constrainttextfield1 = Column(String(10))
    constrainttextfield2 = Column(String(12))
    constraintfield3 = Column(String(15))
    constraintflagfield1 = Column(Numeric(10, 0, asdecimal=False))
    constraintflagfield2 = Column(Numeric(10, 0, asdecimal=False))
    constraintflagfield3 = Column(Numeric(10, 0, asdecimal=False))
    scheduleexpressionbitmap = Column(LargeBinary)
    portion = Column(String(20))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    studentid2 = Column(Numeric(10, 0, asdecimal=False), index=True)
    buildid = Column(Numeric(10, 0, asdecimal=False))
    catalogid = Column(Numeric(10, 0, asdecimal=False))
    expression = Column(String(80))
    termid = Column(Numeric(10, 0, asdecimal=False))
    newrecord = Column(Numeric(10, 0, asdecimal=False))


class Schedulecoursecatalog(Base):
    __tablename__ = 'schedulecoursecatalogs'
    __table_args__ = (
        Index('schedulecoursecatalogs_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    course_number = Column(String(11), index=True)
    course_name = Column(String(40))
    credit_hours = Column(Float)
    add_to_gpa = Column(Float)
    code = Column(String(20))
    prerequisitesvalue = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    custom = Column(Text)
    corequisites = Column(Text)
    powerlink = Column(String(50))
    powerlinkspan = Column(String(80))
    regavailable = Column(Numeric(10, 0, asdecimal=False))
    reggradelevels = Column(String(40))
    regteachers = Column(Text)
    targetclasssize = Column(Numeric(10, 0, asdecimal=False))
    maxclasssize = Column(Numeric(10, 0, asdecimal=False))
    regcoursegroup = Column(String(80))
    multiterm = Column(String(40))
    termsoffered = Column(Text)
    sectionstooffer = Column(Numeric(10, 0, asdecimal=False))
    schoolgroup = Column(Numeric(10, 0, asdecimal=False))
    vocational = Column(Numeric(10, 0, asdecimal=False))
    status = Column(Numeric(10, 0, asdecimal=False))
    credittype = Column(String(20))
    crhrweight = Column(Float)
    sched_year = Column(Numeric(10, 0, asdecimal=False))
    sched_department = Column(String(12))
    sched_coursesubjectareacode = Column(String(8))
    sched_fullcatalogdescription = Column(Text)
    sched_coursepackage = Column(Numeric(10, 0, asdecimal=False))
    sched_coursepkgcontents = Column(Text)
    sched_scheduled = Column(Numeric(10, 0, asdecimal=False))
    sched_scheduletypecode = Column(String(8))
    sched_sectionsoffered = Column(Numeric(10, 0, asdecimal=False))
    sched_teachercount = Column(Numeric(10, 0, asdecimal=False))
    sched_periodspermeeting = Column(Numeric(10, 0, asdecimal=False))
    sched_frequency = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumperiodsperday = Column(Numeric(10, 0, asdecimal=False))
    sched_minimumperiodsperday = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumdayspercycle = Column(Numeric(10, 0, asdecimal=False))
    sched_minimumdayspercycle = Column(Numeric(10, 0, asdecimal=False))
    sched_consecutiveperiods = Column(Numeric(10, 0, asdecimal=False))
    sched_blockstart = Column(Numeric(10, 0, asdecimal=False))
    sched_validstartperiods = Column(Text)
    sched_validdaycombinations = Column(Text)
    validextradaycombinations = Column(Text)
    sched_extradayscheduletypecode = Column(String(8))
    sched_lengthinnumberofterms = Column(Numeric(10, 0, asdecimal=False))
    sched_consecutiveterms = Column(Numeric(10, 0, asdecimal=False))
    sched_balanceterms = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumenrollment = Column(Numeric(10, 0, asdecimal=False))
    sched_concurrentflag = Column(Numeric(10, 0, asdecimal=False))
    sched_facilities = Column(String(50))
    sched_multiplerooms = Column(Numeric(10, 0, asdecimal=False))
    sched_labflag = Column(Numeric(10, 0, asdecimal=False))
    sched_labfrequency = Column(Numeric(10, 0, asdecimal=False))
    sched_labperiodspermeeting = Column(Numeric(10, 0, asdecimal=False))
    sched_repeatsallowed = Column(Numeric(10, 0, asdecimal=False))
    sched_loadpriority = Column(Numeric(10, 0, asdecimal=False))
    sched_loadtype = Column(String(15))
    sched_substitutionallowed = Column(Numeric(10, 0, asdecimal=False))
    sched_globalsubstitution1 = Column(String(10))
    sched_globalsubstitution2 = Column(String(10))
    sched_globalsubstitution3 = Column(String(10))
    sched_usepreestablishedteams = Column(Numeric(10, 0, asdecimal=False))
    sched_closesectionaftermax = Column(Numeric(10, 0, asdecimal=False))
    sched_usesectiontypes = Column(Numeric(10, 0, asdecimal=False))
    sched_balancepriority = Column(String(10))
    sched_periodspercycle = Column(Numeric(10, 0, asdecimal=False))
    gradescaleid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    coursecatalogid = Column(Numeric(10, 0, asdecimal=False), index=True)
    sched_rank = Column(Numeric(10, 0, asdecimal=False))
    sched_demand = Column(Numeric(10, 0, asdecimal=False))
    sched_totalconflictstudents = Column(Numeric(10, 0, asdecimal=False))
    sched_totalconflictcourses = Column(Numeric(10, 0, asdecimal=False))
    sched_minroomcapacity = Column(Numeric(10, 0, asdecimal=False))
    sched_overlapallowed = Column(Numeric(10, 0, asdecimal=False))
    sched_lunchcourse = Column(Numeric(10, 0, asdecimal=False))
    sched_do_not_print = Column(Numeric(10, 0, asdecimal=False))
    schoolcrseinfo_guid = Column(String(32), index=True)
    sched_prepcode = Column(String(12))


class Schedulecourserelationship(Base):
    __tablename__ = 'schedulecourserelationships'
    __table_args__ = (
        Index('schedulecourserelationships_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    blockteacher = Column(Numeric(10, 0, asdecimal=False))
    course_number1 = Column(String(11))
    course_number2 = Column(String(11))
    relationshipcode = Column(String(15))
    relationshiptype = Column(String(15))
    buildid = Column(Numeric(10, 0, asdecimal=False))
    catalogid = Column(Numeric(10, 0, asdecimal=False))
    extradata = Column(String(80))
    blockmakedepsects = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))


class Scheduleday(Base):
    __tablename__ = 'scheduledays'
    __table_args__ = (
        Index('scheduledays_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    dayid = Column(Numeric(10, 0, asdecimal=False))
    abbr = Column(String(3))
    letter = Column(String(2))
    buildid = Column(Numeric(10, 0, asdecimal=False))


class Scheduledepartment(Base):
    __tablename__ = 'scheduledepartments'
    __table_args__ = (
        Index('scheduledepartments_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Schedulefacility(Base):
    __tablename__ = 'schedulefacilities'
    __table_args__ = (
        Index('schedulefacilities_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(20))
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Schedulehouse(Base):
    __tablename__ = 'schedulehouses'
    __table_args__ = (
        Index('schedulehouses_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Scheduleitem(Base):
    __tablename__ = 'scheduleitems'
    __table_args__ = (
        Index('scheduleitems_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    period = Column(String(20))
    starttime = Column(Numeric(10, 0, asdecimal=False))
    endtime = Column(Numeric(10, 0, asdecimal=False))
    minutes = Column(Numeric(10, 0, asdecimal=False))
    attendanceweight = Column(Float)
    scheduleid = Column(String(20), index=True)
    usefordailyattendance = Column(Numeric(10, 0, asdecimal=False))
    defaulttimein = Column(Numeric(10, 0, asdecimal=False))
    defaulttimeout = Column(Numeric(10, 0, asdecimal=False))
    membershipvalue = Column(Float)


class Scheduleloaddiagnostic(Base):
    __tablename__ = 'scheduleloaddiagnostics'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    ld_code = Column(String(25))
    ld_studentid = Column(Numeric(10, 0, asdecimal=False))
    ld_text = Column(Text)
    ld_value = Column(Numeric(10, 0, asdecimal=False))
    ld_buildid = Column(Numeric(10, 0, asdecimal=False))


class Scheduleloadtype(Base):
    __tablename__ = 'scheduleloadtypes'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Scheduleperiod(Base):
    __tablename__ = 'scheduleperiods'
    __table_args__ = (
        Index('scheduleperiods_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(15))
    scheduleid = Column(Numeric(10, 0, asdecimal=False))
    periodnumber = Column(Numeric(10, 0, asdecimal=False))
    periodid = Column(String(2))
    starttime1 = Column(String(7))
    endtime1 = Column(String(7))
    useforbuild = Column(Numeric(10, 0, asdecimal=False))
    schedulestudies = Column(Numeric(10, 0, asdecimal=False))
    useforlunches = Column(Numeric(10, 0, asdecimal=False))
    blockstart = Column(Numeric(10, 0, asdecimal=False))
    starttime2 = Column(String(5))
    endtime2 = Column(String(5))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    abbr = Column(String(3))
    sort = Column(Numeric(10, 0, asdecimal=False))
    coreperiod = Column(Numeric(10, 0, asdecimal=False))
    buildid = Column(Numeric(10, 0, asdecimal=False), index=True)


class Schedulequeue(Base):
    __tablename__ = 'schedulequeue'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)


class Schedulerequest(Base):
    __tablename__ = 'schedulerequests'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    coursenumber = Column(String(11), index=True)
    sectiontypecode = Column(String(2))
    globalalternatecourse = Column(Numeric(10, 0, asdecimal=False))
    alternatepriority = Column(Numeric(10, 0, asdecimal=False))
    alternategroupcode = Column(String(2))
    alternatecoursenumber1 = Column(String(10), index=True)
    alternatecoursenumber2 = Column(String(10), index=True)
    alternatecoursenumber3 = Column(String(10), index=True)
    noglobalsubstitutionallowed = Column(Numeric(10, 0, asdecimal=False))
    loadstatuscode = Column(String(4))
    studentsortfield = Column(String(12))
    studentyogsort = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    student_number = Column(Float)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    creationcode = Column(Numeric(10, 0, asdecimal=False), index=True)
    registreq_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    unused = Column(Numeric(10, 0, asdecimal=False))


class Scheduleroom(Base):
    __tablename__ = 'schedulerooms'
    __table_args__ = (
        Index('schedulerooms_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    roomnumber = Column(String(10), index=True)
    roomtype = Column(String(8))
    department = Column(String(12))
    building = Column(String(10))
    house = Column(String(10))
    scheduled = Column(Numeric(10, 0, asdecimal=False))
    useashomeroom = Column(Numeric(10, 0, asdecimal=False))
    free = Column(Numeric(10, 0, asdecimal=False))
    facilities = Column(String(50))
    maximum = Column(Numeric(10, 0, asdecimal=False))
    departmentuseonly = Column(Numeric(10, 0, asdecimal=False))
    facilityuseonly = Column(Numeric(10, 0, asdecimal=False))


class Scheduleroomtype(Base):
    __tablename__ = 'scheduleroomtypes'
    __table_args__ = (
        Index('scheduleroomtypes_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Schedulesectionmeeting(Base):
    __tablename__ = 'schedulesectionmeeting'
    __table_args__ = (
        Index('schedulesectionmeeting_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    buildid = Column(Numeric(10, 0, asdecimal=False), index=True)
    day = Column(String(2), index=True)
    period = Column(Numeric(10, 0, asdecimal=False), index=True)


class Schedulesection(Base):
    __tablename__ = 'schedulesections'
    __table_args__ = (
        Index('schedulesections_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    section_number = Column(Numeric(10, 0, asdecimal=False), index=True)
    course_number = Column(String(11), index=True)
    teacher = Column(Numeric(10, 0, asdecimal=False), index=True)
    termid = Column(Numeric(10, 0, asdecimal=False), index=True)
    period_obsolete = Column(String(7))
    no_of_students = Column(Numeric(10, 0, asdecimal=False))
    room = Column(String(10), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    maxenrollment = Column(Numeric(10, 0, asdecimal=False))
    blockperiods_obsolete = Column(String(20))
    dependent_secs = Column(Text)
    grade_level = Column(Numeric(10, 0, asdecimal=False))
    campusid = Column(Numeric(10, 0, asdecimal=False))
    expression = Column(String(80))
    gradescaleid = Column(Numeric(10, 0, asdecimal=False))
    wheretaught = Column(Numeric(10, 0, asdecimal=False))
    excludefromgpa = Column(Numeric(10, 0, asdecimal=False))
    noattendance = Column(Numeric(10, 0, asdecimal=False))
    buildid = Column(Numeric(10, 0, asdecimal=False), index=True)
    bitmap = Column(LargeBinary)
    lockedsection = Column(Numeric(10, 0, asdecimal=False))
    maxcut = Column(Numeric(10, 0, asdecimal=False))
    sectiontype = Column(String(2))
    team = Column(String(10))
    department = Column(String(12), index=True)
    credittype = Column(String(20), index=True)
    excludefromclassrank = Column(Numeric(10, 0, asdecimal=False))
    excludefromhonorroll = Column(Numeric(10, 0, asdecimal=False))
    building = Column(String(10))
    house = Column(String(10))
    comment_value = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    max_load_status = Column(String(24))


class Schedulesectiontype(Base):
    __tablename__ = 'schedulesectiontypes'
    __table_args__ = (
        Index('schedulesectiontypes_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    sectiontypecode = Column(String(2), index=True)
    courseteacher = Column(String(20))


class Scheduleteacherassignment(Base):
    __tablename__ = 'scheduleteacherassignments'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    buildid = Column(Numeric(10, 0, asdecimal=False), index=True)
    teacherkey = Column(Numeric(10, 0, asdecimal=False), index=True)
    priority = Column(Numeric(10, 0, asdecimal=False))
    coursenumber = Column(String(11), index=True)
    sectiontype = Column(String(2), index=True)
    scheduletermcode = Column(String(6))
    sectionsassigned = Column(Numeric(10, 0, asdecimal=False))
    requiredassignment = Column(Numeric(10, 0, asdecimal=False))
    catalogid = Column(Numeric(10, 0, asdecimal=False))


class Scheduleterm(Base):
    __tablename__ = 'scheduleterms'
    __table_args__ = (
        Index('scheduleterms_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(30), index=True)
    firstday = Column(DateTime, index=True)
    lastday = Column(DateTime)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    abbreviation = Column(String(6))
    noofdays = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearlycredithrs = Column(Float)
    termsinyear = Column(Numeric(10, 0, asdecimal=False))
    portion = Column(Numeric(10, 0, asdecimal=False))
    importmap = Column(String(20))
    autobuildbin = Column(Numeric(10, 0, asdecimal=False))
    isyearrec = Column(Numeric(10, 0, asdecimal=False))


class Schedulevalidation(Base):
    __tablename__ = 'schedulevalidation'
    __table_args__ = (
        Index('schedulevalidation_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    buildid = Column(Numeric(10, 0, asdecimal=False), index=True)
    logtext = Column(Text)
    exceptiontype = Column(String(10))


class Schedulevalidterm(Base):
    __tablename__ = 'schedulevalidterms'
    __table_args__ = (
        Index('schedulevalidterms_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    description = Column(String(30))
    schoolid = Column(Numeric(10, 0, asdecimal=False))


class Schemaupdatestatu(Base):
    __tablename__ = 'schemaupdatestatus'

    schemaupdatestatusid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    name = Column(String(100))
    status = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    daterun = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    isvisible = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    shortdescription = Column(String(100), nullable=False)
    longdescription = Column(String(4000))
    problemtext = Column(String(4000))
    remedytext = Column(String(4000))
    migratedcount = Column(Numeric(16, 0, asdecimal=False))
    unmigratedcount = Column(Numeric(16, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class SchoolCourse(Base):
    __tablename__ = 'school_course'
    __table_args__ = (
        Index('school_course_u2', 'id', 'dcid', unique=True),
        Index('school_course_uk', 'yearid', 'schoolid', 'courseid', unique=True)
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), unique=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    courseid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True)
    createdby = Column(String(40))
    createddt = Column(DateTime)
    modifiedby = Column(String(40))
    modifieddt = Column(DateTime)
    alt_course_number = Column(String(40))
    exclude_state_rpt_yn = Column(Numeric(10, 0, asdecimal=False))
    schoolcrseinfo_guid = Column(String(32), index=True)
    att_mode_code = Column(String(20), index=True)
    status = Column(Numeric(3, 0, asdecimal=False), nullable=False, index=True, server_default=text("0 "))


class SchoolCourseSchedParm(Base):
    __tablename__ = 'school_course_sched_parm'
    __table_args__ = (
        Index('school_course_sched_parm_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    school_course_id = Column(ForeignKey('school_course.id'), index=True)
    load_priority = Column(Numeric(10, 0, asdecimal=False))
    load_type = Column(String(15))
    use_section_types = Column(Numeric(10, 0, asdecimal=False))
    substitution_allowed = Column(Numeric(10, 0, asdecimal=False))
    global_substitution1 = Column(String(10), index=True)
    global_substitution2 = Column(String(10), index=True)
    global_substitution3 = Column(String(10), index=True)
    allow_std_rpt_same_term = Column(Numeric(10, 0, asdecimal=False))
    allow_std_rpt_diff_term = Column(Numeric(10, 0, asdecimal=False))
    use_team = Column(Numeric(10, 0, asdecimal=False))
    balance_priority = Column(String(10))
    lunch_course = Column(Numeric(10, 0, asdecimal=False))

    school_course = relationship('SchoolCourse')


t_schoolcourses = Table(
    'schoolcourses', metadata,
    Column('schooldcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('coursedcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('course_number', String(11)),
    Column('course_name', String(40)),
    Column('credit_hours', Float),
    Column('code', String(20)),
    Column('vocational', Numeric(10, 0, asdecimal=False)),
    Column('credittype', String(20)),
    Column('gradescaleid', Numeric(10, 0, asdecimal=False)),
    Column('excludefromgpa', Numeric(10, 0, asdecimal=False)),
    Column('excludefromclassrank', Numeric(10, 0, asdecimal=False)),
    Column('excludefromhonorroll', Numeric(10, 0, asdecimal=False)),
    Column('exclude_ada', Numeric(10, 0, asdecimal=False))
)


class Schoolfee(Base):
    __tablename__ = 'schoolfee'
    __table_args__ = (
        Index('schoolfee_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    course_number = Column(String(11), index=True)
    fee_type_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    fee_type_name = Column(String(79), index=True)
    fee_type_priority = Column(Numeric(10, 0, asdecimal=False))
    fee_type_description = Column(Text)
    fee_category_name = Column(String(21), index=True)
    fee_amount = Column(Float)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    departmentid = Column(Numeric(10, 0, asdecimal=False))
    date_value = Column(DateTime)
    pro_ratable = Column(Numeric(10, 0, asdecimal=False))
    school_fee_prorate_period = Column(String(11))
    custom = Column(Text)
    course_name = Column(String(79))
    creationdate = Column(DateTime)
    modificationdate = Column(DateTime)
    department_name = Column(String(79))
    description = Column(Text)
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Schoolmap(Base):
    __tablename__ = 'schoolmap'

    schoolmapid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    school_number = Column(ForeignKey('schools.school_number'), nullable=False, index=True)
    mimetype = Column(String(50))
    mapdata = Column(LargeBinary)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    school = relationship('School')


class School(Base):
    __tablename__ = 'schools'
    __table_args__ = (
        Index('schools_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(60), index=True)
    address = Column(Text)
    district_number = Column(Numeric(10, 0, asdecimal=False))
    school_number = Column(Numeric(10, 0, asdecimal=False), index=True)
    pscomm_path = Column(Text)
    low_grade = Column(Numeric(10, 0, asdecimal=False))
    high_grade = Column(Numeric(10, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    abbreviation = Column(String(20))
    schoolgroup = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    activecrslist = Column(Text)
    bulletinemail = Column(Text)
    sysemailfrom = Column(Text)
    hist_low_grade = Column(Numeric(10, 0, asdecimal=False))
    hist_high_grade = Column(Numeric(10, 0, asdecimal=False))
    tchrlogentrto = Column(Text)
    dfltnextschool = Column(Numeric(10, 0, asdecimal=False))
    portalid = Column(String(20))
    view_in_portal = Column(Numeric(10, 0, asdecimal=False))
    state_excludefromreporting = Column(Numeric(10, 0, asdecimal=False))
    alternate_school_number = Column(Numeric(10, 0, asdecimal=False))
    schooladdress = Column(String(79))
    schoolcity = Column(String(79))
    schoolstate = Column(String(79))
    schoolzip = Column(String(79))
    schoolphone = Column(String(31))
    schoolfax = Column(String(31))
    schoolcountry = Column(String(79))
    principal = Column(String(79))
    principalphone = Column(String(31))
    principalemail = Column(String(79))
    asstprincipalphone = Column(String(31))
    asstprincipalemail = Column(String(79))
    countyname = Column(String(79))
    countynbr = Column(String(79))
    asstprincipal = Column(String(79))
    schedulewhichschool = Column(String(10))
    fee_exemption_status = Column(Numeric(10, 0, asdecimal=False))
    schoolinfo_guid = Column(String(32), index=True)
    sif_stateprid = Column(String(32))
    issummerschool = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)


class CSchoolsRegistrar(School):
    __tablename__ = 'c_schools_registrar'

    schoolsdcid = Column(ForeignKey('schools.dcid'), primary_key=True)
    registrar_name = Column(String(37))
    registrar_notes = Column(String(500))
    registrar_phone = Column(String(17))
    registrar_email = Column(String(254))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SSchCrdcX(School):
    __tablename__ = 's_sch_crdc_x'

    schoolsdcid = Column(ForeignKey('schools.dcid'), primary_key=True)
    corppunishment_yn = Column(String(1))
    creditrecovery_yn = Column(String(1))
    dualenrollment_yn = Column(String(1))
    ftesecurity_yn = Column(String(1))
    justicefacilitydays = Column(Numeric(11, 0, asdecimal=False))
    justicefacilityhours = Column(Numeric(11, 0, asdecimal=False))
    justicefacilitytype = Column(String(16))
    prekgagenonidea3_yn = Column(String(1))
    prekgagenonidea4_yn = Column(String(1))
    prekgagenonidea5_yn = Column(String(1))
    primaryschoolrecord_tf = Column(Numeric(1, 0, asdecimal=False))
    sch_id = Column(String(15))
    ungradeddetail = Column(String(1))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    firearmuse_yn = Column(String(1))
    homicide_yn = Column(String(1))
    nonleafacility_yn = Column(String(1))


class SSchNceaX(School):
    __tablename__ = 's_sch_ncea_x'

    schoolsdcid = Column(ForeignKey('schools.dcid'), primary_key=True)
    boardcomcoun_tf = Column(Numeric(1, 0, asdecimal=False))
    erateapplied_tf = Column(Numeric(1, 0, asdecimal=False))
    eratereceived_tf = Column(Numeric(1, 0, asdecimal=False))
    excludefromncea_tf = Column(Numeric(1, 0, asdecimal=False))
    extdayprogram_tf = Column(Numeric(1, 0, asdecimal=False))
    internetaccess_tf = Column(Numeric(1, 0, asdecimal=False))
    location = Column(String(1))
    offersfednutrition_tf = Column(Numeric(1, 0, asdecimal=False))
    offerssubsidizedtrans_tf = Column(Numeric(1, 0, asdecimal=False))
    offerstitlei_tf = Column(Numeric(1, 0, asdecimal=False))
    pk12singleschool_tf = Column(Numeric(1, 0, asdecimal=False))
    schoolgender = Column(String(1))
    sponsorship = Column(String(1))
    waitlist_tf = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Schoolalertconfig(School):
    __tablename__ = 'schoolalertconfig'

    school_number = Column(ForeignKey('schools.school_number'), primary_key=True)
    enabled = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    mindaysstored = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    maxdaysstored = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    alertthreshold = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))


class Schoolscorefield(School):
    __tablename__ = 'schoolscorefields'

    schoolsdcid = Column(ForeignKey('schools.dcid'), primary_key=True)
    att_sec_email = Column(String(4000))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Schoolssuccessnetfield(School):
    __tablename__ = 'schoolssuccessnetfields'

    schoolsdcid = Column(ForeignKey('schools.dcid'), primary_key=True)
    ab_psn_schoolpid = Column(String(4000))
    ak_psn_schoolpid = Column(String(4000))
    al_psn_schoolpid = Column(String(4000))
    ar_psn_schoolpid = Column(String(4000))
    as_psn_schoolpid = Column(String(4000))
    az_psn_schoolpid = Column(String(4000))
    bc_psn_schoolpid = Column(String(4000))
    ca_psn_schoolpid = Column(String(4000))
    co_psn_schoolpid = Column(String(4000))
    ct_psn_schoolpid = Column(String(4000))
    dc_psn_schoolpid = Column(String(4000))
    de_psn_schoolpid = Column(String(4000))
    fl_psn_schoolpid = Column(String(4000))
    ga_psn_schoolpid = Column(String(4000))
    gu_psn_schoolpid = Column(String(4000))
    hi_psn_schoolpid = Column(String(4000))
    ia_psn_schoolpid = Column(String(4000))
    id_psn_schoolpid = Column(String(4000))
    il_psn_schoolpid = Column(String(4000))
    in_psn_schoolpid = Column(String(4000))
    ks_psn_schoolpid = Column(String(4000))
    ky_psn_schoolpid = Column(String(4000))
    la_psn_schoolpid = Column(String(4000))
    ma_psn_schoolpid = Column(String(4000))
    mb_psn_schoolpid = Column(String(4000))
    md_psn_schoolpid = Column(String(4000))
    me_psn_schoolpid = Column(String(4000))
    mi_psn_schoolpid = Column(String(4000))
    mn_psn_schoolpid = Column(String(4000))
    mo_psn_schoolpid = Column(String(4000))
    ms_psn_schoolpid = Column(String(4000))
    mt_psn_schoolpid = Column(String(4000))
    nb_psn_schoolpid = Column(String(4000))
    nc_psn_schoolpid = Column(String(4000))
    nd_psn_schoolpid = Column(String(4000))
    ne_psn_schoolpid = Column(String(4000))
    nh_psn_schoolpid = Column(String(4000))
    nj_psn_schoolpid = Column(String(4000))
    nl_psn_schoolpid = Column(String(4000))
    nm_psn_schoolpid = Column(String(4000))
    ns_psn_schoolpid = Column(String(4000))
    nt_psn_schoolpid = Column(String(4000))
    nu_psn_schoolpid = Column(String(4000))
    nv_psn_schoolpid = Column(String(4000))
    ny_psn_schoolpid = Column(String(4000))
    oh_psn_schoolpid = Column(String(4000))
    ok_psn_schoolpid = Column(String(4000))
    on_psn_schoolpid = Column(String(4000))
    or_psn_schoolpid = Column(String(4000))
    pa_psn_schoolpid = Column(String(4000))
    pe_psn_schoolpid = Column(String(4000))
    pr_psn_schoolpid = Column(String(4000))
    qc_psn_schoolpid = Column(String(4000))
    ri_psn_schoolpid = Column(String(4000))
    sc_psn_schoolpid = Column(String(4000))
    sd_psn_schoolpid = Column(String(4000))
    sk_psn_schoolpid = Column(String(4000))
    tn_psn_schoolpid = Column(String(4000))
    tx_psn_schoolpid = Column(String(4000))
    ut_psn_schoolpid = Column(String(4000))
    va_psn_schoolpid = Column(String(4000))
    vi_psn_schoolpid = Column(String(4000))
    vt_psn_schoolpid = Column(String(4000))
    wa_psn_schoolpid = Column(String(4000))
    wi_psn_schoolpid = Column(String(4000))
    wv_psn_schoolpid = Column(String(4000))
    wy_psn_schoolpid = Column(String(4000))
    yt_psn_schoolpid = Column(String(4000))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Schoolstaff(Base):
    __tablename__ = 'schoolstaff'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    users_dcid = Column(ForeignKey('users.dcid'), nullable=False, index=True)
    balance1 = Column(Float)
    balance2 = Column(Float)
    balance3 = Column(Float)
    balance4 = Column(Float)
    classpua = Column(Text)
    noofcurclasses = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    log = Column(Text)
    staffstatus = Column(Numeric(10, 0, asdecimal=False), index=True)
    status = Column(Numeric(10, 0, asdecimal=False), index=True)
    sched_gender = Column(String(2))
    sched_classroom = Column(String(10))
    sched_homeroom = Column(String(10))
    sched_department = Column(String(10))
    sched_maximumcourses = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumduty = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumfree = Column(Numeric(10, 0, asdecimal=False))
    sched_totalcourses = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumconsecutive = Column(Numeric(10, 0, asdecimal=False))
    sched_isteacherfree = Column(Numeric(10, 0, asdecimal=False))
    sched_housecode = Column(String(10))
    sched_buildingcode = Column(String(10))
    sched_activitystatuscode = Column(String(8))
    sched_primaryschoolcode = Column(String(10))
    sched_teachermoreoneschool = Column(Numeric(10, 0, asdecimal=False))
    sched_substitute = Column(Numeric(10, 0, asdecimal=False))
    sched_scheduled = Column(Numeric(10, 0, asdecimal=False))
    sched_usebuilding = Column(Numeric(10, 0, asdecimal=False))
    sched_usehouse = Column(Numeric(10, 0, asdecimal=False))
    sched_team = Column(String(12))
    sched_lunch = Column(Numeric(10, 0, asdecimal=False))
    sched_maxpers = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))
    sched_maxpreps = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))
    notes = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    psguid = Column(String(50), unique=True)

    user = relationship('User')


class SSsfNceaX(Schoolstaff):
    __tablename__ = 's_ssf_ncea_x'

    schoolstaffdcid = Column(ForeignKey('schoolstaff.dcid'), primary_key=True)
    excludefromncea_tf = Column(Numeric(1, 0, asdecimal=False))
    fte_code = Column(String(2))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SectionMeeting(Base):
    __tablename__ = 'section_meeting'
    __table_args__ = (
        Index('section_meeting_n7', 'schoolid', 'year_id', 'period_number', 'sectionid', 'cycle_day_letter'),
        Index('section_meeting_n8', 'sectionid', 'cycle_day_letter', 'schoolid', 'year_id', 'period_number'),
        Index('section_meeting_u2', 'id', 'dcid', unique=True)
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    year_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    period_number = Column(Numeric(10, 0, asdecimal=False), index=True)
    cycle_day_letter = Column(String(2), index=True)
    meeting = Column(String(7), index=True)
    psguid = Column(String(50), unique=True)


class Sectionattrib(Base):
    __tablename__ = 'sectionattrib'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    sectionsdcid = Column(ForeignKey('sections.dcid'), nullable=False, unique=True)
    isearnedvarcreditallowed = Column(Numeric(3, 0, asdecimal=False), server_default=text("0"))
    ispotentialvarcreditallowed = Column(Numeric(3, 0, asdecimal=False), server_default=text("0"))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    section = relationship('Section')


class Section(Base):
    __tablename__ = 'sections'
    __table_args__ = (
        Index('sections_u2', 'id', 'dcid', unique=True),
        Index('sections_n16', 'id', 'att_mode_code', 'course_number'),
        Index('sections_n17', 'teacher', 'course_number', 'att_mode_code')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    section_number = Column(String(10), index=True)
    course_number = Column(String(11), index=True)
    teacher = Column(Numeric(10, 0, asdecimal=False), index=True)
    termid = Column(Numeric(10, 0, asdecimal=False), index=True)
    period_obsolete = Column(String(7), index=True)
    no_of_students = Column(Numeric(10, 0, asdecimal=False))
    room = Column(String(10), index=True)
    fastperlist = Column(String(11), index=True)
    ccrnarray = Column(Text)
    attendance = Column(Text)
    lastattupdate = Column(DateTime, index=True)
    custom = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    noofterms = Column(Numeric(10, 0, asdecimal=False))
    trackteacheratt = Column(Numeric(10, 0, asdecimal=False))
    maxenrollment = Column(Numeric(10, 0, asdecimal=False))
    distuniqueid = Column(Numeric(10, 0, asdecimal=False))
    wheretaught = Column(Numeric(10, 0, asdecimal=False))
    pgflags = Column(Text)
    days_obsolete = Column(String(7))
    gradeprofile = Column(String(11))
    log = Column(Text)
    rostermodser = Column(Numeric(10, 0, asdecimal=False))
    teacherdescr = Column(Text)
    pgversion = Column(Numeric(10, 0, asdecimal=False))
    blockperiods_obsolete = Column(String(20))
    dependent_secs = Column(Text)
    grade_level = Column(Numeric(10, 0, asdecimal=False))
    campusid = Column(Numeric(10, 0, asdecimal=False))
    exclude_ada = Column(Numeric(10, 0, asdecimal=False))
    expression = Column(String(80))
    gradescaleid = Column(Numeric(10, 0, asdecimal=False))
    excludefromgpa = Column(Numeric(10, 0, asdecimal=False))
    buildid = Column(Numeric(10, 0, asdecimal=False))
    bitmap = Column(LargeBinary)
    schedulesectionid = Column(Numeric(10, 0, asdecimal=False))
    wheretaughtdistrict = Column(Numeric(10, 0, asdecimal=False))
    excludefromclassrank = Column(Numeric(10, 0, asdecimal=False))
    excludefromhonorroll = Column(Numeric(10, 0, asdecimal=False))
    parent_section_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    original_expression = Column(String(80))
    comment_value = Column(Text)
    attendance_type_code = Column(Numeric(10, 0, asdecimal=False), index=True)
    section_type = Column(String(2))
    team = Column(String(10))
    house = Column(String(10))
    maxcut = Column(Numeric(10, 0, asdecimal=False))
    exclude_state_rpt_yn = Column(Numeric(10, 0, asdecimal=False))
    instruction_lang = Column(String(40))
    sectioninfo_guid = Column(String(32), index=True)
    att_mode_code = Column(String(20), index=True)
    sortorder = Column(Numeric(10, 0, asdecimal=False), index=True)
    programid = Column(Numeric(10, 0, asdecimal=False), index=True)
    excludefromstoredgrades = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))
    max_load_status = Column(String(24))
    psguid = Column(String(50), unique=True)
    gradebooktype = Column(Numeric(10, 0, asdecimal=False))


class SSecCrdcX(Section):
    __tablename__ = 's_sec_crdc_x'

    sectionsdcid = Column(ForeignKey('sections.dcid'), primary_key=True)
    blockscheduledclass_tf = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    creditrecovery_yn = Column(String(1))
    distancelearning_yn = Column(String(1))
    dualenrollment_yn = Column(String(1))


class Sectionscore(Base):
    __tablename__ = 'sectionscores'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    assignment = Column(LargeBinary)
    percent = Column(LargeBinary)
    score = Column(LargeBinary)
    grade = Column(LargeBinary)
    comment_value = Column(LargeBinary)
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    exempt = Column(Text)


class Sectionscoresassignment(Base):
    __tablename__ = 'sectionscoresassignments'
    __table_args__ = (
        Index('sectionscoresassignments_u2', 'fdcid', 'assignment', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    fdcid = Column(Numeric(10, 0, asdecimal=False))
    assignment = Column(Numeric(10, 0, asdecimal=False), index=True)
    percent = Column(String(31))
    score = Column(String(31))
    grade = Column(String(31))
    comment_value = Column(Text)
    exempt = Column(String(2))


class Sectionscoresid(Base):
    __tablename__ = 'sectionscoresid'
    __table_args__ = (
        Index('sectionscoresid_u2', 'studentid', 'sectionid', 'dcid', unique=True),
        Index('sectionscoresididx5', 'sectionid', 'studentid')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))


class Sectionteacher(Base):
    __tablename__ = 'sectionteacher'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    teacherid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    sectionid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    roleid = Column(ForeignKey('roledef.id'), nullable=False, index=True)
    start_date = Column(DateTime, nullable=False, index=True)
    end_date = Column(DateTime, nullable=False, index=True)
    allocation = Column(Numeric(10, 2), nullable=False)
    priorityorder = Column(Numeric(10, 0, asdecimal=False))
    notes = Column(Text)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("sysdate"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("sysdate"))

    roledef = relationship('Roledef')


class Sectprogsetting(Base):
    __tablename__ = 'sectprogsettings'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    sections_dcid = Column(ForeignKey('sections.dcid'), nullable=False, index=True)
    program_gendcid = Column(ForeignKey('gen.dcid'), nullable=False, index=True)
    operation = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gen = relationship('Gen')
    section = relationship('Section')


class Selection(Base):
    __tablename__ = 'selections'
    __table_args__ = (
        Index('selections_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    tableid = Column(Numeric(10, 0, asdecimal=False), index=True)
    userid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(80))
    blobids = Column(LargeBinary)
    nofrecs = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)


t_sepc_3265_dcidlist = Table(
    'sepc_3265_dcidlist', metadata,
    Column('fieldtable_log_id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('dcid', Numeric(10, 0, asdecimal=False))
)


t_sepc_3265_fieldtable_log = Table(
    'sepc_3265_fieldtable_log', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('fieldstableid', Numeric(10, 0, asdecimal=False)),
    Column('fieldstablefieldno', Numeric(10, 0, asdecimal=False)),
    Column('dupe_dcid', Numeric(10, 0, asdecimal=False)),
    Column('dupe_fileno', Numeric(10, 0, asdecimal=False)),
    Column('dupe_name', String(50)),
    Column('orig_dcid', Numeric(10, 0, asdecimal=False)),
    Column('orig_fileno', Numeric(10, 0, asdecimal=False)),
    Column('orig_name', String(50)),
    Column('extensionname', String(256)),
    Column('extendedtable', String(32)),
    Column('extendedcolumn', String(32)),
    Column('extendedfieldcount', Numeric(10, 0, asdecimal=False)),
    Column('created', DateTime),
    Column('notes', String(4000)),
    Column('shouldfix', Numeric(1, 0, asdecimal=False))
)


class Seqno(Base):
    __tablename__ = 'seqno'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    seqnoname = Column(String(40), index=True)
    seqnoid = Column(Numeric(10, 0, asdecimal=False))


class ServerConfig(Base):
    __tablename__ = 'server_config'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    server_instanceid = Column(Numeric(10, 0, asdecimal=False), index=True)
    config_groupid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(80))
    config_value = Column(String(4000))
    created_by = Column(String(40))
    created_ts = Column(Numeric(10, 0, asdecimal=False))
    modified_by = Column(String(40))
    modified_ts = Column(Numeric(10, 0, asdecimal=False))


class ServerInstance(Base):
    __tablename__ = 'server_instance'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    host_ip = Column(String(40))
    host_name = Column(String(80))
    description = Column(Text)
    user_supplied_name = Column(String(80))
    server_state = Column(String(20))
    server_state_ts = Column(Numeric(10, 0, asdecimal=False))
    version_number = Column(String(40))


class ServerInstanceSingleton(Base):
    __tablename__ = 'server_instance_singleton'

    process_name = Column(String(100), primary_key=True)
    server_instance_dcid = Column(ForeignKey('server_instance.dcid'), nullable=False, index=True)
    last_activity = Column(DateTime)

    server_instance = relationship('ServerInstance')


class SifMessage(Base):
    __tablename__ = 'sif_message'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    server_instanceid = Column(Numeric(10, 0, asdecimal=False), index=True)
    agent_ident = Column(Numeric(10, 0, asdecimal=False), index=True)
    queue_ident = Column(Numeric(10, 0, asdecimal=False), index=True)
    msg_guid = Column(String(32))
    msg_content = Column(Text)
    msg_type = Column(String(40))
    created_ts = Column(Numeric(10, 0, asdecimal=False))


class Sifenrollment(Base):
    __tablename__ = 'sifenrollment'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    schoolnum = Column(String(50), index=True)
    sifsourceid = Column(String(50))
    grade = Column(String(10))
    refid = Column(String(32), unique=True)
    studentrefid = Column(String(32), index=True)
    schoolrefid = Column(String(32))
    entercode = Column(String(5))
    exitcode = Column(String(5))
    effdate = Column(String(8))
    membershiptype = Column(String(1))
    sifdata = Column(String(1024))


class Sifeventsqueue(Base):
    __tablename__ = 'sifeventsqueue'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    refid = Column(String(32))
    objtype = Column(Numeric(scale=0, asdecimal=False))
    eventtime = Column(DateTime)
    eventtimezone = Column(String(9))
    eventaction = Column(Numeric(scale=0, asdecimal=False))
    eventdata = Column(Text)
    sifzoneid = Column(String(50))
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    source = Column(Numeric(scale=0, asdecimal=False))
    schoolnum = Column(String(50))
    ready = Column(Numeric(scale=0, asdecimal=False))


class Siffutureeventsqueue(Base):
    __tablename__ = 'siffutureeventsqueue'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    refid = Column(String(32))
    objtype = Column(Numeric(scale=0, asdecimal=False))
    eventtime = Column(DateTime)
    eventtimezone = Column(String(9))
    eventaction = Column(Numeric(scale=0, asdecimal=False))
    eventdata = Column(Text)
    effectivedate = Column(DateTime)
    sifzoneid = Column(String(50))
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    source = Column(Numeric(scale=0, asdecimal=False))
    schoolnum = Column(String(50))
    ready = Column(Numeric(scale=0, asdecimal=False))


class Sifobjectstate(Base):
    __tablename__ = 'sifobjectstate'

    refid = Column(String(32), primary_key=True, nullable=False)
    sifzoneid = Column(String(50), primary_key=True, nullable=False)
    eventdata = Column(Text)


t_sifproperties = Table(
    'sifproperties', metadata,
    Column('propkey', String(50), unique=True),
    Column('propvalue', String(255))
)


class Sifrefid(Base):
    __tablename__ = 'sifrefids'
    __table_args__ = (
        Index('sifrefids_u2', 'objtype', 'primarykey', 'secondarykey', 'schoolnum', unique=True),
    )

    refid = Column(String(32), primary_key=True)
    objtype = Column(Numeric(scale=0, asdecimal=False))
    primarykey = Column(String(50))
    secondarykey = Column(String(50))
    schoolnum = Column(String(50))


class Sifroom(Base):
    __tablename__ = 'sifrooms'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    refid = Column(String(32), index=True)
    schoolnum = Column(String(50))
    roomname = Column(String(50))
    roomnum = Column(String(50))
    teacherrefid = Column(String(32))


class Sifschool(Base):
    __tablename__ = 'sifschools'

    sifzoneid = Column(String(50))
    schoolnum = Column(String(50))
    refid = Column(String(32), primary_key=True)
    name = Column(String(50))
    sisnum = Column(String(50))


class Sifstaffassignment(Base):
    __tablename__ = 'sifstaffassignment'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    schoolnum = Column(String(50), index=True)
    sifsourceid = Column(String(50))
    refid = Column(String(32), index=True)
    staffrefid = Column(String(32), index=True)
    schoolrefid = Column(String(32))


class Spenrollment(Base):
    __tablename__ = 'spenrollments'
    __table_args__ = (
        Index('spenrollments_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    programid = Column(Numeric(10, 0, asdecimal=False), index=True)
    enter_date = Column(DateTime)
    exit_date = Column(DateTime)
    code1 = Column(String(15))
    code2 = Column(String(15))
    exitcode = Column(String(15))
    sp_comment = Column(Text)
    custom = Column(Text)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    gradelevel = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    psguid = Column(String(50), unique=True)


t_srp_letter_grade_percentage = Table(
    'srp_letter_grade_percentage', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('gradescaleid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('gradelabel', String(30), nullable=False),
    Column('highvalue', Numeric(asdecimal=False)),
    Column('cutoffpercent', Numeric(18, 6)),
    Column('description', String(4000))
)


t_srp_psm_gradescale_and_default = Table(
    'srp_psm_gradescale_and_default', metadata,
    Column('id', Numeric(asdecimal=False)),
    Column('name', String(50))
)


class Standard(Base):
    __tablename__ = 'standard'
    __table_args__ = (
        Index('standard_u2', 'longitudinalid', 'yearid', unique=True),
        Index('standard_u3', 'yearid', 'identifier', unique=True)
    )

    standardid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    parentstandardid = Column(ForeignKey('standard.standardid'), index=True)
    longitudinalid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    name = Column(String(400), nullable=False)
    description = Column(String(4000))
    identifier = Column(String(20), nullable=False, index=True)
    subjectarea = Column(String(40))
    conversionscale = Column(Numeric(10, 0, asdecimal=False))
    gradescaleitemdcid = Column(ForeignKey('gradescaleitem.dcid'), nullable=False, index=True)
    isassignmentallowed = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    isactive = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1        "))
    deactivatedate = Column(DateTime)
    displayposition = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    iscommentincluded = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    maxcommentlength = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("4000     "))
    isexcludedfromreports = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0        "))
    importbatchtracking = Column(String(30))
    psguid = Column(String(50))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    transientcourselist = Column(Text)
    externalid = Column(String(50))

    gradescaleitem = relationship('Gradescaleitem')
    parent = relationship('Standard', remote_side=[standardid])


class Standardcourseassoc(Base):
    __tablename__ = 'standardcourseassoc'
    __table_args__ = (
        Index('standardcourseassoc_u2', 'standardid', 'coursesdcid', unique=True),
    )

    standardcourseassocid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    coursesdcid = Column(ForeignKey('courses.dcid'), nullable=False, index=True)
    standardid = Column(ForeignKey('standard.standardid'), nullable=False, index=True)
    isprimary = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    isactive = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    weight = Column(Numeric(10, 4), server_default=text("NULL        "))
    iscalcbylowerstandard = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    course = relationship('Course')
    standard = relationship('Standard')


class Standardcourselowerweight(Base):
    __tablename__ = 'standardcourselowerweight'

    standardcourselowerweightid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    standardcourseassocid = Column(ForeignKey('standardcourseassoc.standardcourseassocid'), nullable=False, index=True)
    standardid = Column(ForeignKey('standard.standardid'), nullable=False, index=True)
    reportingtermstorecode = Column(String(8))
    weight = Column(Numeric(10, 4), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    standardcourseassoc = relationship('Standardcourseassoc')
    standard = relationship('Standard')


class Standardgraderollup(Base):
    __tablename__ = 'standardgraderollup'
    __table_args__ = (
        Index('standardgraderollup_n4', 'standardid', 'studentsdcid', 'yearid', 'storecode'),
        Index('standardgraderollup_u4', 'standardid', 'studentsdcid', 'yearid', unique=True)
    )

    standardgraderollupid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    standardid = Column(ForeignKey('standard.standardid'), nullable=False, index=True)
    storecode = Column(String(10), nullable=False)
    schoolsdcid = Column(ForeignKey('schools.dcid'), index=True)
    schoolname = Column(String(60))
    standardname = Column(String(400))
    isenrolled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    isadminmodified = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    islocked = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    ismigrated = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    lastupdated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    numscores = Column(Numeric(10, 0, asdecimal=False))
    standardaveragepercent = Column(Float)
    standardaveragegrade = Column(String(50))
    standardhighpercent = Column(Float)
    standardhighgrade = Column(String(40))
    gradelevel = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    school = relationship('School')
    standard = relationship('Standard')
    student = relationship('Student')


class Standardgraderollupcomment(Base):
    __tablename__ = 'standardgraderollupcomment'
    __table_args__ = (
        Index('standardgraderollupcomment_n3', 'yearid', 'studentsdcid', 'gradelevel'),
    )

    standardgraderollupcommentid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    standardgraderollupid = Column(ForeignKey('standardgraderollup.standardgraderollupid'), nullable=False, unique=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    gradelevel = Column(Numeric(10, 0, asdecimal=False))
    commentvalue = Column(Text)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    standardgraderollup = relationship('Standardgraderollup')
    student = relationship('Student')


class Standardgradesection(Base):
    __tablename__ = 'standardgradesection'
    __table_args__ = (
        Index('standardgradesection_n5', 'standardid', 'studentsdcid', 'yearid'),
        Index('standardgradesection_u5', 'sectionsdcid', 'studentsdcid', 'standardid', 'yearid', unique=True)
    )

    standardgradesectionid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    standardid = Column(ForeignKey('standard.standardid'), nullable=False, index=True)
    storecode = Column(String(10), nullable=False)
    sectionsdcid = Column(ForeignKey('sections.dcid'), index=True)
    schoolsdcid = Column(ForeignKey('schools.dcid'), index=True)
    schoolname = Column(String(60))
    coursename = Column(String(40))
    standardname = Column(String(400))
    gradelevel = Column(Numeric(10, 0, asdecimal=False))
    lastupdated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    isenrolled = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    isadminmodified = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    islocked = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    ismigrated = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    isreportsrollupexcluded = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    standardpercent = Column(Float)
    standardgrade = Column(String(50))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    ismanuallyoverridden = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    calculatedgrade = Column(String(50))
    isincomplete = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    isexempt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    calculatedmean = Column(String(50))
    calculatedmode = Column(String(50))
    calculatedmedian = Column(String(50))
    calculatedweightedmean = Column(String(50))
    calculatedhighest = Column(String(50))
    calculatedmostrecentscores = Column(String(50))
    calculatedpower = Column(String(50))
    calculatedhighestmostrecent = Column(String(50))

    school = relationship('School')
    section = relationship('Section')
    standard = relationship('Standard')
    student = relationship('Student')


class Standardgradesectioncomment(Base):
    __tablename__ = 'standardgradesectioncomment'

    standardgradesectioncommentid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    standardgradesectionid = Column(ForeignKey('standardgradesection.standardgradesectionid'), nullable=False, unique=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    gradelevel = Column(Numeric(10, 0, asdecimal=False))
    commentvalue = Column(String(4000))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    standardgradesection = relationship('Standardgradesection')
    student = relationship('Student')


t_standardgradesectiontransient = Table(
    'standardgradesectiontransient', metadata,
    Column('sgsstandardgradesectionid', Numeric(16, 0, asdecimal=False)),
    Column('coursenumber', String(11)),
    Column('standardid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('standardidentifier', String(20), nullable=False),
    Column('standarddescription', String(4000)),
    Column('subjectarea', String(40)),
    Column('isexcludedfromreports', Numeric(1, 0, asdecimal=False), nullable=False),
    Column('sectionnumber', String(10)),
    Column('sectionexpression', String(80)),
    Column('sgsgradelevel', Numeric(10, 0, asdecimal=False)),
    Column('sgsyearid', Numeric(10, 0, asdecimal=False)),
    Column('sgsstorecode', String(10)),
    Column('sgsstandardgrade', String(50)),
    Column('sgsstandardpercent', Float),
    Column('sgsstudentsdcid', Numeric(10, 0, asdecimal=False)),
    Column('sgsschoolsdcid', Numeric(10, 0, asdecimal=False)),
    Column('sgsccommentvalue', String(4000)),
    Column('sgsisreportsrollupexcluded', Numeric(1, 0, asdecimal=False)),
    Column('trmabbreviation', String(6)),
    Column('lastfirst', String(40)),
    Column('coursename', String(40)),
    Column('standardname', String(400)),
    Column('schoolname', String(60))
)


t_standardorderandlevel = Table(
    'standardorderandlevel', metadata,
    Column('standardid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('standardorder', Numeric(asdecimal=False)),
    Column('standardlevel', Numeric(asdecimal=False)),
    Column('name', String(400), nullable=False)
)


class Standardretakescore(Base):
    __tablename__ = 'standardretakescore'

    standardretakescoreid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    parentscoreretakeid = Column(ForeignKey('standardretakescore.standardretakescoreid'), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    standardscoreid = Column(ForeignKey('standardscore.standardscoreid'), nullable=False, index=True)
    assignmentstandardassocid = Column(ForeignKey('assignmentstandardassoc.assignmentstandardassocid'), nullable=False, index=True)
    assignmentretakescoreid = Column(ForeignKey('assignmentretakescore.assignmentretakescoreid'), index=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    islate = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0     "))
    iscollected = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0     "))
    isexempt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0     "))
    ismissing = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0     "))
    isabsent = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0     "))
    isincomplete = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0     "))
    actualscoreentered = Column(String(30), nullable=False)
    actualscorekind = Column(String(30))
    actualscoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    displayposition = Column(Numeric(6, 0, asdecimal=False))
    scorepercent = Column(Numeric(18, 6))
    scorepoints = Column(Numeric(18, 6))
    scorelettergrade = Column(String(30))
    scorenumericgrade = Column(Numeric(18, 6))
    scoreentrydate = Column(DateTime, nullable=False, server_default=text("SYSDATE   "))
    scoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    altnumericgrade = Column(Numeric(18, 6))
    altalphagrade = Column(String(30))
    altscoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    gradescaleitem = relationship('Gradescaleitem', primaryjoin='Standardretakescore.actualscoregradescaledcid == Gradescaleitem.dcid')
    gradescaleitem1 = relationship('Gradescaleitem', primaryjoin='Standardretakescore.altscoregradescaledcid == Gradescaleitem.dcid')
    assignmentretakescore = relationship('Assignmentretakescore', primaryjoin='Standardretakescore.assignmentretakescoreid == Assignmentretakescore.assignmentretakescoreid')
    assignmentstandardassoc = relationship('Assignmentstandardassoc')
    parent = relationship('Standardretakescore', remote_side=[standardretakescoreid])
    gradescaleitem2 = relationship('Gradescaleitem', primaryjoin='Standardretakescore.scoregradescaledcid == Gradescaleitem.dcid')
    standardscore = relationship('Standardscore')
    student = relationship('Student')


t_standards = Table(
    'standards', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False)),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('name', String(400)),
    Column('description', String(4000)),
    Column('levelvalue', Numeric(asdecimal=False)),
    Column('listparent', String(20)),
    Column('identifier', String(20)),
    Column('sortorder', Numeric(10, 0, asdecimal=False)),
    Column('courses', Text),
    Column('subjectarea', String(40)),
    Column('conversionscale', Numeric(10, 0, asdecimal=False)),
    Column('allowassignments', Numeric(1, 0, asdecimal=False)),
    Column('includecomment', Numeric(10, 0, asdecimal=False)),
    Column('maxcommentlength', Numeric(10, 0, asdecimal=False)),
    Column('psguid', String(50))
)


class StandardsMigrationBackup(Base):
    __tablename__ = 'standards_migration_backup'
    __table_args__ = (
        Index('standards_u2_bk', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(80))
    description = Column(Text)
    levelvalue = Column(Numeric(10, 0, asdecimal=False))
    alignmentidentifier = Column(String(20))
    identifier = Column(String(20), index=True)
    calculationparent = Column(String(20))
    type = Column(Numeric(10, 0, asdecimal=False), index=True)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    listparent = Column(String(20), index=True)
    courses = Column(Text)
    subjectarea = Column(String(40))
    conversionscale = Column(Numeric(10, 0, asdecimal=False))
    allowassignments = Column(Numeric(10, 0, asdecimal=False))
    includecomment = Column(Numeric(10, 0, asdecimal=False))
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    maxcommentlength = Column(Numeric(10, 0, asdecimal=False), nullable=False, server_default=text("4000 "))
    psguid = Column(String(50), unique=True)
    ismigrated = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    migrationfailurereason = Column(String(200))
    originalidentifier = Column(String(20))


class Standardscore(Base):
    __tablename__ = 'standardscore'
    __table_args__ = (
        Index('standardscore_u4', 'assignmentsectionid', 'assignmentstandardassocid', 'studentsdcid', 'yearid', unique=True),
    )

    standardscoreid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    assignmentsectionid = Column(ForeignKey('assignmentsection.assignmentsectionid'), nullable=False, index=True)
    assignmentstandardassocid = Column(ForeignKey('assignmentstandardassoc.assignmentstandardassocid'), nullable=False, index=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    islate = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0   "))
    iscollected = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0   "))
    isexempt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0   "))
    ismissing = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0   "))
    isabsent = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0   "))
    isincomplete = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0   "))
    actualscoreentered = Column(String(30))
    actualscorekind = Column(String(30))
    actualscoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    scorepercent = Column(Numeric(18, 6))
    scorepoints = Column(Numeric(18, 6))
    scorelettergrade = Column(String(30))
    scorenumericgrade = Column(Numeric(18, 6))
    scoreentrydate = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    scoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    altnumericgrade = Column(Numeric(18, 6))
    altalphagrade = Column(String(30))
    altscoregradescaledcid = Column(ForeignKey('gradescaleitem.dcid'), index=True)
    hasretake = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL    "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    gradescaleitem = relationship('Gradescaleitem', primaryjoin='Standardscore.actualscoregradescaledcid == Gradescaleitem.dcid')
    gradescaleitem1 = relationship('Gradescaleitem', primaryjoin='Standardscore.altscoregradescaledcid == Gradescaleitem.dcid')
    assignmentsection = relationship('Assignmentsection')
    assignmentstandardassoc = relationship('Assignmentstandardassoc')
    gradescaleitem2 = relationship('Gradescaleitem', primaryjoin='Standardscore.scoregradescaledcid == Gradescaleitem.dcid')
    student = relationship('Student')


class Standardscurrent(Base):
    __tablename__ = 'standardscurrent'
    __table_args__ = (
        Index('standardscurrent_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    standardsid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    numscores = Column(Numeric(10, 0, asdecimal=False))
    averagescore = Column(Float)
    highscore = Column(Float)
    unused1 = Column(String(50))
    unused2 = Column(Text)


t_standardsgrades = Table(
    'standardsgrades', metadata,
    Column('dcid', Numeric(16, 0, asdecimal=False)),
    Column('id', Numeric(16, 0, asdecimal=False)),
    Column('standardsid', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('schoolname', String(60)),
    Column('storecode', String(10)),
    Column('datestored', DateTime),
    Column('numscores', Numeric(asdecimal=False)),
    Column('averagescore', Float),
    Column('transaveragescore', String(50)),
    Column('highscore', Float),
    Column('transhighscore', String(50)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('comment_value', Text)
)


class StandardsgradesBackup(Base):
    __tablename__ = 'standardsgrades_backup'
    __table_args__ = (
        Index('standardsgrades_u2_bk', 'id', 'dcid', unique=True),
        Index('standardsgrades_u3_bk', 'studentid', 'standardsid', 'yearid', 'storecode', unique=True),
        Index('standardsgrades_n5_bk', 'storecode', 'grade_level')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    standardsid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolname = Column(String(31))
    storecode = Column(String(10))
    datestored = Column(DateTime)
    numscores = Column(Numeric(10, 0, asdecimal=False))
    averagescore = Column(Float)
    transaveragescore = Column(String(50))
    highscore = Column(Float)
    transhighscore = Column(String(40))
    comment_value = Column(Text)
    log = Column(Text)
    grade_level = Column(Numeric(10, 0, asdecimal=False))
    ismigrated = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    migrationfailurereason = Column(String(200))


class Stateeventqueue(Base):
    __tablename__ = 'stateeventqueue'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    eventtype = Column(Numeric(10, 0, asdecimal=False), index=True)
    eventdate = Column(DateTime, index=True)
    eventtime = Column(Numeric(10, 0, asdecimal=False))
    action = Column(String(20), index=True)
    status = Column(Numeric(10, 0, asdecimal=False), index=True)
    eventdata = Column(Text)
    errortext = Column(Text)
    extract_layoutrecordid = Column(String(79))
    origeventdate = Column(DateTime, index=True)


class StateextractCodeconversion(Base):
    __tablename__ = 'stateextract_codeconversion'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    extract_layoutname_id = Column(String(79))
    dataelement_name = Column(String(79))
    powerschool_code = Column(String(9))
    stateapproved_code = Column(String(9))


class StateextractLayoutelement(Base):
    __tablename__ = 'stateextract_layoutelements'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    extract_layoutrecordid = Column(String(9), index=True)
    powerschool_fullfieldname = Column(String(79), index=True)
    dataelement_name = Column(String(79))
    dataelement_positionnumber = Column(Numeric(10, 0, asdecimal=False))
    dataelement_fixedlength_length = Column(Numeric(10, 0, asdecimal=False))
    dataelement_fixedlength_format = Column(String(9))
    dataelement_valueconvertflag = Column(Numeric(10, 0, asdecimal=False))
    dataelement_valuecalculateflag = Column(Numeric(10, 0, asdecimal=False))
    dataelement_valuelogictestflag = Column(Numeric(10, 0, asdecimal=False))
    dataelement_trackeventflag = Column(Numeric(10, 0, asdecimal=False))
    unused = Column(Numeric(10, 0, asdecimal=False))


class StateextractLayout(Base):
    __tablename__ = 'stateextract_layouts'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    internal_id = Column(Numeric(10, 0, asdecimal=False))
    extract_layoutname = Column(String(79), index=True)
    extract_layoutrecordid = Column(String(9), index=True)
    extract_layoutversion = Column(String(9))
    powerschool_mastertablename = Column(String(79))


class State(Base):
    __tablename__ = 'states'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    country = Column(String(10), nullable=False)
    state = Column(String(10), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Statesupportdatum(Base):
    __tablename__ = 'statesupportdata'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    type = Column(Numeric(10, 0, asdecimal=False))
    data = Column(LargeBinary)
    modificationdate = Column(DateTime)
    modificationtime = Column(Numeric(10, 0, asdecimal=False))
    unused1 = Column(Numeric(10, 0, asdecimal=False))


class Statetransactionqueue(Base):
    __tablename__ = 'statetransactionqueue'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    transactionid = Column(String(30), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    transactiontype = Column(Numeric(10, 0, asdecimal=False))
    operation = Column(String(8))
    transactiondata = Column(LargeBinary)
    status = Column(Numeric(10, 0, asdecimal=False), index=True)
    modificationdate = Column(DateTime)
    modificationtime = Column(Numeric(10, 0, asdecimal=False))
    submissiondate = Column(DateTime)
    responsedate = Column(DateTime)
    responsetime = Column(Numeric(10, 0, asdecimal=False))
    responsecode = Column(String(20))
    responsetext = Column(Text)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    filename = Column(String(79))


class Stat(Base):
    __tablename__ = 'stats'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    date_value = Column(DateTime, index=True)
    unused = Column(Numeric(10, 0, asdecimal=False))
    hitstoday = Column(Numeric(10, 0, asdecimal=False))
    adminhits = Column(Numeric(10, 0, asdecimal=False))
    guardianhits = Column(Numeric(10, 0, asdecimal=False))
    otherhits = Column(Numeric(10, 0, asdecimal=False))
    enrollment = Column(Numeric(10, 0, asdecimal=False))
    unused6 = Column(Numeric(10, 0, asdecimal=False))
    unused7 = Column(Numeric(10, 0, asdecimal=False))
    unused8 = Column(Numeric(10, 0, asdecimal=False))
    unused9 = Column(Numeric(10, 0, asdecimal=False))
    unused10 = Column(Numeric(10, 0, asdecimal=False))
    unused12 = Column(Numeric(10, 0, asdecimal=False))
    unused14 = Column(Numeric(10, 0, asdecimal=False))
    unused15 = Column(Numeric(10, 0, asdecimal=False))
    unused16 = Column(Numeric(10, 0, asdecimal=False))


class Storedgrade(Base):
    __tablename__ = 'storedgrades'
    __table_args__ = (
        Index('storedgrades_u2', 'studentid', 'termid', 'dcid', unique=True),
        Index('storedgrades_n3', 'studentid', 'course_number', 'storecode', 'termid')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    termid = Column(Numeric(10, 0, asdecimal=False), index=True)
    storecode = Column(String(10))
    datestored = Column(DateTime)
    grade = Column(String(7))
    percent = Column(Float)
    absences = Column(Float)
    tardies = Column(Float)
    behavior = Column(String(7))
    potentialcrhrs = Column(Float)
    earnedcrhrs = Column(Float)
    comment_value = Column(Text)
    course_name = Column(String(40))
    course_number = Column(String(11))
    credit_type = Column(String(20))
    grade_level = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    log = Column(Text)
    course_equiv = Column(String(11))
    schoolname = Column(String(60))
    gradescale_name = Column(String(50))
    teacher_name = Column(String(40))
    excludefromgpa = Column(Numeric(10, 0, asdecimal=False))
    gpa_points = Column(Float)
    gpa_addedvalue = Column(Float)
    gpa_custom2 = Column(Float)
    excludefromclassrank = Column(Numeric(10, 0, asdecimal=False))
    excludefromhonorroll = Column(Numeric(10, 0, asdecimal=False))
    gpa_custom1 = Column(String(79))
    custom = Column(Text)
    ab_course_cmp_fun_flg = Column(String(2))
    ab_course_cmp_ext_crd = Column(String(2))
    ab_course_cmp_fun_sch = Column(String(3))
    ab_course_cmp_met_cd = Column(String(4))
    ab_course_eva_pro_cd = Column(String(2))
    ab_course_cmp_sta_cd = Column(String(3))
    ab_pri_del_met_cd = Column(String(3))
    ab_lng_cd = Column(String(2))
    ab_dipl_exam_mark = Column(String(3))
    ab_final_mark = Column(String(3))
    isearnedcrhrsfromgb = Column(Numeric(10, 0, asdecimal=False))
    ispotentialcrhrsfromgb = Column(Numeric(10, 0, asdecimal=False))
    termbinsname = Column(String(8))
    psguid = Column(String(50), unique=True)
    replaced_grade = Column(String(2))
    excludefromtranscripts = Column(Numeric(10, 0, asdecimal=False))
    replaced_dcid = Column(Numeric(10, 0, asdecimal=False))
    excludefromgraduation = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))
    excludefromgradesuppression = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))
    replaced_equivalent_course = Column(String(11))
    gradereplacementpolicy_id = Column(Numeric(10, 0, asdecimal=False), index=True)


class Studentattendancesummary(Base):
    __tablename__ = 'studentattendancesummary'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentdcid = Column(Numeric(10, 0, asdecimal=False))
    schooldcid = Column(Numeric(10, 0, asdecimal=False))
    schoolyear = Column(Numeric(10, 0, asdecimal=False))
    startdate = Column(DateTime)
    startday = Column(Numeric(10, 0, asdecimal=False))
    enddate = Column(DateTime)
    endday = Column(Numeric(10, 0, asdecimal=False))
    resident = Column(String(10))
    daysattended = Column(Float)
    excusedabsences = Column(Float)
    unexcusedabsences = Column(Float)
    membershipvalue = Column(Float)
    daystransportedeligiblestaid = Column(Float)


class Studentrace(Base):
    __tablename__ = 'studentrace'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    racecd = Column(String(20), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whomodified = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))
    psguid = Column(String(50), unique=True)


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = (
        Index('students_n25', 'id', 'schoolid', 'entrydate', 'exitdate', 'track'),
        Index('students_n26', 'enroll_status', 'student_allowwebaccess'),
        Index('students_u2', 'id', 'dcid', unique=True),
        Index('students_n24', 'last_name', 'first_name')
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    lastfirst = Column(String(135), index=True)
    first_name = Column(String(50))
    middle_name = Column(String(30))
    last_name = Column(String(50))
    student_number = Column(Float, index=True)
    enroll_status = Column(Numeric(10, 0, asdecimal=False), index=True)
    grade_level = Column(Numeric(10, 0, asdecimal=False), index=True)
    balance1 = Column(Float)
    balance2 = Column(Float)
    phone_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    lunch_id = Column(Float, index=True)
    photoflag = Column(Numeric(10, 0, asdecimal=False))
    gender = Column(String(2), index=True)
    entrydate = Column(DateTime, index=True)
    exitdate = Column(DateTime, index=True)
    web_id = Column(String(20), index=True)
    web_password = Column(String(4000))
    sdatarn = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    dob = Column(DateTime)
    street = Column(String(60))
    city = Column(String(50))
    state = Column(String(2))
    zip = Column(String(10))
    guardianemail = Column(Text)
    allowwebaccess = Column(Numeric(10, 0, asdecimal=False))
    transfercomment = Column(Text)
    guardianfax = Column(String(30))
    custom = Column(Text)
    ssn = Column(String(12), index=True)
    entrycode = Column(String(10))
    exitcode = Column(String(10))
    lunchstatus = Column(String(3))
    ethnicity = Column(String(20))
    cumulative_gpa = Column(Float)
    simple_gpa = Column(Float)
    cumulative_pct = Column(Float)
    lastmeal = Column(String(20))
    pl_language = Column(String(12))
    simple_pct = Column(Float)
    classof = Column(Numeric(10, 0, asdecimal=False))
    family_ident = Column(String(30))
    next_school = Column(Numeric(10, 0, asdecimal=False))
    log = Column(Text)
    track = Column(String(20))
    exclude_fr_rank = Column(Numeric(10, 0, asdecimal=False))
    gradreqset = Column(String(3))
    teachergroupid = Column(Numeric(10, 0, asdecimal=False))
    campusid = Column(Numeric(10, 0, asdecimal=False))
    balance3 = Column(Float)
    balance4 = Column(Float)
    enrollment_schoolid = Column(Numeric(10, 0, asdecimal=False))
    gradreqsetid = Column(Numeric(10, 0, asdecimal=False))
    applic_submitted_date = Column(DateTime)
    applic_response_recvd_date = Column(DateTime)
    student_web_id = Column(String(20), index=True)
    student_web_password = Column(String(4000))
    student_allowwebaccess = Column(Numeric(10, 0, asdecimal=False))
    bus_route = Column(String(20))
    bus_stop = Column(String(20))
    doctor_name = Column(String(60))
    doctor_phone = Column(String(30))
    emerg_contact_1 = Column(String(60))
    emerg_contact_2 = Column(String(60))
    emerg_phone_1 = Column(String(30))
    emerg_phone_2 = Column(String(30))
    father = Column(String(60))
    home_phone = Column(String(30), index=True)
    home_room = Column(String(60))
    locker_combination = Column(String(20))
    locker_number = Column(String(15))
    mailing_city = Column(String(50))
    mailing_street = Column(String(60))
    mailing_state = Column(String(2))
    mailing_zip = Column(String(10))
    mother = Column(String(60))
    wm_status = Column(String(10))
    wm_statusdate = Column(DateTime)
    wm_tier = Column(Numeric(10, 0, asdecimal=False))
    wm_address = Column(String(70), index=True)
    wm_password = Column(Text)
    wm_createdate = Column(DateTime)
    wm_createtime = Column(Numeric(10, 0, asdecimal=False))
    sched_yearofgraduation = Column(Numeric(10, 0, asdecimal=False))
    sched_nextyearhouse = Column(String(10))
    sched_nextyearbuilding = Column(String(10))
    sched_nextyearteam = Column(String(10))
    sched_nextyearhomeroom = Column(String(10))
    sched_nextyeargrade = Column(Numeric(10, 0, asdecimal=False))
    sched_nextyearbus = Column(String(20))
    sched_scheduled = Column(Numeric(10, 0, asdecimal=False))
    sched_lockstudentschedule = Column(Numeric(10, 0, asdecimal=False))
    wm_ta_flag = Column(String(3))
    wm_ta_date = Column(DateTime)
    sched_priority = Column(Numeric(10, 0, asdecimal=False))
    districtentrydate = Column(DateTime)
    districtentrygradelevel = Column(Numeric(10, 0, asdecimal=False))
    schoolentrydate = Column(DateTime)
    schoolentrygradelevel = Column(Numeric(10, 0, asdecimal=False))
    graduated_schoolname = Column(String(60))
    graduated_schoolid = Column(Numeric(10, 0, asdecimal=False))
    graduated_rank = Column(Numeric(10, 0, asdecimal=False))
    alert_discipline = Column(Text)
    alert_disciplineexpires = Column(DateTime)
    alert_guardian = Column(Text)
    alert_guardianexpires = Column(DateTime)
    alert_medical = Column(Text)
    alert_medicalexpires = Column(DateTime)
    alert_other = Column(Text)
    alert_otherexpires = Column(DateTime)
    customrank_gpa = Column(Float)
    state_studentnumber = Column(String(32), index=True)
    state_excludefromreporting = Column(Numeric(10, 0, asdecimal=False))
    state_enrollflag = Column(Numeric(10, 0, asdecimal=False))
    districtofresidence = Column(String(20))
    enrollmenttype = Column(String(2))
    enrollmentcode = Column(Numeric(10, 0, asdecimal=False))
    fulltimeequiv_obsolete = Column(Float)
    membershipshare = Column(Float)
    tuitionpayer = Column(Numeric(10, 0, asdecimal=False))
    enrollment_transfer_date_pend = Column(DateTime)
    enrollment_transfer_info = Column(LargeBinary)
    exitcomment = Column(Text)
    fee_exemption_status = Column(Numeric(10, 0, asdecimal=False))
    team = Column(String(10))
    house = Column(String(10))
    building = Column(String(10))
    fteid = Column(Numeric(10, 0, asdecimal=False), index=True)
    withdrawal_reason_code = Column(String(3))
    guardian_studentcont_guid = Column(String(32), index=True)
    father_studentcont_guid = Column(String(32), index=True)
    mother_studentcont_guid = Column(String(32), index=True)
    studentpers_guid = Column(String(32), index=True)
    studentpict_guid = Column(String(32), index=True)
    studentschlenrl_guid = Column(String(32), index=True)
    sched_loadlock = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))
    person_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    ldapenabled = Column(Numeric(10, 0, asdecimal=False))
    summerschoolid = Column(Numeric(10, 0, asdecimal=False))
    summerschoolnote = Column(String(80))
    geocode = Column(String(50))
    mailing_geocode = Column(String(50))
    fedracedecline = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))
    fedethnicity = Column(Numeric(10, 0, asdecimal=False), server_default=text("-1"))
    gpentryyear = Column(Numeric(10, 0, asdecimal=False))
    enrollmentid = Column(Numeric(10, 0, asdecimal=False), unique=True)
    psguid = Column(String(50), unique=True)


class Activity(Student):
    __tablename__ = 'activities'

    studentsdcid = Column(ForeignKey('students.dcid'), primary_key=True)
    act_ss_mun = Column(String(4000))
    act_ss_ten = Column(String(4000))
    elementary_choir = Column(String(4000))
    elementary_drama_performance = Column(String(4000))
    es_hip_hop = Column(String(4000))
    es_tae_kwon_do_sat = Column(String(4000))
    es_tae_kwon_do_thu = Column(String(4000))
    tae_kwon_do = Column(String(4000))
    u11_soccer = Column(String(4000))
    u9_soccer = Column(String(4000))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    acamis_volleyball = Column(String(4000))


class CStudentlookup(Student):
    __tablename__ = 'c_studentlookup'

    studentsdcid = Column(ForeignKey('students.dcid'), primary_key=True)
    isok_to_transfer = Column(Numeric(1, 0, asdecimal=False))
    next_locator = Column(String(100))
    prev_locator = Column(String(100))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SStuCrdcX(Student):
    __tablename__ = 's_stu_crdc_x'

    studentsdcid = Column(ForeignKey('students.dcid'), primary_key=True)
    distancelearning_yn = Column(String(1))
    dualenrollment_yn = Column(String(1))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    creditrecovery_yn = Column(String(1))


class SStuNceaX(Student):
    __tablename__ = 's_stu_ncea_x'

    studentsdcid = Column(ForeignKey('students.dcid'), primary_key=True)
    diagnoseddisability_tf = Column(Numeric(1, 0, asdecimal=False))
    excludefromncea_tf = Column(Numeric(1, 0, asdecimal=False))
    federalnutrition = Column(String(2))
    religiousaffiliation = Column(String(1))
    subsidizedtrans_tf = Column(Numeric(1, 0, asdecimal=False))
    titlei_tf = Column(Numeric(1, 0, asdecimal=False))
    ungraded_tf = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Studentcorefield(Student):
    __tablename__ = 'studentcorefields'

    studentsdcid = Column(ForeignKey('students.dcid'), primary_key=True)
    pscore_legal_first_name = Column(String(100))
    pscore_legal_gender = Column(String(10))
    pscore_legal_last_name = Column(String(100))
    pscore_legal_middle_name = Column(String(100))
    pscore_legal_suffix = Column(String(10))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    act_composite = Column(String(4000))
    act_date = Column(String(4000))
    act_english = Column(String(4000))
    act_math = Column(String(4000))
    act_reading = Column(String(4000))
    act_science = Column(String(4000))
    afdc = Column(String(4000))
    afdcappnum = Column(String(4000))
    allergies = Column(String(4000))
    area = Column(String(4000))
    ate_skill_cert = Column(String(4000))
    dateofentryintousa = Column(String(4000))
    dentist_name = Column(String(4000))
    dentist_phone = Column(String(4000))
    emerg_1_ptype = Column(String(4000))
    emerg_1_rel = Column(String(4000))
    emerg_2_ptype = Column(String(4000))
    emerg_2_rel = Column(String(4000))
    emerg_3_phone = Column(String(4000))
    emerg_3_ptype = Column(String(4000))
    emerg_3_rel = Column(String(4000))
    emerg_contact_3 = Column(String(4000))
    equipstudent = Column(String(4000))
    esl_placement = Column(String(4000))
    family_rep = Column(String(4000))
    father_employer = Column(String(4000))
    father_home_phone = Column(String(4000))
    fatherdayphone = Column(String(4000))
    graduation_year = Column(String(4000))
    guardian = Column(String(4000))
    guardian_fn = Column(String(4000))
    guardian_ln = Column(String(4000))
    guardian_mn = Column(String(4000))
    guardiandayphone = Column(String(4000))
    guardianrelcode = Column(String(4000))
    guardianship = Column(String(4000))
    hln = Column(String(4000))
    homeless_code = Column(String(4000))
    ildp = Column(String(4000))
    immunizaton_dpt = Column(String(4000))
    immunizaton_mmr = Column(String(4000))
    immunizaton_polio = Column(String(4000))
    lep_exit_date = Column(String(4000))
    lep_status = Column(String(4000))
    lpac_date = Column(String(4000))
    medical_considerations = Column(String(4000))
    mesa = Column(String(4000))
    monitor_date = Column(String(4000))
    mother_employer = Column(String(4000))
    mother_home_phone = Column(String(4000))
    motherdayphone = Column(String(4000))
    parttimestudent = Column(String(4000))
    phlote = Column(String(4000))
    prevstudentid = Column(String(4000))
    primarylanguage = Column(String(4000))
    sat = Column(String(4000))
    secondarylanguage = Column(String(4000))
    singleparenthshldflag = Column(String(4000))
    tracker = Column(String(4000))
    autosend_attendancedetail = Column(String(4000))
    autosend_balancealert = Column(String(4000))
    autosend_gradedetail = Column(String(4000))
    autosend_howoften = Column(String(4000))
    autosend_schoolannouncements = Column(String(4000))
    autosend_summary = Column(String(4000))
    awards = Column(String(4000))
    c_504_information = Column(String(4000))
    career_goal = Column(String(4000))
    cip_code = Column(String(4000))
    competencies = Column(String(4000))
    crt_7thmath = Column(String(4000))
    crt_7thscience = Column(String(4000))
    crt_8thscience = Column(String(4000))
    crt_applemath2 = Column(String(4000))
    crt_applmath1 = Column(String(4000))
    crt_biology = Column(String(4000))
    crt_chemistry = Column(String(4000))
    crt_earthsys = Column(String(4000))
    crt_elemalg = Column(String(4000))
    crt_elemmath = Column(String(4000))
    crt_elemread = Column(String(4000))
    crt_humanbiol = Column(String(4000))
    crt_interalg = Column(String(4000))
    crt_physics = Column(String(4000))
    crt_prealg = Column(String(4000))
    crt_secmath = Column(String(4000))
    crt_secscience = Column(String(4000))
    ec_athletics = Column(String(4000))
    ec_clubs = Column(String(4000))
    ec_community = Column(String(4000))
    ec_leadership = Column(String(4000))
    ipt_oral_curdate = Column(String(4000))
    ipt_oral_currentscore = Column(String(4000))
    ipt_oral_origdate = Column(String(4000))
    ipt_oral_origscore = Column(String(4000))
    ipt_reading_curdate = Column(String(4000))
    ipt_reading_currentscore = Column(String(4000))
    ipt_reading_origdate = Column(String(4000))
    ipt_reading_origscore = Column(String(4000))
    ipt_writing_curdate = Column(String(4000))
    ipt_writing_currentscore = Column(String(4000))
    ipt_writing_origdate = Column(String(4000))
    ipt_writing_origscore = Column(String(4000))
    language_form = Column(String(4000))
    lunchapplicno = Column(String(4000))
    post_secondary_objectives = Column(String(4000))
    primary_pathway = Column(String(4000))
    secondary_pathway = Column(String(4000))
    seop_notes = Column(String(4000))
    spedlep = Column(String(4000))
    test_comments = Column(String(4000))


class Studentschedulingresult(Base):
    __tablename__ = 'studentschedulingresults'
    __table_args__ = (
        Index('studentschedulingresults_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    buildid = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    totalrequests = Column(Numeric(10, 0, asdecimal=False))
    enrolledslots = Column(Numeric(10, 0, asdecimal=False))
    coreslots = Column(Numeric(10, 0, asdecimal=False))
    primereqsatisfied = Column(Numeric(10, 0, asdecimal=False))
    totalreqsatisfied = Column(Numeric(10, 0, asdecimal=False))


class Studentsectcategorytotal(Base):
    __tablename__ = 'studentsectcategorytotal'
    __table_args__ = (
        Index('studentsectcategorytotal_u4', 'sectionsdcid', 'studentsdcid', 'teachercategoryid', unique=True),
    )

    studentsectcategorytotalid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    sectionsdcid = Column(ForeignKey('sections.dcid'), nullable=False, index=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    teachercategoryid = Column(ForeignKey('teachercategory.teachercategoryid'), nullable=False, index=True)
    scorepercent = Column(Numeric(18, 6))
    scoregrade = Column(String(30))
    scorepoints = Column(Numeric(18, 6))
    pointspossible = Column(Numeric(10, 0, asdecimal=False))
    lastupdated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    storecode = Column(String(10), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    section = relationship('Section')
    student = relationship('Student')
    teachercategory = relationship('Teachercategory')


class Studenttest(Base):
    __tablename__ = 'studenttest'
    __table_args__ = (
        Index('studenttest_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    testid = Column(Numeric(10, 0, asdecimal=False), index=True)
    test_date = Column(DateTime, index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    grade_level = Column(Numeric(10, 0, asdecimal=False))
    termid = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)


class Studenttestscore(Base):
    __tablename__ = 'studenttestscore'
    __table_args__ = (
        Index('studenttestscore_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    testscoreid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studenttestid = Column(Numeric(10, 0, asdecimal=False), index=True)
    numscore = Column(Float)
    percentscore = Column(Float)
    alphascore = Column(String(20))
    psguid = Column(String(50), unique=True)


class SyncCoursemap(Base):
    __tablename__ = 'sync_coursemap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    coursesdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    courseid = Column(ForeignKey('psm_course.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_course = relationship('PsmCourse')


class SyncCycledaymap(Base):
    __tablename__ = 'sync_cycledaymap'

    dcid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    cycledaydcid = Column(Numeric(19, 0, asdecimal=False), nullable=False, unique=True)
    cycledayid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)


class SyncGrademap(Base):
    __tablename__ = 'sync_grademap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    gradescaleitemdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    gradeid = Column(ForeignKey('psm_grade.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_grade = relationship('PsmGrade')


class SyncGradescalemap(Base):
    __tablename__ = 'sync_gradescalemap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    gradescaleitemdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    gradescaleid = Column(ForeignKey('psm_gradescale.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_gradescale = relationship('PsmGradescale')


class SyncPeriodmap(Base):
    __tablename__ = 'sync_periodmap'

    dcid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    perioddcid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    periodid = Column(Numeric(19, 0, asdecimal=False), nullable=False, index=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)


class SyncPgassignmentsmap(Base):
    __tablename__ = 'sync_pgassignmentsmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    pgassignmentsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    sectionassignmentid = Column(ForeignKey('psm_sectionassignment.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_sectionassignment = relationship('PsmSectionassignment')


class SyncPgcategoriesmap(Base):
    __tablename__ = 'sync_pgcategoriesmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    pgcategoriesdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    assignmentcategoryid = Column(ForeignKey('psm_assignmentcategory.id'), nullable=False, index=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_assignmentcategory = relationship('PsmAssignmentcategory')


class SyncPgcommentbankmap(Base):
    __tablename__ = 'sync_pgcommentbankmap'

    dcid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    pgcommentbankdcid = Column(Numeric(19, 0, asdecimal=False), nullable=False, unique=True)
    commentbankid = Column(Numeric(19, 0, asdecimal=False), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)


class SyncReportingtermmap(Base):
    __tablename__ = 'sync_reportingtermmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    termbinsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    reportingtermid = Column(ForeignKey('psm_reportingterm.id'), nullable=False, index=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_reportingterm = relationship('PsmReportingterm')


class SyncSchoolmap(Base):
    __tablename__ = 'sync_schoolmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    schoolsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    schoolid = Column(ForeignKey('psm_school.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_school = relationship('PsmSchool')


class SyncSectionenrollmentmap(Base):
    __tablename__ = 'sync_sectionenrollmentmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    ccdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    sectionenrollmentid = Column(ForeignKey('psm_sectionenrollment.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_sectionenrollment = relationship('PsmSectionenrollment')


class SyncSectionmap(Base):
    __tablename__ = 'sync_sectionmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    sectionsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    sectionid = Column(ForeignKey('psm_section.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_section = relationship('PsmSection')


class SyncSectionmeetingmap(Base):
    __tablename__ = 'sync_sectionmeetingmap'

    dcid = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    sectionmeetingdcid = Column(Numeric(19, 0, asdecimal=False), nullable=False, unique=True)
    meetingid = Column(Numeric(19, 0, asdecimal=False), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)


class SyncSectionteachermap(Base):
    __tablename__ = 'sync_sectionteachermap'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    pssectionteacherid = Column(Numeric(19, 0, asdecimal=False), nullable=False, unique=True)
    psmsectionteacherid = Column(ForeignKey('psm_sectionteacher.id'), nullable=False, unique=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    psm_sectionteacher = relationship('PsmSectionteacher')


class SyncStandardmap(Base):
    __tablename__ = 'sync_standardmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    standardsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    standardid = Column(ForeignKey('psm_standard.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_standard = relationship('PsmStandard')


class SyncStdconversionmap(Base):
    __tablename__ = 'sync_stdconversionmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    gendcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    gradeid = Column(ForeignKey('psm_grade.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_grade = relationship('PsmGrade')


class SyncStdconversionscalemap(Base):
    __tablename__ = 'sync_stdconversionscalemap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    gendcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    gradescaleid = Column(ForeignKey('psm_gradescale.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_gradescale = relationship('PsmGradescale')


class SyncStudentmap(Base):
    __tablename__ = 'sync_studentmap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    studentsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    studentid = Column(ForeignKey('psm_student.id'), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_student = relationship('PsmStudent')


class SyncTeachermap(Base):
    __tablename__ = 'sync_teachermap'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    teachersdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False, index=True)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_teacher = relationship('PsmTeacher')


class SyncTermmap(Base):
    __tablename__ = 'sync_termmap'
    __table_args__ = (
        Index('sync_termmap_u3', 'termid', 'termsdcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    termsdcid = Column(Numeric(10, 0, asdecimal=False), nullable=False, unique=True)
    termid = Column(ForeignKey('psm_term.id'), nullable=False)
    created = Column(DateTime, nullable=False)
    lastupdated = Column(DateTime, nullable=False)

    psm_term = relationship('PsmTerm')


class Syncdistrict(Base):
    __tablename__ = 'syncdistricts'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sifzoneid = Column(String(50))
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    schoolnum = Column(String(50))
    sifdata = Column(Text)
    refid = Column(String(32), unique=True)
    displaytitle = Column(String(50))
    eventaction = Column(Numeric(scale=0, asdecimal=False))


t_syncerrors = Table(
    'syncerrors', metadata,
    Column('syncstatusid', Numeric(scale=0, asdecimal=False), index=True),
    Column('severity', String(1)),
    Column('message', String(255)),
    Column('details', Text)
)


class Syncgenericobject(Base):
    __tablename__ = 'syncgenericobjects'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    objtype = Column(Numeric(scale=0, asdecimal=False))
    refid = Column(String(32))
    schoolnum = Column(String(50), index=True)
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    sifdata = Column(Text)
    eventaction = Column(Numeric(scale=0, asdecimal=False))
    zoneid = Column(String(50))


t_syncpendingmatches = Table(
    'syncpendingmatches', metadata,
    Column('syncrecordid', Numeric(scale=0, asdecimal=False)),
    Column('objtype', Numeric(scale=0, asdecimal=False)),
    Column('schoolnum', String(50)),
    Column('apptitle', String(128)),
    Column('appmatchvaluedisplay', String(128)),
    Column('appmatchvalues', String(128)),
    Column('appprimarykey', String(50)),
    Column('appsecondarykey', String(50)),
    Column('sifmatchvaluedisplay', String(128)),
    Column('sifmatchvalues', String(128)),
    Column('sifrefid', String(32)),
    Column('siftitle', String(128)),
    Column('status', Numeric(scale=0, asdecimal=False), index=True),
    Column('sort', String(128)),
    Column('zoneid', String(50)),
    Index('syncpendingmatches_n2', 'objtype', 'schoolnum')
)


class Syncroom(Base):
    __tablename__ = 'syncrooms'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    schoolnum = Column(String(50), index=True)
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    roomnum = Column(String(50))
    sifdata = Column(Text)
    refid = Column(String(32), unique=True)
    displaytitle = Column(String(50))
    zoneid = Column(String(50))


class Syncschool(Base):
    __tablename__ = 'syncschools'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sifzoneid = Column(String(50))
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    schoolnum = Column(String(50))
    appschoolnum = Column(String(50))
    sifdata = Column(Text)
    refid = Column(String(32), unique=True)
    displaytitle = Column(String(50))


class Syncsession(Base):
    __tablename__ = 'syncsessions'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    synctype = Column(Numeric(scale=0, asdecimal=False))
    owner = Column(String(50))
    host = Column(String(50))
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    status = Column(Numeric(scale=0, asdecimal=False))


class Syncstaff(Base):
    __tablename__ = 'syncstaff'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    schoolnum = Column(String(50), index=True)
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    staffnum = Column(String(50))
    matchvalues = Column(String(128))
    sifdata = Column(Text)
    refid = Column(String(32), unique=True)
    displaytitle = Column(String(50))
    zoneid = Column(String(50))


class Syncstatu(Base):
    __tablename__ = 'syncstatus'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    objtype = Column(Numeric(scale=0, asdecimal=False))
    sifrequestid = Column(String(32), unique=True)
    sifrequesttime = Column(DateTime)
    sifzoneid = Column(String(50))
    stage = Column(Numeric(scale=0, asdecimal=False))


class Syncstudentcontact(Base):
    __tablename__ = 'syncstudentcontacts'
    __table_args__ = (
        Index('syncstudentcontacts_u2', 'refid', 'schoolnum', unique=True),
    )

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    refid = Column(String(32))
    schoolnum = Column(String(50), index=True)
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    studentcontactnum = Column(String(50))
    matchvalues = Column(String(128))
    sifdata = Column(Text)
    displaytitle = Column(String(128))
    studentrefid = Column(String(32), index=True)
    zoneid = Column(String(50))


class Syncstudent(Base):
    __tablename__ = 'syncstudents'
    __table_args__ = (
        Index('syncstudents_u2', 'refid', 'schoolnum', unique=True),
    )

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    refid = Column(String(32))
    schoolnum = Column(String(50), index=True)
    sifsourceid = Column(String(50))
    sifmsgid = Column(String(32))
    studentnum = Column(String(50))
    matchvalues = Column(String(128))
    sifdata = Column(Text)
    displaytitle = Column(String(50))
    zoneid = Column(String(50))


class SysSequence(Base):
    __tablename__ = 'sys_sequence'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    name = Column(String(80), nullable=False, unique=True)
    next_id = Column(Numeric(10, 0, asdecimal=False))
    quantity = Column(Numeric(10, 0, asdecimal=False))


class Tablenumbermap(Base):
    __tablename__ = 'tablenumbermap'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    tablename = Column(String(30), nullable=False, unique=True)
    tablenumber = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))


class Teachercategory(Base):
    __tablename__ = 'teachercategory'
    __table_args__ = (
        Index('teachercategory_u3', 'usersdcid', 'districtteachercategoryid', unique=True),
    )

    teachercategoryid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    districtteachercategoryid = Column(ForeignKey('districtteachercategory.districtteachercategoryid'), index=True)
    name = Column(String(30))
    usersdcid = Column(ForeignKey('users.dcid'), nullable=False, index=True)
    description = Column(String(4000))
    categorytype = Column(String(30), nullable=False)
    color = Column(String(30))
    isinfinalgrades = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    isactive = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    isusermodifiable = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    teachermodified = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    displayposition = Column(Numeric(6, 0, asdecimal=False), nullable=False, server_default=text("9999    "))
    defaultscoreentrypoints = Column(Numeric(18, 6))
    defaultextracreditpoints = Column(Numeric(18, 6))
    defaultweight = Column(Numeric(18, 6))
    defaulttotalvalue = Column(Numeric(18, 6))
    defaultpublishstate = Column(String(30))
    defaultpublishoption = Column(String(30))
    isdefaultpublishscores = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1       "))
    defaultscoretype = Column(String(30))
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    defaultdaysbeforedue = Column(Numeric(3, 0, asdecimal=False))

    districtteachercategory = relationship('Districtteachercategory')
    user = relationship('User')


class Teachercatsectexcludeassoc(Base):
    __tablename__ = 'teachercatsectexcludeassoc'
    __table_args__ = (
        Index('teachercatsectexcludeassoc_u2', 'teachercategoryid', 'sectionsdcid', unique=True),
    )

    teachercatsectexcludeassocid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    yearid = Column(Numeric(10, 0, asdecimal=False))
    teachercategoryid = Column(ForeignKey('teachercategory.teachercategoryid'), nullable=False, index=True)
    sectionsdcid = Column(ForeignKey('sections.dcid'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER    "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER    "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))

    section = relationship('Section')
    teachercategory = relationship('Teachercategory')


class Teacherdailyload(Base):
    __tablename__ = 'teacherdailyload'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    dailyloaddate = Column(DateTime, index=True)
    loadquantity = Column(Float, index=True)


class Teacheremailqueue(Base):
    __tablename__ = 'teacheremailqueue'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    emailqueueid = Column(ForeignKey('emailqueue.id'), nullable=False, index=True)
    psm_teacherid = Column(ForeignKey('psm_teacher.id'), nullable=False, index=True)
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))

    emailqueue = relationship('Emailqueue')
    psm_teacher = relationship('PsmTeacher')


class Teacherfavoritecomment(Base):
    __tablename__ = 'teacherfavoritecomment'

    teacherfavoritecommentid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    usersdcid = Column(ForeignKey('users.dcid'), nullable=False, index=True)
    pgcommentbankdcid = Column(ForeignKey('pgcommentbank.dcid'), index=True)
    displayposition = Column(Numeric(6, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    pgcommentbank = relationship('Pgcommentbank')
    user = relationship('User')


class Teacherpreference(Base):
    __tablename__ = 'teacherpreference'

    teacherpreferenceid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    usersdcid = Column(ForeignKey('users.dcid'), nullable=False, index=True)
    sectionnames = Column(String(30), server_default=text("NULL                 "))
    isstandardsshown = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL                 "))
    isstandardsshownonasgmt = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL                 "))
    istraditionalgradeshown = Column(Numeric(1, 0, asdecimal=False), server_default=text("NULL                 "))
    standardtraditionalorder = Column(String(30), server_default=text("NULL                 "))
    studentnamedisplayoption = Column(String(30), nullable=False, server_default=text("'Last_First'   "))
    studentsortoption = Column(String(30), nullable=False, server_default=text("'Last_Name'    "))
    assignmentsortoption = Column(String(30), nullable=False, server_default=text("'Due_Date_Asc' "))
    isnewstudaddedtobottom = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0                "))
    ispreregstudenthidden = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0                "))
    ispercentdisplayed = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    ispointsearneddisplayed = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0                "))
    islettergradedisplayed = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    calcdirectioninitstate = Column(String(30), nullable=False, server_default=text("'UnSet'        "))
    iscalchelpfullclassshown = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    iscalchelpstudentshown = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1                "))
    overlaymask = Column(Numeric(16, 0, asdecimal=False), nullable=False, server_default=text("0                "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER             "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE          "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER             "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE          "))

    user = relationship('User')


class Teacherrace(Base):
    __tablename__ = 'teacherrace'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    racecd = Column(String(20), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whomodified = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


t_teachers = Table(
    'teachers', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('lastfirst', String(40)),
    Column('first_name', String(20)),
    Column('middle_name', String(20)),
    Column('last_name', String(20)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('status', Numeric(10, 0, asdecimal=False)),
    Column('photo', Numeric(10, 0, asdecimal=False)),
    Column('balance1', Float),
    Column('title', String(40)),
    Column('homeroom', String(20)),
    Column('email_addr', String(50)),
    Column('password', String(4000)),
    Column('numlogins', Numeric(10, 0, asdecimal=False)),
    Column('ipaddrrestrict', Text),
    Column('allowloginstart', Numeric(10, 0, asdecimal=False)),
    Column('allowloginend', Numeric(10, 0, asdecimal=False)),
    Column('psaccess', Numeric(10, 0, asdecimal=False)),
    Column('accessvalue', Text),
    Column('homepage', Text),
    Column('loginid', String(20)),
    Column('classpua', Text),
    Column('noofcurclasses', Numeric(10, 0, asdecimal=False)),
    Column('defaultstudscrn', Text),
    Column('custom', Text),
    Column('groupvalue', Numeric(10, 0, asdecimal=False)),
    Column('teachernumber', String(20)),
    Column('lunch_id', Float),
    Column('balance2', Float),
    Column('ssn', String(12)),
    Column('home_phone', String(20)),
    Column('school_phone', String(20)),
    Column('street', String(80)),
    Column('city', String(40)),
    Column('state', String(2)),
    Column('zip', String(10)),
    Column('periodsavail', String(40)),
    Column('powergradepw', String(20)),
    Column('canchangeschool', Text),
    Column('log', Text),
    Column('teacherloginpw', String(4000)),
    Column('nameasimported', String(40)),
    Column('teacherloginid', String(20)),
    Column('teacherloginip', Text),
    Column('supportcontact', Numeric(10, 0, asdecimal=False)),
    Column('balance3', Float),
    Column('balance4', Float),
    Column('wm_status', String(10)),
    Column('wm_statusdate', DateTime),
    Column('wm_tier', Numeric(10, 0, asdecimal=False)),
    Column('wm_address', String(70)),
    Column('wm_password', String(20)),
    Column('wm_createdate', DateTime),
    Column('wm_createtime', Numeric(10, 0, asdecimal=False)),
    Column('wm_ta_flag', String(3)),
    Column('wm_ta_date', DateTime),
    Column('wm_exclude', Numeric(10, 0, asdecimal=False)),
    Column('staffstatus', Numeric(10, 0, asdecimal=False)),
    Column('sched_gender', String(2)),
    Column('sched_classroom', String(10)),
    Column('sched_homeroom', String(10)),
    Column('sched_department', String(10)),
    Column('sched_maximumcourses', Numeric(10, 0, asdecimal=False)),
    Column('sched_maximumduty', Numeric(10, 0, asdecimal=False)),
    Column('sched_maximumfree', Numeric(10, 0, asdecimal=False)),
    Column('sched_totalcourses', Numeric(10, 0, asdecimal=False)),
    Column('sched_maximumconsecutive', Numeric(10, 0, asdecimal=False)),
    Column('sched_isteacherfree', Numeric(10, 0, asdecimal=False)),
    Column('sched_housecode', String(10)),
    Column('sched_buildingcode', String(10)),
    Column('sched_activitystatuscode', String(8)),
    Column('sched_primaryschoolcode', String(10)),
    Column('sched_teachermoreoneschool', Numeric(10, 0, asdecimal=False)),
    Column('sched_substitute', Numeric(10, 0, asdecimal=False)),
    Column('sched_scheduled', Numeric(10, 0, asdecimal=False)),
    Column('wm_alias', String(70)),
    Column('sched_usebuilding', Numeric(10, 0, asdecimal=False)),
    Column('sched_usehouse', Numeric(10, 0, asdecimal=False)),
    Column('ethnicity', String(20)),
    Column('sched_team', String(12)),
    Column('preferredname', String(45)),
    Column('lastmeal', String(20)),
    Column('sched_lunch', Numeric(10, 0, asdecimal=False)),
    Column('staffpers_guid', String(32)),
    Column('sched_maxpers', Numeric(10, 0, asdecimal=False)),
    Column('sched_maxpreps', Numeric(10, 0, asdecimal=False)),
    Column('adminldapenabled', Numeric(10, 0, asdecimal=False)),
    Column('teacherldapenabled', Numeric(10, 0, asdecimal=False)),
    Column('sif_stateprid', String(32)),
    Column('maximum_load', Numeric(10, 0, asdecimal=False)),
    Column('gradebooktype', Numeric(10, 0, asdecimal=False)),
    Column('fedethnicity', Numeric(10, 0, asdecimal=False)),
    Column('fedracedecline', Numeric(10, 0, asdecimal=False)),
    Column('homeschoolid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('notes', Text),
    Column('ptaccess', Numeric(1, 0, asdecimal=False)),
    Column('users_dcid', Numeric(10, 0, asdecimal=False), nullable=False)
)


class TeachersNcf31(Base):
    __tablename__ = 'teachers_ncf31'
    __table_args__ = (
        Index('teachers_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    lastfirst = Column(String(130), index=True)
    first_name = Column(String(50))
    middle_name = Column(String(30))
    last_name = Column(String(50))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    status = Column(Numeric(10, 0, asdecimal=False), index=True)
    photo = Column(Numeric(10, 0, asdecimal=False))
    balance1 = Column(Float)
    title = Column(String(40))
    homeroom = Column(String(20))
    email_addr = Column(String(50))
    password = Column(String(4000))
    numlogins = Column(Numeric(10, 0, asdecimal=False))
    ipaddrrestrict = Column(Text)
    allowloginstart = Column(Numeric(10, 0, asdecimal=False))
    allowloginend = Column(Numeric(10, 0, asdecimal=False))
    psaccess = Column(Numeric(10, 0, asdecimal=False))
    accessvalue = Column(Text)
    homepage = Column(Text)
    loginid = Column(String(20), index=True)
    classpua = Column(Text)
    noofcurclasses = Column(Numeric(10, 0, asdecimal=False))
    defaultstudscrn = Column(Text)
    custom = Column(Text)
    groupvalue = Column(Numeric(10, 0, asdecimal=False))
    teachernumber = Column(String(20))
    lunch_id = Column(Float, index=True)
    balance2 = Column(Float)
    ssn = Column(String(12))
    home_phone = Column(String(20))
    school_phone = Column(String(20))
    street = Column(String(80))
    city = Column(String(40))
    state = Column(String(2))
    zip = Column(String(10))
    periodsavail = Column(String(40))
    powergradepw = Column(String(20))
    canchangeschool = Column(Text)
    log = Column(Text)
    teacherloginpw = Column(String(4000))
    nameasimported = Column(String(40))
    teacherloginid = Column(String(20))
    teacherloginip = Column(Text)
    supportcontact = Column(Numeric(10, 0, asdecimal=False))
    balance3 = Column(Float)
    balance4 = Column(Float)
    wm_status = Column(String(10))
    wm_statusdate = Column(DateTime)
    wm_tier = Column(Numeric(10, 0, asdecimal=False))
    wm_address = Column(String(70), index=True)
    wm_password = Column(String(20), index=True)
    wm_createdate = Column(DateTime)
    wm_createtime = Column(Numeric(10, 0, asdecimal=False))
    wm_ta_flag = Column(String(3))
    wm_ta_date = Column(DateTime)
    wm_exclude = Column(Numeric(10, 0, asdecimal=False))
    staffstatus = Column(Numeric(10, 0, asdecimal=False), index=True)
    sched_gender = Column(String(2))
    sched_classroom = Column(String(10))
    sched_homeroom = Column(String(10))
    sched_department = Column(String(10))
    sched_maximumcourses = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumduty = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumfree = Column(Numeric(10, 0, asdecimal=False))
    sched_totalcourses = Column(Numeric(10, 0, asdecimal=False))
    sched_maximumconsecutive = Column(Numeric(10, 0, asdecimal=False))
    sched_isteacherfree = Column(Numeric(10, 0, asdecimal=False))
    sched_housecode = Column(String(10))
    sched_buildingcode = Column(String(10))
    sched_activitystatuscode = Column(String(8))
    sched_primaryschoolcode = Column(String(10))
    sched_teachermoreoneschool = Column(Numeric(10, 0, asdecimal=False))
    sched_substitute = Column(Numeric(10, 0, asdecimal=False))
    sched_scheduled = Column(Numeric(10, 0, asdecimal=False))
    wm_alias = Column(String(70))
    sched_usebuilding = Column(Numeric(10, 0, asdecimal=False))
    sched_usehouse = Column(Numeric(10, 0, asdecimal=False))
    ethnicity = Column(String(20))
    sched_team = Column(String(12))
    preferredname = Column(String(45))
    lastmeal = Column(String(20))
    sched_lunch = Column(Numeric(10, 0, asdecimal=False))
    staffpers_guid = Column(String(32), index=True)
    sched_maxpers = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))
    sched_maxpreps = Column(Numeric(10, 0, asdecimal=False), server_default=text("(0)"))
    adminldapenabled = Column(Numeric(10, 0, asdecimal=False))
    teacherldapenabled = Column(Numeric(10, 0, asdecimal=False))
    sif_stateprid = Column(String(32))
    maximum_load = Column(Numeric(10, 0, asdecimal=False))
    gradebooktype = Column(Numeric(10, 0, asdecimal=False))
    fedracedecline = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))
    fedethnicity = Column(Numeric(10, 0, asdecimal=False), server_default=text("-1"))


class Teacherscorecode(Base):
    __tablename__ = 'teacherscorecode'
    __table_args__ = (
        Index('teacherscorecode_u2', 'name', 'usersdcid', unique=True),
    )

    teacherscorecodeid = Column(Numeric(16, 0, asdecimal=False), primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(4000))
    usersdcid = Column(ForeignKey('users.dcid'), index=True)
    islate = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    iscollected = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    isexempt = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    ismissing = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    isabsent = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    isincomplete = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("0       "))
    percentvalue = Column(Numeric(18, 6))
    numerictype = Column(String(30))
    numericvalue = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), nullable=False, server_default=text("USER     "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER     "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE  "))

    user = relationship('User')


class Termbinattrib(Base):
    __tablename__ = 'termbinattrib'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    termbinsdcid = Column(ForeignKey('termbins.dcid'), nullable=False, unique=True)
    isexcludedfrommobile = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    ishistoryused = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("sysdate "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("sysdate "))
    isexcludedadmin = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    isexcludedteacher = Column(Numeric(3, 0, asdecimal=False), nullable=False, server_default=text("1 "))

    termbin = relationship('Termbin')


t_termbins = Table(
    'termbins', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False), nullable=False, unique=True),
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('termid', Numeric(10, 0, asdecimal=False)),
    Column('storecode', String(8), index=True),
    Column('schoolid', Numeric(10, 0, asdecimal=False), index=True),
    Column('creditpct', Float),
    Column('collect', Numeric(10, 0, asdecimal=False)),
    Column('date1', DateTime),
    Column('creditstring', String(15)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('collectiondate', DateTime),
    Column('showonspreadsht', Numeric(10, 0, asdecimal=False)),
    Column('description', String(30)),
    Column('currentgrade', Numeric(10, 0, asdecimal=False)),
    Column('storegrades', Numeric(10, 0, asdecimal=False)),
    Column('date2', DateTime),
    Column('citasmt', String(50)),
    Column('numattpoints', Float),
    Column('changegradeto', String(20)),
    Column('suppressltrgrd', Numeric(10, 0, asdecimal=False)),
    Column('excludedmarks', Text),
    Column('gradescaleid', Numeric(10, 0, asdecimal=False)),
    Column('suppresspercentscr', Numeric(10, 0, asdecimal=False)),
    Index('termbins_idx1', 'termid', 'schoolid', 'dcid', unique=True),
    Index('termbins_u2', 'id', 'dcid', unique=True)
)


class Term(Base):
    __tablename__ = 'terms'
    __table_args__ = (
        Index('terms_n5', 'schoolid', 'yearid', 'firstday', 'lastday', 'id'),
        Index('terms_n6', 'yearid', 'schoolid', 'firstday', 'lastday', 'id'),
        Index('terms_u2', 'id', 'dcid', unique=True)
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(30))
    firstday = Column(DateTime, index=True)
    lastday = Column(DateTime)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    abbreviation = Column(String(6))
    noofdays = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearlycredithrs = Column(Float)
    termsinyear = Column(Numeric(10, 0, asdecimal=False))
    portion = Column(Numeric(10, 0, asdecimal=False))
    importmap = Column(String(20))
    autobuildbin = Column(Numeric(10, 0, asdecimal=False))
    isyearrec = Column(Numeric(10, 0, asdecimal=False))
    periods_per_day = Column(Numeric(10, 0, asdecimal=False))
    days_per_cycle = Column(Numeric(10, 0, asdecimal=False))
    attendance_calculation_code = Column(Numeric(10, 0, asdecimal=False))
    sterms = Column(Numeric(10, 0, asdecimal=False))
    terminfo_guid = Column(String(32), index=True)
    psguid = Column(String(50), unique=True)


class Test(Base):
    __tablename__ = 'test'
    __table_args__ = (
        Index('test_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    name = Column(String(35), index=True)
    description = Column(Text)
    test_type = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)


class Testscore(Base):
    __tablename__ = 'testscore'
    __table_args__ = (
        Index('testscore_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    testid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(35))
    description = Column(Text)
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    psguid = Column(String(50), unique=True)


class Tmpdalxtable(Base):
    __tablename__ = 'tmpdalxtables'

    tablename = Column(String(30), primary_key=True)
    creationtimestamp = Column(DateTime, nullable=False, server_default=text("current_timestamp "))
    userid = Column(Numeric(10, 0, asdecimal=False))
    stacktrace = Column(Text)


class Transformtemp(Base):
    __tablename__ = 'transformtemp'

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    usersession = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    transformgroup = Column(Numeric(19, 0, asdecimal=False), nullable=False)
    transformpart = Column(Text, nullable=False)
    whencreated = Column(DateTime, nullable=False)


class Transportation(Base):
    __tablename__ = 'transportation'
    __table_args__ = (
        Index('transportation_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    description = Column(String(79))
    fromto = Column(String(79))
    type = Column(String(79))
    routenumber = Column(String(79))
    busnumber = Column(String(79))
    drivername = Column(String(79))
    contactnumber = Column(String(79))
    departuretime = Column(Numeric(10, 0, asdecimal=False))
    stopnumber = Column(String(79))
    address = Column(Text)
    distance = Column(Float)
    distanceindicator = Column(String(79))
    arrivaltime = Column(Numeric(10, 0, asdecimal=False))
    specialinstructions = Column(Text)
    monday = Column(Numeric(10, 0, asdecimal=False))
    tuesday = Column(Numeric(10, 0, asdecimal=False))
    wednesday = Column(Numeric(10, 0, asdecimal=False))
    thursday = Column(Numeric(10, 0, asdecimal=False))
    friday = Column(Numeric(10, 0, asdecimal=False))
    saturday = Column(Numeric(10, 0, asdecimal=False))
    sunday = Column(Numeric(10, 0, asdecimal=False))
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    linkingcode = Column(String(3))


class Truancy(Base):
    __tablename__ = 'truancies'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    date_value = Column(DateTime)
    reason = Column(String(60))
    comments = Column(Text)
    howmany = Column(Float)


class UAsaSelect(Base):
    __tablename__ = 'u_asa_select'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    activityid = Column(Numeric(11, 0, asdecimal=False))
    asaid = Column(String(40))
    cut = Column(String(4000))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    selstudents = Column(String(4000))
    t1selstudents = Column(String(4000))
    t2selstudents = Column(String(4000))
    t3selstudents = Column(String(4000))
    team = Column(String(40))
    termid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UAsaactivity(Base):
    __tablename__ = 'u_asaactivities'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    allowedgradelevel = Column(String(400))
    allowedgradelevels = Column(Numeric(11, 0, asdecimal=False))
    asatermid = Column(Numeric(11, 0, asdecimal=False))
    description = Column(Text)
    maxenrollment = Column(Numeric(11, 0, asdecimal=False))
    name = Column(String(1000))
    room = Column(String(400))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    teacher = Column(String(120))
    timestring = Column(String(100))
    unused1 = Column(String(400))
    unused2 = Column(String(4000))
    weekday = Column(String(40))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UAsastudentsignup(Base):
    __tablename__ = 'u_asastudentsignups'
    __table_args__ = (
        Index('u_asastudentsignupsu001', 'studentsdcid', 'activityid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    activityid = Column(Numeric(11, 0, asdecimal=False))
    bus = Column(String(500))
    confirmed = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    student = relationship('Student')


class UAsaterm(Base):
    __tablename__ = 'u_asaterms'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    description = Column(Text)
    name = Column(String(200))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    signupclosedate = Column(DateTime)
    signupopendate = Column(DateTime)
    unused1 = Column(String(400))
    unused2 = Column(String(4000))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UFamilyshared(Base):
    __tablename__ = 'u_familyshared'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    familyident = Column(String(30))
    odaddress = Column(Numeric(11, 0, asdecimal=False))
    odemail = Column(Numeric(11, 0, asdecimal=False))
    odlisting = Column(Numeric(11, 0, asdecimal=False))
    odphone = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    odfathername = Column(Numeric(11, 0, asdecimal=False))
    odfatherphone = Column(Numeric(11, 0, asdecimal=False))
    odmothername = Column(Numeric(11, 0, asdecimal=False))
    odmotherphone = Column(Numeric(11, 0, asdecimal=False))


class UGroupptcExcludedcourse(Base):
    __tablename__ = 'u_groupptc_excludedcourses'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    coursenumber = Column(String(40))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    termid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


t_u_groupptc_signups = Table(
    'u_groupptc_signups', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False, unique=True),
    Column('studentsdcid', ForeignKey('students.dcid'), nullable=False, index=True),
    Column('ptctermid', Numeric(11, 0, asdecimal=False), nullable=False),
    Column('remarks', String(4000)),
    Column('schoolid', Numeric(11, 0, asdecimal=False), nullable=False),
    Column('sectionid', Numeric(11, 0, asdecimal=False), nullable=False),
    Column('slotid', Numeric(11, 0, asdecimal=False), nullable=False),
    Column('termid', Numeric(11, 0, asdecimal=False), nullable=False),
    Column('userid', Numeric(11, 0, asdecimal=False)),
    Column('whocreated', String(100)),
    Column('whencreated', DateTime, server_default=text("SYSDATE")),
    Column('whomodified', String(100)),
    Column('whenmodified', DateTime),
    Index('u_groupptc_signupsu001', 'studentsdcid', 'ptctermid', 'sectionid', unique=True)
)


class UGroupptcTeacherslot(Base):
    __tablename__ = 'u_groupptc_teacherslot'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    remark = Column(String(4000))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    slotid = Column(Numeric(11, 0, asdecimal=False))
    teacherid = Column(Numeric(11, 0, asdecimal=False))
    termid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UGroupptcTerm(Base):
    __tablename__ = 'u_groupptc_terms'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    dateend = Column(DateTime)
    datestart = Column(DateTime)
    description = Column(String(4000))
    name = Column(String(40))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UGroupptcTimeslot(Base):
    __tablename__ = 'u_groupptc_timeslot'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    allowedgradelevels = Column(String(40))
    capacity = Column(Numeric(11, 0, asdecimal=False))
    endtime = Column(String(40))
    name = Column(String(400))
    remarks = Column(String(4000))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    slotdate = Column(DateTime)
    starttime = Column(String(40))
    termid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UOpenapplyIntegration(Base):
    __tablename__ = 'u_openapply_integration'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    oa_id = Column(Numeric(25, 10))
    oa_name = Column(String(40))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)
    ps_student_number = Column(String(10))


class UReRegister(Base):
    __tablename__ = 'u_re_register'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    familyid = Column(Numeric(11, 0, asdecimal=False))
    loginname = Column(String(100))
    status = Column(Numeric(11, 0, asdecimal=False))
    stuid = Column(Numeric(11, 0, asdecimal=False))
    termid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UReportCard(Base):
    __tablename__ = 'u_report_cards'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    name = Column(String(40))
    school_id = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    student = relationship('Student')


class UTripactivity(Base):
    __tablename__ = 'u_tripactivities'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    allowedgradelevel = Column(String(400))
    description = Column(Text)
    maxenrollment = Column(Numeric(11, 0, asdecimal=False))
    name = Column(String(1000))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    teacher = Column(String(120))
    triptermid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UTripstudentsignup(Base):
    __tablename__ = 'u_tripstudentsignups'
    __table_args__ = (
        Index('u_tripstudentsignupsu001', 'studentsdcid', 'tripid', unique=True),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    bus = Column(String(500))
    tripid = Column(Numeric(11, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    student = relationship('Student')


class UTripterm(Base):
    __tablename__ = 'u_tripterms'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    description = Column(Text)
    name = Column(String(200))
    schoolid = Column(Numeric(11, 0, asdecimal=False))
    signupclosedate = Column(DateTime)
    signupopendate = Column(DateTime)
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class UWidaTest(Base):
    __tablename__ = 'u_wida_test'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentsdcid = Column(ForeignKey('students.dcid'), nullable=False, index=True)
    composite = Column(String(40))
    grade_level = Column(Numeric(11, 0, asdecimal=False))
    listening = Column(String(40))
    reading = Column(String(40))
    speaking = Column(String(40))
    test_date = Column(DateTime)
    writing = Column(String(40))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)

    student = relationship('Student')


class Ucol(Base):
    __tablename__ = 'ucols'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    utableid = Column(Numeric(10, 0, asdecimal=False), index=True)
    seq = Column(Numeric(10, 0, asdecimal=False))
    title = Column(Text)
    contenttype = Column(Numeric(10, 0, asdecimal=False))
    contentli = Column(Numeric(10, 0, asdecimal=False))
    contents = Column(String(400))
    width = Column(Float)
    alignment = Column(Numeric(10, 0, asdecimal=False))
    format = Column(String(20))
    runningwidth = Column(Float)
    label = Column(Text)
    data = Column(Text)
    type = Column(Numeric(10, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    unused1 = Column(Numeric(10, 0, asdecimal=False))
    unused2 = Column(Numeric(10, 0, asdecimal=False))


class Unexcusedhistorical(Base):
    __tablename__ = 'unexcusedhistorical'
    __table_args__ = (
        Index('ueat_hist_n1', 'schoolid', 'unexcuseddate'),
        Index('ueat_hist_n2', 'studentid', 'unexcuseddate')
    )

    id = Column(Numeric(19, 0, asdecimal=False), primary_key=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    studentid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    unexcuseddate = Column(DateTime, index=True)
    periodcnt = Column(Numeric(10, 0, asdecimal=False), index=True)
    periodnumber = Column(Numeric(10, 0, asdecimal=False))
    periodname = Column(String(80))
    periodabbreviation = Column(String(3))
    conversioncnt = Column(Numeric(3, 2))
    teacherid = Column(Numeric(10, 0, asdecimal=False))
    teacherfirstname = Column(String(20))
    teachermiddlename = Column(String(20))
    teacherlastname = Column(String(20))
    courseid = Column(Numeric(10, 0, asdecimal=False))
    coursenumber = Column(String(11))
    coursename = Column(String(40))
    sectionid = Column(Numeric(10, 0, asdecimal=False))
    sectionnumber = Column(String(10))
    rectype = Column(String(5), index=True)
    levelreached = Column(Numeric(10, 0, asdecimal=False))
    levelname = Column(String(30))
    semester = Column(Numeric(10, 0, asdecimal=False))
    quarter = Column(Numeric(10, 0, asdecimal=False))
    trimester = Column(Numeric(10, 0, asdecimal=False))
    enrollmentnumber = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("current_date"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("current_date"))
    potential_minutes_attended = Column(Numeric(10, 0, asdecimal=False))
    threshold_period_cnt = Column(Numeric(10, 0, asdecimal=False))
    percent_match = Column(Numeric(10, 0, asdecimal=False))
    atn_month = Column(Numeric(10, 0, asdecimal=False))
    atn_week = Column(Numeric(10, 0, asdecimal=False))
    consecutive_group = Column(Numeric(10, 0, asdecimal=False))
    consecutive_subgroup = Column(Numeric(10, 0, asdecimal=False))


class Unexcusednotify(Base):
    __tablename__ = 'unexcusednotify'
    __table_args__ = (
        Index('ueat_not_n4', 'levelreached', 'levelname'),
    )

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False), index=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    yearid = Column(Numeric(10, 0, asdecimal=False), index=True)
    levelreached = Column(Numeric(10, 0, asdecimal=False))
    levelname = Column(String(30))
    datereached = Column(DateTime, index=True)
    dateextracted = Column(DateTime, index=True)
    datecleared = Column(DateTime, index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("current_date"))
    whomodified = Column(String(100), server_default=text("USER"))
    whenmodified = Column(DateTime, server_default=text("current_date"))


class Unexcusednotifydate(Base):
    __tablename__ = 'unexcusednotifydates'

    unexcusednotifydates_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    unexcused_notify_id = Column(ForeignKey('unexcusednotify.id'), index=True)
    rectype = Column(String(10))
    notifydate = Column(DateTime)

    unexcused_notify = relationship('Unexcusednotify')


class Unexcusednotifydateshist(Base):
    __tablename__ = 'unexcusednotifydateshist'

    unexcusednotifydateshist_id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    unexcused_notify_id = Column(Numeric(10, 0, asdecimal=False))
    rectype = Column(String(10))
    notifydate = Column(DateTime)


t_unexcusednotifyhistory = Table(
    'unexcusednotifyhistory', metadata,
    Column('id', Numeric(10, 0, asdecimal=False), nullable=False, unique=True),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('levelreached', Numeric(10, 0, asdecimal=False)),
    Column('levelname', String(30)),
    Column('datereached', DateTime),
    Column('dateextracted', DateTime),
    Column('datecleared', DateTime),
    Column('whocreated', String(100)),
    Column('whencreated', DateTime),
    Column('whomodified', String(100)),
    Column('whenmodified', DateTime),
    Column('ueat_status', String(1)),
    Column('ueat_status_date', DateTime)
)


class Unschedstudschedlink(Base):
    __tablename__ = 'unschedstudschedlink'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    unschedtermdayperiodslot_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    unscheduledstudent_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    unscheduledteacher_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    unscheduledroom_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    whocreated = Column(String(100), server_default=text("USER"))
    whomodified = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class Unschedtermdayperiodslot(Base):
    __tablename__ = 'unschedtermdayperiodslot'

    dcid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    buildid = Column(Numeric(10, 0, asdecimal=False))
    yearid = Column(Numeric(10, 0, asdecimal=False))
    termcode = Column(String(30))
    termportion = Column(Numeric(10, 0, asdecimal=False))
    day = Column(Numeric(10, 0, asdecimal=False))
    period = Column(Numeric(10, 0, asdecimal=False))
    lastmoddate = Column(DateTime)
    lastmodtime = Column(Numeric(10, 0, asdecimal=False))
    sortorder = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whomodified = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class Unscheduledroom(Base):
    __tablename__ = 'unscheduledroom'

    dcid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    roomnumber = Column(String(10), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    bitmap = Column(LargeBinary)
    lastmoddate = Column(DateTime)
    lastmodtime = Column(Numeric(10, 0, asdecimal=False))
    alwaysfree = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whomodified = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class Unscheduledstudent(Base):
    __tablename__ = 'unscheduledstudent'

    dcid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    studentid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    bitmap = Column(LargeBinary)
    lastmoddate = Column(DateTime)
    lastmodtime = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whomodified = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class Unscheduledteacher(Base):
    __tablename__ = 'unscheduledteacher'

    dcid = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    teacherid = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    bitmap = Column(LargeBinary)
    lastmoddate = Column(DateTime)
    lastmodtime = Column(Numeric(10, 0, asdecimal=False))
    isalwaysfree = Column(Numeric(10, 0, asdecimal=False))
    scheduledbreak = Column(String(7))
    maxinrow = Column(Numeric(10, 0, asdecimal=False))
    whocreated = Column(String(100), server_default=text("USER"))
    whomodified = Column(String(100), server_default=text("USER"))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whenmodified = Column(DateTime, server_default=text("SYSDATE"))


class User(Base):
    __tablename__ = 'users'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    homeschoolid = Column(Numeric(10, 0, asdecimal=False), nullable=False, index=True, server_default=text("0 "))
    lastfirst = Column(String(40), index=True)
    first_name = Column(String(20))
    middle_name = Column(String(20))
    last_name = Column(String(20))
    photo = Column(Numeric(10, 0, asdecimal=False))
    title = Column(String(40))
    homeroom = Column(String(20))
    email_addr = Column(String(50))
    password = Column(String(4000))
    numlogins = Column(Numeric(10, 0, asdecimal=False))
    ipaddrrestrict = Column(Text)
    allowloginstart = Column(Numeric(10, 0, asdecimal=False))
    allowloginend = Column(Numeric(10, 0, asdecimal=False))
    psaccess = Column(Numeric(10, 0, asdecimal=False))
    accessvalue = Column(Text)
    homepage = Column(Text)
    loginid = Column(String(20), index=True)
    defaultstudscrn = Column(Text)
    groupvalue = Column(Numeric(10, 0, asdecimal=False))
    teachernumber = Column(String(20))
    lunch_id = Column(Float, index=True)
    ssn = Column(String(12))
    home_phone = Column(String(20))
    school_phone = Column(String(20))
    street = Column(String(80))
    city = Column(String(40))
    state = Column(String(2))
    zip = Column(String(10))
    periodsavail = Column(String(40))
    powergradepw = Column(String(20))
    canchangeschool = Column(Text)
    teacherloginpw = Column(String(4000))
    nameasimported = Column(String(40))
    teacherloginid = Column(String(20), index=True)
    teacherloginip = Column(Text)
    supportcontact = Column(Numeric(10, 0, asdecimal=False))
    wm_status = Column(String(10))
    wm_statusdate = Column(DateTime)
    wm_tier = Column(Numeric(10, 0, asdecimal=False))
    wm_address = Column(String(70), index=True)
    wm_password = Column(String(20), index=True)
    wm_createdate = Column(DateTime)
    wm_createtime = Column(Numeric(10, 0, asdecimal=False))
    wm_ta_flag = Column(String(3))
    wm_ta_date = Column(DateTime)
    wm_exclude = Column(Numeric(10, 0, asdecimal=False))
    wm_alias = Column(String(70))
    ethnicity = Column(String(20))
    preferredname = Column(String(45))
    lastmeal = Column(String(20))
    staffpers_guid = Column(String(32), index=True)
    adminldapenabled = Column(Numeric(10, 0, asdecimal=False))
    teacherldapenabled = Column(Numeric(10, 0, asdecimal=False))
    sif_stateprid = Column(String(32))
    maximum_load = Column(Numeric(10, 0, asdecimal=False))
    gradebooktype = Column(Numeric(10, 0, asdecimal=False))
    fedethnicity = Column(Numeric(10, 0, asdecimal=False), server_default=text("-1"))
    fedracedecline = Column(Numeric(10, 0, asdecimal=False), server_default=text("0"))
    ptaccess = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    whocreated = Column(String(100), nullable=False, server_default=text("USER "))
    whencreated = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    whomodified = Column(String(100), nullable=False, server_default=text("USER "))
    whenmodified = Column(DateTime, nullable=False, server_default=text("SYSDATE "))
    psguid = Column(String(50), unique=True)


class SUsrCrdcX(User):
    __tablename__ = 's_usr_crdc_x'

    usersdcid = Column(ForeignKey('users.dcid'), primary_key=True)
    certifiedadvmath_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedalgebrai_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedalgebraii_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedbiology_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedcalculus_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedchemistry_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedgeneralmath_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedgeneralscience_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedgeometry_tf = Column(Numeric(1, 0, asdecimal=False))
    certifiedphysics_tf = Column(Numeric(1, 0, asdecimal=False))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class SUsrNceaX(User):
    __tablename__ = 's_usr_ncea_x'

    usersdcid = Column(ForeignKey('users.dcid'), primary_key=True)
    religiousaffiliation = Column(String(1))
    religiousclergylay = Column(String(1))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Userscorefield(User):
    __tablename__ = 'userscorefields'

    usersdcid = Column(ForeignKey('users.dcid'), primary_key=True)
    dob = Column(String(4000))
    gender = Column(String(4000))
    whocreated = Column(String(100))
    whencreated = Column(DateTime, server_default=text("SYSDATE"))
    whomodified = Column(String(100))
    whenmodified = Column(DateTime)


class Utable(Base):
    __tablename__ = 'utable'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False), index=True)
    filenumber = Column(Numeric(10, 0, asdecimal=False), index=True)
    type = Column(String(30))
    name = Column(String(50), index=True)
    noofcolumns = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    width = Column(Float)
    data = Column(Text)
    unused5 = Column(Numeric(10, 0, asdecimal=False))
    unused6 = Column(Numeric(10, 0, asdecimal=False))


t_viewscontrol = Table(
    'viewscontrol', metadata,
    Column('process', String(4)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('starttime', DateTime),
    Column('endtime', DateTime),
    Column('cutoffday', DateTime),
    Column('yearid', Numeric(10, 0, asdecimal=False)),
    Column('rowsprocessed', Numeric(10, 0, asdecimal=False)),
    Index('viewscontrol_idx', 'schoolid', 'process')
)


class Virtualfieldsdef(Base):
    __tablename__ = 'virtualfieldsdef'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    unique_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    linkto_virttabdefid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(30))
    userlabel = Column(String(40))
    type = Column(Numeric(10, 0, asdecimal=False))
    reference = Column(Numeric(10, 0, asdecimal=False))
    description = Column(Text)
    displayinlist = Column(Numeric(10, 0, asdecimal=False))
    displayinpageview = Column(Numeric(10, 0, asdecimal=False))
    accessprivileges = Column(String(20))
    format = Column(String(31))
    popupmenucontents = Column(Text)
    mandatory = Column(Numeric(10, 0, asdecimal=False))
    default_value = Column(String(79))
    orderonentryform = Column(Numeric(10, 0, asdecimal=False))
    minimum_value = Column(String(79))
    maximum_value = Column(String(79))
    maxnbrofchars = Column(Numeric(10, 0, asdecimal=False))
    modifiable = Column(Numeric(10, 0, asdecimal=False))
    kind = Column(String(11))
    display_as = Column(String(11))
    hidefromuser = Column(Numeric(10, 0, asdecimal=False))


class Virtualtablesdatum(Base):
    __tablename__ = 'virtualtablesdata'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    unique_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    linkto_def_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    created_on = Column(DateTime)
    created_by = Column(String(31))
    last_modified = Column(DateTime)
    modified_by = Column(String(31))
    related_to_table = Column(String(31))
    foreignkey = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    foreignkey_alpha = Column(String(31), index=True)
    user_defined_date = Column(DateTime)
    user_defined_date2 = Column(DateTime)
    user_defined_integer = Column(Numeric(10, 0, asdecimal=False))
    user_defined_numeric = Column(Float)
    user_defined_text = Column(String(79))
    user_defined_text2 = Column(String(79))


class Virtualtablesdata2(Base):
    __tablename__ = 'virtualtablesdata2'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    unique_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    linkto_def_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    created_on = Column(DateTime)
    created_by = Column(String(31))
    last_modified = Column(DateTime)
    modified_by = Column(String(31))
    related_to_table = Column(String(31))
    foreignkey = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    foreignkey_alpha = Column(String(31), index=True)
    user_defined_date = Column(DateTime)
    user_defined_date2 = Column(DateTime)
    user_defined_integer = Column(Numeric(10, 0, asdecimal=False))
    user_defined_numeric = Column(Float)
    user_defined_text = Column(String(79))
    user_defined_text2 = Column(String(79))


class Virtualtablesdata3(Base):
    __tablename__ = 'virtualtablesdata3'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    unique_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    linkto_def_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    created_on = Column(DateTime)
    created_by = Column(String(31))
    last_modified = Column(DateTime)
    modified_by = Column(String(31))
    related_to_table = Column(String(31))
    foreignkey = Column(Numeric(10, 0, asdecimal=False), index=True)
    schoolid = Column(Numeric(10, 0, asdecimal=False))
    custom = Column(Text)
    foreignkey_alpha = Column(String(31), index=True)
    user_defined_date = Column(DateTime)
    user_defined_date2 = Column(DateTime)
    user_defined_integer = Column(Numeric(10, 0, asdecimal=False))
    user_defined_numeric = Column(Float)
    user_defined_text = Column(String(79))
    user_defined_text2 = Column(String(79))


class Virtualtablesdef(Base):
    __tablename__ = 'virtualtablesdef'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    unique_id = Column(Numeric(10, 0, asdecimal=False), index=True)
    created_on = Column(DateTime)
    created_by = Column(String(31))
    last_modified = Column(DateTime)
    modified_by = Column(String(31))
    table_name = Column(String(30))
    actualdatatable_ref = Column(Numeric(10, 0, asdecimal=False))
    school_id = Column(Numeric(10, 0, asdecimal=False))
    linkedtotable = Column(String(30))
    linkingfield = Column(String(30))
    kind = Column(String(20))
    includeinlist = Column(Numeric(10, 0, asdecimal=False))
    listpageinfo = Column(String(79))
    inputpageinfo = Column(String(79))
    description = Column(Text)
    accessprivileges = Column(String(20))
    invisible = Column(Numeric(10, 0, asdecimal=False))
    schoolspecific = Column(Numeric(10, 0, asdecimal=False))
    listoption_showindex = Column(Numeric(10, 0, asdecimal=False))
    user_label = Column(String(40))
    listoption_insertlinktopage = Column(Numeric(10, 0, asdecimal=False))
    loadedfrom_filepathonly = Column(Text)
    loadedfrom_filename = Column(String(79))
    loadedfrom_datestamp = Column(String(21))
    dateofimport = Column(DateTime)
    data_can_be_deleted = Column(Numeric(10, 0, asdecimal=False))
    data_can_be_modified = Column(Numeric(10, 0, asdecimal=False))
    data_can_be_added = Column(Numeric(10, 0, asdecimal=False))
    def_sort_fld1 = Column(String(79))
    def_sort_dir1 = Column(Numeric(10, 0, asdecimal=False))
    excludefromlistforexport = Column(Numeric(10, 0, asdecimal=False))
    excludefromlistforimport = Column(Numeric(10, 0, asdecimal=False))
    ismigrated = Column(Numeric(1, 0, asdecimal=False), nullable=False, index=True, server_default=text("0 "))


class V(Base):
    __tablename__ = 'vs'

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(30), index=True)
    value = Column(Text)
    date_value = Column(DateTime)


t_vw_dashboard_lea_localdates = Table(
    'vw_dashboard_lea_localdates', metadata,
    Column('yearid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('reportid', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('report_title', String(100), nullable=False),
    Column('report_subtitle', String(100), nullable=False),
    Column('localstartdate', DateTime),
    Column('localenddate', DateTime)
)


t_vw_dashboard_localdates = Table(
    'vw_dashboard_localdates', metadata,
    Column('schoolid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('yearid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('localid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('localstartdate', DateTime, nullable=False),
    Column('localenddate', DateTime, nullable=False),
    Column('dshstate', String(6))
)


t_vw_dashboard_prefs = Table(
    'vw_dashboard_prefs', metadata,
    Column('dshreportsubmission_id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('dshreportpref_id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('dshreport_id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('prefname', String(100), nullable=False),
    Column('prefvalue', String(100)),
    Column('whocreated', String(100)),
    Column('whencreated', DateTime),
    Column('whomodified', String(100)),
    Column('whenmodified', DateTime)
)


t_vw_dashboard_subparams = Table(
    'vw_dashboard_subparams', metadata,
    Column('id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('dshreportsubmission_id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('param_id', Numeric(19, 0, asdecimal=False), nullable=False),
    Column('param_name', String(255), nullable=False),
    Column('param_type', String(50)),
    Column('param_value', Text),
    Column('whocreated', String(100)),
    Column('whencreated', DateTime),
    Column('whomodified', String(100)),
    Column('whenmodified', DateTime)
)


class Webasmt(Base):
    __tablename__ = 'webasmt'
    __table_args__ = (
        Index('webasmt_u2', 'id', 'dcid', unique=True),
    )

    dcid = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    id = Column(Numeric(10, 0, asdecimal=False))
    sectionid = Column(Numeric(10, 0, asdecimal=False), index=True)
    name = Column(String(50))
    abbrev = Column(String(15))
    description = Column(Text)
    ptsposs = Column(Numeric(10, 0, asdecimal=False))
    categoryid = Column(Numeric(10, 0, asdecimal=False))
    duedate = Column(DateTime)
    transferred = Column(Numeric(10, 0, asdecimal=False))
    scores = Column(LargeBinary)
    standard = Column(Text)
    distcoursenumber = Column(String(11))
    distcategory = Column(String(60))
    weight = Column(Float)


t_z_activity_info = Table(
    'z_activity_info', metadata,
    Column('name', String(50)),
    Column('budget_code', String(79))
)


t_z_admissionexporttemplate = Table(
    'z_admissionexporttemplate', metadata,
    Column('id', Text),
    Column('templatename', String(50)),
    Column('fldid', Numeric(asdecimal=False))
)


t_z_amortization_detail = Table(
    'z_amortization_detail', metadata,
    Column('studentid', String(50)),
    Column('enroll_status', Numeric(10, 0, asdecimal=False)),
    Column('fee_category_name', String(50)),
    Column('yearcd', String(10)),
    Column('term0', Numeric(10, 2)),
    Column('term1', Numeric(10, 2)),
    Column('term2', Numeric(10, 2)),
    Column('jan', Numeric(10, 2)),
    Column('feb', Numeric(10, 2)),
    Column('mar', Numeric(10, 2)),
    Column('apr', Numeric(10, 2)),
    Column('may', Numeric(10, 2)),
    Column('jun', Numeric(10, 2)),
    Column('jul', Numeric(10, 2)),
    Column('aug', Numeric(10, 2)),
    Column('sep', Numeric(10, 2)),
    Column('oct', Numeric(10, 2)),
    Column('nov', Numeric(10, 2)),
    Column('dec', Numeric(10, 2))
)


t_z_amortization_detail1 = Table(
    'z_amortization_detail1', metadata,
    Column('studentid', String(50)),
    Column('enroll_status', Numeric(10, 0, asdecimal=False)),
    Column('fee_category_name', String(50)),
    Column('yearcd', String(10)),
    Column('term0', Numeric(10, 2)),
    Column('term1', Numeric(10, 2)),
    Column('term2', Numeric(10, 2)),
    Column('jan', Numeric(10, 2)),
    Column('feb', Numeric(10, 2)),
    Column('mar', Numeric(10, 2)),
    Column('apr', Numeric(10, 2)),
    Column('may', Numeric(10, 2)),
    Column('jun', Numeric(10, 2)),
    Column('jul', Numeric(10, 2)),
    Column('aug', Numeric(10, 2)),
    Column('sep', Numeric(10, 2)),
    Column('oct', Numeric(10, 2)),
    Column('nov', Numeric(10, 2)),
    Column('dec', Numeric(10, 2))
)


t_z_amortization_detail_new = Table(
    'z_amortization_detail_new', metadata,
    Column('studentid', String(50)),
    Column('enroll_status', Numeric(10, 0, asdecimal=False)),
    Column('fee_category_name', String(50)),
    Column('yearcd', String(10)),
    Column('term0', Numeric(10, 2)),
    Column('term1', Numeric(10, 2)),
    Column('term2', Numeric(10, 2)),
    Column('jan', Numeric(10, 2)),
    Column('feb', Numeric(10, 2)),
    Column('mar', Numeric(10, 2)),
    Column('apr', Numeric(10, 2)),
    Column('may', Numeric(10, 2)),
    Column('jun', Numeric(10, 2)),
    Column('jul', Numeric(10, 2)),
    Column('aug', Numeric(10, 2)),
    Column('sep', Numeric(10, 2)),
    Column('oct', Numeric(10, 2)),
    Column('nov', Numeric(10, 2)),
    Column('dec', Numeric(10, 2)),
    Column('ys_flag', String(1))
)


t_z_bank_refund = Table(
    'z_bank_refund', metadata,
    Column('id', Numeric(11, 0, asdecimal=False)),
    Column('bankname', String(30)),
    Column('bankbranchname', String(150)),
    Column('bankcardnumber', String(30)),
    Column('cardholdername', String(50))
)


t_z_bank_refund_fee = Table(
    'z_bank_refund_fee', metadata,
    Column('id', Numeric(11, 0, asdecimal=False)),
    Column('bankid', Numeric(15, 0, asdecimal=False)),
    Column('feerefnbr', String(100))
)


class ZBusinfo(Base):
    __tablename__ = 'z_businfo'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    busnumber = Column(Numeric(asdecimal=False))
    busassis = Column(String(50))
    assitmp = Column(String(50))


class ZBusstopinfo(Base):
    __tablename__ = 'z_busstopinfo'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    busid = Column(Numeric(asdecimal=False))
    compoundcn = Column(String(50))
    compounden = Column(String(50))
    streetcn = Column(String(100))
    streeten = Column(String(100))
    pickup = Column(String(10))
    _return = Column('return', String(10))


t_z_create_fee_log = Table(
    'z_create_fee_log', metadata,
    Column('studentnumber', String(20)),
    Column('fee_name', String(100)),
    Column('fee_amount', String(20)),
    Column('createdate', DateTime),
    Column('is_success', String(4)),
    Column('reason', String(300)),
    Column('id', Numeric(20, 0, asdecimal=False))
)


t_z_ebs_if_log = Table(
    'z_ebs_if_log', metadata,
    Column('data_date', DateTime),
    Column('tuitiontransportation', String(1)),
    Column('activity', String(1)),
    Column('othertype', String(1)),
    Column('refund', String(1)),
    Column('ar', String(1)),
    Column('al', String(1))
)


t_z_fee_cash_bank_detail = Table(
    'z_fee_cash_bank_detail', metadata,
    Column('feeid', Numeric(10, 0, asdecimal=False)),
    Column('creationdate', DateTime),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('fee_type_id', Numeric(10, 0, asdecimal=False)),
    Column('fee_type_name', String(79)),
    Column('fee_category_name', String(21)),
    Column('term', String(79)),
    Column('fee_amount', Float),
    Column('fee_balance', Float),
    Column('fee_paid', Float),
    Column('cash_bank_income', Numeric(asdecimal=False)),
    Column('cash_bank_refund', Numeric(asdecimal=False)),
    Column('net_fee_amount', Numeric(asdecimal=False)),
    Column('net_fee_received', Numeric(asdecimal=False))
)


t_z_fee_cash_bank_detail2 = Table(
    'z_fee_cash_bank_detail2', metadata,
    Column('feeid', Numeric(10, 0, asdecimal=False)),
    Column('creationdate', DateTime),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('fee_type_id', Numeric(10, 0, asdecimal=False)),
    Column('fee_type_name', String(79)),
    Column('fee_category_name', String(21)),
    Column('term', String(79)),
    Column('fee_amount', Float),
    Column('fee_balance', Float),
    Column('fee_paid', Float),
    Column('cash_bank_income_ys', Numeric(asdecimal=False)),
    Column('cash_bank_refund', Numeric(asdecimal=False)),
    Column('cash_bank_refund_ys', Numeric(asdecimal=False)),
    Column('cash_bank_income', Numeric(asdecimal=False))
)


t_z_fee_trans_vouchernumber = Table(
    'z_fee_trans_vouchernumber', metadata,
    Column('id', Numeric(20, 0, asdecimal=False)),
    Column('serial_number', String(20)),
    Column('voucher_number', String(200))
)


t_z_fee_us_amount = Table(
    'z_fee_us_amount', metadata,
    Column('id', Numeric(asdecimal=False)),
    Column('serialnumber', String(20)),
    Column('studentid', String(20)),
    Column('feeid', String(20)),
    Column('amount', Float),
    Column('isinsert', String(2)),
    Column('reason', String(1000)),
    Column('method', String(50)),
    Column('type', String(500)),
    Column('createdate', DateTime)
)


t_z_finance_report = Table(
    'z_finance_report', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('created_on', DateTime),
    Column('reportname', String(100)),
    Column('success', String(10)),
    Column('reason', String(300)),
    Column('realallname', String(150)),
    Column('log1', String(300)),
    Column('log2', String(300)),
    Column('log3', String(300))
)


t_z_generate_fee_log = Table(
    'z_generate_fee_log', metadata,
    Column('run_seq_id', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('fee_type_id', String(10)),
    Column('amount', Float),
    Column('is_insert', String(1)),
    Column('reason', String(1000))
)


t_z_import_school_fee = Table(
    'z_import_school_fee', metadata,
    Column('student_number', Numeric(15, 0, asdecimal=False)),
    Column('fee_type_name', String(100)),
    Column('amount', Numeric(20, 2)),
    Column('paid', Numeric(20, 2)),
    Column('term', String(50)),
    Column('result', String(50))
)


t_z_inventory_stuinfo_log = Table(
    'z_inventory_stuinfo_log', metadata,
    Column('rundate', DateTime),
    Column('logtype', String(30)),
    Column('result', String(10)),
    Column('reason', String(150)),
    Column('statistics', String(150))
)


t_z_overpayment_cash_bank_detail = Table(
    'z_overpayment_cash_bank_detail', metadata,
    Column('feeid', Numeric(10, 0, asdecimal=False)),
    Column('creationdate', DateTime),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('fee_type_id', Numeric(10, 0, asdecimal=False)),
    Column('fee_type_name', String(79)),
    Column('fee_category_name', String(21)),
    Column('fee_amount', Float),
    Column('fee_balance', Float),
    Column('fee_paid', Float),
    Column('cash_bank_refund', Numeric(asdecimal=False)),
    Column('net_fee_amount', Numeric(asdecimal=False))
)


t_z_pay_fee_log = Table(
    'z_pay_fee_log', metadata,
    Column('pay_ref_nbr', String(20)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('fee_id', Numeric(10, 0, asdecimal=False)),
    Column('amount', Float),
    Column('is_insert', String(1)),
    Column('reason', String(1000))
)


t_z_paymentmethod_view = Table(
    'z_paymentmethod_view', metadata,
    Column('code', String(40)),
    Column('dscr', String(50))
)


t_z_staff_paymentmethod = Table(
    'z_staff_paymentmethod', metadata,
    Column('dcid', Numeric(10, 0, asdecimal=False), nullable=False),
    Column('staff_id', Numeric(10, 0, asdecimal=False)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('lastfirst', String(40)),
    Column('teachernumber', String(20)),
    Column('payment_method_id', String(79)),
    Column('pmdesc', String(50))
)


t_z_student_fee_discount_info = Table(
    'z_student_fee_discount_info', metadata,
    Column('student_id', Numeric(10, 0, asdecimal=False)),
    Column('student_number', Float),
    Column('student_name', String(135)),
    Column('grade_level', Numeric(10, 0, asdecimal=False)),
    Column('tuition', Float),
    Column('tuition_discount_rate', Float),
    Column('tuition_price_after_discount', Float),
    Column('tuition_discount_type', String(100)),
    Column('starting_school_date', DateTime),
    Column('term', Numeric(4, 0, asdecimal=False)),
    Column('operational_date', DateTime),
    Column('operational_person', String(100)),
    Column('void_flag', String(1)),
    Column('manual_operation_flag', String(1)),
    Column('bus_fee', Float),
    Column('bus_fee_discount_rate', Float),
    Column('bus_fee_price_after_discount', Float),
    Column('bus_fee_disount_type', String(100)),
    Column('lodging_fee', Float),
    Column('lodging_fee_discount_rate', Float),
    Column('lodging_fee_price_discount', Float),
    Column('lodging_fee_disount_type', String(100))
)


t_z_student_report = Table(
    'z_student_report', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('created_on', DateTime),
    Column('last_modified', DateTime),
    Column('fromdt', DateTime),
    Column('reportname', String(100)),
    Column('reporttype', String(20)),
    Column('success', String(10)),
    Column('realallname', String(150)),
    Column('reason', String(300)),
    Column('todt', DateTime)
)


t_z_student_transactions = Table(
    'z_student_transactions', metadata,
    Column('id', Numeric(10, 0, asdecimal=False)),
    Column('studentid', Numeric(10, 0, asdecimal=False)),
    Column('student_number', Float),
    Column('home_room', String(60)),
    Column('student_name', String(135)),
    Column('schoolid', Numeric(10, 0, asdecimal=False)),
    Column('school_name', String(60)),
    Column('department', String(4000)),
    Column('feeid', Numeric(10, 0, asdecimal=False)),
    Column('fee_type', String(79)),
    Column('fee_category_name', String(21)),
    Column('date_value', DateTime),
    Column('amount', Float),
    Column('transaction_type', String(13)),
    Column('payment_method_id', String(40)),
    Column('payment_method', String(50)),
    Column('operator_id', Numeric(10, 0, asdecimal=False)),
    Column('operator_name', String(40)),
    Column('description', String(79)),
    Column('payment_ref_nbr', String(79)),
    Column('refund_to_fee_type', String(79)),
    Column('refund_to_fee_category_name', String(21)),
    Column('usd_amount', Float),
    Column('payment_method_code', String(40))
)


t_z_sync_teacher_log = Table(
    'z_sync_teacher_log', metadata,
    Column('run_seq_id', Numeric(10, 0, asdecimal=False)),
    Column('sync_teachernumber', String(20)),
    Column('sync_type', String(100)),
    Column('sync_success', String(10)),
    Column('sync_reason', String(500)),
    Column('sync_time', DateTime),
    Column('sync_teachername', String(100))
)


t_z_term_period_view = Table(
    'z_term_period_view', metadata,
    Column('term', Numeric(asdecimal=False)),
    Column('pre_vacation_start_date', DateTime),
    Column('term_start_date', DateTime),
    Column('term_end_date', DateTime),
    Column('post_vacation_end_date', DateTime)
)


t_z_term_view = Table(
    'z_term_view', metadata,
    Column('term_code', Numeric(10, 0, asdecimal=False)),
    Column('term_des', String(37)),
    Column('schoolid', Numeric(10, 0, asdecimal=False))
)


t_z_termcd_mapping_view = Table(
    'z_termcd_mapping_view', metadata,
    Column('term_cd', String(40)),
    Column('term_cd_ebs', String(40))
)


class ZTourfollowup(Base):
    __tablename__ = 'z_tourfollowup'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    followupdt = Column(DateTime)
    followupcomment = Column(String(200))
    studid = Column(Numeric(10, 0, asdecimal=False))


class ZTourgiven(Base):
    __tablename__ = 'z_tourgiven'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    givenby = Column(String(100))
    tourdt = Column(DateTime)
    studid = Column(Numeric(10, 0, asdecimal=False))


class ZVoidRefund(Base):
    __tablename__ = 'z_void_refund'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    payment_ref_nbr = Column(String(79))
    feeid = Column(Numeric(10, 0, asdecimal=False))
