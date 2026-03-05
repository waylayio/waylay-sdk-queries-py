"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_query_queries_v1_data_post_freq import (
        ExecuteQueryQueriesV1DataPostFreq,
    )

    ExecuteQueryQueriesV1DataPostFreqAdapter = TypeAdapter(
        ExecuteQueryQueriesV1DataPostFreq
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_query_queries_v1_data_post_freq_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Override for the `freq` query attribute.",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostFreqInferred"
  } ]
}
""",
    object_hook=with_example_provider,
)
execute_query_queries_v1_data_post_freq_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_query_queries_v1_data_post_freq_faker = JSF(
    execute_query_queries_v1_data_post_freq_model_schema, allow_none_optionals=1
)


class ExecuteQueryQueriesV1DataPostFreqStub:
    """ExecuteQueryQueriesV1DataPostFreq unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_query_queries_v1_data_post_freq_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteQueryQueriesV1DataPostFreq":
        """Create ExecuteQueryQueriesV1DataPostFreq stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteQueryQueriesV1DataPostFreqAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteQueryQueriesV1DataPostFreqAdapter.validate_python(
            json, context={"skip_validation": True}
        )
