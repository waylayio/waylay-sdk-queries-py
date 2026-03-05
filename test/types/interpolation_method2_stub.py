"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.interpolation_method2 import (
        InterpolationMethod2,
    )

    InterpolationMethod2Adapter = TypeAdapter(InterpolationMethod2)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

interpolation_method_2_model_schema = json.loads(
    r"""{
  "title" : "Interpolation method",
  "type" : "string",
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
interpolation_method_2_model_schema.update({"definitions": MODEL_DEFINITIONS})

interpolation_method_2_faker = JSF(
    interpolation_method_2_model_schema, allow_none_optionals=1
)


class InterpolationMethod2Stub:
    """InterpolationMethod2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return interpolation_method_2_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "InterpolationMethod2":
        """Create InterpolationMethod2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                InterpolationMethod2Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return InterpolationMethod2Adapter.validate_python(
            json, context={"skip_validation": True}
        )
