"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.series_spec_pad import SeriesSpecPad

    SeriesSpecPadAdapter = TypeAdapter(SeriesSpecPad)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

series_spec_pad_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the value of the first observed point. This method also extrapolates.",
  "enum" : [ "pad" ]
}
""",
    object_hook=with_example_provider,
)
series_spec_pad_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_spec_pad_faker = JSF(series_spec_pad_model_schema, allow_none_optionals=1)


class SeriesSpecPadStub:
    """SeriesSpecPad unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_spec_pad_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "SeriesSpecPad":
        """Create SeriesSpecPad stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SeriesSpecPadAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesSpecPadAdapter.validate_python(
            json, context={"skip_validation": True}
        )
