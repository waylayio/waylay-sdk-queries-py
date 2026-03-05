"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.alignment_grid import AlignmentGrid

    AlignmentGridAdapter = TypeAdapter(AlignmentGrid)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

alignment_grid_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Align to a fixed grid defined by the alignment `frequency` and `timezone`.",
  "enum" : [ "grid" ]
}
""",
    object_hook=with_example_provider,
)
alignment_grid_model_schema.update({"definitions": MODEL_DEFINITIONS})

alignment_grid_faker = JSF(alignment_grid_model_schema, allow_none_optionals=1)


class AlignmentGridStub:
    """AlignmentGrid unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alignment_grid_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AlignmentGrid":
        """Create AlignmentGrid stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlignmentGridAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlignmentGridAdapter.validate_python(
            json, context={"skip_validation": True}
        )
