"""
Script for syncing Altair with Vegalite
"""
import os
import shutil
import json
from contextlib import contextmanager

import git  # pip install gitpython


def abspath(*args):
    """Get absolute path relative to this file"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))


DEFAULT_TAG = 'v1.0.8'
VEGALITE_PATH = abspath('repos', 'vega-lite')


@contextmanager
def vegalite_tag(tag, vegalite_repo,
                 url='https://github.com/vega/vega-lite.git'):
    repo_dir = os.path.abspath(os.path.join(vegalite_repo, '..'))
    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)

    if not os.path.exists(vegalite_repo):
        print('cloning {0}'.format(url))
        vegalite = git.Repo.clone_from(url, vegalite_repo)
    else:
        vegalite = git.Repo(vegalite_repo)
        vegalite.branches.master.checkout()
        vegalite.remotes.origin.pull()

    if tag not in vegalite.tags:
        raise ValueError("Tag='{0}' is not valid. Options are:\n{1}"
                        "".format(tag, list(map(str, vegalite.tags))))

    print("Using tag='{0}'".format(tag))
    vegalite.git.checkout('tags/{0}'.format(tag))
    try:
        yield
    finally:
        vegalite.branches.master.checkout()


def sync_schema(vegalite_repo,
                filename='vega-lite-schema.json',
                destination=abspath('..', 'altair', 'schema')):
    source = os.path.join(vegalite_repo, filename)
    destination = os.path.join(destination, filename)
    print("Copying Vega-Lite Schema:")
    print("  Source:     ", source)
    print("  Destination:", destination)
    shutil.copyfile(source, destination)


def sync_examples(vegalite_repo,
                  destination=abspath('..', 'altair', 'examples', 'json'),
                  data_url='http://vega.github.io/vega-lite/'):
    source_dir = os.path.join(vegalite_repo, 'examples', 'specs')
    print("Reading from {0}".format(source_dir))
    if not os.path.exists(source_dir):
        raise ValueError("{0} does not exist".format(source_dir))
    if not os.path.exists(destination):
        raise ValueError("{0} does not exist".format(destination))

    # remove old files before syncing
    for example in os.listdir(destination):
        if os.path.splitext(example)[1] == '.json':
            os.remove(os.path.join(destination, example))

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination, filename)

        print(source_file)
        with open(source_file) as f:
            spec = json.load(f)

        # Adjust to use absolute URLs
        try:
            url = spec['data']['url']
            if url.startswith('data/'):
                spec['data']['url'] = data_url + url
        except KeyError:
            continue

        print(" -> {0}".format(destination_file))
        with open(destination_file, 'w') as f:
            json.dump(spec, f, indent=4, sort_keys=True)

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Sync Vega-Lite Schema')
    parser.add_argument('-t', '--tag', default=DEFAULT_TAG,
                        help='Version tag to use')
    parser.add_argument('-e', '--examples', action='store_true',
                        help='Sync the Vega-Lite examples')
    parser.add_argument('-s', '--schema', action='store_true',
                        help='Sync the Vega-Lite schema')

    args = parser.parse_args()

    if not (args.examples or args.schema):
        parser.print_help()

    if args.schema:
        with vegalite_tag(args.tag, VEGALITE_PATH):
            sync_schema(VEGALITE_PATH)

    if args.examples:
        with vegalite_tag(args.tag, VEGALITE_PATH):
            sync_examples(VEGALITE_PATH)


if __name__ == '__main__':
    main()
