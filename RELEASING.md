# Releasing Altair

Altair has two release paths:

- Automated stable releases for routine `fix` and `feat` changes.
- Manual releases for major releases or any release that needs extra maintainer judgment.

## Automated Stable Release

The `Prepare Release Draft` workflow is started manually from GitHub Actions. A commented schedule is included in the workflow file and can be enabled after the manual release flow has been tested.

The workflow uses the default `GITHUB_TOKEN` unless a `RELEASE_TOKEN` secret is configured. If branch protection prevents GitHub Actions from pushing release commits or tags to `main`, configure `RELEASE_TOKEN` with a maintainer or bot token that is allowed to push through the repository's release rules.

The workflow:

1. Checks for an existing draft release and exits if one already exists.
2. Uses Cocogitto to inspect conventional commits since the latest `v*` tag.
3. Skips the release if no SemVer-relevant changes are found.
4. Runs the test suite.
5. Commits the release version and creates a `vX.Y.Z` tag.
6. Creates a draft GitHub release.

Review the draft GitHub release notes. If everything looks correct, publish the draft release in GitHub.

Publishing a non-prerelease GitHub release whose tag matches `vX.Y.Z` triggers the `Publish Release to PyPI` workflow. That workflow checks out the release tag, builds the package, and publishes to PyPI using trusted publishing.

After publishing, double-check that a conda-forge pull request is generated from the updated PyPI package by the conda-forge bot. This may take up to several hours:

https://github.com/conda-forge/altair-feedstock/pulls

## Manual Release

Use this path for major releases, releases that should not follow the automatic SemVer calculation, or if the automated workflow exits and says the release should be manual.

1. Check all [Vega project](https://github.com/orgs/vega/repositories?type=source) versions are up-to-date. See [NOTES_FOR_MAINTAINERS.md](NOTES_FOR_MAINTAINERS.md).

2. Make sure to have [set up your environment](CONTRIBUTING.md#setting-up-your-environment). Update your environment with the latest dependencies:

       uv sync --all-extras

3. Make certain your branch is in sync with head, and that you have no uncommitted modifications. If you work on a fork, replace `origin` with `upstream`:

       git checkout main
       git pull origin main
       git status  # Should show "nothing to commit, working tree clean"

4. Do a [clean doc build](CONTRIBUTING.md#building-the-documentation-locally):

       uv run task doc-build -- --clean

   Navigate to http://localhost:8000 and ensure it looks OK, particularly the gallery thumbnails.

5. Create a new release branch:

       git switch -c release_6.0.0

6. Commit any release-specific changes and push:

       git add . -u
       git commit -m "chore: release 6.0.0"
       git push

7. Merge the release branch into main and make sure that all required checks pass.

8. Switch to main. If you work on a fork, replace `origin` with `upstream`:

       git switch main
       git pull origin main

9. On main, tag the release. If you work on a fork, replace `origin` with `upstream`:

        git tag -a v6.0.0 -m "Version 6.0.0 release"
        git push origin tag v6.0.0

10. Create a draft release at https://github.com/vega/altair/releases/new for the tag. Review the release notes, then publish the release. Publishing the GitHub release triggers PyPI publishing automatically for `vX.Y.Z` tags.

11. Double-check that a conda-forge pull request is generated from the updated PyPI package by the conda-forge bot. This may take up to several hours:

    https://github.com/conda-forge/altair-feedstock/pulls

## Documentation Publishing

Publishing documentation still requires write access to [altair-viz/altair-viz.github.io](https://github.com/altair-viz/altair-viz.github.io):

    uv run task doc-build -- --clean
    uv run task doc-publish

This is not yet automated by the release workflows because the required credentials and review policy are separate from PyPI trusted publishing.
