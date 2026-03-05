"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_query_queries_v1_data_post_render_hierdict import (
        ExecuteQueryQueriesV1DataPostRenderHIERDICT,
    )

    ExecuteQueryQueriesV1DataPostRenderHIERDICTAdapter = TypeAdapter(
        ExecuteQueryQueriesV1DataPostRenderHIERDICT
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_query_queries_v1_data_post_render_hier_dict_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render an hierarchical object for each observation. Shows an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `True`\n- `show_levels`: `True`\n- `roll_up`: `True`",
  "enum" : [ "HIER_DICT" ]
}
""",
    object_hook=with_example_provider,
)
execute_query_queries_v1_data_post_render_hier_dict_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_query_queries_v1_data_post_render_hier_dict_faker = JSF(
    execute_query_queries_v1_data_post_render_hier_dict_model_schema,
    allow_none_optionals=1,
)


class ExecuteQueryQueriesV1DataPostRenderHIERDICTStub:
    """ExecuteQueryQueriesV1DataPostRenderHIERDICT unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_query_queries_v1_data_post_render_hier_dict_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteQueryQueriesV1DataPostRenderHIERDICT":
        """Create ExecuteQueryQueriesV1DataPostRenderHIERDICT stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteQueryQueriesV1DataPostRenderHIERDICTAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteQueryQueriesV1DataPostRenderHIERDICTAdapter.validate_python(
            json, context={"skip_validation": True}
        )
