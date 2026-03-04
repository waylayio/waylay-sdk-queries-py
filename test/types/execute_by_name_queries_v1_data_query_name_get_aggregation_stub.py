"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_by_name_queries_v1_data_query_name_get_aggregation import (
        ExecuteByNameQueriesV1DataQueryNameGetAggregation,
    )

    ExecuteByNameQueriesV1DataQueryNameGetAggregationAdapter = TypeAdapter(
        ExecuteByNameQueriesV1DataQueryNameGetAggregation
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_by_name_queries_v1_data_query_name_get_aggregation_model_schema = json.loads(
    r"""{
  "type" : "string",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationFirst"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationLast"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationMean"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationSum"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationCount"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationStd"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationMax"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationMin"
  } ]
}
""",
    object_hook=with_example_provider,
)
execute_by_name_queries_v1_data_query_name_get_aggregation_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_by_name_queries_v1_data_query_name_get_aggregation_faker = JSF(
    execute_by_name_queries_v1_data_query_name_get_aggregation_model_schema,
    allow_none_optionals=1,
)


class ExecuteByNameQueriesV1DataQueryNameGetAggregationStub:
    """ExecuteByNameQueriesV1DataQueryNameGetAggregation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return (
            execute_by_name_queries_v1_data_query_name_get_aggregation_faker.generate(
                use_defaults=True, use_examples=True
            )
        )

    @classmethod
    def create_instance(cls) -> "ExecuteByNameQueriesV1DataQueryNameGetAggregation":
        """Create ExecuteByNameQueriesV1DataQueryNameGetAggregation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteByNameQueriesV1DataQueryNameGetAggregationAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteByNameQueriesV1DataQueryNameGetAggregationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
