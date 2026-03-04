"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.interpolation_spec_akima import (
        InterpolationSpecAkima,
    )

    InterpolationSpecAkimaAdapter = TypeAdapter(InterpolationSpecAkima)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

interpolation_spec_akima_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a non-smoothing spline of order 2, called Akima interpolation.",
  "enum" : [ "akima" ]
}
""",
    object_hook=with_example_provider,
)
interpolation_spec_akima_model_schema.update({"definitions": MODEL_DEFINITIONS})

interpolation_spec_akima_faker = JSF(
    interpolation_spec_akima_model_schema, allow_none_optionals=1
)


class InterpolationSpecAkimaStub:
    """InterpolationSpecAkima unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return interpolation_spec_akima_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "InterpolationSpecAkima":
        """Create InterpolationSpecAkima stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                InterpolationSpecAkimaAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return InterpolationSpecAkimaAdapter.validate_python(
            json, context={"skip_validation": True}
        )
