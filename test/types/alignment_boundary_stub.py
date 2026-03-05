"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.alignment_boundary import AlignmentBoundary

    AlignmentBoundaryAdapter = TypeAdapter(AlignmentBoundary)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

alignment_boundary_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Align a the `from` boundary if specified, otherwise use the `until` boundary (specfied or computed)",
  "enum" : [ "boundary" ]
}
""",
    object_hook=with_example_provider,
)
alignment_boundary_model_schema.update({"definitions": MODEL_DEFINITIONS})

alignment_boundary_faker = JSF(alignment_boundary_model_schema, allow_none_optionals=1)


class AlignmentBoundaryStub:
    """AlignmentBoundary unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alignment_boundary_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlignmentBoundary":
        """Create AlignmentBoundary stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlignmentBoundaryAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlignmentBoundaryAdapter.validate_python(
            json, context={"skip_validation": True}
        )
