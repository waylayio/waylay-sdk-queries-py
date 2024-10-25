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
    from waylay.services.queries.models.query_output import QueryOutput

    QueryOutputAdapter = TypeAdapter(QueryOutput)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

query_output_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "resource" : {
      "title" : "Default Resource",
      "type" : "string",
      "description" : "Default resource for the series in the query."
    },
    "metric" : {
      "title" : "Default Metric",
      "type" : "string",
      "description" : "Default metric for the series in the query."
    },
    "aggregation" : {
      "$ref" : "#/components/schemas/Default_Aggregation"
    },
    "interpolation" : {
      "$ref" : "#/components/schemas/Default_Interpolation"
    },
    "freq" : {
      "$ref" : "#/components/schemas/Grouping_interval"
    },
    "from" : {
      "$ref" : "#/components/schemas/Time_Window_From"
    },
    "until" : {
      "$ref" : "#/components/schemas/Time_Window_Until"
    },
    "window" : {
      "$ref" : "#/components/schemas/Window"
    },
    "periods" : {
      "title" : "Periods",
      "type" : "integer",
      "description" : "The size of the time window in number of `freq` units. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers."
    },
    "align" : {
      "$ref" : "#/components/schemas/Alignment"
    },
    "data" : {
      "title" : "Series specifications",
      "type" : "array",
      "description" : "List of series specifications. When not specified, a single default series specification is assumed(`[{}]`, using the default `metric`,`resource`, ... ).",
      "items" : {
        "$ref" : "#/components/schemas/SeriesSpec"
      }
    },
    "render" : {
      "$ref" : "#/components/schemas/Render"
    }
  },
  "additionalProperties" : true,
  "description" : "Query definition for a Waylay analytics query.\n\nSee also [api docs](https://docs.waylay.io/#/api/query/?id=data-query-json-representation)."
}
""",
    object_hook=with_example_provider,
)
query_output_model_schema.update({"definitions": MODEL_DEFINITIONS})

query_output_faker = JSF(query_output_model_schema, allow_none_optionals=1)


class QueryOutputStub:
    """QueryOutput unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return query_output_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "QueryOutput":
        """Create QueryOutput stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(QueryOutputAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return QueryOutputAdapter.validate_python(
            json, context={"skip_validation": True}
        )
