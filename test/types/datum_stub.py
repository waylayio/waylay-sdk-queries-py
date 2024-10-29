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
    from waylay.services.queries.models.datum import Datum

    DatumAdapter = TypeAdapter(Datum)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

datum_model_schema = json.loads(
    r"""{
  "title" : "Datum",
  "description" : "A single metric value for a timeseries.\n\nA null value indicates that no (aggregated/interpolated) value  exists for the corresponding timestamp.",
  "oneOf" : [ {
    "type" : "number",
    "nullable" : true
  }, {
    "type" : "string",
    "nullable" : true
  }, {
    "type" : "boolean",
    "nullable" : true
  } ]
}
""",
    object_hook=with_example_provider,
)
datum_model_schema.update({"definitions": MODEL_DEFINITIONS})

datum_faker = JSF(datum_model_schema, allow_none_optionals=1)


class DatumStub:
    """Datum unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return datum_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "Datum":
        """Create Datum stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(DatumAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return DatumAdapter.validate_python(json, context={"skip_validation": True})
