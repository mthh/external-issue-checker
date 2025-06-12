from git import Repo
from .parser import extract_external_issues


def get_commits_with_external_refs(repo_path="."):
    repo = Repo(repo_path)
    result = []
    for commit in repo.iter_commits():
        refs = extract_external_issues(commit.message)
        if refs:
            result.append((commit.hexsha, commit.summary, refs))
    return result
