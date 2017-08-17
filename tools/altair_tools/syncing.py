"""Tools for syncing vega-lite schemas & example files"""

import os
import shutil
import json

from .utils import urlopen, checkout_tag, path_within_altair


def abspath(*args):
    """Get absolute path relative to this file"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))


SCHEMA_URL = "https://vega.github.io/schema/{library}/{version}.json"
TMP_PATH = abspath('..', '_build')
REPO_PATH = os.path.join(TMP_PATH, 'repos')

VEGALITE_PATH = os.path.join(REPO_PATH, 'vega-lite')
VEGALITE_URL = 'https://github.com/vega/vega-lite.git'

VEGA_DATA_PATH = os.path.join(REPO_PATH, 'vega-datasets')
VEGA_DATA_URL = 'https://github.com/vega/vega-datasets.git'

VERSION_FILE = """# Automatically written by tools/sync_vegalite.py
# Do not modify this manually
vegalite_version = '{vegalite_version}'
vegalite_schema_url = '{vegalite_schema_url}'
"""


def sync_schema(vegalite_version,
                schema_path=path_within_altair('schema'),
                schema_file='vega-lite-schema.json',
                version_file='_vegalite_version.py'):
    """
    Download the appropriate version of the vega-lite schema
    and save at the specified destination
    """
    if not os.path.exists(schema_path):
        os.makedirs(schema_path)

    vegalite_schema_url = SCHEMA_URL.format(library='vega-lite',
                                            version=vegalite_version)
    schema_file = os.path.join(schema_path, schema_file)
    version_file = os.path.join(schema_path, version_file)

    version_file_content = VERSION_FILE.format(
                                    vegalite_version=vegalite_version,
                                    vegalite_schema_url=vegalite_schema_url)

    print("Downloading Vega-Lite {0} Schema".format(vegalite_version))
    print(" Source:      {0}".format(vegalite_schema_url))
    print(" Destination: {0}".format(schema_file))
    with urlopen(vegalite_schema_url) as source:
        content = source.read()
    with open(schema_file, 'wb') as dest:
        dest.write(content)

    print("Writing version info")
    print(" Filename: {0}".format(version_file))
    with open(version_file, 'w') as f:
        f.write(version_file_content)


def sync_examples(vegalite_version,
                  destination=path_within_altair('examples', 'json'),
                  data_url='http://vega.github.io/vega-lite/',
                  vegalite_path=VEGALITE_PATH, vegalite_url=VEGALITE_URL):
    """
    Clone the vega-lite repository, check-out the appropriate version, and
    copy all example files into Altair
    """
    if not os.path.exists(destination):
        os.makedirs(destination)

    source_dir = os.path.join(vegalite_path, 'examples', 'specs')
    if vegalite_version.startswith('v1'):
        index_source = os.path.join(vegalite_path, 'examples',
                                    'vl-examples.json')
    else:
        index_source = os.path.join(vegalite_path, '_data', 'examples.json')
    index_destination = os.path.join(destination, '..', 'example-listing.json')
    print("Reading from {0}".format(source_dir))

    if not os.path.exists(destination):
        raise ValueError("{0} does not exist".format(destination))


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

    with checkout_tag(vegalite_version, vegalite_path, vegalite_url):
        if not os.path.exists(source_dir):
            raise ValueError("{0} does not exist".format(source_dir))
        if not os.path.exists(index_source):
            raise ValueError("{0} does not exist".format(index_source))


        # remove old files before syncing
        shutil.rmtree(destination)
        copy_tree_and_replace_urls(source_dir, destination)

        # sync the index
        with open(index_source) as f:
            with open(index_destination, 'w') as of:
                of.write(f.read())


def sync_datasets(datasets_version,
                  destination=path_within_altair('datasets'),
                  filename='datasets.json',
                  vega_data_path=VEGA_DATA_PATH, vega_data_url=VEGA_DATA_URL):
    """
    Clone the vega-datasets repository, check-out the appropriate version,
    and copy data URL listing into Altair.
    """
    if not os.path.exists(destination):
        os.makedirs(destination)

    with checkout_tag(datasets_version, vega_data_path, vega_data_url):
        sourcedir = os.path.join(vega_data_path, 'data')
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
