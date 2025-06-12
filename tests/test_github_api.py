from external_issue_checker.github_api import check_issue_status
from httpx import Response, Request
from unittest.mock import patch


@patch("external_issue_checker.github_api.httpx.get")
def test_check_issue_status_ok(mock_get):
    mock_get.return_value = Response(
        200,
        json={
            "title": "Test Issue",
            "state": "open",
            "html_url": "https://github.com/org/repo/issues/1",
        },
        request=Request("GET", "https://api.github.com/"),
    )
    status = check_issue_status("org", "repo", "1")
    assert status["state"] == "open"
