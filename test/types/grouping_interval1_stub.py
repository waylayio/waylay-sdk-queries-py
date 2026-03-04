"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.grouping_interval1 import GroupingInterval1

    GroupingInterval1Adapter = TypeAdapter(GroupingInterval1)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

grouping_interval_1_model_schema = json.loads(
    r"""{
  "title" : "Grouping interval",
  "type" : "string",
  "description" : "Interval used to aggregate or regularize data. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  }, {
    "$ref" : "#/components/schemas/Query-OutputInferred"
  } ]
}
""",
    object_hook=with_example_provider,
)
grouping_interval_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

grouping_interval_1_faker = JSF(
    grouping_interval_1_model_schema, allow_none_optionals=1
)


class GroupingInterval1Stub:
    """GroupingInterval1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return grouping_interval_1_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "GroupingInterval1":
        """Create GroupingInterval1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GroupingInterval1Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GroupingInterval1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
