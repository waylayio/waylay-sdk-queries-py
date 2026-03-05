"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_query_queries_v1_data_post_aggregation_mean import (
        ExecuteQueryQueriesV1DataPostAggregationMean,
    )

    ExecuteQueryQueriesV1DataPostAggregationMeanAdapter = TypeAdapter(
        ExecuteQueryQueriesV1DataPostAggregationMean
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_query_queries_v1_data_post_aggregation_mean_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the mean value: The sum of values divided by number of observations.",
  "enum" : [ "mean" ]
}
""",
    object_hook=with_example_provider,
)
execute_query_queries_v1_data_post_aggregation_mean_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_query_queries_v1_data_post_aggregation_mean_faker = JSF(
    execute_query_queries_v1_data_post_aggregation_mean_model_schema,
    allow_none_optionals=1,
)


class ExecuteQueryQueriesV1DataPostAggregationMeanStub:
    """ExecuteQueryQueriesV1DataPostAggregationMean unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_query_queries_v1_data_post_aggregation_mean_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteQueryQueriesV1DataPostAggregationMean":
        """Create ExecuteQueryQueriesV1DataPostAggregationMean stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteQueryQueriesV1DataPostAggregationMeanAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteQueryQueriesV1DataPostAggregationMeanAdapter.validate_python(
            json, context={"skip_validation": True}
        )
