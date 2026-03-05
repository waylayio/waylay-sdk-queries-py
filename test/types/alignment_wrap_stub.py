"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.alignment_wrap import AlignmentWrap

    AlignmentWrapAdapter = TypeAdapter(AlignmentWrap)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

alignment_wrap_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Shift first boundary backward, and last boundary forward to align with the grid",
  "enum" : [ "wrap" ]
}
""",
    object_hook=with_example_provider,
)
alignment_wrap_model_schema.update({"definitions": MODEL_DEFINITIONS})

alignment_wrap_faker = JSF(alignment_wrap_model_schema, allow_none_optionals=1)


class AlignmentWrapStub:
    """AlignmentWrap unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alignment_wrap_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlignmentWrap":
        """Create AlignmentWrap stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlignmentWrapAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlignmentWrapAdapter.validate_python(
            json, context={"skip_validation": True}
        )
