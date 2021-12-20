from dataclasses import dataclass, field

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from ..issue.model import Issue
from ..mapper import mapper_registry, metadata


@dataclass
class Assignee:
    id: int = field(init=False)
    name: str = None
    issues: list[Issue] = field(default_factory=list)


assignee_table = Table(
    'assignee', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
)
mapper_registry.map_imperatively(
    Assignee, assignee_table,
    properties={
        'issues': relationship(Issue, lazy='subquery', backref='assignee')
    }
)
