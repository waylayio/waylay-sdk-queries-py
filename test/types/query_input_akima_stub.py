"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.query_input_akima import QueryInputAkima

    QueryInputAkimaAdapter = TypeAdapter(QueryInputAkima)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

query_input_akima_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a non-smoothing spline of order 2, called Akima interpolation.",
  "enum" : [ "akima" ]
}
""",
    object_hook=with_example_provider,
)
query_input_akima_model_schema.update({"definitions": MODEL_DEFINITIONS})

query_input_akima_faker = JSF(query_input_akima_model_schema, allow_none_optionals=1)


class QueryInputAkimaStub:
    """QueryInputAkima unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return query_input_akima_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "QueryInputAkima":
        """Create QueryInputAkima stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                QueryInputAkimaAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QueryInputAkimaAdapter.validate_python(
            json, context={"skip_validation": True}
        )
