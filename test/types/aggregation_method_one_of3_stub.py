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
    from waylay.services.queries.models.aggregation_method_one_of3 import (
        AggregationMethodOneOf3,
    )

    AggregationMethodOneOf3Adapter = TypeAdapter(AggregationMethodOneOf3)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

aggregation_method_one_of_3_model_schema = json.loads(
    r"""{
  "title" : "AggregationMethod_oneOf_3",
  "type" : "string",
  "description" : "Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.",
  "enum" : [ "median" ]
}
""",
    object_hook=with_example_provider,
)
aggregation_method_one_of_3_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregation_method_one_of_3_faker = JSF(
    aggregation_method_one_of_3_model_schema, allow_none_optionals=1
)


class AggregationMethodOneOf3Stub:
    """AggregationMethodOneOf3 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregation_method_one_of_3_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AggregationMethodOneOf3":
        """Create AggregationMethodOneOf3 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AggregationMethodOneOf3Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregationMethodOneOf3Adapter.validate_python(
            json, context={"skip_validation": True}
        )