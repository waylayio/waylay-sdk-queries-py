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
    from waylay.services.queries.models.aggregation_method_one_of import (
        AggregationMethodOneOf,
    )

    AggregationMethodOneOfAdapter = TypeAdapter(AggregationMethodOneOf)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

aggregation_method_one_of_model_schema = json.loads(
    r"""{
  "title" : "AggregationMethod_oneOf",
  "type" : "string",
  "description" : "Use the first value (in time) to represent all data for the sample interval.",
  "enum" : [ "first" ]
}
""",
    object_hook=with_example_provider,
)
aggregation_method_one_of_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregation_method_one_of_faker = JSF(
    aggregation_method_one_of_model_schema, allow_none_optionals=1
)


class AggregationMethodOneOfStub:
    """AggregationMethodOneOf unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregation_method_one_of_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AggregationMethodOneOf":
        """Create AggregationMethodOneOf stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AggregationMethodOneOfAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregationMethodOneOfAdapter.validate_python(
            json, context={"skip_validation": True}
        )
