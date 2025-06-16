# external-issue-checker

[![License MIT](https://img.shields.io/badge/Licence-MIT-green)](./LICENSE)
[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

**Lists commits in a Git repository that refer to external issues / pull requests.**

This tool is useful for tracking issues and pull requests that are not managed within
the repository itself  and for which a workaround may have been implemented in the
codebase.

For example sometimes you refer to an issue of another package in a commit
(e.g. *“Apply some workaround while waiting for orga/project#12 to be fixed”*).
In the meantime, maybe the issue has been resolved (and maybe you've redone a commit
like *"Remove the workaround now that orga/project#12 is fixed"*, or not).

It's time to check with `external-issue-checker`!

Currently, it supports GitHub and GitLab issues and pull (or merge) requests, but it
might be extended to support other platforms (such as Bitbucket, Codeberg, etc.) in
the future.

## Demo

![Demo showing terminal being recorded](./misc/demo.svg)

## Instructions for developers

Install the dependencies:

```bash
poetry install
```

Activate the virtual environment:

```bash
poetry env activate
```

Run the test suite:

```bash
poetry run pytest
```

Run the CLI tool:

```bash
poetry run external-issue-checker --help
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
