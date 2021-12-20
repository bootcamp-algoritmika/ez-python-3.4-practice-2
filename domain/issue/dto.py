from dataclasses import dataclass
from typing import List


@dataclass
class CreateIssueDTO:
    status: int
    title: str
    text: str
    assignee: str
    tags: List[str]
    author: str


@dataclass
class UpdateIssueDTO:
    id: int
    status: int
    title: str
    text: str
    assignee: str
    tags: List[str]
    author: str


@dataclass
class PartiallyUpdateIssueDTO:
    id: int
    status: int = None
    title: str = None
    text: str = None
    assignee: str = None
    tags: List[str] = None
    author: str = None
