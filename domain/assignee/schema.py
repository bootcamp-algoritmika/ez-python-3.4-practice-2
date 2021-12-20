from marshmallow import Schema, post_dump
from marshmallow.fields import String


class AssigneeSchema(Schema):
    name = String()

    @post_dump
    def postdump_assignee(self, data: dict, **kwargs):
        return data['name']
