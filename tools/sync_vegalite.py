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


VEGALITE_TAG = 'v1.2.0'
VEGALITE_PATH = abspath('repos', 'vega-lite')
VEGALITE_URL = 'https://github.com/vega/vega-lite.git'

VEGA_DATA_TAG = 'v1.8.0'
VEGA_DATA_PATH = abspath('repos', 'vega-datasets')
VEGA_DATA_URL = 'https://github.com/vega/vega-datasets.git'

VEGALITE_VERSION_FILE = """
# Automatically written by tools/sync_vegalite.py
# Do not modify this manually
vegalite_version = '{version}'
"""


@contextmanager
def checkout_tag(tag, local_repo, url):
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


def sync_schema(vegalite_repo, version,
                filename='vega-lite-schema.json',
                destination=abspath('..', 'altair', 'schema')):
    versionfile = os.path.join(destination, '_vegalite_version.py')
    with open(versionfile, 'w') as f:
        f.write(VEGALITE_VERSION_FILE.format(version=version))

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
    index_source = os.path.join(vegalite_repo, 'examples', 'vl-examples.json')
    print("Reading from {0}".format(source_dir))
    if not os.path.exists(source_dir):
        raise ValueError("{0} does not exist".format(source_dir))
    if not os.path.exists(destination):
        raise ValueError("{0} does not exist".format(destination))

    # remove old files before syncing
    for example in os.listdir(destination):
        if os.path.splitext(example)[1] == '.json':
            os.remove(os.path.join(destination, example))

    # sync the index
    listingfile = abspath(destination, '..', 'example-listing.json')
    with open(index_source) as f:
        with open(listingfile, 'w') as of:
            of.write(f.read())

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


def sync_datasets(datasets_repo,
                  filename='datasets.json',
                  destination=abspath('..', 'altair', 'datasets')):
    sourcedir = os.path.join(datasets_repo, 'data')
    datasets_dict = {}
    for dataset in os.listdir(sourcedir):
        root, ext = os.path.splitext(dataset)
        ext = ext.lstrip('.')
        if ext in ['json', 'csv']:
            datasets_dict[root] = {'filename': dataset, 'format': ext}

    outfile = os.path.join(destination, filename)
    print("Writing datasets dict to {0}".format(outfile))
    with open(outfile, 'w') as f:
        f.write(json.dumps(datasets_dict, indent=2, sort_keys=True))


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Sync Vega-Lite Schema')
    parser.add_argument('-t', '--tag', default=None,
                        help='Version tag to use')
    parser.add_argument('-e', '--examples', action='store_true',
                        help='Sync examples from github.com/vega/vega-lite')
    parser.add_argument('-s', '--schema', action='store_true',
                        help='Sync schema from github.com/vega/vega-lite')
    parser.add_argument('-d', '--datasets', action='store_true',
                        help='Sync datasets from github.com/vega/vega-datasets')

    args = parser.parse_args()

    if not (args.examples or args.schema or args.datasets):
        parser.print_help()

    if args.schema:
        tag = args.tag or VEGALITE_TAG
        with checkout_tag(tag, VEGALITE_PATH, VEGALITE_URL):
            sync_schema(VEGALITE_PATH, tag.strip('v'))

    if args.examples:
        tag = args.tag or VEGALITE_TAG
        with checkout_tag(tag, VEGALITE_PATH, VEGALITE_URL):
            sync_examples(VEGALITE_PATH)

    if args.datasets:
        tag = args.tag or VEGA_DATA_TAG
        with checkout_tag(tag, VEGA_DATA_PATH, VEGA_DATA_URL):
            sync_datasets(VEGA_DATA_PATH)


if __name__ == '__main__':
    main()
