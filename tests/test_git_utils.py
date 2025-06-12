from external_issue_checker.git_utils import extract_external_issues


def test_extract_from_message():
    msg = "Fixes org/repo#12"
    assert extract_external_issues(msg) == [("org", "repo", "12")]
