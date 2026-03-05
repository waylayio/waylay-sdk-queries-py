"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.default_interpolation1_any_of import (
        DefaultInterpolation1AnyOf,
    )

    DefaultInterpolation1AnyOfAdapter = TypeAdapter(DefaultInterpolation1AnyOf)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

default_interpolation_1_any_of_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/Query-OutputPad"
  }, {
    "$ref" : "#/components/schemas/Query-OutputFixed"
  }, {
    "$ref" : "#/components/schemas/Query-OutputBackfill"
  }, {
    "$ref" : "#/components/schemas/Query-OutputLinear"
  }, {
    "$ref" : "#/components/schemas/Query-OutputNearest"
  }, {
    "$ref" : "#/components/schemas/Query-OutputZero"
  }, {
    "$ref" : "#/components/schemas/Query-OutputSlinear"
  }, {
    "$ref" : "#/components/schemas/Query-OutputQuadratic"
  }, {
    "$ref" : "#/components/schemas/Query-OutputCubic"
  }, {
    "$ref" : "#/components/schemas/Query-OutputPolynomial"
  }, {
    "$ref" : "#/components/schemas/Query-OutputSpline"
  }, {
    "$ref" : "#/components/schemas/Query-OutputFrom_derivatives"
  }, {
    "$ref" : "#/components/schemas/Query-OutputPchip"
  }, {
    "$ref" : "#/components/schemas/Query-OutputAkima"
  } ]
}
""",
    object_hook=with_example_provider,
)
default_interpolation_1_any_of_model_schema.update({"definitions": MODEL_DEFINITIONS})

default_interpolation_1_any_of_faker = JSF(
    default_interpolation_1_any_of_model_schema, allow_none_optionals=1
)


class DefaultInterpolation1AnyOfStub:
    """DefaultInterpolation1AnyOf unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return default_interpolation_1_any_of_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "DefaultInterpolation1AnyOf":
        """Create DefaultInterpolation1AnyOf stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                DefaultInterpolation1AnyOfAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DefaultInterpolation1AnyOfAdapter.validate_python(
            json, context={"skip_validation": True}
        )
