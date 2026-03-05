"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_query_queries_v1_data_post_render_upload import (
        ExecuteQueryQueriesV1DataPostRenderUPLOAD,
    )

    ExecuteQueryQueriesV1DataPostRenderUPLOADAdapter = TypeAdapter(
        ExecuteQueryQueriesV1DataPostRenderUPLOAD
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_query_queries_v1_data_post_render_upload_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render in an object format compatible with the `/data/v1/events` upload.\n\n###### options\n- `iso_timestamp`: `False`\n- `hierarchical`: `False`\n- `show_levels`: `False`\n- `roll_up`: `True`",
  "enum" : [ "UPLOAD" ]
}
""",
    object_hook=with_example_provider,
)
execute_query_queries_v1_data_post_render_upload_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_query_queries_v1_data_post_render_upload_faker = JSF(
    execute_query_queries_v1_data_post_render_upload_model_schema,
    allow_none_optionals=1,
)


class ExecuteQueryQueriesV1DataPostRenderUPLOADStub:
    """ExecuteQueryQueriesV1DataPostRenderUPLOAD unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_query_queries_v1_data_post_render_upload_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteQueryQueriesV1DataPostRenderUPLOAD":
        """Create ExecuteQueryQueriesV1DataPostRenderUPLOAD stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteQueryQueriesV1DataPostRenderUPLOADAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteQueryQueriesV1DataPostRenderUPLOADAdapter.validate_python(
            json, context={"skip_validation": True}
        )
