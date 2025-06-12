import typer
from .scan import scan

app = typer.Typer(
    help="Scans commits for references to external GitHub issues.",
)


@app.command()
def cli_scan(
    path: str = typer.Argument(help="Path to the local Git repository to analyze"),
    token: str = typer.Option(
        None,
        "--token",
        "-t",
        help="Personal GitHub token to avoid API limitations.",
    ),
):
    """
    Scans the commits of a Git repository and detects references to external
    GitHub issues.

    For each reference found, queries the GitHub API to display the current
    status of the issue.
    """
    scan(path, token)


if __name__ == "__main__":
    app()
