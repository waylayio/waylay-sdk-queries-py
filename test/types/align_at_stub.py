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
    from waylay.services.queries.models.align_at import AlignAt

    AlignAtAdapter = TypeAdapter(AlignAt)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

align_at_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Possible values for `align.at`.\n\n* 'grid' Align to a fixed grid (possibly using timezone information)\n* 'from' Align a the `from` boundary\n* 'until' Align a the `until` boundary\n* 'boundary' Align a the `from` boundary if specified,\n   otherwise the `until` boundary.\n\nWhen not specified, 'grid' is used.",
  "enum" : [ "grid", "boundary", "from", "until" ]
}
""",
    object_hook=with_example_provider,
)
align_at_model_schema.update({"definitions": MODEL_DEFINITIONS})

align_at_faker = JSF(align_at_model_schema, allow_none_optionals=1)


class AlignAtStub:
    """AlignAt unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return align_at_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlignAt":
        """Create AlignAt stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(AlignAtAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlignAtAdapter.validate_python(json, context={"skip_validation": True})
