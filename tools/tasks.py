from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Literal

from tools._tasks import Tasks, cmd

if TYPE_CHECKING:
    import sys

    if sys.version_info >= (3, 11):
        from typing import LiteralString
    else:
        from typing_extensions import LiteralString
    from tools._tasks import Commands

__all__ = ["app"]


REPO_ROOT: Path = Path(__file__).parent.parent
DOC: Literal["doc"] = "doc"
DOC_BUILD: LiteralString = f"{DOC}/_build"
DOC_IMAGES: LiteralString = f"{DOC}/_images"
DOC_BUILD_HTML: LiteralString = f"{DOC_BUILD}/html"
TOOLS: Literal["tools"] = "tools"

app = Tasks(runner="uv")

# -----------------------------------------------------------------------------
# NOTE: ruff


@app.task()
def lint() -> Commands:
    """Runs ruff check."""
    yield "ruff check"


@app.task()
def format() -> Commands:
    yield "ruff format --diff --check"


@app.task("ruff-fix")
def ruff_fix() -> Commands:
    yield "ruff check"
    yield "ruff format"


# -----------------------------------------------------------------------------
# NOTE: mypy


@app.task("type-check")
def type_check() -> Commands:
    yield "mypy altair tests"


# -----------------------------------------------------------------------------
# NOTE: pytest


@app.task()
def pytest() -> Commands:
    yield "pytest"


@app.task()
def test() -> Commands:
    yield from ("lint", "format", "type-check", "pytest")


@app.task("test-fast")
def test_fast() -> Commands:
    yield "ruff-fix"
    yield 'pytest -m "not slow"'


@app.task("test-slow")
def test_slow() -> Commands:
    yield "ruff-fix"
    yield 'pytest -m "slow"'


# -----------------------------------------------------------------------------
# NOTE: Generation


@app.task("generate-schema-wrapper")
def generate_schema_wrapper() -> Commands:
    yield f"mypy {TOOLS}"
    yield cmd.script(f"{TOOLS}/generate_schema_wrapper.py")
    yield "test"


@app.task("update-init-file")
def update_init_file() -> Commands:
    yield cmd.script(f"{TOOLS}/update_init_file.py")
    yield "ruff-fix"


# -----------------------------------------------------------------------------
# NOTE: Docs


@app.task("doc-clean")
def doc_clean() -> Commands:
    yield cmd.rm_rf(REPO_ROOT / DOC_BUILD)


@app.task("doc-clean-generated")
def doc_clean_generated() -> Commands:
    yield cmd.rm_rf(REPO_ROOT / f"{DOC}/user_guide/generated")
    yield cmd.rm_rf(REPO_ROOT / f"{DOC}/gallery")


@app.task("doc-clean-all")
def doc_clean_all() -> Commands:
    yield from ("doc-clean", "doc-clean-generated")
    yield cmd.rm_rf(REPO_ROOT / DOC_IMAGES)


@app.task("doc-build-html", extras=DOC)
def doc_build_html() -> Commands:
    yield cmd.mkdir(DOC_IMAGES)
    yield f"sphinx-build -b html -d {DOC_BUILD}/doctrees {DOC} {DOC_BUILD_HTML}"


@app.task("doc-serve")
def doc_serve() -> Commands:
    ADDRESS = "127.0.0.1"
    PORT = 8000
    yield cmd.mod(
        "http.server", f'--bind "{ADDRESS}"', f"--directory {DOC_BUILD_HTML}", f"{PORT}"
    )


@app.task("doc-publish")
def doc_publish() -> Commands:
    yield cmd.script(f"{TOOLS}/sync_website.py", "--no-commit")


@app.task("doc-clean-build", extras=DOC)
def doc_clean_build() -> Commands:
    yield "doc-clean-all"
    yield "doc-build-html"


@app.task("doc-publish-clean-build", extras=DOC)
def doc_publish_clean_build() -> Commands:
    yield "doc-clean-build"
    yield "doc-publish"


# -----------------------------------------------------------------------------
# TODO: Build


# -----------------------------------------------------------------------------
# NOTE: Meta


@app.task("export-tasks")
def export_tasks() -> Commands:
    TASKS_TOML = "tasks.toml"
    yield cmd("from tools.tasks import app", f"app.to_path({TASKS_TOML!r})")


def main() -> None:
    import os

    os.chdir(REPO_ROOT)
    parser = app.parser(Path(__file__).name)
    args = parser.parse_args()
    app.run(args.commands, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
