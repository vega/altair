1. Update version to, e.g. 2.0.0

   - in altair/__init__.py
   - in doc/conf.py (two places)

2. Make sure CHANGES.md is up to date for the release

3. Commit change and push to master

       git add . -u
       git commit -m "MAINT: bump version to 2.0.0"
       git push origin master

4. Tag the release:

       git tag -a v2.0.0 -m "version 2.0.0 release"
       git push origin v2.0.0

5. Build source & wheel distributions

       rm -r dist build  # clean old builds & distributions
       python setup.py sdist  # create a source distribution
       python setup.py bdist_wheel  # create a universal wheel

6. publish to PyPI (Requires correct PyPI owner permissions)

       twine upload dist/*

7. build and publish docs (Requires write-access to altair-viz/altair-viz.github.io)

       cd docs
       make clean
       make html
       bash sync_website.sh

8. update version to, e.g. 2.1.0dev

   - in altair/__init__.py
   - in doc/conf.py (two places)

9. add a new changelog entry for the unreleased version

10. Commit change and push to master

       git add . -u
       git commit -m "MAINT: bump version to 2.1.0dev"
       git push origin master

11. Update version and hash in the recipe at conda-forge/altair-feedstock:
    https://github.com/conda-forge/altair-feedstock/blob/master/recipe/meta.yaml
    & submit a pull request.
    
    Note: the conda-forge bot may take care of this automatically.
