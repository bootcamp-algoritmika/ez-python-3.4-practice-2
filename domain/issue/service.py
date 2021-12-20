from typing import List

from adapters.interfaces import IssueServiceI
from domain.issue.dto import CreateIssueDTO, UpdateIssueDTO, PartiallyUpdateIssueDTO
from domain.issue.model import Issue
from domain.issue.storage import IssueStorageI


class IssueService(IssueServiceI):
    def __init__(self, storage: IssueStorageI):
        self.storage = storage

    def get_issues(self, limit: int, offset: int) -> List[Issue]:
        # in real life any filters or something else
        return self.storage.get_all(limit, offset)

    def get_issue(self, issue_id: int) -> Issue:
        return self.storage.get_one(issue_id=issue_id)

    def create_issue(self, issue: CreateIssueDTO) -> int:
        return self.storage.create(issue=issue)

    def delete_issue(self, issue_id: int) -> None:
        return self.storage.delete(issue_id=issue_id)

    def update_issue(self, issue: UpdateIssueDTO) -> None:
        return self.storage.update(issue=issue)

    def partially_update(self, issue: PartiallyUpdateIssueDTO) -> None:
        return self.storage.partially_update(issue=issue)
