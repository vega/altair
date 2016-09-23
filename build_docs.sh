#---------------------------------------------------------------------------
# bash script to build Altair's docs
#
# we run this first with Python 2.7 to correctly create image thumbnails
# (this relies on nodejs tools that fail in Python 3.5)
# and then run again in Python 3.5 to get the final doc build.
#
# Usage: bash ./build_docs.sh   # must run from altair root directory
#---------------------------------------------------------------------------


# first build docs using 2.7; this is required for nodejs tools
conda create --yes -n altair-docs-27 python=2.7 || echo "conda 2.7 env exists"
source activate altair-docs-27
conda install --yes --file requirements.txt --channel conda-forge
conda install --yes --file doc/requirements.txt

# nodejs used to build thumbnails
conda install --yes nodejs --channel conda-forge
node -p "require('vega/package.json').version" || npm install vega
node -p "require('canvas/package.json').version" || npm install canvas

# install altair & build docs
python setup.py install
cd doc
make clean
make html
cd ..

#------------------------------------------------------------------
# next re-build docs using 3.5; this will use thumbnails from above
conda create --yes -n altair-docs-35 python=3.5 || echo "conda 3.5 env exists"
source activate altair-docs-35
conda install --yes --file requirements.txt --channel conda-forge
conda install --yes --file doc/requirements.txt

# install altair & build docs
python setup.py install
cd doc
make clean
make html
cd ..
