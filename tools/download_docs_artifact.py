from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path

DEFAULT_DIR = Path("pr-preview-docs")
WORKFLOW_NAME = "docbuild"
WORKFLOW_PATH = ".github/workflows/docbuild.yml"


def run_command(command: list[str]) -> str:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def latest_docbuild_run_id(*, pr_number: int | None) -> str:
    if pr_number is not None:
        return latest_docbuild_run_id_for_pr(pr_number)

    command = [
        "gh",
        "run",
        "list",
        "--workflow",
        "docbuild",
        "--limit",
        "1",
        "--json",
        "databaseId",
        "--jq",
        ".[0].databaseId",
    ]
    run_id = run_command(command)
    if not run_id:
        msg = "No docbuild workflow run found."
        raise RuntimeError(msg)
    return run_id


def latest_docbuild_run_id_for_pr(pr_number: int) -> str:
    repo = run_command(
        ["gh", "repo", "view", "--json", "nameWithOwner", "--jq", ".nameWithOwner"]
    )
    pr_head_sha = run_command(
        ["gh", "pr", "view", str(pr_number), "--json", "headRefOid", "--jq", ".headRefOid"]
    )
    workflow_id = run_command(
        [
            "gh",
            "api",
            f"repos/{repo}/actions/workflows",
            "--jq",
            (
                f'.workflows[] | select(.name == "{WORKFLOW_NAME}" '
                f'or .path == "{WORKFLOW_PATH}") | .id'
            ),
        ]
    ).splitlines()[0]
    query = (
        ".workflow_runs[] | "
        f"select(any(.pull_requests[]?; .number == {pr_number}) "
        f'or .head_sha == "{pr_head_sha}") | '
        ".id"
    )
    run_id = run_command(
        [
            "gh",
            "api",
            "--method",
            "GET",
            f"repos/{repo}/actions/workflows/{workflow_id}/runs",
            "--field",
            "event=pull_request",
            "--field",
            "per_page=50",
            "--jq",
            query,
        ]
    ).splitlines()
    if not run_id:
        msg = f"No docbuild workflow run found for PR #{pr_number}."
        raise RuntimeError(msg)
    return run_id[0]


def download_artifact(*, run_id: str, output_dir: Path) -> None:
    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "gh",
            "run",
            "download",
            run_id,
            "--name",
            "docs-html",
            "--dir",
            str(output_dir),
        ],
        check=True,
    )


def serve_artifact(*, output_dir: Path, port: int) -> None:
    url = f"http://localhost:{port}"
    print(f"Serving docs artifact from {output_dir} at {url}")
    webbrowser.open(url)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "http.server",
            str(port),
            "--directory",
            str(output_dir),
        ],
        check=True,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download and serve the docs-html artifact from a docbuild run."
    )
    parser.add_argument(
        "pr_number",
        nargs="?",
        type=int,
        help="Pull request number. Defaults to the latest docbuild run.",
    )
    parser.add_argument(
        "--run-id",
        help="GitHub Actions run ID. Defaults to the latest docbuild run.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_DIR,
        help=f"Directory to download the artifact into. Defaults to ./{DEFAULT_DIR}.",
    )
    parser.add_argument("--port", type=int, default=8000, help="Local server port.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_id = args.run_id or latest_docbuild_run_id(pr_number=args.pr_number)
    download_artifact(run_id=run_id, output_dir=args.output_dir)
    serve_artifact(output_dir=args.output_dir, port=args.port)


if __name__ == "__main__":
    main()
