"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_query_queries_v1_data_post_freq_inferred import (
        ExecuteQueryQueriesV1DataPostFreqInferred,
    )

    ExecuteQueryQueriesV1DataPostFreqInferredAdapter = TypeAdapter(
        ExecuteQueryQueriesV1DataPostFreqInferred
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_query_queries_v1_data_post_freq_inferred_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "When `inferred` is specified, the frequency of aggregation will be inferred from the main/first time series. This can be used to regularize the time series",
  "enum" : [ "inferred" ]
}
""",
    object_hook=with_example_provider,
)
execute_query_queries_v1_data_post_freq_inferred_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_query_queries_v1_data_post_freq_inferred_faker = JSF(
    execute_query_queries_v1_data_post_freq_inferred_model_schema,
    allow_none_optionals=1,
)


class ExecuteQueryQueriesV1DataPostFreqInferredStub:
    """ExecuteQueryQueriesV1DataPostFreqInferred unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_query_queries_v1_data_post_freq_inferred_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteQueryQueriesV1DataPostFreqInferred":
        """Create ExecuteQueryQueriesV1DataPostFreqInferred stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteQueryQueriesV1DataPostFreqInferredAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteQueryQueriesV1DataPostFreqInferredAdapter.validate_python(
            json, context={"skip_validation": True}
        )
