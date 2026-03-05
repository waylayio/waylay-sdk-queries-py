"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.interpolation_specification import (
        InterpolationSpecification,
    )

    InterpolationSpecificationAdapter = TypeAdapter(InterpolationSpecification)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

interpolation_specification__model_schema = json.loads(
    r"""{
  "title" : "Interpolation Specification.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/InterpolationSpec_3"
  }, {
    "$ref" : "#/components/schemas/Interpolation_Specification__anyOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
interpolation_specification__model_schema.update({"definitions": MODEL_DEFINITIONS})

interpolation_specification__faker = JSF(
    interpolation_specification__model_schema, allow_none_optionals=1
)


class InterpolationSpecificationStub:
    """InterpolationSpecification unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return interpolation_specification__faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "InterpolationSpecification":
        """Create InterpolationSpecification stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                InterpolationSpecificationAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return InterpolationSpecificationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
