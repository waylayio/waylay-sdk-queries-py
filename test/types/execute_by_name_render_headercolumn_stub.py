"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_by_name_render_headercolumn import (
        ExecuteByNameRenderHEADERCOLUMN,
    )

    ExecuteByNameRenderHEADERCOLUMNAdapter = TypeAdapter(
        ExecuteByNameRenderHEADERCOLUMN
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_by_name_render_header_column_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Renders row index in `rows`, and each series as a values array.\n\nThe series are prefixed by their series attributes.The `rows` index is prefixed by the labels for these attributes.\n\n###### options\n- `iso_timestamp`: `True`\n- `header_array`: `column`\n- `roll_up`: `False`\n- `data_axis`: `row`",
  "enum" : [ "HEADER_COLUMN" ]
}
""",
    object_hook=with_example_provider,
)
execute_by_name_render_header_column_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_by_name_render_header_column_faker = JSF(
    execute_by_name_render_header_column_model_schema, allow_none_optionals=1
)


class ExecuteByNameRenderHEADERCOLUMNStub:
    """ExecuteByNameRenderHEADERCOLUMN unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_by_name_render_header_column_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteByNameRenderHEADERCOLUMN":
        """Create ExecuteByNameRenderHEADERCOLUMN stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteByNameRenderHEADERCOLUMNAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteByNameRenderHEADERCOLUMNAdapter.validate_python(
            json, context={"skip_validation": True}
        )
