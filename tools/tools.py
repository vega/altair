import os
from contextlib import contextmanager


DEFAULT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'repos'))
DEFAULT_SITE = 'https://github.com/'


@contextmanager
def execute_in(directory):
    current = os.getcwd()
    os.chdir(directory)
    try:
        yield
    finally:
        os.chdir(current)


class GitRepo(object):
    def __init__(self, repo, org='vega', path=DEFAULT_PATH, site=DEFAULT_SITE):
        self.repo = repo
        self.org = org
        self.path = path
        self.site = site
        self.currentdir = os.getcwd()

    @property
    def git_address(self):
        return "{0}{1}/{2}.git".format(self.site, self.org, self.repo)

    @property
    def repopath(self):
        return os.path.join(self.path, self.repo)

    def clone(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        with execute_in(self.path):
            if os.path.exists(self.repo):
                print("Found existing repo at {0}".format(self.repo))
            else:
                print("git clone {0}".format(self.git_address))
                os.system('git clone {0}'.format(self.git_address))
        return self

    def update(self):
        with execute_in(self.repopath):
            os.system('git checkout master')
            os.system('git pull')
        return self

    def checkout_branch(self, branch):
        with execute_in(self.repopath):
            os.system('git checkout {0}'.format(branch))
        return self

    def checkout_tag(self, tag):
        with execute_in(self.repopath):
            os.system('git checkout tags/{0}'.format(tag))
        return self


vegalite = GitRepo('vega-lite')
vegalite.clone().update()
vegalite.checkout_tag('v1.0.9')
