"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.default_interpolation_any_of import (
        DefaultInterpolationAnyOf,
    )

    DefaultInterpolationAnyOfAdapter = TypeAdapter(DefaultInterpolationAnyOf)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

default_interpolation_any_of_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/Query-InputPad"
  }, {
    "$ref" : "#/components/schemas/Query-InputFixed"
  }, {
    "$ref" : "#/components/schemas/Query-InputBackfill"
  }, {
    "$ref" : "#/components/schemas/Query-InputLinear"
  }, {
    "$ref" : "#/components/schemas/Query-InputNearest"
  }, {
    "$ref" : "#/components/schemas/Query-InputZero"
  }, {
    "$ref" : "#/components/schemas/Query-InputSlinear"
  }, {
    "$ref" : "#/components/schemas/Query-InputQuadratic"
  }, {
    "$ref" : "#/components/schemas/Query-InputCubic"
  }, {
    "$ref" : "#/components/schemas/Query-InputPolynomial"
  }, {
    "$ref" : "#/components/schemas/Query-InputSpline"
  }, {
    "$ref" : "#/components/schemas/Query-InputFrom_derivatives"
  }, {
    "$ref" : "#/components/schemas/Query-InputPchip"
  }, {
    "$ref" : "#/components/schemas/Query-InputAkima"
  } ]
}
""",
    object_hook=with_example_provider,
)
default_interpolation_any_of_model_schema.update({"definitions": MODEL_DEFINITIONS})

default_interpolation_any_of_faker = JSF(
    default_interpolation_any_of_model_schema, allow_none_optionals=1
)


class DefaultInterpolationAnyOfStub:
    """DefaultInterpolationAnyOf unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return default_interpolation_any_of_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "DefaultInterpolationAnyOf":
        """Create DefaultInterpolationAnyOf stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                DefaultInterpolationAnyOfAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DefaultInterpolationAnyOfAdapter.validate_python(
            json, context={"skip_validation": True}
        )
