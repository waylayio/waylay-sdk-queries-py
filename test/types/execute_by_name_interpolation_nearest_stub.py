"""Waylay Query: timeseries queries (v1 protocol) model tests.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.queries.models.execute_by_name_interpolation_nearest import (
        ExecuteByNameInterpolationNearest,
    )

    ExecuteByNameInterpolationNearestAdapter = TypeAdapter(
        ExecuteByNameInterpolationNearest
    )
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

execute_by_name_interpolation_nearest_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
    object_hook=with_example_provider,
)
execute_by_name_interpolation_nearest_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

execute_by_name_interpolation_nearest_faker = JSF(
    execute_by_name_interpolation_nearest_model_schema, allow_none_optionals=1
)


class ExecuteByNameInterpolationNearestStub:
    """ExecuteByNameInterpolationNearest unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_by_name_interpolation_nearest_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecuteByNameInterpolationNearest":
        """Create ExecuteByNameInterpolationNearest stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecuteByNameInterpolationNearestAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecuteByNameInterpolationNearestAdapter.validate_python(
            json, context={"skip_validation": True}
        )
