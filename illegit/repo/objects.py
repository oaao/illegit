import configparser # to read and write Git's .ini-like config file format
import os

from . import helpers

class Repository:
    """ Git repository object """

    working_tree = None
    git_dir      = None
    config       = None

    def __init__(self, path, force=False):

        self.working_tree = path
        self.git_dir      = os.path.join(path, '.git')

        if not (force or os.path.isdir(self.git_dir)):
            raise Exception(f'No Git repository at: {path}')

        # read .git/config file
        self.config = configparser.ConfigParser()
        cfg         = helpers.repo_file(self, 'config')

        if cfg and os.path.exists(cfg):
            self.config.read([cfg])
        elif not force:
            raise Exception('Missing config file')

        if not force:
            version = int(self.config.get('core', 'repository_format_version'))
            if version != 0:
                raise Exception(
                    f'Unsupported repository format version: {version}'
                )
