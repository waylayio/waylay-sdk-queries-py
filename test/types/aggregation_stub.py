"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.aggregation import Aggregation

    AggregationAdapter = TypeAdapter(Aggregation)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

aggregation_model_schema = json.loads(
    r"""{
  "title" : "Aggregation",
  "type" : "string",
  "description" : "Aggregation method for a series in the query.",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/Query-InputFirst"
  }, {
    "$ref" : "#/components/schemas/Query-InputLast"
  }, {
    "$ref" : "#/components/schemas/Query-InputMean"
  }, {
    "$ref" : "#/components/schemas/Query-InputMedian"
  }, {
    "$ref" : "#/components/schemas/Query-InputSum"
  }, {
    "$ref" : "#/components/schemas/Query-InputCount"
  }, {
    "$ref" : "#/components/schemas/Query-InputCount-numeric"
  }, {
    "$ref" : "#/components/schemas/Query-InputCount-non-numeric"
  }, {
    "$ref" : "#/components/schemas/Query-InputStd"
  }, {
    "$ref" : "#/components/schemas/Query-InputMax"
  }, {
    "$ref" : "#/components/schemas/Query-InputMin"
  } ]
}
""",
    object_hook=with_example_provider,
)
aggregation_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregation_faker = JSF(aggregation_model_schema, allow_none_optionals=1)


class AggregationStub:
    """Aggregation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregation_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Aggregation":
        """Create Aggregation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(AggregationAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AggregationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
