"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.interpolation_method3 import (
        InterpolationMethod3,
    )

    InterpolationMethod3Adapter = TypeAdapter(InterpolationMethod3)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

interpolation_method_3_model_schema = json.loads(
    r"""{
  "title" : "Interpolation method",
  "type" : "string",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/SeriesSpecPad"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecFixed"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecBackfill"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecLinear"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecNearest"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecZero"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecSlinear"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecQuadratic"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecCubic"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecPolynomial"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecSpline"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecFrom_derivatives"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecPchip"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecAkima"
  } ]
}
""",
    object_hook=with_example_provider,
)
interpolation_method_3_model_schema.update({"definitions": MODEL_DEFINITIONS})

interpolation_method_3_faker = JSF(
    interpolation_method_3_model_schema, allow_none_optionals=1
)


class InterpolationMethod3Stub:
    """InterpolationMethod3 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return interpolation_method_3_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "InterpolationMethod3":
        """Create InterpolationMethod3 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                InterpolationMethod3Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return InterpolationMethod3Adapter.validate_python(
            json, context={"skip_validation": True}
        )
