# coding: utf-8
"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.interpolation_spec import InterpolationSpec

    InterpolationSpecAdapter = TypeAdapter(InterpolationSpec)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

interpolation_spec_model_schema = json.loads(
    r"""{
  "required" : [ "method" ],
  "type" : "object",
  "properties" : {
    "method" : {
      "$ref" : "#/components/schemas/Interpolation_method"
    },
    "value" : {
      "title" : "Interpolation parameter",
      "type" : "integer",
      "description" : "Optional parameter value for the interpolation method (see method description)."
    },
    "order" : {
      "title" : "Interpolation order",
      "type" : "integer",
      "description" : "Optional order parameter for the interpolation method (see method description)."
    }
  },
  "additionalProperties" : true,
  "description" : "Defines whether, and how to treat missing values.\n\nThis can occur in two circumstances when aggregating (setting a sample frequency):\n* missing values: if there are missing (or invalid) values stored for\na given freq-interval,\n\"interpolation\" specifies how to compute these.\n* down-sampling: when the specified freq is smaller than the series’\nactual frequency.\n\"interpolation\" specifies how to compute intermediate values."
}
""",
    object_hook=with_example_provider,
)
interpolation_spec_model_schema.update({"definitions": MODEL_DEFINITIONS})

interpolation_spec_faker = JSF(interpolation_spec_model_schema, allow_none_optionals=1)


class InterpolationSpecStub:
    """InterpolationSpec unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return interpolation_spec_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "InterpolationSpec":
        """Create InterpolationSpec stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                InterpolationSpecAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return InterpolationSpecAdapter.validate_python(
            json, context={"skip_validation": True}
        )
