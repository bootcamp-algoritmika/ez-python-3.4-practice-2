from abc import ABC, abstractmethod

from domain.issue.dto import *
from domain.issue.model import Issue


class IssueServiceI(ABC):
    @abstractmethod
    def get_issues(self, limit: int, offset: int) -> List[Issue]: pass

    @abstractmethod
    def get_issue(self, issue_id) -> Issue: pass

    @abstractmethod
    def create_issue(self, issue: CreateIssueDTO) -> int: pass

    @abstractmethod
    def delete_issue(self, issue_id): pass

    @abstractmethod
    def update_issue(self, issue: UpdateIssueDTO): pass

    @abstractmethod
    def partially_update(self, issue: PartiallyUpdateIssueDTO): pass
