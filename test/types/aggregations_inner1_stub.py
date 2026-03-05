"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.aggregations_inner1 import AggregationsInner1

    AggregationsInner1Adapter = TypeAdapter(AggregationsInner1)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

aggregations_inner_1_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Aggregation_1"
  } ]
}
""",
    object_hook=with_example_provider,
)
aggregations_inner_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregations_inner_1_faker = JSF(
    aggregations_inner_1_model_schema, allow_none_optionals=1
)


class AggregationsInner1Stub:
    """AggregationsInner1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregations_inner_1_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "AggregationsInner1":
        """Create AggregationsInner1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AggregationsInner1Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregationsInner1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
