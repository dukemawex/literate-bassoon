# Contributing

Thank you for your interest in contributing to the Research Product Lab meta-repo!

---

## How to Add a New Child Repository

Follow these steps whenever a new child repository is created and needs to be tracked
by this meta-repo.

### 1 — Add an entry to `repos.yaml`

Open `repos.yaml` and append a new entry under the `repos` list:

```yaml
  - name: my-new-repo
    description: A short description of what this repository does.
    pages_url: https://dukemawex.github.io/my-new-repo/
```

* `name` must match the exact GitHub repository name.
* `description` should be one concise sentence.
* `pages_url` is the expected GitHub Pages URL.  If Pages is not enabled yet,
  set it to the URL it _will_ have once enabled.

### 2 — Add a row to the Child Repositories table in `README.md`

Find the **Child Repositories** table in `README.md` and add a new row using the
same pattern as existing rows:

```markdown
| [my-new-repo](https://github.com/dukemawex/my-new-repo) | A short description. | [![CI](https://github.com/dukemawex/my-new-repo/actions/workflows/ci.yml/badge.svg)](https://github.com/dukemawex/my-new-repo/actions/workflows/ci.yml) | [![Pipeline](https://github.com/dukemawex/my-new-repo/actions/workflows/pipeline.yml/badge.svg)](https://github.com/dukemawex/my-new-repo/actions/workflows/pipeline.yml) | [Pages](https://dukemawex.github.io/my-new-repo/) |
```

Replace the workflow file names (`ci.yml`, `pipeline.yml`) with the actual names
used in the child repo if they differ.

### 3 — Add a row to the `docs/index.md` table

Mirror the same addition in `docs/index.md` to keep the MkDocs site in sync.

### 4 — Open a Pull Request

Commit your changes to a feature branch and open a PR against `main`.  The PR
description should include:

* A link to the new child repository.
* Confirmation that `repos.yaml`, `README.md`, and `docs/index.md` have all been
  updated.

---

## Running the Health Check After Adding a Repo

After the PR is merged, trigger the health workflow manually to verify the new repo
is detected correctly:

1. Go to [Actions → Repo Health Check](https://github.com/dukemawex/literate-bassoon/actions/workflows/health.yml).
2. Click **Run workflow → Run workflow**.
3. Confirm the new repo appears in the updated README health table.

---

## Code Style

* Python files must be compatible with **Python 3.11+**.
* Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
* Keep YAML files tidy: 2-space indentation, no trailing whitespace.
* Wrap Markdown lines at 100 characters where practical.

---

## Questions?

Open a [GitHub Issue](https://github.com/dukemawex/literate-bassoon/issues) and
tag it with the `question` label.
