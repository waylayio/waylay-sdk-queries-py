# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

AlignmentTimezone = Union[
    Annotated[
        str,
        "[ICANN timezone identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)",
    ],
    Annotated[str, "[UTC offset](https://en.wikipedia.org/wiki/UTC_offset)"],
]
""" The timezone to use when shifting boundaries, especially at day granularity. Also affects the rendering of timestamps when `render.iso_timestamp` is enabled.  When not specified, the `UTC` timezone is used. ."""