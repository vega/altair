"""
This script will sync the vegalite schema
"""
import os
import shutil
from tools import GitRepo

FILENAME = 'vega-lite-schema.json'
DESTINATION = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           '..', 'altair', 'schema'))
DEFAULT_VERSION = 'v1.0.8'


def sync_schema(vegalite_repo, filename=FILENAME):
    source = os.path.join(vegalite_repo, FILENAME)
    destination = os.path.join(DESTINATION, FILENAME)
    print("Copying Vega-Lite Schema:")
    print("  Source:     ", source)
    print("  Destination:", destination)
    shutil.copyfile(source, destination)


def clone_and_sync(version=DEFAULT_VERSION):
    vegalite_repo = GitRepo('vega-lite').clone().update()
    vegalite_repo.checkout_tag(version)
    sync_schema(vegalite_repo.repopath)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Sync Vega-Lite Schema')
    parser.add_argument('-v', '--version', default=DEFAULT_VERSION,
                        help='Version tag to use')

    args = parser.parse_args()
    clone_and_sync(args.version)


if __name__ == '__main__':
    main()
