from datetime import datetime

from marshmallow import Schema
from marshmallow.fields import String, Integer, DateTime, Nested
from ..tag.schema import TagSchema
from ..author.schema import AuthorSchema
from ..assignee.schema import AssigneeSchema


class IssueSchema(Schema):
    id: int = Integer()
    status: str = String()
    title: str = String()
    text: str = String()
    assignee: str = Nested(AssigneeSchema)
    tags: list[str] = Nested(TagSchema, many=True)
    author: str = Nested(AuthorSchema)
    created_date: datetime = DateTime()
    modified_date: datetime = DateTime()
