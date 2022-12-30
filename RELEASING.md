1. Create a new virtual environment following the instructions in `CONTRIBUTING.md`. 
   Make sure to also install all dependencies for the documentation including `altair_saver`
   and uninstall `vl-convert-python`.

2. Make certain your branch is in sync with head
   
       $ git pull upstream master
   
3. Do a clean doc build:

       $ cd doc
       $ make clean-all
       $ make html
       $ cd _build/html; python -m http.server
   
   Navigate to http://localhost:8000 and ensure it looks OK (particularly
   do a visual scan of the gallery thumbnails).

4. Make sure changes.rst is up to date for the release: compare against PRs
   merged since the last release & update top heading with release date.

5. Update version to, e.g. 5.0.0

   - in ``altair/__init__.py``
   - in ``doc/conf.py`` (two places)

6. Double-check that all vega-lite/vega/vega-embed versions are up-to-date:

   - URLs in ``doc/conf.py``
   - versions in ``altair/vegalite/v5/display.py``

7. Commit change and push to master:

       git add . -u
       git commit -m "MAINT: bump version to 2.0.0"
       git push upstream master

8. Tag the release:

       git tag -a v2.0.0 -m "version 2.0.0 release"
       git push upstream v2.0.0

9. Build source & wheel distributions:

       rm -r dist build  # clean old builds & distributions
       python setup.py sdist  # create a source distribution
       python setup.py bdist_wheel  # create a universal wheel

10. publish to PyPI (Requires correct PyPI owner permissions):

       twine upload dist/*

11. build and publish docs (Requires write-access to altair-viz/altair-viz.github.io):

        cd doc
        make clean-all
        make html
        bash sync_website.sh

12. update version to, e.g. 5.1.0dev:

    - in ``altair/__init__.py``
    - in ``doc/conf.py`` (two places)

13. add a new changelog entry for the unreleased version:

       Version 5.1.0 (unreleased)
       --------------------------

       Enhancements
       ~~~~~~~~~~~~
       Bug Fixes
       ~~~~~~~~~
       Backward-Incompatible Changes
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

14. Commit change and push to master

        git add . -u
        git commit -m "MAINT: bump version to 5.1.0dev"
        git push upstream master

15. Double-check that a conda-forge pull request is generated from the updated
    pip package by the conda-forge bot (may take up to ~an hour):
    https://github.com/conda-forge/altair-feedstock/pulls

16. Copy changes.rst section into release notes within
    https://github.com/altair-viz/altair/releases/, and publish the release.
