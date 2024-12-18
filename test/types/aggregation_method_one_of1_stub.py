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
    from waylay.services.queries.models.aggregation_method_one_of1 import (
        AggregationMethodOneOf1,
    )

    AggregationMethodOneOf1Adapter = TypeAdapter(AggregationMethodOneOf1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

aggregation_method_one_of_1_model_schema = json.loads(
    r"""{
  "title" : "AggregationMethod_oneOf_1",
  "type" : "string",
  "description" : "Use the last value (in time) to represent all data for the sample interval.",
  "enum" : [ "last" ]
}
""",
    object_hook=with_example_provider,
)
aggregation_method_one_of_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregation_method_one_of_1_faker = JSF(
    aggregation_method_one_of_1_model_schema, allow_none_optionals=1
)


class AggregationMethodOneOf1Stub:
    """AggregationMethodOneOf1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregation_method_one_of_1_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AggregationMethodOneOf1":
        """Create AggregationMethodOneOf1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AggregationMethodOneOf1Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregationMethodOneOf1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
