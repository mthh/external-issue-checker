import sys
import typer
from git import InvalidGitRepositoryError
from rich import print
from .git_utils import get_commits_with_external_refs
from .github_api import gh_check_issue_status

app = typer.Typer(
    help="Scans commits for references to external GitHub issues.",
)


@app.command()
def cli_scan(
    path: str = typer.Argument(help="Path to the local Git repository to analyze"),
    token: str | None = typer.Option(
        None,
        "--token",
        "-t",
        help="Personal GitHub token to avoid API limitations.",
    ),
) -> int:
    """
    Scans the commits of a Git repository and detects references to external
    GitHub issues.

    For each reference found, queries the GitHub API to display the current
    status of the issue.
    """
    try:
        commits = get_commits_with_external_refs(path)
    except InvalidGitRepositoryError:
        print(f"[red]Error: Invalid Git repository at {path}[/]")
        sys.exit(1)
    except Exception as e:
        print(f"[red]Unexpected error: {e}[/]")
        sys.exit(1)

    print(f"[bold]Analyzing repository:[/] {path}")

    if not commits:
        print("[yellow]No external references found.[/]")

    for sha, summary, refs in commits:
        print(f"\n[bold cyan]{sha[:7]}[/] - {summary}")
        for org, repo, issue in refs:
            status = gh_check_issue_status(org, repo, issue, token)
            if "error" in status:
                print(f"  [red]❌ {org}/{repo}#{issue}[/] → " f"{status['error']}")
            else:
                print(
                    f"  [green]✔ {org}/{repo}#{issue}[/] → "
                    f"[bold]{status['state'].upper()}[/] - {status['title']}"
                )

    sys.exit(0)


if __name__ == "__main__":
    app()
