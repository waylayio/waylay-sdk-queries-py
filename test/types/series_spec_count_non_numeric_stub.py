"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.series_spec_count_non_numeric import (
        SeriesSpecCountNonNumeric,
    )

    SeriesSpecCountNonNumericAdapter = TypeAdapter(SeriesSpecCountNonNumeric)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

series_spec_count_non_numeric_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the count of non-numeric observations in the sample interval.",
  "enum" : [ "count-non-numeric" ]
}
""",
    object_hook=with_example_provider,
)
series_spec_count_non_numeric_model_schema.update({"definitions": MODEL_DEFINITIONS})

series_spec_count_non_numeric_faker = JSF(
    series_spec_count_non_numeric_model_schema, allow_none_optionals=1
)


class SeriesSpecCountNonNumericStub:
    """SeriesSpecCountNonNumeric unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return series_spec_count_non_numeric_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "SeriesSpecCountNonNumeric":
        """Create SeriesSpecCountNonNumeric stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                SeriesSpecCountNonNumericAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return SeriesSpecCountNonNumericAdapter.validate_python(
            json, context={"skip_validation": True}
        )
