1. Make certain your branch is in sync with head
   
       $ git pull upstream master
   
2. Do a clean doc build:

       $ cd doc
       $ make clean-all
       $ make html
       $ cd _build/html; python -m http.server
   
   Navigate to http://localhost:8000 and ensure it looks OK (particularly
   do a visual scan of the gallery thumbnails).

3. Make sure CHANGES.md is up to date for the release: compare against PRs
   merged since the last release & update top heading with release date.

4. Update version to, e.g. 2.0.0

   - in ``altair/__init__.py``
   - in ``doc/conf.py`` (two places)

5. Double-check that all vega-lite/vega/vega-embed versions are up-to-date:

   - URLs in ``doc/conf.py``
   - versions in ``altair/vegalite/v3/display.py``

6. Commit change and push to master

       git add . -u
       git commit -m "MAINT: bump version to 2.0.0"
       git push upstream master

7. Tag the release:

       git tag -a v2.0.0 -m "version 2.0.0 release"
       git push upstream v2.0.0

8. Build source & wheel distributions

       rm -r dist build  # clean old builds & distributions
       python setup.py sdist  # create a source distribution
       python setup.py bdist_wheel  # create a universal wheel

9. publish to PyPI (Requires correct PyPI owner permissions)

       twine upload dist/*

10. build and publish docs (Requires write-access to altair-viz/altair-viz.github.io)

        cd doc
        make clean-all
        make html
        bash sync_website.sh

11. update version to, e.g. 2.1.0dev

    - in ``altair/__init__.py``
    - in ``doc/conf.py`` (two places)

12. add a new changelog entry for the unreleased version:

        ## Version 2.1.0 (unreleased)
        ### Enhancements
        ### Bug Fixes
        ### Backward-Incompatible Changes

13. Commit change and push to master

        git add . -u
        git commit -m "MAINT: bump version to 2.1.0dev"
        git push upstream master

14. Double-check that a conda-forge pull request is generated from the updated
    pip package by the conda-forge bot (may take up to ~an hour):
    https://github.com/conda-forge/altair-feedstock/pulls
