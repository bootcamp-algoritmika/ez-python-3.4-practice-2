from enum import Enum

from sqlalchemy.orm import subqueryload

from domain.assignee import Assignee
from domain.author import Author
from domain.issue.exceptions import IssueNotFoundException
from domain.issue.model import Issue
from domain.tag.model import Tag
from domain.issue.storage import IssueStorageI
from domain.issue.dto import CreateIssueDTO, UpdateIssueDTO, PartiallyUpdateIssueDTO
from adapters.db.db_init import Session


class IssueStatus(Enum):
    NEW = 1
    TO_APPROVE = 2
    APPROVED = 3
    DECLINED = 4


class IssueStorage(IssueStorageI):

    def create(self, issue: CreateIssueDTO) -> int:
        with Session() as session:
            new_issue = Issue(
                status=issue.status,
                title=issue.title,
                text=issue.text,
                assignee=self.get_assignee(assignee=issue.assignee, session=session),
                tags=self.get_tags(tags=issue.tags, session=session),
                author=self.get_author(author=issue.author, session=session)
            )
            session.add(new_issue)
            session.flush()
            new_issue_id = new_issue.id
            session.commit()
        return new_issue_id

    def update(self, issue: UpdateIssueDTO):
        with Session() as session:
            issue_query: Issue = session.query(Issue).filter(Issue.id == issue.id).one_or_none()
            if not issue_query:
                raise IssueNotFoundException(message="issue not found")
            issue_query.status = issue.status
            issue_query.title = issue.title
            issue_query.text = issue.text
            issue_query.assignee = self.get_assignee(assignee=issue.assignee, session=session)
            issue_query.tags = self.get_tags(tags=issue.tags, session=session)
            issue_query.author = self.get_author(author=issue.author, session=session)
            session.flush()
            session.commit()
        return issue

    def partially_update(self, issue: PartiallyUpdateIssueDTO):
        with Session() as session:
            issue_query: Issue = session.query(Issue).filter(Issue.id == issue.id).one_or_none()
            if not issue_query:
                raise IssueNotFoundException(message="issue not found")
            if issue.status is not None:
                issue_query.status = issue.status
            if issue.status is not None:
                issue_query.title = issue.title
            if issue.status is not None:
                issue_query.text = issue.text
            if issue.status is not None:
                issue_query.assignee = self.get_assignee(assignee=issue.assignee, session=session)
            if issue.status is not None:
                issue_query.tags = self.get_tags(tags=issue.tags, session=session)
            if issue.status is not None:
                issue_query.author = self.get_author(author=issue.author, session=session)
            session.flush()
            session.commit()
        return issue

    def delete(self, issue_id: int):
        with Session() as session:
            issue_query = session.query(Issue).filter(Issue.id == issue_id).one_or_none()
            if not issue_query:
                raise IssueNotFoundException(message="issue not found")
            session.delete(issue_query)
            session.commit()

    def get_one(self, issue_id: str):
        with Session() as session:
            issue_query = session.query(Issue).options(
                subqueryload(Issue.author),
                subqueryload(Issue.assignee),
                subqueryload(Issue.tags)
            ).filter(Issue.id == issue_id).one_or_none()
            if not issue_query:
                raise IssueNotFoundException(message="issue not found")
        return issue_query

    def get_all(self, limit: int, offset: int):
        with Session() as session:
            issues = session.query(Issue).options(
                subqueryload(Issue.author),
                subqueryload(Issue.assignee),
                subqueryload(Issue.tags)
            ).offset(offset).limit(limit).all()
        return issues

    def get_tags(self, session: Session, tags: list[str]) -> list[Tag]:
        query_tags: list[Tag] = []
        for tag in tags:
            query_tag = session.query(Tag).filter(Tag.name == tag).one_or_none()
            if not query_tag:
                session.add(Tag(name=tag))
                session.flush()
                query_tag = session.query(Tag).filter(Tag.name == tag).first()
            query_tags.append(query_tag)
        return query_tags

    def get_author(self, session: Session, author: str) -> Author:
        author_query = session.query(Author).filter(Author.name == author).one_or_none()
        if not author_query:
            session.add(Author(name=author))
            session.flush()
            author_query = session.query(Author).filter(Author.name == author).first()
        return author_query

    def get_assignee(self, session: Session, assignee: str) -> Assignee:
        assignee_query = session.query(Assignee).filter(Assignee.name == assignee).one_or_none()
        if not assignee_query:
            session.add(Assignee(name=assignee))
            session.flush()
            assignee_query = session.query(Assignee).filter(Assignee.name == assignee).first()
        return assignee_query
