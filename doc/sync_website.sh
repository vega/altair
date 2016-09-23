#!/bin/bash

# get git hash for commit message
GITHASH=$(git rev-parse HEAD)
MSG="doc build for commit $GITHASH"
cd _build

# clone the repo if needed
if test -d altair-viz.github.io; 
then echo "using existing cloned astropy directory";
else git clone git@github.com:altair-viz/altair-viz.github.io.git;
fi

# sync the website
cd altair-viz.github.io
git pull

# remove all tracked files
git ls-files -z | xargs -0 rm -f

# sync files from html build
rsync -r ../html/ ./

# add commit, and push to github
git add . --all
git commit -m "$MSG"
git push origin master
