# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol): Service.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

version: 0.5.0

 Execute and store queries on the Waylay timeseries.  Protocol version: v1.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

__version__ = "0.5.0.20240802"

from .service import QueriesService

PLUGINS = [QueriesService]

__all__ = [
    "__version__",
    "QueriesService",
]