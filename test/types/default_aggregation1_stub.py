"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.default_aggregation1 import DefaultAggregation1

    DefaultAggregation1Adapter = TypeAdapter(DefaultAggregation1)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

default_aggregation_1_model_schema = json.loads(
    r"""{
  "title" : "Default Aggregation",
  "description" : "Default aggregation method(s) for the series in the query.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Aggregation_1"
  }, {
    "title" : "Aggregations",
    "type" : "array",
    "description" : "Aggregation methods, leading to sepearate series.",
    "nullable" : true,
    "items" : {
      "$ref" : "#/components/schemas/Aggregations_inner_1"
    }
  }, {
    "title" : "Aggregation by Resource or Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_or_Metric_value_1"
    },
    "description" : "Aggregation methods specified per resource or metric.",
    "nullable" : true
  }, {
    "title" : "Aggregation by Resource and Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_and_Metric_value_1"
    },
    "description" : "Aggregation methods specified per resource and metric.",
    "nullable" : true
  } ]
}
""",
    object_hook=with_example_provider,
)
default_aggregation_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

default_aggregation_1_faker = JSF(
    default_aggregation_1_model_schema, allow_none_optionals=1
)


class DefaultAggregation1Stub:
    """DefaultAggregation1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return default_aggregation_1_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "DefaultAggregation1":
        """Create DefaultAggregation1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                DefaultAggregation1Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DefaultAggregation1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
