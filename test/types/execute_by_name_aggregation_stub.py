"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_by_name_aggregation import (
        ExecuteByNameAggregation,
    )

    ExecuteByNameAggregationAdapter = TypeAdapter(ExecuteByNameAggregation)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_by_name_aggregation_model_schema = json.loads(
    r"""{
  "type" : "string",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationFirst"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationLast"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationMean"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationMedian"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationSum"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationCount"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationCount-numeric"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationCount-non-numeric"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationStd"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationMax"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameAggregationMin"
  } ]
}
""",
    object_hook=with_example_provider,
)
execute_by_name_aggregation_model_schema.update({"definitions": MODEL_DEFINITIONS})

execute_by_name_aggregation_faker = JSF(
    execute_by_name_aggregation_model_schema, allow_none_optionals=1
)


class ExecuteByNameAggregationStub:
    """ExecuteByNameAggregation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_by_name_aggregation_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteByNameAggregation":
        """Create ExecuteByNameAggregation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteByNameAggregationAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteByNameAggregationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
