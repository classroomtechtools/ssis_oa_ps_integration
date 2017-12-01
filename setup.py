from distutils.core import setup
setup(
    name = "SSIS OpenApply PowerSchool Syncer",
    version = "0.5",
    description = "",
    author = "Adam Morris",
    author_email = "classroomtechtools.ctt@gmail.com",
    keywords = [],
    packages=['cli', 'app', 'gns'],
    entry_points='''
        [console_scripts]
        ssis_oaps_syncer=cli.main:main
    ''',
    install_requires = ['click', 'sqlalchemy',
    'python-dateutil',
    'aiohttp', 'cchardet', 'aiodns', 'aiofiles', 'uvloop',
    'cx_Oracle'
    ],

    long_description = """\
TODO: DESCRIBE THIS!


"""
)
