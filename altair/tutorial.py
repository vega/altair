

import os
import shutil
from six.moves.urllib.request import urlretrieve

TUTORIAL_DIR = 'AltairTutorial'

BASE_URL = 'https://raw.githubusercontent.com/ellisonbg/altair/master/notebooks/'

FILES = [
    '01-Index.ipynb',
    '02-Introduction.ipynb',
    '03-ScatterCharts.ipynb',
    '04-BarCharts.ipynb',
    '05-LineCharts.ipynb',
    '06-AreaCharts.ipynb',
    '07-LayeredCharts.ipynb',
    '08-GroupedRegressionCharts.ipynb',
    '09-CarsDataset.ipynb',
    '10-IrisPairgrid.ipynb'
]
 
 
def download_tutorial(overwrite=True):
    """Download the Altair tutorial notebooks."""
    if os.path.isdir(TUTORIAL_DIR) and overwrite:
        print('Removing old tutorial directory: {}'.format(TUTORIAL_DIR))
        shutil.rmtree(TUTORIAL_DIR, ignore_errors=True)
    print('Downloading fresh tutorial directory: {}'.format(TUTORIAL_DIR))
    os.mkdir(TUTORIAL_DIR)
    for f in FILES:
        urlretrieve(BASE_URL+f, os.path.join(TUTORIAL_DIR, f))


def tutorial(overwrite=True):
    """Download the Altair tutorial notebooks and show a link in the notebook."""
    download_tutorial(overwrite=overwrite)
    print('Click on the following notebooks to explore the tutorial:')
    from IPython.display import FileLinks, display
    display(FileLinks(TUTORIAL_DIR))
