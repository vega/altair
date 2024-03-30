1. Make sure to have an environment set up with `hatch` installed. See `CONTRIBUTING.md`.
   Remove any existing environments managed by `hatch` so that it will create new ones
   with the latest dependencies when executing the commands further below:
   
       hatch env prune

2. Make certain your branch is in sync with head:
 
       git pull upstream main

3. Do a clean doc build:

       hatch run doc:clean-all
       hatch run doc:build-html
       hatch run doc:serve
   
   Navigate to http://localhost:8000 and ensure it looks OK (particularly
   do a visual scan of the gallery thumbnails).

4. Update version to, e.g. 5.0.0:

   - in ``altair/__init__.py``
   - in ``doc/conf.py``

5. Commit change and push to main:

       git add . -u
       git commit -m "chore: bump version to 5.0.0"
       git push upstream main

6. Tag the release:

       git tag -a v5.0.0 -m "version 5.0.0 release"
       git push upstream v5.0.0

7. Build source & wheel distributions:

       hatch clean  # clean old builds & distributions
       hatch build  # create a source distribution and universal wheel

8. publish to PyPI (Requires correct PyPI owner permissions):

        hatch publish

9. build and publish docs (Requires write-access to altair-viz/altair-viz.github.io):

        hatch run doc:publish-clean-build

10. update version to, e.g. 5.1.0dev:

    - in ``altair/__init__.py``
    - in ``doc/conf.py``

11. Commit change and push to main:

        git add . -u
        git commit -m "chore: bump version to 5.1.0dev"
        git push upstream main

12. Double-check that a conda-forge pull request is generated from the updated
    pip package by the conda-forge bot (may take up to ~an hour):
    https://github.com/conda-forge/altair-feedstock/pulls

13. Publish a new release in https://github.com/altair-viz/altair/releases/
