"""
Global Name Space
Simple way to have global variables defined, used throughout the app
Reads in settings.ini and provides logging as well

"""

import contextlib, os, logging
import configparser
import datetime
import click
import inspect
import functools
import pprint

class GNS(object):
    def __init__(self, *args, **kwargs):
        self.COLON = ':'
        self.CLN = ':'
        self.COMMA = ','
        self.CMMA = ','
        self.SEMICOLON = ';'
        self.NEWLINE = '\n'
        self.NWLNE = '\n'
        self.SPACE = ' '
        self.SPCE = ' '
        self.TAB = '\t'
        self.TB = '\t'
        self.SLASH = '/'
        self.LPARENS = '('
        self.RPARENS = ')'
        self.AT = '@'

        # Useful regexp phrases
        self.DOT = '.'
        self.ASTER = '*'

        self._tutorial_id = 0

        # Now, create namespaces associated with setting.ini and config

        self.set_namespace('config')
        self.set_namespace('config.paths')

        self.config.paths.home = os.sep.join(os.path.realpath(__file__).split(os.sep)[:-2]) + os.sep
        self.config.paths.settings_dir = self.config.paths.home + '/settings/'
        self.config.paths.settings_ini = self.config.paths.settings_dir + 'settings.ini'
        settings = configparser.ConfigParser()
        results = settings.read(self.config.paths.settings_ini)
        if not settings.sections():
            # If no settings file or a file without settings, we should exit early
            print("No sections named, is there any legit file at {}?".format(self.config.paths.settings_ini))
            exit()

        if 'META' in settings.sections() and 'secrets' in settings['META']:
            meta_settings = configparser.ConfigParser()
            meta_settings.read(self.config.paths.settings_dir + settings['META']['secrets'])
            for SECTION in [s for s in meta_settings.sections()]:
                section = SECTION.lower()
                self.set_namespace(f'config.{section}')
                for OPTION in meta_settings.options(SECTION):
                    option = OPTION.lower()
                    value = meta_settings.get(SECTION, OPTION)
                    setattr(getattr(self.config, section), option, self.pythonize(value))

        for SECTION in [s for s in settings.sections()]:
            section = SECTION.lower()
            self.set_namespace('config.{}'.format(section))
            for OPTION in settings.options(SECTION):
                option = OPTION.lower()
                value = settings.get(SECTION, OPTION)
                setattr(getattr(self.config, section), option, self.pythonize(value))

        path_to_logging = self('{config.paths.logging}/{date}', date=datetime.datetime.now().strftime('%x--%X').replace('/', '-'))
        #used to keep this in a file, let's just set it up right, shall we?
        log_level = self.config.logging.log_level
        numeric_level = getattr(logging, log_level.upper())
        if numeric_level is None:
            raise ValueError('Invalid log level: {}'.format(loglevel))

        logging.basicConfig(filename=path_to_logging, filemode='a+', level=numeric_level)

        if hasattr(sys.stdout, 'isatty') and sys.stdout.isatty():
            # running with an attached terminal, automatically
            # set stdout debugging to full verbosity
            root = logging.getLogger()
            stdout_level = logging.DEBUG
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setLevel(logging.INFO)
            root.addHandler(stdout_handler)


    @staticmethod
    def pythonize(value):
        if isinstance(value, str) or isinstance(value, unicode):
            return {
                'true':True, 'false':False, 
                'on':True, 'off':False, 
                'yes':True, 'no':False
                }.get(value.lower().strip(), value)
        return value

    @property
    def dict_not_underscore_not_upper(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_') and not key.isupper()}

    def set_namespace(self, ns):
        if not '.' in ns:
            setattr(self, ns, type(ns, (), {}))
        else:
            class_name = []
            prev_class = self
            for inner in ns.split('.'):
                class_name.append(inner)
                if not hasattr(prev_class, inner):
                    setattr(prev_class, inner, type(".".join(class_name), (), {}))
                prev_class = getattr(prev_class, inner)

    def new(self):
        for key in self.dict_not_underscore_not_upper:
            del self.__dict__[key]

    @property
    def dict_from_dict(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}

    def __call__(self, *args, **kwargs):
        d = self.dict_from_dict
        d.update(kwargs)
        return ''.join(args).format(**d)

    @classmethod
    def string(cls, astring, *args, **kwargs):
        for arg in args:
            kwargs.update(arg.__dict__)
        return cls(*args, **kwargs)(astring)

    def get(self, path, default=None, required=True):
        me = self
        for inner in path.split('.'):
            if not hasattr(me, inner):
                if required:
                    raise TypeError(self('This app requires a setting for {path}', path=path))
                return default
            else:
                me = getattr(me, inner)
        return me

    @property
    def kwargs(self):
        return {key: value for key, value in self.__dict__.items() if key.islower() and not key.startswith('_')}

    @property
    def declared_kwargs(self):
        return {key: value for key, value in self.__dict__.items() if key.islower() and not key.startswith('_')}

    def __repr__(self):
        """
        VERY MEAGER WAY TO OUTPUT THIS DATA
        """
        return str(self.dict_not_underscore_not_upper)

import sys
sys.modules['gns'] = GNS()
