1. Do a release of schemapi if necessary

2. Update version in altair/__init__.py to, e.g. 1.2.0

3. Commit change and push to master

       git add altair -u
       git commit -m "MAINT: bump version to 1.2.0"
       git push origin master

4. Tag the release:

       git tag -a v1.2.0 -m "version 1.3.0 release"
       git push origin v1.2.0

5. publish to PyPI (Requires correct PyPI owner permissions)

       python setup.py sdist upload

6. update version in altair/__init__.py to, e.g. 1.3.0dev

7. Commit change and push to master

       git add altair -u
       git commit -m "MAINT: bump version to 1.3.0dev"
       git push origin master

8. Update recipe on conda-forge/altair-feedstock

    