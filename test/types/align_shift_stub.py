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
    from waylay.services.queries.models.align_shift import AlignShift

    AlignShiftAdapter = TypeAdapter(AlignShift)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

align_shift_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Possible values for `align.shift`.\n\n* 'backward': keep the window size of the original interval specification,\n   shifting back.\n* 'forward': keep the window size of the original interval specification,\n   shifting forward.\n* 'wrap': enlarge the window size to include all of the original interval.\n\nWhen not specified, 'backward' is used.",
  "enum" : [ "backward", "forward", "wrap" ]
}
""",
    object_hook=with_example_provider,
)
align_shift_model_schema.update({"definitions": MODEL_DEFINITIONS})

align_shift_faker = JSF(align_shift_model_schema, allow_none_optionals=1)


class AlignShiftStub:
    """AlignShift unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return align_shift_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlignShift":
        """Create AlignShift stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(AlignShiftAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlignShiftAdapter.validate_python(
            json, context={"skip_validation": True}
        )