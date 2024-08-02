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
    from waylay.services.queries.models.grouping_interval_override import (
        GroupingIntervalOverride,
    )

    GroupingIntervalOverrideAdapter = TypeAdapter(GroupingIntervalOverride)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

grouping_interval_override_model_schema = json.loads(
    r"""{
  "title" : "Grouping Interval Override",
  "type" : "string",
  "description" : "Override for the `freq` query attribute.",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  }, {
    "$ref" : "#/components/schemas/Grouping_Interval_Override_oneOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
grouping_interval_override_model_schema.update({"definitions": MODEL_DEFINITIONS})

grouping_interval_override_faker = JSF(
    grouping_interval_override_model_schema, allow_none_optionals=1
)


class GroupingIntervalOverrideStub:
    """GroupingIntervalOverride unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return grouping_interval_override_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GroupingIntervalOverride":
        """Create GroupingIntervalOverride stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GroupingIntervalOverrideAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GroupingIntervalOverrideAdapter.validate_python(
            json, context={"skip_validation": True}
        )