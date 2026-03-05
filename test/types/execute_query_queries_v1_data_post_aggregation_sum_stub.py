"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_query_queries_v1_data_post_aggregation_sum import (
        ExecuteQueryQueriesV1DataPostAggregationSum,
    )

    ExecuteQueryQueriesV1DataPostAggregationSumAdapter = TypeAdapter(
        ExecuteQueryQueriesV1DataPostAggregationSum
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_query_queries_v1_data_post_aggregation_sum_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "The sum of all values summarizes the data for the sample interval.",
  "enum" : [ "sum" ]
}
""",
    object_hook=with_example_provider,
)
execute_query_queries_v1_data_post_aggregation_sum_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_query_queries_v1_data_post_aggregation_sum_faker = JSF(
    execute_query_queries_v1_data_post_aggregation_sum_model_schema,
    allow_none_optionals=1,
)


class ExecuteQueryQueriesV1DataPostAggregationSumStub:
    """ExecuteQueryQueriesV1DataPostAggregationSum unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_query_queries_v1_data_post_aggregation_sum_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteQueryQueriesV1DataPostAggregationSum":
        """Create ExecuteQueryQueriesV1DataPostAggregationSum stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteQueryQueriesV1DataPostAggregationSumAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteQueryQueriesV1DataPostAggregationSumAdapter.validate_python(
            json, context={"skip_validation": True}
        )
