"""Waylay Query: timeseries queries (v1 protocol): apis."""

# import apis into api package
from .execute_queries_api import ExecuteQueriesApi
from .named_queries_api import NamedQueriesApi
from .status_api import StatusApi

__all__ = [
    "ExecuteQueriesApi",
    "NamedQueriesApi",
    "StatusApi",
]
