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
    from waylay.services.queries.models.hal_link import HALLink

    HALLinkAdapter = TypeAdapter(HALLink)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "title" : "Link URL",
      "type" : "string",
      "description" : "Target url for this link."
    },
    "type" : {
      "title" : "Link type",
      "type" : "string",
      "description" : "Type of the resource referenced by this link."
    },
    "method" : {
      "$ref" : "#/components/schemas/HALLinkMethod"
    }
  },
  "additionalProperties" : true,
  "description" : "A link target in a HAL response."
}
""",
    object_hook=with_example_provider,
)
hal_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

hal_link_faker = JSF(hal_link_model_schema, allow_none_optionals=1)


class HALLinkStub:
    """HALLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return hal_link_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "HALLink":
        """Create HALLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(HALLinkAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return HALLinkAdapter.validate_python(json, context={"skip_validation": True})
