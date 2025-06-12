from typing import Optional
from rich import print
from .git_utils import get_commits_with_external_refs
from .github_api import check_issue_status


def scan(
    path: str,
    token: Optional[str] = None,
):
    """
    Scans the commits of a Git repository and detects references to external
    GitHub issues.

    For each reference found, queries the GitHub API to display the current
    status of the issue.
    """
    print(f"[bold]Analyzing repository:[/] {path}")
    commits = get_commits_with_external_refs(path)

    if not commits:
        print("[yellow]No external references found.[/]")

    for sha, summary, refs in commits:
        print(f"\n[bold cyan]{sha[:7]}[/] - {summary}")
        for org, repo, issue in refs:
            status = check_issue_status(org, repo, issue, token)
            if "error" in status:
                print(f"  [red]❌ {org}/{repo}#{issue}[/] → " f"{status['error']}")
            else:
                print(
                    f"  [green]✔ {org}/{repo}#{issue}[/] → "
                    f"[bold]{status['state'].upper()}[/] - {status['title']}"
                )
