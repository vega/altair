"""
Script for syncing Altair with Vegalite
"""
import os
import shutil
import json
from contextlib import contextmanager

import git  # pip install gitpython

try:
    from urllib.request import urlopen
except ImportError:
    # Python 2.X
    from urllib2 import urlopen


def abspath(*args):
    """Get absolute path relative to this file"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))


SCHEMA_URL = "https://vega.github.io/schema/{library}/{version}.json"

VEGALITE_VERSION = 'v2.0.0-beta.11'
VEGA_VERSION = 'v2.6.5'
VEGALITE_PATH = abspath('repos', 'vega-lite')
VEGALITE_URL = 'https://github.com/vega/vega-lite.git'

VEGA_DATA_VERSION = 'v1.8.0'
VEGA_DATA_PATH = abspath('repos', 'vega-datasets')
VEGA_DATA_URL = 'https://github.com/vega/vega-datasets.git'

VERSION_FILE = """# Automatically written by tools/sync_vegalite.py
# Do not modify this manually
vegalite_version = '{vegalite_version}'
vegalite_schema_url = '{vegalite_schema_url}'
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


def sync_schema(vegalite_version,
                destination=abspath('..', 'altair', 'schema'),
                schema_filename='vega-lite-schema.json'):
    vegalite_schema_url = SCHEMA_URL.format(library='vega-lite',
                                            version=vegalite_version)

    version_file_path = os.path.join(destination, '_vegalite_version.py')
    version_file_content = VERSION_FILE.format(
                                    vegalite_version=vegalite_version,
                                    vegalite_schema_url=vegalite_schema_url)
    print("Writing version info")
    print(" Filename: {0}".format(version_file_path))
    with open(version_file_path, 'w') as f:
        f.write(version_file_content)

    schema_destination = os.path.join(destination, schema_filename)
    print("Downloading Vega-Lite {0} Schema".format(vegalite_version))
    print(" Source:      {0}".format(vegalite_schema_url))
    print(" Destination: {0}".format(schema_destination))
    with urlopen(vegalite_schema_url) as source:
        with open(schema_destination, 'wb') as dest:
            dest.write(source.read())


def sync_examples(vegalite_repo,
                  destination=abspath('..', 'altair', 'examples', 'json'),
                  data_url='http://vega.github.io/vega-lite/'):
    source_dir = os.path.join(vegalite_repo, 'examples', 'specs')
    index_source = os.path.join(vegalite_repo, '_data', 'examples.json')
    print("Reading from {0}".format(source_dir))
    if not os.path.exists(source_dir):
        raise ValueError("{0} does not exist".format(source_dir))
    if not os.path.exists(destination):
        raise ValueError("{0} does not exist".format(destination))

    # sync the index
    listingfile = abspath(destination, '..', 'example-listing.json')
    with open(index_source) as f:
        with open(listingfile, 'w') as of:
            of.write(f.read())

    # remove old files before syncing
    shutil.rmtree(destination)


    def make_data_urls_absolute(spec, root_data_url):
        """Modify spec in-place, making all data urls absolute"""
        for key, subspec in spec.items():
            if key == 'data':
                url = subspec.get('url', '')
                if url.startswith('data/'):
                    subspec['url'] = root_data_url + url
            if isinstance(subspec, dict):
                make_data_urls_absolute(subspec, root_data_url=root_data_url)
        return spec


    def copy_tree_and_replace_urls(source_dir, destination):
        os.mkdir(destination)
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination, filename)
            print(source_file)
            print(" -> {0}".format(destination_file))
            if os.path.isdir(source_file):
                pass
                # TODO: copy subdirectories as well. This will require updating
                #       iter_examples to handle this correctly
                #copy_tree_and_replace_urls(source_file,
                #                           destination_file)
            else:
                with open(source_file) as f:
                    spec = json.load(f)

                # Adjust to use absolute URLs
                make_data_urls_absolute(spec, data_url)

                with open(destination_file, 'w') as f:
                    json.dump(spec, f, indent=4, sort_keys=True)

    copy_tree_and_replace_urls(source_dir, destination)


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
        version = args.tag or VEGALITE_VERSION
        sync_schema(version)

    if args.examples:
        tag = args.tag or VEGALITE_VERSION
        with checkout_tag(tag, VEGALITE_PATH, VEGALITE_URL):
            sync_examples(VEGALITE_PATH)

    if args.datasets:
        tag = args.tag or VEGA_DATA_TAG
        with checkout_tag(tag, VEGA_DATA_PATH, VEGA_DATA_URL):
            sync_datasets(VEGA_DATA_PATH)


if __name__ == '__main__':
    main()
