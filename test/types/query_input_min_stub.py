"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.query_input_min import QueryInputMin

    QueryInputMinAdapter = TypeAdapter(QueryInputMin)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

query_input_min_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the minimum of all values in the sample interval.",
  "enum" : [ "min" ]
}
""",
    object_hook=with_example_provider,
)
query_input_min_model_schema.update({"definitions": MODEL_DEFINITIONS})

query_input_min_faker = JSF(query_input_min_model_schema, allow_none_optionals=1)


class QueryInputMinStub:
    """QueryInputMin unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return query_input_min_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "QueryInputMin":
        """Create QueryInputMin stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                QueryInputMinAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QueryInputMinAdapter.validate_python(
            json, context={"skip_validation": True}
        )
