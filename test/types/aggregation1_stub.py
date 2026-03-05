"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.aggregation1 import Aggregation1

    Aggregation1Adapter = TypeAdapter(Aggregation1)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

aggregation_1_model_schema = json.loads(
    r"""{
  "title" : "Aggregation",
  "type" : "string",
  "description" : "Aggregation method for a series in the query.",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/Query-OutputFirst"
  }, {
    "$ref" : "#/components/schemas/Query-OutputLast"
  }, {
    "$ref" : "#/components/schemas/Query-OutputMean"
  }, {
    "$ref" : "#/components/schemas/Query-OutputMedian"
  }, {
    "$ref" : "#/components/schemas/Query-OutputSum"
  }, {
    "$ref" : "#/components/schemas/Query-OutputCount"
  }, {
    "$ref" : "#/components/schemas/Query-OutputStd"
  }, {
    "$ref" : "#/components/schemas/Query-OutputMax"
  }, {
    "$ref" : "#/components/schemas/Query-OutputMin"
  } ]
}
""",
    object_hook=with_example_provider,
)
aggregation_1_model_schema.update({"definitions": MODEL_DEFINITIONS})

aggregation_1_faker = JSF(aggregation_1_model_schema, allow_none_optionals=1)


class Aggregation1Stub:
    """Aggregation1 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return aggregation_1_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Aggregation1":
        """Create Aggregation1 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                Aggregation1Adapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return Aggregation1Adapter.validate_python(
            json, context={"skip_validation": True}
        )
