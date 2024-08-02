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
    from waylay.services.queries.models.aggregation_method import AggregationMethod

    AggregationMethodAdapter = TypeAdapter(AggregationMethod)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

aggregation_method_model_schema = json.loads(
    r"""{
  "type" : "string",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf"
  }, {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf_1"
  }, {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf_2"
  }, {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf_3"
  }, {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf_4"
  }, {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf_5"
  }, {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf_6"
  }, {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf_7"
  }, {
    "$ref" : "#/components/schemas/AggregationMethod_oneOf_8"
  } ]
}
""",
    object_hook=with_example_provider,
)
aggregation_method_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregation_method_faker = JSF(aggregation_method_model_schema, allow_none_optionals=1)


class AggregationMethodStub:
    """AggregationMethod unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregation_method_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AggregationMethod":
        """Create AggregationMethod stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AggregationMethodAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregationMethodAdapter.validate_python(
            json, context={"skip_validation": True}
        )
