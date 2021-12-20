from dataclasses import dataclass, field

from sqlalchemy.orm import relationship
from sqlalchemy import Table, ForeignKey, Column, Integer, String

from ..mapper import mapper_registry, metadata
from ..issue.model import Issue


@dataclass
class Tag:
    id: int = field(init=False)
    name: str = None
    issues: list[Issue] = field(default_factory=list)
    
    
tag_table = Table(
    'tag', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
)

tag_issue_table = Table(
    'tag_issue', metadata,
    Column('tags_id', Integer, ForeignKey('issue.id'), primary_key=True),
    Column('issues_id', Integer, ForeignKey('tag.id'), primary_key=True)
)

mapper_registry.map_imperatively(
    Tag, tag_table,
    properties={
        'issues': relationship(Issue, secondary=tag_issue_table, lazy='subquery', backref='tags')
    }
)
