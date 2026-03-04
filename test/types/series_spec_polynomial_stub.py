"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.series_spec_polynomial import (
        SeriesSpecPolynomial,
    )

    SeriesSpecPolynomialAdapter = TypeAdapter(SeriesSpecPolynomial)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

series_spec_polynomial_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a polynomial of the lowest possible degree passing trough the data points.",
  "enum" : [ "polynomial" ]
}
""",
    object_hook=with_example_provider,
)
series_spec_polynomial_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_spec_polynomial_faker = JSF(
    series_spec_polynomial_model_schema, allow_none_optionals=1
)


class SeriesSpecPolynomialStub:
    """SeriesSpecPolynomial unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_spec_polynomial_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "SeriesSpecPolynomial":
        """Create SeriesSpecPolynomial stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SeriesSpecPolynomialAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesSpecPolynomialAdapter.validate_python(
            json, context={"skip_validation": True}
        )
