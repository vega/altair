

import os
import shutil
import glob
from six.moves.urllib.request import urlretrieve


SRC_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__)
)[0], 'notebooks')

DEST_PATH = './AltairTutorial'

def copy_tutorial(overwrite=False):
    """Copy the Altair tutorial notebooks into ./AltairTutorial."""
    if os.path.isdir(DEST_PATH) and overwrite:
        print('Removing old tutorial directory: {}'.format(DEST_PATH))
        shutil.rmtree(DEST_PATH, ignore_errors=True)
    if os.path.isdir(DEST_PATH):
        raise RuntimeError('{} already exists, run with overwrite=True to discard existing files'.format(DEST_PATH))
    print('Copying notebooks into fresh tutorial directory: {}'.format(DEST_PATH))
    shutil.copytree(SRC_PATH, DEST_PATH)


def tutorial(overwrite=False):
    """Copy the Altair tutorial notebooks into ./AltairTutorial and show a link in the notebook."""
    copy_tutorial(overwrite=overwrite)
    print('Click on the following notebooks to explore the tutorial:')
    from IPython.display import FileLinks, display
    display(FileLinks(DEST_PATH))
