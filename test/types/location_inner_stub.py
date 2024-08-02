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
    from waylay.services.queries.models.location_inner import LocationInner

    LocationInnerAdapter = TypeAdapter(LocationInner)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

location_inner_model_schema = json.loads(
    r"""{
  "title" : "Location_inner",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "type" : "integer"
  } ]
}
""",
    object_hook=with_example_provider,
)
location_inner_model_schema.update({"definitions": MODEL_DEFINITIONS})

location_inner_faker = JSF(location_inner_model_schema, allow_none_optionals=1)


class LocationInnerStub:
    """LocationInner unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return location_inner_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "LocationInner":
        """Create LocationInner stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                LocationInnerAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LocationInnerAdapter.validate_python(
            json, context={"skip_validation": True}
        )