# 🔬 Research Product Lab — Meta-Repo

This repository is the **single source of truth** for the 15 child repositories that make up the Research Product Lab. It provides a live health dashboard, MkDocs documentation site, and automation scripts to keep everything in sync.

---

## 📋 Table of Contents

1. [Child Repositories](#child-repositories)
2. [Repo Health Dashboard](#repo-health-dashboard)
3. [How to Find the Latest Artifacts](#how-to-find-the-latest-artifacts)
4. [Quickstart](#quickstart)
5. [Docs Site](#docs-site)
6. [Contributing](#contributing)

---

## 📦 Child Repositories

| Repository | Description | CI | Pipeline | Docs |
|---|---|:---:|:---:|:---:|
| [research-core](https://github.com/dukemawex/research-core) | Core research utilities and shared libraries used across all projects. | [![CI](https://github.com/dukemawex/research-core/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/research-core/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/research-core/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/research-core/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/research-core/) |
| [data-pipeline](https://github.com/dukemawex/data-pipeline) | ETL pipeline for ingesting, transforming, and loading research datasets. | [![CI](https://github.com/dukemawex/data-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/data-pipeline/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/data-pipeline/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/data-pipeline/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/data-pipeline/) |
| [ml-models](https://github.com/dukemawex/ml-models) | Machine-learning model training, evaluation, and versioning toolkit. | [![CI](https://github.com/dukemawex/ml-models/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/ml-models/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/ml-models/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/ml-models/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/ml-models/) |
| [api-gateway](https://github.com/dukemawex/api-gateway) | Unified REST/GraphQL gateway exposing internal research services. | [![CI](https://github.com/dukemawex/api-gateway/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/api-gateway/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/api-gateway/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/api-gateway/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/api-gateway/) |
| [frontend-app](https://github.com/dukemawex/frontend-app) | React-based web application for exploring and visualising research outputs. | [![CI](https://github.com/dukemawex/frontend-app/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/frontend-app/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/frontend-app/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/frontend-app/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/frontend-app/) |
| [auth-service](https://github.com/dukemawex/auth-service) | Authentication and authorisation microservice (OAuth2 / JWT). | [![CI](https://github.com/dukemawex/auth-service/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/auth-service/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/auth-service/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/auth-service/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/auth-service/) |
| [data-storage](https://github.com/dukemawex/data-storage) | Abstraction layer for structured and unstructured research data storage. | [![CI](https://github.com/dukemawex/data-storage/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/data-storage/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/data-storage/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/data-storage/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/data-storage/) |
| [analytics-engine](https://github.com/dukemawex/analytics-engine) | Real-time analytics engine for aggregating experiment metrics. | [![CI](https://github.com/dukemawex/analytics-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/analytics-engine/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/analytics-engine/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/analytics-engine/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/analytics-engine/) |
| [report-generator](https://github.com/dukemawex/report-generator) | Automated PDF/HTML report generation from experiment results. | [![CI](https://github.com/dukemawex/report-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/report-generator/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/report-generator/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/report-generator/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/report-generator/) |
| [notification-service](https://github.com/dukemawex/notification-service) | Event-driven notification service (email, Slack, webhook). | [![CI](https://github.com/dukemawex/notification-service/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/notification-service/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/notification-service/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/notification-service/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/notification-service/) |
| [config-manager](https://github.com/dukemawex/config-manager) | Centralised configuration management and secrets distribution. | [![CI](https://github.com/dukemawex/config-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/config-manager/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/config-manager/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/config-manager/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/config-manager/) |
| [testing-framework](https://github.com/dukemawex/testing-framework) | Shared test fixtures, mocks, and integration-test harness. | [![CI](https://github.com/dukemawex/testing-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/testing-framework/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/testing-framework/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/testing-framework/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/testing-framework/) |
| [deployment-tools](https://github.com/dukemawex/deployment-tools) | Infrastructure-as-code and Helm charts for Kubernetes deployments. | [![CI](https://github.com/dukemawex/deployment-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/deployment-tools/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/deployment-tools/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/deployment-tools/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/deployment-tools/) |
| [documentation-hub](https://github.com/dukemawex/documentation-hub) | Aggregated documentation site built from all child-repo doc sources. | [![CI](https://github.com/dukemawex/documentation-hub/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/documentation-hub/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/documentation-hub/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/documentation-hub/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/documentation-hub/) |
| [monitoring-dashboard](https://github.com/dukemawex/monitoring-dashboard) | Grafana dashboards and alerting rules for platform observability. | [![CI](https://github.com/dukemawex/monitoring-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/monitoring-dashboard/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/monitoring-dashboard/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/monitoring-dashboard/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/monitoring-dashboard/) |

---

## 🩺 Repo Health Dashboard

The table below is automatically updated every day at 06:00 UTC by the
[Health Check workflow](.github/workflows/health.yml).  
You can also trigger it manually from the
[Actions tab](https://github.com/dukemawex/literate-bassoon/actions/workflows/health.yml).

<!-- HEALTH_TABLE_START -->
> Last updated: (not yet generated — run the health workflow to populate this table)

| Repository | Exists | Actions | Pages | Pages URL | Notes |
|---|:---:|:---:|:---:|---|---|
| research-core | ❓ | ❓ | ❓ | — | run workflow |
| data-pipeline | ❓ | ❓ | ❓ | — | run workflow |
| ml-models | ❓ | ❓ | ❓ | — | run workflow |
| api-gateway | ❓ | ❓ | ❓ | — | run workflow |
| frontend-app | ❓ | ❓ | ❓ | — | run workflow |
| auth-service | ❓ | ❓ | ❓ | — | run workflow |
| data-storage | ❓ | ❓ | ❓ | — | run workflow |
| analytics-engine | ❓ | ❓ | ❓ | — | run workflow |
| report-generator | ❓ | ❓ | ❓ | — | run workflow |
| notification-service | ❓ | ❓ | ❓ | — | run workflow |
| config-manager | ❓ | ❓ | ❓ | — | run workflow |
| testing-framework | ❓ | ❓ | ❓ | — | run workflow |
| deployment-tools | ❓ | ❓ | ❓ | — | run workflow |
| documentation-hub | ❓ | ❓ | ❓ | — | run workflow |
| monitoring-dashboard | ❓ | ❓ | ❓ | — | run workflow |
<!-- HEALTH_TABLE_END -->

---

## 📥 How to Find the Latest Artifacts

Each child repo's CI/pipeline workflow uploads build artifacts to GitHub Actions.
To download the most-recent artifact for any repo:

1. Navigate to the child repo on GitHub (links in the table above).
2. Click **Actions** in the top navigation bar.
3. Select the relevant workflow (e.g. `CI` or `Pipeline`).
4. Click the **latest successful run** in the list.
5. Scroll to the **Artifacts** section at the bottom of the run summary page.
6. Click the artifact name to download it as a `.zip` file.

> **Tip:** You can also use the GitHub CLI:
> ```bash
> gh run download --repo dukemawex/<child-repo> --name <artifact-name>
> ```

For this meta-repo, the latest health report is uploaded as the `health-report`
artifact each time the Health Check workflow runs:

1. Go to [Actions → Repo Health Check](https://github.com/dukemawex/literate-bassoon/actions/workflows/health.yml).
2. Click the most recent run.
3. Download the **health-report** artifact (`artifacts/health_report.json`).

---

## 🚀 Quickstart

### 1 — Set `GITHUB_TOKEN` locally

```bash
export GITHUB_TOKEN="ghp_YourPersonalAccessTokenHere"
```

The token needs at minimum **`public_repo`** scope.  
For private repositories, add the **`repo`** scope.

> Create a token at <https://github.com/settings/tokens>.

---

### 2 — Run the health check locally

```bash
# Install dependencies (once)
pip install requests pyyaml

# Run the check — writes artifacts/health_report.json
python scripts/health_check.py

# Run and print a human-readable summary to the terminal
python scripts/health_check.py --print

# Override the repos list or output path
python scripts/health_check.py --repos path/to/repos.yaml --output /tmp/report.json
```

---

### 3 — Regenerate the docs site

```bash
# Install MkDocs and the Material theme (once)
pip install mkdocs mkdocs-material

# Serve locally with live-reload
mkdocs serve
# → open http://127.0.0.1:8000

# Build a static site into the site/ directory
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

---

## 📚 Docs Site

The MkDocs documentation site mirrors this README but with richer navigation and
search.  Once deployed it is available at:

<https://dukemawex.github.io/literate-bassoon/>

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on adding a new child
repository to this meta-repo.

---

## 🗂️ Repo Structure

```
literate-bassoon/
├── .github/
│   └── workflows/
│       └── health.yml          # Daily + on-demand health check workflow
├── artifacts/
│   └── health_report.json      # Auto-generated; committed by the workflow
├── docs/
│   ├── index.md                # MkDocs home page (mirrors README)
│   └── health.md               # Live health dashboard page
├── scripts/
│   └── health_check.py         # Python 3.11 health-check tool
├── CONTRIBUTING.md             # How to add a new child repo
├── README.md                   # This file — the dashboard
├── mkdocs.yml                  # MkDocs site configuration
└── repos.yaml                  # Source of truth for the 15 child repos
```