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
    from waylay.services.queries.models.row_data_set import RowDataSet

    RowDataSetAdapter = TypeAdapter(RowDataSet)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

row_data_set_model_schema = json.loads(
    r"""{
  "required" : [ "columns", "data" ],
  "type" : "object",
  "properties" : {
    "attributes" : {
      "$ref" : "#/components/schemas/DataSetAttributes"
    },
    "window_spec" : {
      "$ref" : "#/components/schemas/DataSetWindow"
    },
    "data_axis" : {
      "$ref" : "#/components/schemas/RowDataSet_data_axis"
    },
    "columns" : {
      "title" : "Column Headers",
      "type" : "array",
      "description" : "Header Attributes for the column data.\n\nThe initial string-valued headers (normally a single `timestamp`) indicate that column to contain row index data (i.e. timestamps).\n\nThe remaining object-valued column headers identify and describe the actual series data.",
      "items" : {
        "$ref" : "#/components/schemas/Column_Headers_inner"
      },
      "x-prefixItems" : [ {
        "const" : "timestamp",
        "title" : "Unix epoch milliseconds timestamp."
      } ]
    },
    "data" : {
      "title" : "Data",
      "type" : "array",
      "items" : {
        "title" : "Observation",
        "type" : "array",
        "description" : "Row index data (timestamp), and a value for each of the series.",
        "items" : {
          "$ref" : "#/components/schemas/Datum"
        },
        "x-prefixItems" : [ {
          "$ref" : "#/components/schemas/Timestamp"
        } ]
      }
    }
  },
  "additionalProperties" : true,
  "description" : "Row-oriented dataset.\n\nTimeseries data layout with a column header and a data row per timestamp.\nResult for render options `data_axis=column` and `header_array=row`.\","
}
""",
    object_hook=with_example_provider,
)
row_data_set_model_schema.update({"definitions": MODEL_DEFINITIONS})

row_data_set_faker = JSF(row_data_set_model_schema, allow_none_optionals=1)


class RowDataSetStub:
    """RowDataSet unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return row_data_set_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "RowDataSet":
        """Create RowDataSet stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(RowDataSetAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RowDataSetAdapter.validate_python(
            json, context={"skip_validation": True}
        )
