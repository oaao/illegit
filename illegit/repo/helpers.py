import configparser # to read and write Git's .ini-like config file format
import os

from . import objects


def repo_path(repo, *path):
    """ Compose the path under repository's Git dir """
    return os.path.join(repo.git_dir, *path)


def repo_dir(repo, *path, mkdir=False):
    """ Similar to repo_path(), but create a new directory *path if mkdir """

    path = repo_path(repo, *path)

    if os.path.exists(path):
        if (os.path.isdir(path)):
            return path
        else:
            raise Exception(f"{path} is not a directory.")

    if mkdir:
        os.makedirs(path)
        return path
    #else:
    #    return None

def repo_create(path):
    """ Create a new repository at path """

    repo = objects.Repository(path, force=True)

    # begin by ensuring path is either nonexistent or empty
    if os.path.exists(repo.working_tree):
        if not os.path.isdir(repo.working_tree):
            raise Exception(f"{path} is not a directory.")
        if os.listdir(repo.working_tree):
            raise Exception(f"{path} is not empty.")
    else:
        os.makedirs(repo.working_tree)

    assert(repo_dir(repo, 'branches',      mkdir=True))
    assert(repo_dir(repo, 'objects',       mkdir = True))
    assert(repo_dir(repo, 'refs', 'tags',  mkdir=True))
    assert(repo_dir(repo, 'refs', 'heads', mkdir=True))

    # creating a .git/description
    with open(repo_file(repo, 'description'), 'w') as f:
        f.write(
            'Repository unnamed; edit this file ("description") to name it.\n'
        )

    # creating .git/HEAD
    with open(repo_file(repo, 'HEAD'), 'w') as f:
        f.write('ref: refs/heads/master\n')

    # creating .git/config
    with open(repo_file(repo, 'config'), 'w') as f:
        config = repo_default_config()
        config.write(f)

    return repo

def repo_default_config():
    cp = configparser.ConfigParser()

    cp.add_section('core')

    # git_dir format; 0 is initial format, 1 initial with extensions
    # >1 means git panics; illegit acceps 0 only
    cp.set('core', 'repository_format_version', '0')

    # filemode=false disables tracking of file mode changes in working_tree
    cp.set('core', 'filemode', 'false')

    # bare=false means repository has a working tree
    # 'real' git supports an optional 'worktree' key
    # indicating location if not '..'
    cp.set('core', 'bare', 'false')

    return cp
