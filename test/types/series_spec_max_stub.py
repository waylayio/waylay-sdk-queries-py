"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.series_spec_max import SeriesSpecMax

    SeriesSpecMaxAdapter = TypeAdapter(SeriesSpecMax)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

series_spec_max_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the maximum of all values in the sample interval.",
  "enum" : [ "max" ]
}
""",
    object_hook=with_example_provider,
)
series_spec_max_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_spec_max_faker = JSF(series_spec_max_model_schema, allow_none_optionals=1)


class SeriesSpecMaxStub:
    """SeriesSpecMax unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_spec_max_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "SeriesSpecMax":
        """Create SeriesSpecMax stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SeriesSpecMaxAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesSpecMaxAdapter.validate_python(
            json, context={"skip_validation": True}
        )
