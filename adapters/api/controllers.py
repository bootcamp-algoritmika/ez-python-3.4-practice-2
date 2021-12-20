import json

import falcon

from adapters.interfaces import IssueServiceI
from domain.issue.dto import UpdateIssueDTO, PartiallyUpdateIssueDTO, CreateIssueDTO
from domain.issue.exceptions import IssueNotFoundException
from domain.issue.schema import IssueSchema
from domain.issue.model import Issue


class IssueResource:
    def __init__(self, service: IssueServiceI):
        self.service = service

    def on_get(self, req, resp, issue_id):
        try:
            issue: Issue = self.service.get_issue(issue_id=issue_id)
        except IssueNotFoundException as e:
            raise falcon.HTTPNotFound(title=e.message)
        schema = IssueSchema()
        resp.body = json.dumps(schema.dump(issue))
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp, issue_id):
        updated_issue = req.media
        dto = UpdateIssueDTO(id=issue_id, **updated_issue)
        try:
            self.service.update_issue(dto)
        except IssueNotFoundException as e:
            raise falcon.HTTPNotFound(title=e.message)
        resp.status = falcon.HTTP_204

    def on_patch(self, req, resp, issue_id):
        patched_issue = req.media
        dto = PartiallyUpdateIssueDTO(id=issue_id, **patched_issue)
        try:
            self.service.partially_update(dto)
        except IssueNotFoundException as e:
            raise falcon.HTTPNotFound(title=e.message)
        resp.status = falcon.HTTP_204

    def on_delete(self, req, resp, issue_id):
        try:
            self.service.delete_issue(issue_id)
        except IssueNotFoundException as e:
            raise falcon.HTTPNotFound(title=e.message)
        resp.status = falcon.HTTP_204


class IssuesResource:
    def __init__(self, service: IssueServiceI):
        self.service = service

    def on_get(self, req, resp):
        limit = req.get_param_as_int('limit') or 50
        offset = req.get_param_as_int('offset') or 0
        issues: list[Issue] = self.service.get_issues(limit=limit, offset=offset)
        schema = IssueSchema()
        resp.body = json.dumps(schema.dump(issues, many=True))
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = req.get_media()
        new_issue = CreateIssueDTO(**data)
        issue_id: int = self.service.create_issue(new_issue)
        resp.status = falcon.HTTP_201
        resp.location = f'/issues/{issue_id}'
