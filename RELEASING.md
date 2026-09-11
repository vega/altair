# Releasing Altair

Altair has two release paths:

- Automated stable releases for routine releases where Cocogitto's SemVer calculation is appropriate.
- Manual releases when maintainers need to choose the release tag themselves.

## Before Releasing

Check that all [Vega project](https://github.com/orgs/vega/repositories?type=source) versions are up-to-date. See [NOTES_FOR_MAINTAINERS.md](NOTES_FOR_MAINTAINERS.md).

## Releasing

### Semi-Automated Release

The `release` environment in the repository settings must have at least one required reviewer. The workflow verifies this before creating a version tag.

1. A couple of times a month, GitHub Actions will check if notable commits have been made to main (e.g. fixes and features) since the last release. If so, a release candidate will be prepared and an issue will be opened tagging the maintainers to review it before releasing.
    - If a scheduled candidate proposes an undesired version bump, reject its pending deployment, close its review issue, and rerun the workflow manually. Manual workflow dispatch let's you choose whether to use a `major`, `minor`, or `patch` bump.
        - To trigger this release workflow manually: go to the "Actions" tab, click the `Prepare Release Draft` workflow to the left, and then "Run workflow".
    - This workflow automates the following steps:
        1. Checks for an existing release review issue or draft release and exits if one already exists.
        2. Uses Cocogitto to inspect conventional commits since the latest `v*` tag.
        3. Skips the release if no SemVer-relevant changes are found.
        4. Runs the test suite.
        5. Generates a release notes preview without creating a version tag.
        6. Builds and publishes a docs preview from the candidate commit with a release-candidate banner at `release-preview/latest/`.
        7. Opens an issue with the candidate commit, release notes, docs preview, and review instructions.
        8. Waits for approval through the protected `release` environment.
2. Review the issue opened by the workflow. Approve the pending release deployment if the release notes and docs preview look correct, or reject it to abort the release. Rejection creates no version tag or GitHub release.
3. Approval creates an immutable `vX.Y.Z` tag at the exact reviewed commit and creates a draft GitHub release. Review the draft, publish it on GitHub, and close the release review issue.
    - Publishing a non-prerelease GitHub release whose tag matches `vX.Y.Z` triggers the `Publish Release to PyPI` workflow. That workflow checks out the release tag, builds the package, publishes to PyPI using trusted publishing, and updates the official documentation.

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

7. Publish the updated documentation. To do this manually, write access to [altair-viz/altair-viz.github.io](https://github.com/altair-viz/altair-viz.github.io) is required:

        uv run task doc-build -- --clean
        uv run task doc-publish

## After Releasing

Double-check that a conda-forge pull request is generated from the updated PyPI package by the conda-forge bot. This is usually quick, but may take up to several hours: https://github.com/conda-forge/altair-feedstock/pulls
