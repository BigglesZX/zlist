''' The canonical package version '''
__version_info__ = ('2', '0', '1')
__version__ = '.'.join(__version_info__)


def get_version():
    ''' Return the package version as a string, e.g. for use in setup.py '''
    return __version__
