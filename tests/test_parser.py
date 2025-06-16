# type: ignore
from external_issue_checker.parser import (
    extract_external_issues,
    Platform,
    ReferenceType,
)


def test_extract_github_refs():
    msg = "Fixes electron/electron#123 and https://github.com/python/cpython/issues/456"
    refs = extract_external_issues(msg)
    assert (Platform.GITHUB, ReferenceType.ISSUE, "electron", "electron", "123") in refs
    assert (Platform.GITHUB, ReferenceType.ISSUE, "python", "cpython", "456") in refs


def test_extract_nothing():
    msg = "No external references here."
    assert extract_external_issues(msg) == []
