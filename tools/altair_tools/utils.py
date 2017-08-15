import os
import subprocess
from contextlib import contextmanager

import git  # pip install gitpython


try:
    from urllib.request import urlopen
except ImportError:
    # Python 2.X
    from urllib2 import urlopen


ALTAIR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           '..', '..', 'altair'))


def path_within_altair(*args):
    return os.path.join(ALTAIR_PATH, *args)


def get_git_commit_info():
    """Return a string describing the git version information"""
    try:
        label = subprocess.check_output(["git", "describe"]).decode().strip()
    except subprocess.CalledProcessError:
        label = "<unavailable>"
    return label


@contextmanager
def checkout_tag(tag, local_repo, url):
    """Temporarily check-out a particular tag in a github repo"""
    repo_dir = os.path.abspath(os.path.join(local_repo, '..'))
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)

    if not os.path.exists(local_repo):
        print('cloning {0}'.format(url))
        vegalite = git.Repo.clone_from(url, local_repo)
    else:
        vegalite = git.Repo(local_repo)
        vegalite.branches[0].checkout()
        vegalite.remotes.origin.pull()

    if tag not in vegalite.tags:
        raise ValueError("Tag='{0}' is not valid. Options are:\n{1}"
                        "".format(tag, list(map(str, vegalite.tags))))

    print("Using tag='{0}'".format(tag))
    vegalite.git.checkout('tags/{0}'.format(tag))
    try:
        yield
    finally:
        vegalite.branches[0].checkout()
