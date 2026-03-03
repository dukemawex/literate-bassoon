# Repo Health Dashboard

This page reflects the most recently generated health report produced by the
[Repo Health Check](.github/workflows/health.yml) GitHub Actions workflow.

The workflow runs **daily at 06:00 UTC** and can also be triggered manually from the
[Actions tab](https://github.com/dukemawex/literate-bassoon/actions/workflows/health.yml).

---

## What Is Checked

For each of the 15 child repositories the workflow verifies:

| Check | How |
|---|---|
| **Exists** | GitHub REST API `GET /repos/{owner}/{repo}` returns 200 |
| **Actions enabled** | `GET /repos/{owner}/{repo}/actions/workflows` returns at least one workflow |
| **Pages enabled** | `GET /repos/{owner}/{repo}/pages` returns 200 |
| **Pages URL matches** | The live Pages URL equals the expected URL in `repos.yaml` |

---

## Latest Health Report

The latest `artifacts/health_report.json` is committed back to the repository
after each workflow run.  Download it directly:

```bash
gh run download \
  --repo dukemawex/literate-bassoon \
  --name health-report
```

Or view the live README table on the
[repository home page](https://github.com/dukemawex/literate-bassoon#repo-health-dashboard).

---

## Running Locally

```bash
export GITHUB_TOKEN="ghp_..."
pip install requests pyyaml
python scripts/health_check.py --print
```

The JSON report is written to `artifacts/health_report.json` and the
human-readable summary is printed to the terminal.

---

## Triggering the Workflow Manually

1. Go to [Actions → Repo Health Check](https://github.com/dukemawex/literate-bassoon/actions/workflows/health.yml).
2. Click **Run workflow**.
3. Optionally tick **Print human-readable report to workflow log**.
4. Click **Run workflow** again to start the job.

After the run completes the README health table and `artifacts/health_report.json`
are automatically committed back to the repository.
