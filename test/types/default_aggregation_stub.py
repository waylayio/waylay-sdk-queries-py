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
    from waylay.services.queries.models.default_aggregation import DefaultAggregation

    DefaultAggregationAdapter = TypeAdapter(DefaultAggregation)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

default_aggregation_model_schema = json.loads(
    r"""{
  "title" : "Default Aggregation",
  "description" : "Default aggregation method(s) for the series in the query.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/AggregationMethod"
  }, {
    "title" : "Aggregations",
    "type" : "array",
    "description" : "Aggregation methods, leading to sepearate series.",
    "nullable" : true,
    "items" : {
      "$ref" : "#/components/schemas/Aggregations_inner"
    }
  }, {
    "title" : "Aggregation by Resource or Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_or_Metric"
    },
    "description" : "Aggregation methods specified per resource or metric.",
    "nullable" : true
  }, {
    "title" : "Aggregation by Resource and Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_and_Metric"
    },
    "description" : "Aggregation methods specified per resource and metric.",
    "nullable" : true
  } ]
}
""",
    object_hook=with_example_provider,
)
default_aggregation_model_schema.update({"definitions": MODEL_DEFINITIONS})

default_aggregation_faker = JSF(
    default_aggregation_model_schema, allow_none_optionals=1
)


class DefaultAggregationStub:
    """DefaultAggregation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return default_aggregation_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "DefaultAggregation":
        """Create DefaultAggregation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                DefaultAggregationAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DefaultAggregationAdapter.validate_python(
            json, context={"skip_validation": True}
        )