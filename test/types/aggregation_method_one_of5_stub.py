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
    from waylay.services.queries.models.aggregation_method_one_of5 import (
        AggregationMethodOneOf5,
    )

    AggregationMethodOneOf5Adapter = TypeAdapter(AggregationMethodOneOf5)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

aggregation_method_one_of_5_model_schema = json.loads(
    r"""{
  "title" : "AggregationMethod_oneOf_5",
  "type" : "string",
  "description" : "Use the count of observations in the sample interval.",
  "enum" : [ "count" ]
}
""",
    object_hook=with_example_provider,
)
aggregation_method_one_of_5_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregation_method_one_of_5_faker = JSF(
    aggregation_method_one_of_5_model_schema, allow_none_optionals=1
)


class AggregationMethodOneOf5Stub:
    """AggregationMethodOneOf5 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregation_method_one_of_5_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AggregationMethodOneOf5":
        """Create AggregationMethodOneOf5 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AggregationMethodOneOf5Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregationMethodOneOf5Adapter.validate_python(
            json, context={"skip_validation": True}
        )
