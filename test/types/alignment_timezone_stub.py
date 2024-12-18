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
    from waylay.services.queries.models.alignment_timezone import AlignmentTimezone

    AlignmentTimezoneAdapter = TypeAdapter(AlignmentTimezone)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alignment_timezone__model_schema = json.loads(
    r"""{
  "title" : "Alignment Timezone.",
  "type" : "string",
  "description" : "\nThe timezone to use when shifting boundaries, especially\nat day granularity.\nAlso affects the rendering of timestamps when\n`render.iso_timestamp` is enabled.\n\nWhen not specified, the `UTC` timezone is used.\n",
  "oneOf" : [ {
    "title" : "Timezone Identifier",
    "type" : "string",
    "description" : "[ICANN timezone identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)"
  }, {
    "title" : "UTC Offset",
    "pattern" : "(+|-)\\d\\d:\\d\\d",
    "type" : "string",
    "description" : "[UTC offset](https://en.wikipedia.org/wiki/UTC_offset)"
  } ]
}
""",
    object_hook=with_example_provider,
)
alignment_timezone__model_schema.update({"definitions": MODEL_DEFINITIONS})

alignment_timezone__faker = JSF(
    alignment_timezone__model_schema, allow_none_optionals=1
)


class AlignmentTimezoneStub:
    """AlignmentTimezone unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alignment_timezone__faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlignmentTimezone":
        """Create AlignmentTimezone stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlignmentTimezoneAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlignmentTimezoneAdapter.validate_python(
            json, context={"skip_validation": True}
        )
