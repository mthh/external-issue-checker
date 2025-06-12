from typing import Optional
import httpx


def gh_check_issue_status(org: str, repo: str, issue: str, token: Optional[str] = None):
    headers = {"Authorization": f"token {token}"} if token else {}
    url = f"https://api.github.com/repos/{org}/{repo}/issues/{issue}"
    r = httpx.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        return {"title": data["title"], "state": data["state"], "url": data["html_url"]}
    else:
        return {"error": f"Issue not found: {org}/{repo}#{issue}"}
