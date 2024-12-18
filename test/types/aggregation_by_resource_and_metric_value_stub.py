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
    from waylay.services.queries.models.aggregation_by_resource_and_metric_value import (
        AggregationByResourceAndMetricValue,
    )

    AggregationByResourceAndMetricValueAdapter = TypeAdapter(
        AggregationByResourceAndMetricValue
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

aggregation_by_resource_and_metric_value_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "title" : "Aggregation by Resource or Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_or_Metric_value"
    },
    "description" : "Aggregation methods specified per resource or metric.",
    "nullable" : true
  } ]
}
""",
    object_hook=with_example_provider,
)
aggregation_by_resource_and_metric_value_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

aggregation_by_resource_and_metric_value_faker = JSF(
    aggregation_by_resource_and_metric_value_model_schema, allow_none_optionals=1
)


class AggregationByResourceAndMetricValueStub:
    """AggregationByResourceAndMetricValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregation_by_resource_and_metric_value_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AggregationByResourceAndMetricValue":
        """Create AggregationByResourceAndMetricValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AggregationByResourceAndMetricValueAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregationByResourceAndMetricValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
