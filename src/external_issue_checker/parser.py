import re
from typing import List, Tuple

EXTERNAL_ISSUE_PATTERNS = [
    re.compile(r"(?P<org>[\w-]+)/(?P<repo>[\w-]+)#(?P<issue>\d+)"),
    re.compile(
        r"https://github\.com/(?P<org>[\w-]+)/(?P<repo>[\w-]+)/issues/(?P<issue>\d+)"
    ),
]


def extract_external_issues(commit_message: str) -> List[Tuple[str, str, str]]:
    found = []
    for pattern in EXTERNAL_ISSUE_PATTERNS:
        for match in pattern.finditer(commit_message):
            found.append(
                (match.group("org"), match.group("repo"), match.group("issue"))
            )
    return found
