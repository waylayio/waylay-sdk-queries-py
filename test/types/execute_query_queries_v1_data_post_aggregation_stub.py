"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_query_queries_v1_data_post_aggregation import (
        ExecuteQueryQueriesV1DataPostAggregation,
    )

    ExecuteQueryQueriesV1DataPostAggregationAdapter = TypeAdapter(
        ExecuteQueryQueriesV1DataPostAggregation
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_query_queries_v1_data_post_aggregation_model_schema = json.loads(
    r"""{
  "type" : "string",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationFirst"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationLast"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationMean"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationMedian"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationSum"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationCount"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationCount-numeric"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationCount-non-numeric"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationStd"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationMax"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationMin"
  } ]
}
""",
    object_hook=with_example_provider,
)
execute_query_queries_v1_data_post_aggregation_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_query_queries_v1_data_post_aggregation_faker = JSF(
    execute_query_queries_v1_data_post_aggregation_model_schema, allow_none_optionals=1
)


class ExecuteQueryQueriesV1DataPostAggregationStub:
    """ExecuteQueryQueriesV1DataPostAggregation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_query_queries_v1_data_post_aggregation_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteQueryQueriesV1DataPostAggregation":
        """Create ExecuteQueryQueriesV1DataPostAggregation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteQueryQueriesV1DataPostAggregationAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteQueryQueriesV1DataPostAggregationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
