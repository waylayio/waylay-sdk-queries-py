"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.render_csv import RenderCSV

    RenderCSVAdapter = TypeAdapter(RenderCSV)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

render_csv_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render in csv format with row headers.\n\n###### options\n- `iso_timestamp`: `False`",
  "enum" : [ "CSV" ]
}
""",
    object_hook=with_example_provider,
)
render_csv_model_schema.update({"definitions": MODEL_DEFINITIONS})

render_csv_faker = JSF(render_csv_model_schema, allow_none_optionals=1)


class RenderCSVStub:
    """RenderCSV unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return render_csv_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "RenderCSV":
        """Create RenderCSV stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(RenderCSVAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RenderCSVAdapter.validate_python(json, context={"skip_validation": True})
