from dataclasses import dataclass, field

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from ..issue.model import Issue
from ..mapper import mapper_registry, metadata


@dataclass
class Author:
    id: int = field(init=False)
    name: str = None
    issues: list[Issue] = field(default_factory=list)


author_table = Table(
    'author', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
)
mapper_registry.map_imperatively(
    Author, author_table,
    properties={
        'issues': relationship(Issue, lazy='subquery', backref='author')
    }
)
