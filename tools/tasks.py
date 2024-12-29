from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Literal

from tools._tasks import Tasks, mkdir_cmd, rm_rf_cmd

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


@app.task("type-check")
def type_check() -> Commands:
    yield "mypy altair tests"


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


@app.task("generate-schema-wrapper")
def generate_schema_wrapper() -> Commands:
    yield f"mypy {TOOLS}"
    yield f"python {TOOLS}/generate_schema_wrapper.py"
    yield "test"


@app.task("update-init-file")
def update_init_file() -> Commands:
    yield f"python {TOOLS}/update_init_file.py"
    yield "ruff-fix"


@app.task("clean")
def doc_clean() -> Commands:
    yield rm_rf_cmd(REPO_ROOT / DOC_BUILD)


@app.task("clean-generated")
def doc_clean_generated() -> Commands:
    yield rm_rf_cmd(REPO_ROOT / f"{DOC}/user_guide/generated")
    yield rm_rf_cmd(REPO_ROOT / f"{DOC}/gallery")


@app.task("clean-all")
def doc_clean_all() -> Commands:
    yield from ("clean", "clean-generated")
    yield rm_rf_cmd(REPO_ROOT / DOC_IMAGES)


@app.task("build-html", extras=DOC)
def doc_build_html() -> Commands:
    yield mkdir_cmd(DOC_IMAGES)
    yield f"sphinx-build -b html -d {DOC_BUILD}/doctrees {DOC} {DOC_BUILD_HTML}"


@app.task("serve")
def doc_serve() -> Commands:
    ADDRESS = "127.0.0.1"
    PORT = 8000
    yield f'python -m http.server --bind "{ADDRESS}" --directory {DOC_BUILD_HTML} {PORT}'


@app.task("publish")
def doc_publish() -> Commands:
    SYNC_SCRIPT = f"{TOOLS}/sync_website.py"
    yield f"python {SYNC_SCRIPT} --no-commit"


@app.task("clean-build", extras=DOC)
def doc_clean_build() -> Commands:
    yield "clean-all"
    yield "build-html"


@app.task("publish-clean-build", extras=DOC)
def doc_publish_clean_build() -> Commands:
    yield "clean-build"
    yield "publish"


def main() -> None:
    import os

    os.chdir(REPO_ROOT)
    parser = app.parser(Path(__file__).name)
    args = parser.parse_args()
    app.run(args.commands, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
