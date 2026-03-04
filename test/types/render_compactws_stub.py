"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.render_compactws import RenderCOMPACTWS

    RenderCOMPACTWSAdapter = TypeAdapter(RenderCOMPACTWS)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

render_compact_ws_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers. Show the time window attributes.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`\n- `include_window_spec`: `True`",
  "enum" : [ "COMPACT_WS" ]
}
""",
    object_hook=with_example_provider,
)
render_compact_ws_model_schema.update({"definitions": MODEL_DEFINITIONS})

render_compact_ws_faker = JSF(render_compact_ws_model_schema, allow_none_optionals=1)


class RenderCOMPACTWSStub:
    """RenderCOMPACTWS unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return render_compact_ws_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "RenderCOMPACTWS":
        """Create RenderCOMPACTWS stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                RenderCOMPACTWSAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RenderCOMPACTWSAdapter.validate_python(
            json, context={"skip_validation": True}
        )
