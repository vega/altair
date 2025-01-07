1. Check all [Vega project](https://github.com/orgs/vega/repositories?type=source) versions are up-to-date. See [NOTES_FOR_MAINTAINERS.md](NOTES_FOR_MAINTAINERS.md)

2. Make sure to have an environment set up with `hatch` installed. See [CONTRIBUTING.md](CONTRIBUTING.md).
   Remove any existing environments managed by `hatch` so that it will create new ones
   with the latest dependencies when executing the commands further below:
   
        hatch env prune

3. Make certain your branch is in sync with head, and that you have no uncommitted modifications. If you work on a fork, replace `origin` with `upstream`:
 
        git checkout main
        git pull origin main
        git status  # Should show "nothing to commit, working tree clean"

4. Do a clean doc build:

        hatch run doc:clean-all
        hatch run doc:build-html
        hatch run doc:serve
   
   Navigate to http://localhost:8000 and ensure it looks OK (particularly
   do a visual scan of the gallery thumbnails).

5. Create a new release branch:
       
        git switch -c version_5.0.0

6. Update version to, e.g. 5.0.0:

   - in ``altair/__init__.py``
   - in ``doc/conf.py``

7. Commit changes and push:

        git add . -u
        git commit -m "chore: Bump version to 5.0.0"
        git push

8. Merge release branch into main, make sure that all required checks pass

9.  On main, build source & wheel distributions. If you work on a fork, replace `origin` with `upstream`:

        git switch main
        git pull origin main
        hatch clean  # clean old builds & distributions
        hatch build  # create a source distribution and universal wheel

10. publish to PyPI (Requires correct PyPI owner permissions):

        hatch publish

11. build and publish docs (Requires write-access to altair-viz/altair-viz.github.io):

        hatch run doc:publish-clean-build

12. On main, tag the release. If you work on a fork, replace `origin` with `upstream`:

       git tag -a v5.0.0 -m "Version 5.0.0 release"
       git push origin v5.0.0

13. Create a new branch:
       
       git switch -c maint_5.1.0dev

14. Update version and add 'dev' suffix, e.g. 5.1.0dev:

    - in ``altair/__init__.py``
    - in ``doc/conf.py``

15. Commit changes and push:

        git add . -u
        git commit -m "chore: Bump version to 5.1.0dev"
        git push
        
16. Merge maintenance branch into main

17. Double-check that a conda-forge pull request is generated from the updated
    pip package by the conda-forge bot (may take up to several hours):
    https://github.com/conda-forge/altair-feedstock/pulls

18. Publish a new release in https://github.com/vega/altair/releases/
