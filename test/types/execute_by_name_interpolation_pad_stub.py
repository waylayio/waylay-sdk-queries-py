"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_by_name_interpolation_pad import (
        ExecuteByNameInterpolationPad,
    )

    ExecuteByNameInterpolationPadAdapter = TypeAdapter(ExecuteByNameInterpolationPad)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_by_name_interpolation_pad_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the value of the first observed point. This method also extrapolates.",
  "enum" : [ "pad" ]
}
""",
    object_hook=with_example_provider,
)
execute_by_name_interpolation_pad_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_by_name_interpolation_pad_faker = JSF(
    execute_by_name_interpolation_pad_model_schema, allow_none_optionals=1
)


class ExecuteByNameInterpolationPadStub:
    """ExecuteByNameInterpolationPad unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_by_name_interpolation_pad_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteByNameInterpolationPad":
        """Create ExecuteByNameInterpolationPad stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteByNameInterpolationPadAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteByNameInterpolationPadAdapter.validate_python(
            json, context={"skip_validation": True}
        )
