# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.from_override import FromOverride

    FromOverrideAdapter = TypeAdapter(FromOverride)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

from_override__model_schema = json.loads(
    r"""{
  "title" : "From Override.",
  "type" : "string",
  "oneOf" : [ {
    "title" : "ISO8601 absolute timestamp",
    "pattern" : "[0-9]{4}-[0-9]{2}-[0-9]{2}(T.*)?",
    "type" : "string",
    "description" : "A date or date-time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format. When no timezone is specified, the UTC timezone is assumed (`+00:00`)",
    "format" : "date-time",
    "example" : "2018-03-21T12:23:00+01:00"
  }, {
    "title" : "UNIX epoch milliseconds",
    "minimum" : 0,
    "type" : "integer",
    "description" : "Absolute timestamp milliseconds in unix epoch since 1970-01-01.",
    "example" : 1534836422284
  }, {
    "title" : "ISO8601 Period Before Now",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "Specifies a timestamp before _now_ as a period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
from_override__model_schema.update({"definitions": MODEL_DEFINITIONS})

from_override__faker = JSF(from_override__model_schema, allow_none_optionals=1)


class FromOverrideStub:
    """FromOverride unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return from_override__faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "FromOverride":
        """Create FromOverride stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                FromOverrideAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return FromOverrideAdapter.validate_python(
            json, context={"skip_validation": True}
        )
