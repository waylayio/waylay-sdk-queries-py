# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.render_mode_one_of6 import RenderModeOneOf6

    RenderModeOneOf6Adapter = TypeAdapter(RenderModeOneOf6)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

render_mode_one_of_6_model_schema = json.loads(
    r"""{
  "title" : "_RenderMode_oneOf_6",
  "type" : "string",
  "description" : "Render an hierarchical object for each observation. Shows an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `True`\n- `show_levels`: `True`\n- `roll_up`: `True`",
  "enum" : [ "HIER_DICT" ]
}
""",
    object_hook=with_example_provider,
)
render_mode_one_of_6_model_schema.update({"definitions": MODEL_DEFINITIONS})

render_mode_one_of_6_faker = JSF(
    render_mode_one_of_6_model_schema, allow_none_optionals=1
)


class RenderModeOneOf6Stub:
    """RenderModeOneOf6 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return render_mode_one_of_6_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "RenderModeOneOf6":
        """Create RenderModeOneOf6 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                RenderModeOneOf6Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RenderModeOneOf6Adapter.validate_python(
            json, context={"skip_validation": True}
        )
