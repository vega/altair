from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOC_DIR = REPO_ROOT / "doc"
DOC_BUILD_DIR = DOC_DIR / "_build"
DOC_HTML_DIR = DOC_BUILD_DIR / "html"
DOC_DOCTREES_DIR = DOC_BUILD_DIR / "doctrees"
DOC_IMAGES_DIR = DOC_DIR / "_images"
DOC_GENERATED_DIR = DOC_DIR / "user_guide" / "generated"
DOC_GALLERY_DIR = DOC_DIR / "gallery"
CLEAN_CHOICES = ["build", "generated", "images", "all"]


def run_command(command: list[str], *, env: dict[str, str] | None = None) -> None:
    subprocess.run(command, check=True, cwd=REPO_ROOT, env=env)


def rm_path(path: Path) -> None:
    if path.is_file():
        path.unlink(missing_ok=True)
    else:
        shutil.rmtree(path, ignore_errors=True)


def clean_docs(*, clean_build: bool, clean_generated: bool, clean_images: bool) -> None:
    paths = []
    if clean_build:
        paths.append(DOC_BUILD_DIR)
    if clean_generated:
        paths.extend([DOC_GENERATED_DIR, DOC_GALLERY_DIR])
    if clean_images:
        paths.append(DOC_IMAGES_DIR)
    if paths:
        for path in paths:
            rm_path(path)


def clean_kwargs_from_target(target: str) -> dict[str, bool]:
    clean_all = target == "all"
    return {
        "clean_build": clean_all or target == "build",
        "clean_generated": clean_all or target == "generated",
        "clean_images": clean_all or target == "images",
    }


def build_docs(*, watch: bool, autosummary: bool, gallery: bool) -> None:
    DOC_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["ALTAIR_AUTOSUMMARY_GENERATE"] = "1" if autosummary else "0"
    env["ALTAIR_GALLERY_GENERATE"] = "1" if gallery else "0"

    if watch:
        command = [
            "sphinx-autobuild",
            "--open-browser",
            "--port",
            "0",
            "--delay",
            "1",
            "--ignore",
            "doc/gallery",
            "--ignore",
            "doc/_images/",
            "--ignore",
            "doc/_build/html/gallery/",
            "--ignore",
            "doc/_build/html/user_guide/generated/",
            "--watch",
            "sphinxext/",
            "--watch",
            "tests/examples_methods_syntax/",
            "--watch",
            "tests/examples_arguments_syntax/",
            "-b",
            "html",
            "-d",
            str(DOC_DOCTREES_DIR),
            str(DOC_DIR),
            str(DOC_HTML_DIR),
        ]
    else:
        command = [
            "sphinx-build",
            "-b",
            "html",
            "-d",
            str(DOC_DOCTREES_DIR),
            str(DOC_DIR),
            str(DOC_HTML_DIR),
        ]

    run_command(command, env=env)


def serve_docs(*, bind: str, port: int) -> None:
    run_command(
        [
            sys.executable,
            "-m",
            "http.server",
            "--bind",
            bind,
            "--directory",
            str(DOC_HTML_DIR),
            str(port),
        ]
    )


def publish_docs() -> None:
    run_command([sys.executable, "tools/sync_website.py"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="build-docs")
    subparsers = parser.add_subparsers(dest="command", required=True)

    clean_parser = subparsers.add_parser(
        "clean", help="Remove generated docs artifacts"
    )
    clean_parser.add_argument("--build", action="store_true", help="Remove doc/_build")
    clean_parser.add_argument(
        "--generated",
        action="store_true",
        help="Remove generated user guide and gallery files",
    )
    clean_parser.add_argument(
        "--images", action="store_true", help="Remove doc/_images"
    )
    clean_parser.add_argument(
        "--all", action="store_true", help="Run all clean operations"
    )

    build_parser = subparsers.add_parser("build", help="Build docs with sphinx")
    build_parser.add_argument(
        "--watch",
        action="store_true",
        help="Use sphinx-autobuild instead of sphinx-build",
    )
    build_parser.add_argument(
        "--no-autosummary",
        action="store_true",
        help="Set ALTAIR_AUTOSUMMARY_GENERATE=0 for faster local builds",
    )
    build_parser.add_argument(
        "--no-gallery",
        action="store_true",
        help="Set ALTAIR_GALLERY_GENERATE=0 for faster local builds",
    )
    build_parser.add_argument(
        "--clean",
        nargs="?",
        const="all",
        default=None,
        choices=CLEAN_CHOICES,
        metavar="{build,generated,images,all}",
        help="Run clean before build; default target is all",
    )

    serve_parser = subparsers.add_parser("serve", help="Serve built docs")
    serve_parser.add_argument("--bind", default="127.0.0.1", help="Bind address")
    serve_parser.add_argument("--port", type=int, default=8000, help="Port")

    publish_parser = subparsers.add_parser("publish", help="Publish built docs")
    publish_parser.add_argument(
        "--clean",
        nargs="?",
        const="all",
        default=None,
        choices=CLEAN_CHOICES,
        metavar="{build,generated,images,all}",
        help="Run clean and build before publishing; default clean target is all",
    )
    publish_parser.add_argument(
        "--no-autosummary",
        action="store_true",
        help="Set ALTAIR_AUTOSUMMARY_GENERATE=0 for the pre-publish build",
    )
    publish_parser.add_argument(
        "--no-gallery",
        action="store_true",
        help="Set ALTAIR_GALLERY_GENERATE=0 for the pre-publish build",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.command == "clean":
        clean_docs(
            clean_build=args.build or args.all,
            clean_generated=args.generated or args.all,
            clean_images=args.images or args.all,
        )
        return

    if args.command == "build":
        if args.clean:
            clean_docs(**clean_kwargs_from_target(args.clean))
        build_docs(
            watch=args.watch,
            autosummary=not args.no_autosummary,
            gallery=not args.no_gallery,
        )
        return

    if args.command == "serve":
        serve_docs(bind=args.bind, port=args.port)
        return

    if args.command == "publish":
        if args.clean:
            clean_docs(**clean_kwargs_from_target(args.clean))
            build_docs(
                watch=False,
                autosummary=not args.no_autosummary,
                gallery=not args.no_gallery,
            )
        publish_docs()


if __name__ == "__main__":
    main()
