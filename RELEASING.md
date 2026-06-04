# Releasing Altair

Altair has two release paths:

- Automated stable releases for routine releases where Cocogitto's SemVer calculation is appropriate.
- Manual releases when maintainers need to choose the release tag themselves.

## Before Releasing

Check all [Vega project](https://github.com/orgs/vega/repositories?type=source) versions are up-to-date. See [NOTES_FOR_MAINTAINERS.md](NOTES_FOR_MAINTAINERS.md).

## Releasing

### Semi-Automated Release

1. Go to GitHub actions and start the `Prepare Release Draft` workflow.
    - The workflow uses the default `GITHUB_TOKEN` unless a `RELEASE_TOKEN` secret is configured. If branch protection prevents GitHub Actions from pushing release commits or tags to `main`, configure `RELEASE_TOKEN` with a maintainer or bot token that is allowed to push through the repository's release rules.
    - This workflow automates the following steps:
        1. Checks for an existing draft release and exits if one already exists.
        2. Uses Cocogitto to inspect conventional commits since the latest `v*` tag.
        3. Skips the release if no SemVer-relevant changes are found.
        4. Runs the test suite.
        5. Commits the release version and creates a `vX.Y.Z` tag.
        6. Creates a draft GitHub release.
        7. Builds and publishes docs preview with a draft-release banner at `release-preview/latest/`.
        8. Opens an issue with the instructions for manual review before releasing.
2. Review the issue that was opened by the workflow. This contains instructions on what to review before publishing the draft release, e.g. the release notes and the preview version of the docs.
3. Publish the release on Github.
    - Publishing a non-prerelease GitHub release whose tag matches `vX.Y.Z` triggers the `Publish Release to PyPI` workflow. That workflow checks out the release tag, builds the package, publishes to PyPI using trusted publishing, and publishes the official documentation without the draft-release banner.

### Manual Release

Use this path for major releases, maintenance-branch releases, releases that should not follow Cocogitto's automatic SemVer calculation, or if the automated workflow fails. Unlike the automated workflow, the maintainer chooses and creates the release tag manually.

1. Make sure to have [set up your environment](CONTRIBUTING.md#setting-up-your-environment). Update your environment with the latest dependencies:

       uv sync --all-extras

2. Make certain your branch is in sync with head, and that you have no uncommitted modifications. If you work on a fork, replace `origin` with `upstream`:

       git checkout main
       git pull origin main
       git status  # Should show "nothing to commit, working tree clean"

3. Do a [clean doc build](CONTRIBUTING.md#building-the-documentation-locally):

       uv run task doc-build -- --clean

   Navigate to http://localhost:8000 and ensure it looks OK, particularly the gallery thumbnails.

4. Run the test suite:

       uv run task test

5. Tag the release. If you work on a fork, replace `origin` with `upstream`:

        git tag -a v6.0.0 -m "Version 6.0.0 release"
        git push origin tag v6.0.0

6. Create a draft release at https://github.com/vega/altair/releases/new for the tag. Review the release notes, then publish the release. Publishing the GitHub release triggers PyPI publishing automatically for `vX.Y.Z` tags.

7. Double-check that a conda-forge pull request is generated from the updated PyPI package by the conda-forge bot. This may take up to several hours:

    https://github.com/conda-forge/altair-feedstock/pulls

## After Releasing

Double-check that a conda-forge pull request is generated from the updated PyPI package by the conda-forge bot. This is usually quick, but may take up to several hours: https://github.com/conda-forge/altair-feedstock/pulls
