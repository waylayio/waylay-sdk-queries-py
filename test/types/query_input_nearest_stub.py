"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.query_input_nearest import QueryInputNearest

    QueryInputNearestAdapter = TypeAdapter(QueryInputNearest)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

query_input_nearest_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
    object_hook=with_example_provider,
)
query_input_nearest_model_schema.update({"definitions": MODEL_DEFINITIONS})

query_input_nearest_faker = JSF(
    query_input_nearest_model_schema, allow_none_optionals=1
)


class QueryInputNearestStub:
    """QueryInputNearest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return query_input_nearest_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "QueryInputNearest":
        """Create QueryInputNearest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                QueryInputNearestAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QueryInputNearestAdapter.validate_python(
            json, context={"skip_validation": True}
        )
