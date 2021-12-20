from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..assignee.model import Assignee
    from ..author.model import Author
    from ..tag.model import Tag

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, Table
from sqlalchemy.sql import func

from ..mapper import mapper_registry, metadata


@dataclass
class Issue:
    id: int = field(init=False)
    status: int = None
    title: str = None
    text: str = None
    assignee: Assignee = None
    author: Author = None
    tags: list[Tag] = field(default_factory=list)
    created_date: datetime = None
    modified_date: datetime = None


issue_table = Table(
    'issue', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('status', Integer),
    Column('title', String),
    Column('text', Text),
    Column('created_date', TIMESTAMP, server_default=func.now()),
    Column("assignee_id", Integer, ForeignKey("assignee.id")),
    Column("author_id", Integer, ForeignKey("author.id")),
    Column('modified_date', TIMESTAMP, server_default=func.now(), onupdate=func.now())
)
mapper_registry.map_imperatively(
    Issue, issue_table
)
