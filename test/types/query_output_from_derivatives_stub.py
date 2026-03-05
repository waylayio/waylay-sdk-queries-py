"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.query_output_from_derivatives import (
        QueryOutputFromDerivatives,
    )

    QueryOutputFromDerivativesAdapter = TypeAdapter(QueryOutputFromDerivatives)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

query_output_from_derivatives_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the derivative of order 1.",
  "enum" : [ "from_derivatives" ]
}
""",
    object_hook=with_example_provider,
)
query_output_from_derivatives_model_schema.update({"definitions": MODEL_DEFINITIONS})

query_output_from_derivatives_faker = JSF(
    query_output_from_derivatives_model_schema, allow_none_optionals=1
)


class QueryOutputFromDerivativesStub:
    """QueryOutputFromDerivatives unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return query_output_from_derivatives_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "QueryOutputFromDerivatives":
        """Create QueryOutputFromDerivatives stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                QueryOutputFromDerivativesAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QueryOutputFromDerivativesAdapter.validate_python(
            json, context={"skip_validation": True}
        )
