1. Update version to, e.g. 2.0.0

   - in altair/__init__.py
   - in doc/conf.py (two places)

2. Make sure CHANGES.md is up to date for the release

3. Double-check that all vega-lite/vega/vega-embed versions are up-to-date:

   - URLs in doc/conf.py
   - versions in altair/vegalite/v3/display.py

4. Commit change and push to master

       git add . -u
       git commit -m "MAINT: bump version to 2.0.0"
       git push origin master

5. Tag the release:

       git tag -a v2.0.0 -m "version 2.0.0 release"
       git push origin v2.0.0

6. Build source & wheel distributions

       rm -r dist build  # clean old builds & distributions
       python setup.py sdist  # create a source distribution
       python setup.py bdist_wheel  # create a universal wheel

7. publish to PyPI (Requires correct PyPI owner permissions)

       twine upload dist/*

8. build and publish docs (Requires write-access to altair-viz/altair-viz.github.io)

       cd doc
       make clean-all
       make html
       bash sync_website.sh

9. update version to, e.g. 2.1.0dev

   - in altair/__init__.py
   - in doc/conf.py (two places)

10. add a new changelog entry for the unreleased version

11. Commit change and push to master

       git add . -u
       git commit -m "MAINT: bump version to 2.1.0dev"
       git push origin master

12. Double-check that a conda-forge pull request is generated from the updated
    pip package by the conda-forge bot:
    https://github.com/conda-forge/altair-feedstock/
