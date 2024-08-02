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
    from waylay.services.queries.models.message_arguments import MessageArguments

    MessageArgumentsAdapter = TypeAdapter(MessageArguments)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

message_arguments_model_schema = json.loads(
    r"""{
  "title" : "Message Arguments",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "$ref" : "#/components/schemas/MessageProperties"
  } ]
}
""",
    object_hook=with_example_provider,
)
message_arguments_model_schema.update({"definitions": MODEL_DEFINITIONS})

message_arguments_faker = JSF(message_arguments_model_schema, allow_none_optionals=1)


class MessageArgumentsStub:
    """MessageArguments unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return message_arguments_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "MessageArguments":
        """Create MessageArguments stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                MessageArgumentsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return MessageArgumentsAdapter.validate_python(
            json, context={"skip_validation": True}
        )