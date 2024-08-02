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
    from waylay.services.queries.models.hal_link_method import HALLinkMethod

    HALLinkMethodAdapter = TypeAdapter(HALLinkMethod)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

hal_link_method_model_schema = json.loads(
    r"""{
  "title" : "HALLinkMethod",
  "type" : "string",
  "description" : "An http method that can be specified in a HAL link.",
  "enum" : [ "GET", "POST", "PUT", "DELETE", "PATCH" ]
}
""",
    object_hook=with_example_provider,
)
hal_link_method_model_schema.update({"definitions": MODEL_DEFINITIONS})

hal_link_method_faker = JSF(hal_link_method_model_schema, allow_none_optionals=1)


class HALLinkMethodStub:
    """HALLinkMethod unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return hal_link_method_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "HALLinkMethod":
        """Create HALLinkMethod stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                HALLinkMethodAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return HALLinkMethodAdapter.validate_python(
            json, context={"skip_validation": True}
        )
