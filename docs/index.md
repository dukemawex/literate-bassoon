# Research Product Lab

Welcome to the **Research Product Lab** documentation site.  
This site is generated from the meta-repo
[dukemawex/literate-bassoon](https://github.com/dukemawex/literate-bassoon)
and mirrors the README with nicer navigation and full-text search.

---

## Child Repositories

The lab tracks **15 child repositories**.  Each entry below links directly to
its GitHub page and, where enabled, its GitHub Pages documentation site.

| Repository | Description | Pages |
|---|---|---|
| [research-core](https://github.com/dukemawex/research-core) | Core research utilities and shared libraries used across all projects. | [🔗](https://dukemawex.github.io/research-core/) |
| [data-pipeline](https://github.com/dukemawex/data-pipeline) | ETL pipeline for ingesting, transforming, and loading research datasets. | [🔗](https://dukemawex.github.io/data-pipeline/) |
| [ml-models](https://github.com/dukemawex/ml-models) | Machine-learning model training, evaluation, and versioning toolkit. | [🔗](https://dukemawex.github.io/ml-models/) |
| [api-gateway](https://github.com/dukemawex/api-gateway) | Unified REST/GraphQL gateway exposing internal research services. | [🔗](https://dukemawex.github.io/api-gateway/) |
| [frontend-app](https://github.com/dukemawex/frontend-app) | React-based web application for exploring and visualising research outputs. | [🔗](https://dukemawex.github.io/frontend-app/) |
| [auth-service](https://github.com/dukemawex/auth-service) | Authentication and authorisation microservice (OAuth2 / JWT). | [🔗](https://dukemawex.github.io/auth-service/) |
| [data-storage](https://github.com/dukemawex/data-storage) | Abstraction layer for structured and unstructured research data storage. | [🔗](https://dukemawex.github.io/data-storage/) |
| [analytics-engine](https://github.com/dukemawex/analytics-engine) | Real-time analytics engine for aggregating experiment metrics. | [🔗](https://dukemawex.github.io/analytics-engine/) |
| [report-generator](https://github.com/dukemawex/report-generator) | Automated PDF/HTML report generation from experiment results. | [🔗](https://dukemawex.github.io/report-generator/) |
| [notification-service](https://github.com/dukemawex/notification-service) | Event-driven notification service (email, Slack, webhook). | [🔗](https://dukemawex.github.io/notification-service/) |
| [config-manager](https://github.com/dukemawex/config-manager) | Centralised configuration management and secrets distribution. | [🔗](https://dukemawex.github.io/config-manager/) |
| [testing-framework](https://github.com/dukemawex/testing-framework) | Shared test fixtures, mocks, and integration-test harness. | [🔗](https://dukemawex.github.io/testing-framework/) |
| [deployment-tools](https://github.com/dukemawex/deployment-tools) | Infrastructure-as-code and Helm charts for Kubernetes deployments. | [🔗](https://dukemawex.github.io/deployment-tools/) |
| [documentation-hub](https://github.com/dukemawex/documentation-hub) | Aggregated documentation site built from all child-repo doc sources. | [🔗](https://dukemawex.github.io/documentation-hub/) |
| [monitoring-dashboard](https://github.com/dukemawex/monitoring-dashboard) | Grafana dashboards and alerting rules for platform observability. | [🔗](https://dukemawex.github.io/monitoring-dashboard/) |

---

## CI & Pipeline Badges

Each child repo exposes two GitHub Actions workflow badges:

* **CI** — runs unit/integration tests on every push.
* **Pipeline** — runs the full build, test, and deploy pipeline on merges to `main`.

These badges are embedded in the [README](https://github.com/dukemawex/literate-bassoon#child-repositories)
and reflect the live workflow status.

---

## How to Find the Latest Artifacts

1. Navigate to the child repo's **Actions** tab.
2. Select the relevant workflow.
3. Open the latest successful run.
4. Download the artifact from the **Artifacts** section.

Using the GitHub CLI:

```bash
gh run download --repo dukemawex/<child-repo> --name <artifact-name>
```

---

## Quickstart

### Set `GITHUB_TOKEN`

```bash
export GITHUB_TOKEN="ghp_YourPersonalAccessTokenHere"
```

Minimum scope: **`public_repo`**.  For private repos add **`repo`**.

### Run the health check

```bash
pip install requests pyyaml
python scripts/health_check.py --print
```

### Regenerate this docs site

```bash
pip install mkdocs mkdocs-material
mkdocs serve        # live-reload preview at http://127.0.0.1:8000
mkdocs build        # static output in site/
mkdocs gh-deploy    # push to GitHub Pages
```

---

## Contributing

See [Contributing](contributing.md) for instructions on adding a new child
repository to this meta-repo.
