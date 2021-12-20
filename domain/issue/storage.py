from abc import ABC, abstractmethod

from domain.issue.model import Issue
from domain.issue.dto import CreateIssueDTO, UpdateIssueDTO, PartiallyUpdateIssueDTO


class IssueStorageI(ABC):

    @abstractmethod
    def get_one(self, issue_id: int) -> Issue:
        pass

    @abstractmethod
    def get_all(self, limit: int, offset: int) -> list[Issue]:
        pass

    @abstractmethod
    def create(self, issue: CreateIssueDTO) -> int:
        pass

    @abstractmethod
    def update(self, issue: UpdateIssueDTO) -> None:
        pass

    @abstractmethod
    def partially_update(self, issue: PartiallyUpdateIssueDTO) -> None:
        pass

    @abstractmethod
    def delete(self, issue_id: int) -> None:
        pass
