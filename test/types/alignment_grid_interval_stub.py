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
    from waylay.services.queries.models.alignment_grid_interval import (
        AlignmentGridInterval,
    )

    AlignmentGridIntervalAdapter = TypeAdapter(AlignmentGridInterval)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

alignment_grid_interval__model_schema = json.loads(
    r"""{
  "title" : "Alignment Grid interval.",
  "type" : "string",
  "description" : "\nDefines the grid used to align the aggregation window.\nThe window will align at whole-unit multiples of this interval.\n\nFor intervals like `PT1D`, that are timezone-dependent, use the \n`align.timezone` to fix the absolute timestamp of the grid boundaries.\n\nIf not specified, defaults to the `freq` aggregation interval.\n",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  }, {
    "$ref" : "#/components/schemas/Grouping_Interval_Override_oneOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
alignment_grid_interval__model_schema.update({"definitions": MODEL_DEFINITIONS})

alignment_grid_interval__faker = JSF(
    alignment_grid_interval__model_schema, allow_none_optionals=1
)


class AlignmentGridIntervalStub:
    """AlignmentGridInterval unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return alignment_grid_interval__faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "AlignmentGridInterval":
        """Create AlignmentGridInterval stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                AlignmentGridIntervalAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return AlignmentGridIntervalAdapter.validate_python(
            json, context={"skip_validation": True}
        )
