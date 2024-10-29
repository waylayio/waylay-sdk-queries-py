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
    from waylay.services.queries.models.render_mode_one_of1 import RenderModeOneOf1

    RenderModeOneOf1Adapter = TypeAdapter(RenderModeOneOf1)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

render_mode_one_of_1_model_schema = json.loads(
    r"""{
  "title" : "_RenderMode_oneOf_1",
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`",
  "enum" : [ "COMPACT" ]
}
""",
    object_hook=with_example_provider,
)
render_mode_one_of_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

render_mode_one_of_1_faker = JSF(
    render_mode_one_of_1_model_schema, allow_none_optionals=1
)


class RenderModeOneOf1Stub:
    """RenderModeOneOf1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return render_mode_one_of_1_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "RenderModeOneOf1":
        """Create RenderModeOneOf1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                RenderModeOneOf1Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RenderModeOneOf1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
