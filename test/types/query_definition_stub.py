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
    from waylay.services.queries.models.query_definition import QueryDefinition

    QueryDefinitionAdapter = TypeAdapter(QueryDefinition)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

query_definition_model_schema = json.loads(
    r"""{
  "title" : "Query Definition",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/QueryUpdateInput"
  }, {
    "$ref" : "#/components/schemas/Query-Input"
  } ]
}
""",
    object_hook=with_example_provider,
)
query_definition_model_schema.update({"definitions": MODEL_DEFINITIONS})

query_definition_faker = JSF(query_definition_model_schema, allow_none_optionals=1)


class QueryDefinitionStub:
    """QueryDefinition unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return query_definition_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "QueryDefinition":
        """Create QueryDefinition stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                QueryDefinitionAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QueryDefinitionAdapter.validate_python(
            json, context={"skip_validation": True}
        )
