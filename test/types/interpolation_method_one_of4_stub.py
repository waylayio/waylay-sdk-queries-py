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
    from waylay.services.queries.models.interpolation_method_one_of4 import (
        InterpolationMethodOneOf4,
    )

    InterpolationMethodOneOf4Adapter = TypeAdapter(InterpolationMethodOneOf4)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

interpolation_method_one_of_4_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
    object_hook=with_example_provider,
)
interpolation_method_one_of_4_model_schema.update({"definitions": MODEL_DEFINITIONS})

interpolation_method_one_of_4_faker = JSF(
    interpolation_method_one_of_4_model_schema, allow_none_optionals=1
)


class InterpolationMethodOneOf4Stub:
    """InterpolationMethodOneOf4 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return interpolation_method_one_of_4_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "InterpolationMethodOneOf4":
        """Create InterpolationMethodOneOf4 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                InterpolationMethodOneOf4Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return InterpolationMethodOneOf4Adapter.validate_python(
            json, context={"skip_validation": True}
        )
