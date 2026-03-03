#!/usr/bin/env python3
"""
scripts/health_check.py
=======================
Repo-Health checker for the research-product-lab meta-repo.

Reads repos.yaml, queries the GitHub REST API for each child repository, and
produces a JSON report at artifacts/health_report.json.

Requirements
------------
- Python 3.11+
- PyYAML  (pip install pyyaml)
- requests (pip install requests)

Environment variables
---------------------
GITHUB_TOKEN   GitHub personal access token (required for higher rate limits and
               private-repo access).  Set this locally or let the Actions workflow
               inject it automatically.

Usage
-----
    export GITHUB_TOKEN=ghp_...
    python scripts/health_check.py

    # Pretty-print the report straight to stdout as well:
    python scripts/health_check.py --print

    # Override the path to repos.yaml:
    python scripts/health_check.py --repos path/to/repos.yaml
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GITHUB_API = "https://api.github.com"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REPOS_YAML = REPO_ROOT / "repos.yaml"
DEFAULT_OUTPUT = REPO_ROOT / "artifacts" / "health_report.json"


# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------


def _session(token: str | None) -> requests.Session:
    """Return a requests Session with auth and accept headers set."""
    session = requests.Session()
    session.headers.update(
        {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    if token:
        session.headers["Authorization"] = f"Bearer {token}"
    return session


def _get(session: requests.Session, url: str) -> tuple[int, dict | list | None]:
    """Issue a GET request and return (status_code, parsed_body_or_None)."""
    try:
        response = session.get(url, timeout=15)
        if response.status_code == 200:
            return response.status_code, response.json()
        return response.status_code, None
    except requests.RequestException as exc:
        print(f"  WARNING: request failed for {url}: {exc}", file=sys.stderr)
        return 0, None


# ---------------------------------------------------------------------------
# Per-repo checks
# ---------------------------------------------------------------------------


def check_repo(
    session: requests.Session, owner: str, name: str, expected_pages_url: str
) -> dict:
    """Return a health dict for a single repository."""
    result: dict = {
        "repo": f"{owner}/{name}",
        "exists": False,
        "private": None,
        "default_branch": None,
        "actions_enabled": False,
        "pages_enabled": False,
        "pages_url": None,
        "expected_pages_url": expected_pages_url,
        "pages_url_matches": False,
        "open_issues": None,
        "last_push": None,
        "errors": [],
    }

    # --- Repository metadata ---
    status, repo_data = _get(session, f"{GITHUB_API}/repos/{owner}/{name}")
    if status != 200 or repo_data is None:
        result["errors"].append(f"repo not found (HTTP {status})")
        return result

    result["exists"] = True
    result["private"] = repo_data.get("private", False)
    result["default_branch"] = repo_data.get("default_branch")
    result["open_issues"] = repo_data.get("open_issues_count")
    result["last_push"] = repo_data.get("pushed_at")

    # --- Actions workflows (presence implies Actions is enabled) ---
    wf_status, wf_data = _get(
        session, f"{GITHUB_API}/repos/{owner}/{name}/actions/workflows"
    )
    if wf_status == 200 and wf_data:
        result["actions_enabled"] = wf_data.get("total_count", 0) > 0
    elif wf_status == 404:
        result["actions_enabled"] = False
    else:
        # Could be a permissions issue; record but don't mark as disabled
        result["errors"].append(f"could not determine Actions status (HTTP {wf_status})")

    # --- GitHub Pages ---
    pages_status, pages_data = _get(
        session, f"{GITHUB_API}/repos/{owner}/{name}/pages"
    )
    if pages_status == 200 and pages_data:
        result["pages_enabled"] = True
        result["pages_url"] = pages_data.get("html_url")
        if result["pages_url"]:
            # Normalise trailing slashes before comparison
            actual = result["pages_url"].rstrip("/")
            expected = expected_pages_url.rstrip("/")
            result["pages_url_matches"] = actual == expected
    elif pages_status == 404:
        result["pages_enabled"] = False
    else:
        result["errors"].append(f"could not determine Pages status (HTTP {pages_status})")

    return result


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------


def build_report(repos_yaml: Path, token: str | None) -> dict:
    """Read repos.yaml, run all checks, and return the full report dict."""
    with repos_yaml.open() as fh:
        config = yaml.safe_load(fh)

    owner: str = config["owner"]
    repos: list[dict] = config["repos"]

    session = _session(token)

    results = []
    for repo in repos:
        name: str = repo["name"]
        expected_pages_url: str = repo.get("pages_url", "")
        print(f"  Checking {owner}/{name} …", file=sys.stderr)
        results.append(check_repo(session, owner, name, expected_pages_url))

    summary = {
        "total": len(results),
        "existing": sum(1 for r in results if r["exists"]),
        "actions_enabled": sum(1 for r in results if r["actions_enabled"]),
        "pages_enabled": sum(1 for r in results if r["pages_enabled"]),
        "pages_url_matches": sum(1 for r in results if r["pages_url_matches"]),
        "with_errors": sum(1 for r in results if r["errors"]),
    }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "owner": owner,
        "summary": summary,
        "repos": results,
    }


def print_report(report: dict) -> None:
    """Print a human-readable summary of the report to stdout."""
    s = report["summary"]
    print(f"\n{'='*60}")
    print(f"  Repo Health Report — {report['generated_at']}")
    print(f"  Owner: {report['owner']}")
    print(f"{'='*60}")
    print(f"  Total repos checked : {s['total']}")
    print(f"  Repos found         : {s['existing']}")
    print(f"  Actions enabled     : {s['actions_enabled']}")
    print(f"  Pages enabled       : {s['pages_enabled']}")
    print(f"  Pages URL matches   : {s['pages_url_matches']}")
    print(f"  Repos with errors   : {s['with_errors']}")
    print(f"{'='*60}\n")

    header = f"  {'Repo':<30} {'Exists':<7} {'Actions':<9} {'Pages':<7} {'Errors'}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for r in report["repos"]:
        name = r["repo"].split("/")[-1]
        exists = "yes" if r["exists"] else "NO"
        actions = "yes" if r["actions_enabled"] else "no"
        pages = "yes" if r["pages_enabled"] else "no"
        errors = ", ".join(r["errors"]) if r["errors"] else "—"
        print(f"  {name:<30} {exists:<7} {actions:<9} {pages:<7} {errors}")
    print()


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check health of child repositories listed in repos.yaml."
    )
    parser.add_argument(
        "--repos",
        type=Path,
        default=DEFAULT_REPOS_YAML,
        help="Path to repos.yaml (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Path to write JSON report (default: %(default)s)",
    )
    parser.add_argument(
        "--print",
        dest="print_report",
        action="store_true",
        help="Print a human-readable summary to stdout after writing the JSON report.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print(
            "WARNING: GITHUB_TOKEN is not set. "
            "Requests will be unauthenticated (lower rate limit, no private repos).",
            file=sys.stderr,
        )

    print("Running repo health checks …", file=sys.stderr)
    report = build_report(args.repos, token)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as fh:
        json.dump(report, fh, indent=2)
    print(f"Report written to {args.output}", file=sys.stderr)

    if args.print_report:
        print_report(report)


if __name__ == "__main__":
    main()
