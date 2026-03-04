"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_by_name_queries_v1_data_query_name_get_render_headerrow import (
        ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROW,
    )

    ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROWAdapter = TypeAdapter(
        ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROW
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_by_name_queries_v1_data_query_name_get_render_header_row_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers. Includes an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`",
  "enum" : [ "HEADER_ROW" ]
}
""",
        object_hook=with_example_provider,
    )
)
execute_by_name_queries_v1_data_query_name_get_render_header_row_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_by_name_queries_v1_data_query_name_get_render_header_row_faker = JSF(
    execute_by_name_queries_v1_data_query_name_get_render_header_row_model_schema,
    allow_none_optionals=1,
)


class ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROWStub:
    """ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROW unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_by_name_queries_v1_data_query_name_get_render_header_row_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROW":
        """Create ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROW stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROWAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERROWAdapter.validate_python(
            json, context={"skip_validation": True}
        )
