"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.interpolation_method import InterpolationMethod

    InterpolationMethodAdapter = TypeAdapter(InterpolationMethod)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

interpolation_method_model_schema = json.loads(
    r"""{
  "title" : "Interpolation method",
  "type" : "string",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/InterpolationSpecPad"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecFixed"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecBackfill"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecLinear"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecNearest"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecZero"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecSlinear"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecQuadratic"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecCubic"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecPolynomial"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecSpline"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecFrom_derivatives"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecPchip"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecAkima"
  } ]
}
""",
    object_hook=with_example_provider,
)
interpolation_method_model_schema.update({"definitions": MODEL_DEFINITIONS})

interpolation_method_faker = JSF(
    interpolation_method_model_schema, allow_none_optionals=1
)


class InterpolationMethodStub:
    """InterpolationMethod unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return interpolation_method_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "InterpolationMethod":
        """Create InterpolationMethod stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                InterpolationMethodAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return InterpolationMethodAdapter.validate_python(
            json, context={"skip_validation": True}
        )
