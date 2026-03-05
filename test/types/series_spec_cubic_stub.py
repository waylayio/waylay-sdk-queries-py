"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.series_spec_cubic import SeriesSpecCubic

    SeriesSpecCubicAdapter = TypeAdapter(SeriesSpecCubic)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

series_spec_cubic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 3, which is a piecewise polynomial.",
  "enum" : [ "cubic" ]
}
""",
    object_hook=with_example_provider,
)
series_spec_cubic_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_spec_cubic_faker = JSF(series_spec_cubic_model_schema, allow_none_optionals=1)


class SeriesSpecCubicStub:
    """SeriesSpecCubic unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_spec_cubic_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "SeriesSpecCubic":
        """Create SeriesSpecCubic stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SeriesSpecCubicAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesSpecCubicAdapter.validate_python(
            json, context={"skip_validation": True}
        )
