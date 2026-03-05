"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.alignment_until import AlignmentUntil

    AlignmentUntilAdapter = TypeAdapter(AlignmentUntil)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

alignment_until_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Align a the `until` window boundary",
  "enum" : [ "until" ]
}
""",
    object_hook=with_example_provider,
)
alignment_until_model_schema.update({"definitions": MODEL_DEFINITIONS})

alignment_until_faker = JSF(alignment_until_model_schema, allow_none_optionals=1)


class AlignmentUntilStub:
    """AlignmentUntil unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alignment_until_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlignmentUntil":
        """Create AlignmentUntil stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlignmentUntilAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlignmentUntilAdapter.validate_python(
            json, context={"skip_validation": True}
        )
