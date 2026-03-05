"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

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
except ImportError:
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
      "$ref" : "#/components/schemas/Default_Aggregation_1"
    },
    "interpolation" : {
      "$ref" : "#/components/schemas/Default_Interpolation_1"
    },
    "freq" : {
      "$ref" : "#/components/schemas/Grouping_interval_1"
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
    },
    "lookback" : {
      "title" : "Lookback option.",
      "type" : "boolean",
      "description" : "If enabled, the **last-known value** for each of the series will be taken into account in the result. \nFor **unaggregated** series, that value will be included as is (with a timestamp before the result window).\nFor **aggregated** series, that value will be used at the first timestamp, but only if\n * no aggregated value on the first timestamp could be computed\n * and the aggregation is compatible with the value, i.e. in mean, min, max, first, last, median"
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
