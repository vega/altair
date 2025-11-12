1. Check all [Vega project](https://github.com/orgs/vega/repositories?type=source) versions are up-to-date. See [NOTES_FOR_MAINTAINERS.md](NOTES_FOR_MAINTAINERS.md)


2. Make sure to have [set up your environment](CONTRIBUTING.md#setting-up-your-environment).
   Update your environment with the latest dependencies:
   
        uv sync --all-extras

3. Make certain your branch is in sync with head, and that you have no uncommitted modifications. If you work on a fork, replace `origin` with `upstream`:
 
        git checkout main
        git pull origin main
        git status  # Should show "nothing to commit, working tree clean"

4. Do a [clean doc build](CONTRIBUTING.md#building-the-documentation-locally):
   
   Navigate to http://localhost:8000 and ensure it looks OK (particularly
   do a visual scan of the gallery thumbnails).

5. Create a new release branch:
       
        git switch -c version_6.0.0

6. Update version to, e.g. 6.0.0:

   - in ``altair/__init__.py``
   - in ``doc/conf.py``

7. Commit changes and push:

        git add . -u
        git commit -m "chore: Bump version to 6.0.0"
        git push

8. Merge release branch into main, make sure that all required checks pass

9.  Switch to main, If you work on a fork, replace `origin` with `upstream`:

        git switch main
        git pull origin main
        
10. Build a source distribution and universal wheel, 
    publish to PyPI (Requires correct PyPI owner permissions and [UV_PUBLISH_TOKEN](https://docs.astral.sh/uv/configuration/environment/#uv_publish_token)):

        uv run task publish

11. Build and publish docs (Requires write-access to [altair-viz/altair-viz.github.io](https://github.com/altair-viz/altair-viz.github.io)):

        uv run task doc-publish-clean-build

12. On main, tag the release. If you work on a fork, replace `origin` with `upstream`:

       git tag -a v6.0.0 -m "Version 6.0.0 release"
       git push origin v6.0.0

13. Create a new branch:
       
       git switch -c maint_6.1.0dev

14. Update version and add 'dev' suffix, e.g. 6.1.0dev:

    - in ``altair/__init__.py``
    - in ``doc/conf.py``

15. Commit changes and push:

        git add . -u
        git commit -m "chore: Bump version to 6.1.0dev"
        git push
        
16. Merge maintenance branch into main

17. Double-check that a conda-forge pull request is generated from the updated
    pip package by the conda-forge bot (may take up to several hours):
    https://github.com/conda-forge/altair-feedstock/pulls

18. Publish a new release in https://github.com/vega/altair/releases/
