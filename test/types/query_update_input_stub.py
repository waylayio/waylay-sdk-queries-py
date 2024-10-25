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
    from waylay.services.queries.models.query_update_input import QueryUpdateInput

    QueryUpdateInputAdapter = TypeAdapter(QueryUpdateInput)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

query_update_input_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "meta" : {
      "title" : "Query metadata",
      "type" : "object",
      "description" : "User metadata for the query definition."
    },
    "query" : {
      "$ref" : "#/components/schemas/Query-Input"
    }
  },
  "additionalProperties" : true,
  "description" : "Input data to update a query definition."
}
""",
    object_hook=with_example_provider,
)
query_update_input_model_schema.update({"definitions": MODEL_DEFINITIONS})

query_update_input_faker = JSF(query_update_input_model_schema, allow_none_optionals=1)


class QueryUpdateInputStub:
    """QueryUpdateInput unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return query_update_input_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "QueryUpdateInput":
        """Create QueryUpdateInput stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                QueryUpdateInputAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QueryUpdateInputAdapter.validate_python(
            json, context={"skip_validation": True}
        )
