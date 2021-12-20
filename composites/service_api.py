import falcon
from falcon import App

from adapters.api.controllers import IssuesResource, IssueResource
from adapters.db.issue.storage import IssueStorage
from domain.issue.service import IssueService

storage = IssueStorage()
service = IssueService(storage=storage)


def create_app() -> App:
    app = falcon.App()

    issues_view = IssuesResource(service=service)
    issue_view = IssueResource(service=service)

    app.add_route('/issues/', issues_view)
    app.add_route('/issues/{issue_id}', issue_view)
    return app
