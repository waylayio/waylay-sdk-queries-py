"""Queries Service."""

from waylay.sdk import ApiClient, WaylayService

from ..api.execute_queries_api import ExecuteQueriesApi
from ..api.named_queries_api import NamedQueriesApi
from ..api.status_api import StatusApi


class QueriesService(WaylayService):
    """Queries Service Class."""

    name = "queries"
    title = "Queries Service"

    execute_queries: ExecuteQueriesApi
    named_queries: NamedQueriesApi
    status: StatusApi

    def __init__(self, api_client: ApiClient):
        """Create the queries service."""

        super().__init__(api_client)
        self.execute_queries = ExecuteQueriesApi(api_client)
        self.named_queries = NamedQueriesApi(api_client)
        self.status = StatusApi(api_client)
