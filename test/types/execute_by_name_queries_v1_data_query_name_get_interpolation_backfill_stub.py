"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_by_name_queries_v1_data_query_name_get_interpolation_backfill import (
        ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfill,
    )

    ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfillAdapter = TypeAdapter(
        ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfill
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_by_name_queries_v1_data_query_name_get_interpolation_backfill_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Same as pad, but using the last observed value. This method also extrapolates",
  "enum" : [ "backfill" ]
}
""",
        object_hook=with_example_provider,
    )
)
execute_by_name_queries_v1_data_query_name_get_interpolation_backfill_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_by_name_queries_v1_data_query_name_get_interpolation_backfill_faker = JSF(
    execute_by_name_queries_v1_data_query_name_get_interpolation_backfill_model_schema,
    allow_none_optionals=1,
)


class ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfillStub:
    """ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfill unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_by_name_queries_v1_data_query_name_get_interpolation_backfill_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(
        cls,
    ) -> "ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfill":
        """Create ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfill stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfillAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfillAdapter.validate_python(
            json, context={"skip_validation": True}
        )
