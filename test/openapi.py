import json

import yaml


def with_example_provider(dct):
    has_example = False
    if "example" in dct:
        example, has_example = dct["example"], True
    elif "examples" in dct:
        examples = dct["examples"]
        if isinstance(examples, list) and list:
            example, has_example = examples[0], True
    elif "default" in dct:
        example, has_example = dct["default"], True

    if has_example:
        provider = (
            example
            if example is None or isinstance(example, (dict, list, int, float, bool))
            else f"'{example}'"
        )
        dct.update({"$provider": f"lambda: {provider}"})
    return dct


with open("openapi/queries.transformed.openapi.yaml") as file:
    OPENAPI_SPEC = yaml.safe_load(file)

MODEL_DEFINITIONS = OPENAPI_SPEC["components"]["schemas"]

_aggregation_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"Aggregation": _aggregation_model_schema})

_aggregation_1_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"Aggregation_1": _aggregation_1_model_schema})

_aggregation_by_resource_and_metric_value_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "title" : "Aggregation by Resource or Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_or_Metric_value"
    },
    "description" : "Aggregation methods specified per resource or metric.",
    "nullable" : true
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Aggregation_by_Resource_and_Metric_value": _aggregation_by_resource_and_metric_value_model_schema
})

_aggregation_by_resource_and_metric_value_1_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "title" : "Aggregation by Resource or Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_or_Metric_value_1"
    },
    "description" : "Aggregation methods specified per resource or metric.",
    "nullable" : true
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Aggregation_by_Resource_and_Metric_value_1": _aggregation_by_resource_and_metric_value_1_model_schema
})

_aggregation_by_resource_or_metric_value_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Aggregation"
  }, {
    "title" : "Aggregations",
    "type" : "array",
    "description" : "Aggregation methods, leading to sepearate series.",
    "nullable" : true,
    "items" : {
      "$ref" : "#/components/schemas/Aggregations_inner"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Aggregation_by_Resource_or_Metric_value": _aggregation_by_resource_or_metric_value_model_schema
})

_aggregation_by_resource_or_metric_value_1_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Aggregation_1"
  }, {
    "title" : "Aggregations",
    "type" : "array",
    "description" : "Aggregation methods, leading to sepearate series.",
    "nullable" : true,
    "items" : {
      "$ref" : "#/components/schemas/Aggregations_inner_1"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Aggregation_by_Resource_or_Metric_value_1": _aggregation_by_resource_or_metric_value_1_model_schema
})

_aggregations_inner_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Aggregation"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Aggregations_inner": _aggregations_inner_model_schema})

_aggregations_inner_1_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Aggregation_1"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Aggregations_inner_1": _aggregations_inner_1_model_schema})

_aggregration_model_schema = json.loads(
    r"""{
  "title" : "Aggregration",
  "type" : "string",
  "description" : "Aggregation method for the series (if aggregated). If missing, the query default is used.",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/SeriesSpecFirst"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecLast"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecMean"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecMedian"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecSum"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecCount"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecStd"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecMax"
  }, {
    "$ref" : "#/components/schemas/SeriesSpecMin"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Aggregration": _aggregration_model_schema})

_align_at_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Possible values for `align.at`.\n\n* 'grid' Align to a fixed grid (possibly using timezone information)\n* 'from' Align a the `from` boundary\n* 'until' Align a the `until` boundary\n* 'boundary' Align a the `from` boundary if specified,\n   otherwise the `until` boundary.\n\nWhen not specified, 'grid' is used.",
  "enum" : [ "grid", "boundary", "from", "until" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignAt": _align_at_model_schema})

_align_shift_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Possible values for `align.shift`.\n\n* 'backward': keep the window size of the original interval specification,\n   shifting back.\n* 'forward': keep the window size of the original interval specification,\n   shifting forward.\n* 'wrap': enlarge the window size to include all of the original interval.\n\nWhen not specified, 'backward' is used.",
  "enum" : [ "backward", "forward", "wrap" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignShift": _align_shift_model_schema})

_alignment_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "at" : {
      "$ref" : "#/components/schemas/Alignment_at"
    },
    "shift" : {
      "$ref" : "#/components/schemas/Alignment_shift"
    },
    "freq" : {
      "$ref" : "#/components/schemas/Alignment_Grid_interval_"
    },
    "timezone" : {
      "$ref" : "#/components/schemas/Alignment_Timezone_"
    }
  },
  "additionalProperties" : true,
  "description" : "Aggregation Alignment Options.\n\nSpecifies how the aggregation grid is aligned."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Alignment": _alignment_model_schema})

_alignment_at_model_schema = json.loads(
    r"""{
  "$ref" : "#/components/schemas/AlignAt"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Alignment_at": _alignment_at_model_schema})

_alignment_backward_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Shift both boundaries (`align.at=grid`) or first boundary (`align.at=until`) backward to align with the grid.",
  "enum" : [ "backward" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignmentBackward": _alignment_backward_model_schema})

_alignment_boundary_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Align a the `from` boundary if specified, otherwise use the `until` boundary (specfied or computed)",
  "enum" : [ "boundary" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignmentBoundary": _alignment_boundary_model_schema})

_alignment_forward_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Shift both boundaries (`align.at=grid`) or last boundary (`align.at=from`) forward to align with the grid.",
  "enum" : [ "forward" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignmentForward": _alignment_forward_model_schema})

_alignment_from_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Align a the `from` window boundary.",
  "enum" : [ "from" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignmentFrom": _alignment_from_model_schema})

_alignment_grid_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Align to a fixed grid defined by the alignment `frequency` and `timezone`.",
  "enum" : [ "grid" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignmentGrid": _alignment_grid_model_schema})

_alignment_grid_interval__model_schema = json.loads(
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
    "$ref" : "#/components/schemas/AlignmentInferred"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Alignment_Grid_interval_": _alignment_grid_interval__model_schema
})

_alignment_inferred_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "When `inferred` is specified, the frequency of aggregation will be inferred from the main/first time series. This can be used to regularize the time series",
  "enum" : [ "inferred" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignmentInferred": _alignment_inferred_model_schema})

_alignment_shift_model_schema = json.loads(
    r"""{
  "$ref" : "#/components/schemas/AlignShift"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Alignment_shift": _alignment_shift_model_schema})

_alignment_timezone__model_schema = json.loads(
    r"""{
  "title" : "Alignment Timezone.",
  "type" : "string",
  "description" : "\nThe timezone to use when shifting boundaries, especially\nat day granularity.\nAlso affects the rendering of timestamps when\n`render.iso_timestamp` is enabled.\n\nWhen not specified, the `UTC` timezone is used.\n",
  "oneOf" : [ {
    "title" : "Timezone Identifier",
    "type" : "string",
    "description" : "[ICANN timezone identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)"
  }, {
    "title" : "UTC Offset",
    "pattern" : "(+|-)\\d\\d:\\d\\d",
    "type" : "string",
    "description" : "[UTC offset](https://en.wikipedia.org/wiki/UTC_offset)"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Alignment_Timezone_": _alignment_timezone__model_schema})

_alignment_until_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Align a the `until` window boundary",
  "enum" : [ "until" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignmentUntil": _alignment_until_model_schema})

_alignment_wrap_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Shift first boundary backward, and last boundary forward to align with the grid",
  "enum" : [ "wrap" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AlignmentWrap": _alignment_wrap_model_schema})

_cause_exception_model_schema = json.loads(
    r"""{
  "required" : [ "message", "stacktrace", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "title" : "Exception Type",
      "type" : "string"
    },
    "message" : {
      "title" : "Exception Message",
      "type" : "string"
    },
    "stacktrace" : {
      "title" : "Stack Trace",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    }
  },
  "additionalProperties" : true,
  "description" : "Describes the exception that caused a message."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CauseException": _cause_exception_model_schema})

_column_data_set_model_schema = json.loads(
    r"""{
  "required" : [ "data", "rows" ],
  "type" : "object",
  "properties" : {
    "attributes" : {
      "$ref" : "#/components/schemas/DataSetAttributes"
    },
    "window_spec" : {
      "$ref" : "#/components/schemas/DataSetWindow"
    },
    "data_axis" : {
      "$ref" : "#/components/schemas/ColumnDataSet_data_axis"
    },
    "rows" : {
      "title" : "Row Headers",
      "type" : "array",
      "description" : "Header Attributes for the index data.\n\nThe initial string-valued headers (normally `resource`, `metric`,`aggregation`) indicate that row to contain series attributes.\n\nThe remaining object-valued row headers contain the index data.",
      "items" : {
        "$ref" : "#/components/schemas/Row_Headers_inner"
      }
    },
    "data" : {
      "title" : "Series",
      "type" : "array",
      "description" : "All metric observation values for a single series. Prefixed by the series attributes.",
      "items" : {
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/Datum"
        }
      }
    }
  },
  "additionalProperties" : true,
  "description" : "Column-oriented dataset with rows header.\n\nTimeseries data layout with a rows header containing\nthe index data.\nThe data array contains series data prefixed by series attributes.\nThe `rows` index is prefix by the names of these series attributes.\nResult for render options `data_axis=row` and `header_array=column`."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ColumnDataSet": _column_data_set_model_schema})

_column_data_set_data_axis_model_schema = json.loads(
    r"""{
  "title" : "ColumnDataSet_data_axis",
  "type" : "string",
  "default" : "row",
  "enum" : [ "row" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ColumnDataSet_data_axis": _column_data_set_data_axis_model_schema
})

_column_header_model_schema = json.loads(
    r"""{
  "required" : [ "metric", "resource" ],
  "type" : "object",
  "properties" : {
    "resource" : {
      "title" : "Series resource id",
      "type" : "string"
    },
    "metric" : {
      "title" : "Series metric",
      "type" : "string"
    },
    "aggregation" : {
      "title" : "Aggregation applied to the series.",
      "type" : "string"
    }
  },
  "additionalProperties" : true,
  "description" : "Column attributes.\n\nAttributes that identify and describe the data in this column."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ColumnHeader": _column_header_model_schema})

_column_headers_inner_model_schema = json.loads(
    r"""{
  "title" : "Column_Headers_inner",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/RowIndexColumnHeader"
  }, {
    "$ref" : "#/components/schemas/ColumnHeader"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Column_Headers_inner": _column_headers_inner_model_schema})

_data__model_schema = json.loads(
    r"""{
  "title" : "Data ",
  "oneOf" : [ {
    "title" : "Hierarchical Data",
    "type" : "object",
    "description" : "Values for the series whose attributes corresponds with the key. Keyed by sub-levels."
  }, {
    "$ref" : "#/components/schemas/Datum"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Data_": _data__model_schema})

_data_axis_option_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Allowed values for the render.data_axis option.",
  "enum" : [ "row", "column" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DataAxisOption": _data_axis_option_model_schema})

_data_set_attributes_model_schema = json.loads(
    r"""{
  "title" : "DataSetAttributes",
  "type" : "object",
  "properties" : {
    "role" : {
      "$ref" : "#/components/schemas/Role"
    }
  },
  "additionalProperties" : true,
  "description" : "Data Set Attributes.\n\nData attributes that apply to all data in this set."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DataSetAttributes": _data_set_attributes_model_schema})

_data_set_window_model_schema = json.loads(
    r"""{
  "title" : "DataSetWindow",
  "required" : [ "freq", "until", "window" ],
  "type" : "object",
  "properties" : {
    "until" : {
      "title" : "Time Axis End",
      "type" : "integer",
      "description" : "Exclusive higher bound of the time axis in unix epoch milliseconds."
    },
    "window" : {
      "title" : "Time Axis Length",
      "type" : "string",
      "description" : "Time axis length as ISO8601 period.",
      "format" : "period"
    },
    "freq" : {
      "title" : "Frequency",
      "type" : "string",
      "description" : "Time axis aggregation interval as an ISO8601 period .",
      "format" : "period"
    }
  },
  "additionalProperties" : true,
  "description" : "Data Window.\n\nStatistics of the time axis of a data set.\nPresent with render option `include_window_spec=true`.\","
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DataSetWindow": _data_set_window_model_schema})

_datum_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"Datum": _datum_model_schema})

_default_aggregation_model_schema = json.loads(
    r"""{
  "title" : "Default Aggregation",
  "description" : "Default aggregation method(s) for the series in the query.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Aggregation"
  }, {
    "title" : "Aggregations",
    "type" : "array",
    "description" : "Aggregation methods, leading to sepearate series.",
    "nullable" : true,
    "items" : {
      "$ref" : "#/components/schemas/Aggregations_inner"
    }
  }, {
    "title" : "Aggregation by Resource or Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_or_Metric_value"
    },
    "description" : "Aggregation methods specified per resource or metric.",
    "nullable" : true
  }, {
    "title" : "Aggregation by Resource and Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_and_Metric_value"
    },
    "description" : "Aggregation methods specified per resource and metric.",
    "nullable" : true
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Default_Aggregation": _default_aggregation_model_schema})

_default_aggregation_1_model_schema = json.loads(
    r"""{
  "title" : "Default Aggregation",
  "description" : "Default aggregation method(s) for the series in the query.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Aggregation_1"
  }, {
    "title" : "Aggregations",
    "type" : "array",
    "description" : "Aggregation methods, leading to sepearate series.",
    "nullable" : true,
    "items" : {
      "$ref" : "#/components/schemas/Aggregations_inner_1"
    }
  }, {
    "title" : "Aggregation by Resource or Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_or_Metric_value_1"
    },
    "description" : "Aggregation methods specified per resource or metric.",
    "nullable" : true
  }, {
    "title" : "Aggregation by Resource and Metric",
    "type" : "object",
    "additionalProperties" : {
      "$ref" : "#/components/schemas/Aggregation_by_Resource_and_Metric_value_1"
    },
    "description" : "Aggregation methods specified per resource and metric.",
    "nullable" : true
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Default_Aggregation_1": _default_aggregation_1_model_schema})

_default_interpolation_model_schema = json.loads(
    r"""{
  "title" : "Default Interpolation",
  "description" : "Default Interpolation method for the series (if aggregated).",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Default_Interpolation_anyOf"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpec"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Default_Interpolation": _default_interpolation_model_schema})

_default_interpolation_any_of_model_schema = json.loads(
    r"""{
  "$ref" : "#/components/schemas/InterpolationMethod"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Default_Interpolation_anyOf": _default_interpolation_any_of_model_schema
})

_delete_response_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "messages" : {
      "title" : "Messages",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Message"
      }
    },
    "_links" : {
      "title" : "Links",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Links_value"
      },
      "description" : "HAL links, indexed by link relation.",
      "x-propertyNames" : {
        "$ref" : "#/components/schemas/HALLinkRole"
      }
    },
    "_embeddings" : {
      "title" : "Embeddings",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/Embeddings_value"
      },
      "description" : "Hal embeddings, indexed by relation.",
      "x-propertyNames" : {
        "$ref" : "#/components/schemas/HALLinkRole"
      }
    }
  },
  "additionalProperties" : true,
  "description" : "Confirmation of a delete request."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DeleteResponse": _delete_response_model_schema})

_embeddings_value_model_schema = json.loads(
    r"""{
  "title" : "Embeddings_value",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/HALEmbedding"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/HALEmbedding"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Embeddings_value": _embeddings_value_model_schema})

_execute_by_name_queries_v1_data_query_name_get_aggregation_model_schema = json.loads(
    r"""{
  "type" : "string",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationFirst"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationLast"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationMean"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationSum"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationCount"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationStd"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationMax"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetAggregationMin"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregation": _execute_by_name_queries_v1_data_query_name_get_aggregation_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_count_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Use the count of observations in the sample interval.",
  "enum" : [ "count" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationCount": _execute_by_name_queries_v1_data_query_name_get_aggregation_count_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_first_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Use the first value (in time) to represent all data for the sample interval.",
  "enum" : [ "first" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationFirst": _execute_by_name_queries_v1_data_query_name_get_aggregation_first_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_last_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Use the last value (in time) to represent all data for the sample interval.",
  "enum" : [ "last" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationLast": _execute_by_name_queries_v1_data_query_name_get_aggregation_last_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_max_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Use the maximum of all values in the sample interval.",
  "enum" : [ "max" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationMax": _execute_by_name_queries_v1_data_query_name_get_aggregation_max_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_mean_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Aggregate data by the mean value: The sum of values divided by number of observations.",
  "enum" : [ "mean" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationMean": _execute_by_name_queries_v1_data_query_name_get_aggregation_mean_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_median_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.",
  "enum" : [ "median" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian": _execute_by_name_queries_v1_data_query_name_get_aggregation_median_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_min_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Use the minimum of all values in the sample interval.",
  "enum" : [ "min" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationMin": _execute_by_name_queries_v1_data_query_name_get_aggregation_min_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_std_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Use the standard deviation of all observations in the sample interval.",
  "enum" : [ "std" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationStd": _execute_by_name_queries_v1_data_query_name_get_aggregation_std_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_aggregation_sum_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "The sum of all values summarizes the data for the sample interval.",
  "enum" : [ "sum" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetAggregationSum": _execute_by_name_queries_v1_data_query_name_get_aggregation_sum_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_freq_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Override for the `freq` query attribute.",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  }, {
    "$ref" : "#/components/schemas/ExecuteByNameQueriesV1DataQueryNameGetFreqInferred"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetFreq": _execute_by_name_queries_v1_data_query_name_get_freq_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_freq_inferred_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "When `inferred` is specified, the frequency of aggregation will be inferred from the main/first time series. This can be used to regularize the time series",
  "enum" : [ "inferred" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetFreqInferred": _execute_by_name_queries_v1_data_query_name_get_freq_inferred_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_from_model_schema = json.loads(
    r"""{
  "type" : "string",
  "oneOf" : [ {
    "title" : "ISO8601 absolute timestamp",
    "pattern" : "[0-9]{4}-[0-9]{2}-[0-9]{2}(T.*)?",
    "type" : "string",
    "description" : "A date or date-time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format. When no timezone is specified, the UTC timezone is assumed (`+00:00`)",
    "format" : "date-time",
    "example" : "2018-03-21T12:23:00+01:00"
  }, {
    "title" : "UNIX epoch milliseconds",
    "minimum" : 0,
    "type" : "integer",
    "description" : "Absolute timestamp milliseconds in unix epoch since 1970-01-01.",
    "example" : 1534836422284
  }, {
    "title" : "ISO8601 Period Before Now",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "Specifies a timestamp before _now_ as a period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetFrom": _execute_by_name_queries_v1_data_query_name_get_from_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Default_Interpolation_anyOf"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpec"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolation": _execute_by_name_queries_v1_data_query_name_get_interpolation_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_akima_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with a non-smoothing spline of order 2, called Akima interpolation.",
  "enum" : [ "akima" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationAkima": _execute_by_name_queries_v1_data_query_name_get_interpolation_akima_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_backfill_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Same as pad, but using the last observed value. This method also extrapolates",
  "enum" : [ "backfill" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationBackfill": _execute_by_name_queries_v1_data_query_name_get_interpolation_backfill_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_cubic_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 3, which is a piecewise polynomial.",
  "enum" : [ "cubic" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationCubic": _execute_by_name_queries_v1_data_query_name_get_interpolation_cubic_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_fixed_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with a fixed, user-specified value. This method also extrapolates.",
  "enum" : [ "fixed" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationFixed": _execute_by_name_queries_v1_data_query_name_get_interpolation_fixed_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_from_derivatives_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the derivative of order 1.",
  "enum" : [ "from_derivatives" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationFrom_derivatives": _execute_by_name_queries_v1_data_query_name_get_interpolation_from_derivatives_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_linear_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates",
  "enum" : [ "linear" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationLinear": _execute_by_name_queries_v1_data_query_name_get_interpolation_linear_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_nearest_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationNearest": _execute_by_name_queries_v1_data_query_name_get_interpolation_nearest_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_pad_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with the value of the first observed point. This method also extrapolates.",
  "enum" : [ "pad" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationPad": _execute_by_name_queries_v1_data_query_name_get_interpolation_pad_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_pchip_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with a piecewise cubic spline function.",
  "enum" : [ "pchip" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationPchip": _execute_by_name_queries_v1_data_query_name_get_interpolation_pchip_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_polynomial_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a polynomial of the lowest possible degree passing trough the data points.",
  "enum" : [ "polynomial" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationPolynomial": _execute_by_name_queries_v1_data_query_name_get_interpolation_polynomial_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_quadratic_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 2, which is a piecewise polynomial.",
  "enum" : [ "quadratic" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationQuadratic": _execute_by_name_queries_v1_data_query_name_get_interpolation_quadratic_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_slinear_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 1, which is a piecewise polynomial.",
  "enum" : [ "slinear" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationSlinear": _execute_by_name_queries_v1_data_query_name_get_interpolation_slinear_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_spline_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of a user-specified order.",
  "enum" : [ "spline" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationSpline": _execute_by_name_queries_v1_data_query_name_get_interpolation_spline_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_interpolation_zero_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 0, which is a piecewise polynomial.",
  "enum" : [ "zero" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetInterpolationZero": _execute_by_name_queries_v1_data_query_name_get_interpolation_zero_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Render_mode"
  }, {
    "$ref" : "#/components/schemas/Render"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRender": _execute_by_name_queries_v1_data_query_name_get_render_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_compact_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`",
  "enum" : [ "COMPACT" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderCOMPACT": _execute_by_name_queries_v1_data_query_name_get_render_compact_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_compact_ws_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers. Show the time window attributes.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`\n- `include_window_spec`: `True`",
  "enum" : [ "COMPACT_WS" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderCOMPACT_WS": _execute_by_name_queries_v1_data_query_name_get_render_compact_ws_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_csv_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render in csv format with row headers.\n\n###### options\n- `iso_timestamp`: `False`",
  "enum" : [ "CSV" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderCSV": _execute_by_name_queries_v1_data_query_name_get_render_csv_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_flat_dict_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Render an object for each observation. Uses flattened keys.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `False`\n- `show_levels`: `True`\n- `roll_up`: `False`",
  "enum" : [ "FLAT_DICT" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderFLAT_DICT": _execute_by_name_queries_v1_data_query_name_get_render_flat_dict_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_header_column_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Renders row index in `rows`, and each series as a values array.\n\nThe series are prefixed by their series attributes.The `rows` index is prefixed by the labels for these attributes.\n\n###### options\n- `iso_timestamp`: `True`\n- `header_array`: `column`\n- `roll_up`: `False`\n- `data_axis`: `row`",
  "enum" : [ "HEADER_COLUMN" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderHEADER_COLUMN": _execute_by_name_queries_v1_data_query_name_get_render_header_column_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_header_row_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers. Includes an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`",
  "enum" : [ "HEADER_ROW" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderHEADER_ROW": _execute_by_name_queries_v1_data_query_name_get_render_header_row_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_hier_dict_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Render an hierarchical object for each observation. Shows an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `True`\n- `show_levels`: `True`\n- `roll_up`: `True`",
  "enum" : [ "HIER_DICT" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderHIER_DICT": _execute_by_name_queries_v1_data_query_name_get_render_hier_dict_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_metric_flat_dict_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Render an object with metric keys for each observation. Shows an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `['metric']`\n- `show_levels`: `False`\n- `roll_up`: `True`\n- `key_skip_empty`: `True`",
  "enum" : [ "METRIC_FLAT_DICT" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderMETRIC_FLAT_DICT": _execute_by_name_queries_v1_data_query_name_get_render_metric_flat_dict_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_series_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render timestamps and each series (column) as a values array. Show column headers.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `data_axis`: `row`\n- `roll_up`: `True`\n- `include_window_spec`: `True`",
  "enum" : [ "SERIES" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderSERIES": _execute_by_name_queries_v1_data_query_name_get_render_series_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_render_upload_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render in an object format compatible with the `/data/v1/events` upload.\n\n###### options\n- `iso_timestamp`: `False`\n- `hierarchical`: `False`\n- `show_levels`: `False`\n- `roll_up`: `True`",
  "enum" : [ "UPLOAD" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetRenderUPLOAD": _execute_by_name_queries_v1_data_query_name_get_render_upload_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_until_model_schema = json.loads(
    r"""{
  "type" : "string",
  "oneOf" : [ {
    "title" : "ISO8601 absolute timestamp",
    "pattern" : "[0-9]{4}-[0-9]{2}-[0-9]{2}(T.*)?",
    "type" : "string",
    "description" : "A date or date-time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format. When no timezone is specified, the UTC timezone is assumed (`+00:00`)",
    "format" : "date-time",
    "example" : "2018-03-21T12:23:00+01:00"
  }, {
    "title" : "UNIX epoch milliseconds",
    "minimum" : 0,
    "type" : "integer",
    "description" : "Absolute timestamp milliseconds in unix epoch since 1970-01-01.",
    "example" : 1534836422284
  }, {
    "title" : "ISO8601 Period Before Now",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "Specifies a timestamp before _now_ as a period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetUntil": _execute_by_name_queries_v1_data_query_name_get_until_model_schema
})

_execute_by_name_queries_v1_data_query_name_get_window_model_schema = json.loads(
    r"""{
  "type" : "string",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteByNameQueriesV1DataQueryNameGetWindow": _execute_by_name_queries_v1_data_query_name_get_window_model_schema
})

_execute_query_queries_v1_data_post_aggregation_model_schema = json.loads(
    r"""{
  "type" : "string",
  "nullable" : true,
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationFirst"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationLast"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationMean"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationMedian"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationSum"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationCount"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationStd"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationMax"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostAggregationMin"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregation": _execute_query_queries_v1_data_post_aggregation_model_schema
})

_execute_query_queries_v1_data_post_aggregation_count_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the count of observations in the sample interval.",
  "enum" : [ "count" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationCount": _execute_query_queries_v1_data_post_aggregation_count_model_schema
})

_execute_query_queries_v1_data_post_aggregation_first_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the first value (in time) to represent all data for the sample interval.",
  "enum" : [ "first" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationFirst": _execute_query_queries_v1_data_post_aggregation_first_model_schema
})

_execute_query_queries_v1_data_post_aggregation_last_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the last value (in time) to represent all data for the sample interval.",
  "enum" : [ "last" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationLast": _execute_query_queries_v1_data_post_aggregation_last_model_schema
})

_execute_query_queries_v1_data_post_aggregation_max_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the maximum of all values in the sample interval.",
  "enum" : [ "max" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationMax": _execute_query_queries_v1_data_post_aggregation_max_model_schema
})

_execute_query_queries_v1_data_post_aggregation_mean_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the mean value: The sum of values divided by number of observations.",
  "enum" : [ "mean" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationMean": _execute_query_queries_v1_data_post_aggregation_mean_model_schema
})

_execute_query_queries_v1_data_post_aggregation_median_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.",
  "enum" : [ "median" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationMedian": _execute_query_queries_v1_data_post_aggregation_median_model_schema
})

_execute_query_queries_v1_data_post_aggregation_min_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the minimum of all values in the sample interval.",
  "enum" : [ "min" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationMin": _execute_query_queries_v1_data_post_aggregation_min_model_schema
})

_execute_query_queries_v1_data_post_aggregation_std_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the standard deviation of all observations in the sample interval.",
  "enum" : [ "std" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationStd": _execute_query_queries_v1_data_post_aggregation_std_model_schema
})

_execute_query_queries_v1_data_post_aggregation_sum_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "The sum of all values summarizes the data for the sample interval.",
  "enum" : [ "sum" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostAggregationSum": _execute_query_queries_v1_data_post_aggregation_sum_model_schema
})

_execute_query_queries_v1_data_post_freq_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Override for the `freq` query attribute.",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  }, {
    "$ref" : "#/components/schemas/ExecuteQueryQueriesV1DataPostFreqInferred"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostFreq": _execute_query_queries_v1_data_post_freq_model_schema
})

_execute_query_queries_v1_data_post_freq_inferred_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "When `inferred` is specified, the frequency of aggregation will be inferred from the main/first time series. This can be used to regularize the time series",
  "enum" : [ "inferred" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostFreqInferred": _execute_query_queries_v1_data_post_freq_inferred_model_schema
})

_execute_query_queries_v1_data_post_from_model_schema = json.loads(
    r"""{
  "type" : "string",
  "oneOf" : [ {
    "title" : "ISO8601 absolute timestamp",
    "pattern" : "[0-9]{4}-[0-9]{2}-[0-9]{2}(T.*)?",
    "type" : "string",
    "description" : "A date or date-time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format. When no timezone is specified, the UTC timezone is assumed (`+00:00`)",
    "format" : "date-time",
    "example" : "2018-03-21T12:23:00+01:00"
  }, {
    "title" : "UNIX epoch milliseconds",
    "minimum" : 0,
    "type" : "integer",
    "description" : "Absolute timestamp milliseconds in unix epoch since 1970-01-01.",
    "example" : 1534836422284
  }, {
    "title" : "ISO8601 Period Before Now",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "Specifies a timestamp before _now_ as a period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostFrom": _execute_query_queries_v1_data_post_from_model_schema
})

_execute_query_queries_v1_data_post_interpolation_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Default_Interpolation_anyOf"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpec"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolation": _execute_query_queries_v1_data_post_interpolation_model_schema
})

_execute_query_queries_v1_data_post_interpolation_akima_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a non-smoothing spline of order 2, called Akima interpolation.",
  "enum" : [ "akima" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationAkima": _execute_query_queries_v1_data_post_interpolation_akima_model_schema
})

_execute_query_queries_v1_data_post_interpolation_backfill_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Same as pad, but using the last observed value. This method also extrapolates",
  "enum" : [ "backfill" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationBackfill": _execute_query_queries_v1_data_post_interpolation_backfill_model_schema
})

_execute_query_queries_v1_data_post_interpolation_cubic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 3, which is a piecewise polynomial.",
  "enum" : [ "cubic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationCubic": _execute_query_queries_v1_data_post_interpolation_cubic_model_schema
})

_execute_query_queries_v1_data_post_interpolation_fixed_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a fixed, user-specified value. This method also extrapolates.",
  "enum" : [ "fixed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationFixed": _execute_query_queries_v1_data_post_interpolation_fixed_model_schema
})

_execute_query_queries_v1_data_post_interpolation_from_derivatives_model_schema = (
    json.loads(
        r"""{
  "type" : "string",
  "description" : "Interpolate with the derivative of order 1.",
  "enum" : [ "from_derivatives" ]
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationFrom_derivatives": _execute_query_queries_v1_data_post_interpolation_from_derivatives_model_schema
})

_execute_query_queries_v1_data_post_interpolation_linear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates",
  "enum" : [ "linear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationLinear": _execute_query_queries_v1_data_post_interpolation_linear_model_schema
})

_execute_query_queries_v1_data_post_interpolation_nearest_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationNearest": _execute_query_queries_v1_data_post_interpolation_nearest_model_schema
})

_execute_query_queries_v1_data_post_interpolation_pad_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the value of the first observed point. This method also extrapolates.",
  "enum" : [ "pad" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationPad": _execute_query_queries_v1_data_post_interpolation_pad_model_schema
})

_execute_query_queries_v1_data_post_interpolation_pchip_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a piecewise cubic spline function.",
  "enum" : [ "pchip" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationPchip": _execute_query_queries_v1_data_post_interpolation_pchip_model_schema
})

_execute_query_queries_v1_data_post_interpolation_polynomial_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a polynomial of the lowest possible degree passing trough the data points.",
  "enum" : [ "polynomial" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationPolynomial": _execute_query_queries_v1_data_post_interpolation_polynomial_model_schema
})

_execute_query_queries_v1_data_post_interpolation_quadratic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 2, which is a piecewise polynomial.",
  "enum" : [ "quadratic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationQuadratic": _execute_query_queries_v1_data_post_interpolation_quadratic_model_schema
})

_execute_query_queries_v1_data_post_interpolation_slinear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 1, which is a piecewise polynomial.",
  "enum" : [ "slinear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationSlinear": _execute_query_queries_v1_data_post_interpolation_slinear_model_schema
})

_execute_query_queries_v1_data_post_interpolation_spline_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of a user-specified order.",
  "enum" : [ "spline" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationSpline": _execute_query_queries_v1_data_post_interpolation_spline_model_schema
})

_execute_query_queries_v1_data_post_interpolation_zero_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 0, which is a piecewise polynomial.",
  "enum" : [ "zero" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostInterpolationZero": _execute_query_queries_v1_data_post_interpolation_zero_model_schema
})

_execute_query_queries_v1_data_post_render_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Render_mode"
  }, {
    "$ref" : "#/components/schemas/Render"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRender": _execute_query_queries_v1_data_post_render_model_schema
})

_execute_query_queries_v1_data_post_render_compact_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`",
  "enum" : [ "COMPACT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderCOMPACT": _execute_query_queries_v1_data_post_render_compact_model_schema
})

_execute_query_queries_v1_data_post_render_compact_ws_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers. Show the time window attributes.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`\n- `include_window_spec`: `True`",
  "enum" : [ "COMPACT_WS" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderCOMPACT_WS": _execute_query_queries_v1_data_post_render_compact_ws_model_schema
})

_execute_query_queries_v1_data_post_render_csv_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render in csv format with row headers.\n\n###### options\n- `iso_timestamp`: `False`",
  "enum" : [ "CSV" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderCSV": _execute_query_queries_v1_data_post_render_csv_model_schema
})

_execute_query_queries_v1_data_post_render_flat_dict_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render an object for each observation. Uses flattened keys.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `False`\n- `show_levels`: `True`\n- `roll_up`: `False`",
  "enum" : [ "FLAT_DICT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderFLAT_DICT": _execute_query_queries_v1_data_post_render_flat_dict_model_schema
})

_execute_query_queries_v1_data_post_render_header_column_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Renders row index in `rows`, and each series as a values array.\n\nThe series are prefixed by their series attributes.The `rows` index is prefixed by the labels for these attributes.\n\n###### options\n- `iso_timestamp`: `True`\n- `header_array`: `column`\n- `roll_up`: `False`\n- `data_axis`: `row`",
  "enum" : [ "HEADER_COLUMN" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderHEADER_COLUMN": _execute_query_queries_v1_data_post_render_header_column_model_schema
})

_execute_query_queries_v1_data_post_render_header_row_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers. Includes an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`",
  "enum" : [ "HEADER_ROW" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderHEADER_ROW": _execute_query_queries_v1_data_post_render_header_row_model_schema
})

_execute_query_queries_v1_data_post_render_hier_dict_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render an hierarchical object for each observation. Shows an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `True`\n- `show_levels`: `True`\n- `roll_up`: `True`",
  "enum" : [ "HIER_DICT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderHIER_DICT": _execute_query_queries_v1_data_post_render_hier_dict_model_schema
})

_execute_query_queries_v1_data_post_render_metric_flat_dict_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render an object with metric keys for each observation. Shows an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `['metric']`\n- `show_levels`: `False`\n- `roll_up`: `True`\n- `key_skip_empty`: `True`",
  "enum" : [ "METRIC_FLAT_DICT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderMETRIC_FLAT_DICT": _execute_query_queries_v1_data_post_render_metric_flat_dict_model_schema
})

_execute_query_queries_v1_data_post_render_series_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render timestamps and each series (column) as a values array. Show column headers.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `data_axis`: `row`\n- `roll_up`: `True`\n- `include_window_spec`: `True`",
  "enum" : [ "SERIES" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderSERIES": _execute_query_queries_v1_data_post_render_series_model_schema
})

_execute_query_queries_v1_data_post_render_upload_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render in an object format compatible with the `/data/v1/events` upload.\n\n###### options\n- `iso_timestamp`: `False`\n- `hierarchical`: `False`\n- `show_levels`: `False`\n- `roll_up`: `True`",
  "enum" : [ "UPLOAD" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostRenderUPLOAD": _execute_query_queries_v1_data_post_render_upload_model_schema
})

_execute_query_queries_v1_data_post_until_model_schema = json.loads(
    r"""{
  "type" : "string",
  "oneOf" : [ {
    "title" : "ISO8601 absolute timestamp",
    "pattern" : "[0-9]{4}-[0-9]{2}-[0-9]{2}(T.*)?",
    "type" : "string",
    "description" : "A date or date-time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format. When no timezone is specified, the UTC timezone is assumed (`+00:00`)",
    "format" : "date-time",
    "example" : "2018-03-21T12:23:00+01:00"
  }, {
    "title" : "UNIX epoch milliseconds",
    "minimum" : 0,
    "type" : "integer",
    "description" : "Absolute timestamp milliseconds in unix epoch since 1970-01-01.",
    "example" : 1534836422284
  }, {
    "title" : "ISO8601 Period Before Now",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "Specifies a timestamp before _now_ as a period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostUntil": _execute_query_queries_v1_data_post_until_model_schema
})

_execute_query_queries_v1_data_post_window_model_schema = json.loads(
    r"""{
  "type" : "string",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecuteQueryQueriesV1DataPostWindow": _execute_query_queries_v1_data_post_window_model_schema
})

_grouping_interval_model_schema = json.loads(
    r"""{
  "title" : "Grouping interval",
  "type" : "string",
  "description" : "Interval used to aggregate or regularize data. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  }, {
    "$ref" : "#/components/schemas/Query-InputInferred"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Grouping_interval": _grouping_interval_model_schema})

_grouping_interval_1_model_schema = json.loads(
    r"""{
  "title" : "Grouping interval",
  "type" : "string",
  "description" : "Interval used to aggregate or regularize data. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  }, {
    "$ref" : "#/components/schemas/Query-OutputInferred"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Grouping_interval_1": _grouping_interval_1_model_schema})

_hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "title" : "Link URL",
      "type" : "string",
      "description" : "Target url for this link."
    },
    "type" : {
      "title" : "Link type",
      "type" : "string",
      "description" : "Type of the resource referenced by this link."
    },
    "method" : {
      "$ref" : "#/components/schemas/HALLinkMethod"
    }
  },
  "additionalProperties" : true,
  "description" : "A link target in a HAL response."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLink": _hal_link_model_schema})

_hal_link_method_model_schema = json.loads(
    r"""{
  "title" : "HALLinkMethod",
  "type" : "string",
  "description" : "An http method that can be specified in a HAL link.",
  "enum" : [ "GET", "POST", "PUT", "DELETE", "PATCH" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLinkMethod": _hal_link_method_model_schema})

_hal_link_role_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Supported link and embedding roles in HAL representations.",
  "enum" : [ "self", "first", "prev", "next", "last", "execute" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLinkRole": _hal_link_role_model_schema})

_http_validation_error_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "detail" : {
      "title" : "Detail",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ValidationError"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HTTPValidationError": _http_validation_error_model_schema})

_header_array_option_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Allowed values for the render.header_array option.",
  "enum" : [ "row", "column" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HeaderArrayOption": _header_array_option_model_schema})

_hierarchical_model_schema = json.loads(
    r"""{
  "title" : "Hierarchical",
  "description" : "if true, use hierarchical objects to represent multiple row (or column) dimensions, otherwise multi-keys get concatenated with a dot-delimiter. If the value is a list, only these levels are kept as separate levels, while remaining levels get concatenated keys",
  "anyOf" : [ {
    "type" : "boolean"
  }, {
    "type" : "array",
    "items" : {
      "type" : "string"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Hierarchical": _hierarchical_model_schema})

_interpolation_model_schema = json.loads(
    r"""{
  "title" : "Interpolation",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Default_Interpolation_anyOf"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpec"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Interpolation": _interpolation_model_schema})

_interpolation_method_model_schema = json.loads(
    r"""{
  "title" : "Interpolation method",
  "type" : "string",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/InterpolationSpecPad"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecFixed"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecBackfill"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecLinear"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecNearest"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecZero"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecSlinear"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecQuadratic"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecCubic"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecPolynomial"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecSpline"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecFrom_derivatives"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecPchip"
  }, {
    "$ref" : "#/components/schemas/InterpolationSpecAkima"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Interpolation_method": _interpolation_method_model_schema})

_interpolation_parameter_model_schema = json.loads(
    r"""{
  "title" : "Interpolation parameter",
  "description" : "Optional parameter value for the interpolation method (see method description).",
  "anyOf" : [ {
    "type" : "number"
  }, {
    "type" : "integer"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Interpolation_parameter": _interpolation_parameter_model_schema
})

_interpolation_spec_model_schema = json.loads(
    r"""{
  "required" : [ "method" ],
  "type" : "object",
  "properties" : {
    "method" : {
      "$ref" : "#/components/schemas/Interpolation_method"
    },
    "value" : {
      "$ref" : "#/components/schemas/Interpolation_parameter"
    },
    "order" : {
      "title" : "Interpolation order",
      "type" : "integer",
      "description" : "Optional order parameter for the interpolation method (see method description)."
    }
  },
  "additionalProperties" : true,
  "description" : "Defines whether, and how to treat missing values.\n\nThis can occur in two circumstances when aggregating (setting a sample frequency):\n* missing values: if there are missing (or invalid) values stored for\na given freq-interval,\n\"interpolation\" specifies how to compute these.\n* down-sampling: when the specified freq is smaller than the series’\nactual frequency.\n\"interpolation\" specifies how to compute intermediate values."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"InterpolationSpec": _interpolation_spec_model_schema})

_interpolation_spec_akima_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a non-smoothing spline of order 2, called Akima interpolation.",
  "enum" : [ "akima" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecAkima": _interpolation_spec_akima_model_schema
})

_interpolation_spec_backfill_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Same as pad, but using the last observed value. This method also extrapolates",
  "enum" : [ "backfill" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecBackfill": _interpolation_spec_backfill_model_schema
})

_interpolation_spec_cubic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 3, which is a piecewise polynomial.",
  "enum" : [ "cubic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecCubic": _interpolation_spec_cubic_model_schema
})

_interpolation_spec_fixed_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a fixed, user-specified value. This method also extrapolates.",
  "enum" : [ "fixed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecFixed": _interpolation_spec_fixed_model_schema
})

_interpolation_spec_from_derivatives_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the derivative of order 1.",
  "enum" : [ "from_derivatives" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecFrom_derivatives": _interpolation_spec_from_derivatives_model_schema
})

_interpolation_spec_linear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates",
  "enum" : [ "linear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecLinear": _interpolation_spec_linear_model_schema
})

_interpolation_spec_nearest_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecNearest": _interpolation_spec_nearest_model_schema
})

_interpolation_spec_pad_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the value of the first observed point. This method also extrapolates.",
  "enum" : [ "pad" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"InterpolationSpecPad": _interpolation_spec_pad_model_schema})

_interpolation_spec_pchip_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a piecewise cubic spline function.",
  "enum" : [ "pchip" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecPchip": _interpolation_spec_pchip_model_schema
})

_interpolation_spec_polynomial_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a polynomial of the lowest possible degree passing trough the data points.",
  "enum" : [ "polynomial" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecPolynomial": _interpolation_spec_polynomial_model_schema
})

_interpolation_spec_quadratic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 2, which is a piecewise polynomial.",
  "enum" : [ "quadratic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecQuadratic": _interpolation_spec_quadratic_model_schema
})

_interpolation_spec_slinear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 1, which is a piecewise polynomial.",
  "enum" : [ "slinear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecSlinear": _interpolation_spec_slinear_model_schema
})

_interpolation_spec_spline_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of a user-specified order.",
  "enum" : [ "spline" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecSpline": _interpolation_spec_spline_model_schema
})

_interpolation_spec_zero_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 0, which is a piecewise polynomial.",
  "enum" : [ "zero" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InterpolationSpecZero": _interpolation_spec_zero_model_schema
})

_links_value_model_schema = json.loads(
    r"""{
  "title" : "Links_value",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Links_value": _links_value_model_schema})

_location_inner_model_schema = json.loads(
    r"""{
  "title" : "Location_inner",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "type" : "integer"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Location_inner": _location_inner_model_schema})

_message_model_schema = json.loads(
    r"""{
  "title" : "Message",
  "required" : [ "message" ],
  "type" : "object",
  "properties" : {
    "code" : {
      "title" : "code",
      "type" : "string",
      "nullable" : true
    },
    "message" : {
      "title" : "Message",
      "type" : "string"
    },
    "level" : {
      "$ref" : "#/components/schemas/Message_level"
    },
    "args" : {
      "title" : "args",
      "type" : "object",
      "additionalProperties" : true,
      "nullable" : true
    }
  },
  "description" : "Individual (info/warning/error) message in a response."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Message": _message_model_schema})

_message_arguments_model_schema = json.loads(
    r"""{
  "title" : "Message Arguments",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "$ref" : "#/components/schemas/MessageProperties"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Message_Arguments": _message_arguments_model_schema})

_message_level_model_schema = json.loads(
    r"""{
  "title" : "Message_level",
  "type" : "string",
  "default" : "info",
  "enum" : [ "debug", "info", "warning", "error", "fatal" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Message_level": _message_level_model_schema})

_message_properties_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "resource" : {
      "title" : "Series resource id",
      "type" : "string"
    },
    "metric" : {
      "title" : "Series metric",
      "type" : "string"
    }
  },
  "additionalProperties" : true,
  "description" : "Additional message arguments."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MessageProperties": _message_properties_model_schema})

_object_data_model_schema = json.loads(
    r"""{
  "required" : [ "timestamp" ],
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "$ref" : "#/components/schemas/Timestamp"
    },
    "timestamp_iso" : {
      "$ref" : "#/components/schemas/TimestampIso"
    },
    "role" : {
      "$ref" : "#/components/schemas/Role"
    },
    "resource" : {
      "title" : "Resource",
      "type" : "string",
      "description" : "Series resource id, if applicable for all values."
    },
    "metric" : {
      "title" : "Metric",
      "type" : "string",
      "description" : "Series metric, if applicable for all values."
    },
    "aggregation" : {
      "title" : "Aggregation",
      "type" : "string",
      "description" : "Series aggregation, if applicable for all values."
    },
    "levels" : {
      "title" : "Hierarchical Levels",
      "type" : "array",
      "description" : "Attribute level names used to key the values for this observation.\n\nLevels that are flattened have a dot-separated key.\n\nIf all observations have the same attribute for a level, that level might be omitted.",
      "example" : [ "resource", "metric", "aggregation" ],
      "items" : {
        "type" : "string"
      }
    }
  },
  "additionalProperties" : {
    "$ref" : "#/components/schemas/Data_"
  },
  "description" : "Result data for a timestamp in object format."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ObjectData": _object_data_model_schema})

_object_data_set_model_schema = json.loads(
    r"""{
  "required" : [ "data" ],
  "type" : "object",
  "properties" : {
    "attributes" : {
      "$ref" : "#/components/schemas/DataSetAttributes"
    },
    "window_spec" : {
      "$ref" : "#/components/schemas/DataSetWindow"
    },
    "data" : {
      "title" : "Data",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/ObjectData"
      }
    }
  },
  "additionalProperties" : true,
  "description" : "Data result in object format.\n\nResult item when render option `render.header_array` is not set.\n\nThe data values are keyed by their attributes (`resource`, `metric`, `aggregation`),\naccording to the render options:\n* _hierachical_: for each level, a sub-object is created\n  (e.g. `render.mode=hier_dict`)\n* _flattened_: the attributes are '.'-separated concatenation\n  of the attributes (e.g `render.mode=flat_dict`)\n* _mixed_: (.e.g. `render.mode=metric_flat_dict`) a single level\n    (e.g. `metric`) is used as main key, any remaining levels\n    (`resource`,`aggregation`) are indicated with a flattened subkey.\n\nWhen `render.rollup=true`, the attribute levels that are the same for all series are\nnot used as key, but reported as a data or table attribute."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ObjectDataSet": _object_data_set_model_schema})

_queries_list_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "count", "limit", "offset", "queries" ],
  "type" : "object",
  "properties" : {
    "messages" : {
      "title" : "Messages",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Message"
      }
    },
    "queries" : {
      "title" : "Query item list",
      "type" : "array",
      "description" : "One page of matching query definitions.",
      "items" : {
        "$ref" : "#/components/schemas/QueryListItem"
      }
    },
    "count" : {
      "title" : "Current page size",
      "type" : "integer",
      "description" : "Number of query definitions returned in the current response."
    },
    "offset" : {
      "title" : "Page offset",
      "type" : "integer",
      "description" : "Offset in the full listing (skipped definitions)."
    },
    "limit" : {
      "title" : "Page size limit",
      "type" : "integer",
      "description" : "Maximal number of query definitions returned in one response."
    },
    "total_count" : {
      "title" : "Total count",
      "type" : "integer",
      "description" : "Total number of query definitions matching the filter."
    },
    "_links" : {
      "$ref" : "#/components/schemas/QueryListHALLinks"
    }
  },
  "additionalProperties" : true,
  "description" : "Listing of named queries, with paging links."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueriesListResponse": _queries_list_response_model_schema})

_query_definition_model_schema = json.loads(
    r"""{
  "title" : "Query Definition",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/QueryUpdateInput"
  }, {
    "$ref" : "#/components/schemas/Query-Input"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query_Definition": _query_definition_model_schema})

_query_entity_input_model_schema = json.loads(
    r"""{
  "required" : [ "name", "query" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "Query name",
      "type" : "string",
      "description" : "Name of the stored query definition."
    },
    "meta" : {
      "title" : "Query metadata",
      "type" : "object",
      "additionalProperties" : true,
      "description" : "User metadata for the query definition."
    },
    "query" : {
      "$ref" : "#/components/schemas/Query-Input"
    }
  },
  "additionalProperties" : true,
  "description" : "Input data to create a query definition."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueryEntityInput": _query_entity_input_model_schema})

_query_execution_message_model_schema = json.loads(
    r"""{
  "required" : [ "action", "category", "level", "message", "timestamp" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "title" : "Message",
      "type" : "string",
      "description" : "A human readable message."
    },
    "level" : {
      "$ref" : "#/components/schemas/QueryExecutionMessage_level"
    },
    "timestamp" : {
      "title" : "Timestamp",
      "type" : "string",
      "format" : "date-time"
    },
    "action" : {
      "title" : "Action",
      "type" : "string",
      "description" : "The request action that caused this message."
    },
    "category" : {
      "title" : "Message Category",
      "type" : "string",
      "description" : "The subsystem that issued this message.",
      "example" : "data"
    },
    "properties" : {
      "$ref" : "#/components/schemas/Message_Arguments"
    },
    "exception" : {
      "$ref" : "#/components/schemas/CauseException"
    }
  },
  "additionalProperties" : true,
  "description" : "A message object that informs or warns about a query execution issue."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "QueryExecutionMessage": _query_execution_message_model_schema
})

_query_execution_message_level_model_schema = json.loads(
    r"""{
  "title" : "QueryExecutionMessage_level",
  "type" : "string",
  "enum" : [ "debug", "info", "warning", "error" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "QueryExecutionMessage_level": _query_execution_message_level_model_schema
})

_query_hal_links_model_schema = json.loads(
    r"""{
  "required" : [ "execute", "self" ],
  "type" : "object",
  "properties" : {
    "self" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "execute" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "additionalProperties" : true,
  "description" : "HAL Links for a query entity."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueryHALLinks": _query_hal_links_model_schema})

_query_input_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"Query-Input": _query_input_model_schema})

_query_input_akima_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a non-smoothing spline of order 2, called Akima interpolation.",
  "enum" : [ "akima" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputAkima": _query_input_akima_model_schema})

_query_input_backfill_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Same as pad, but using the last observed value. This method also extrapolates",
  "enum" : [ "backfill" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputBackfill": _query_input_backfill_model_schema})

_query_input_count_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the count of observations in the sample interval.",
  "enum" : [ "count" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputCount": _query_input_count_model_schema})

_query_input_cubic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 3, which is a piecewise polynomial.",
  "enum" : [ "cubic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputCubic": _query_input_cubic_model_schema})

_query_input_first_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the first value (in time) to represent all data for the sample interval.",
  "enum" : [ "first" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputFirst": _query_input_first_model_schema})

_query_input_fixed_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a fixed, user-specified value. This method also extrapolates.",
  "enum" : [ "fixed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputFixed": _query_input_fixed_model_schema})

_query_input_from_derivatives_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the derivative of order 1.",
  "enum" : [ "from_derivatives" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Query-InputFrom_derivatives": _query_input_from_derivatives_model_schema
})

_query_input_inferred_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "When `inferred` is specified, the frequency of aggregation will be inferred from the main/first time series. This can be used to regularize the time series",
  "enum" : [ "inferred" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputInferred": _query_input_inferred_model_schema})

_query_input_last_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the last value (in time) to represent all data for the sample interval.",
  "enum" : [ "last" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputLast": _query_input_last_model_schema})

_query_input_linear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates",
  "enum" : [ "linear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputLinear": _query_input_linear_model_schema})

_query_input_max_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the maximum of all values in the sample interval.",
  "enum" : [ "max" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputMax": _query_input_max_model_schema})

_query_input_mean_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the mean value: The sum of values divided by number of observations.",
  "enum" : [ "mean" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputMean": _query_input_mean_model_schema})

_query_input_median_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.",
  "enum" : [ "median" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputMedian": _query_input_median_model_schema})

_query_input_min_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the minimum of all values in the sample interval.",
  "enum" : [ "min" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputMin": _query_input_min_model_schema})

_query_input_nearest_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputNearest": _query_input_nearest_model_schema})

_query_input_pad_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the value of the first observed point. This method also extrapolates.",
  "enum" : [ "pad" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputPad": _query_input_pad_model_schema})

_query_input_pchip_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a piecewise cubic spline function.",
  "enum" : [ "pchip" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputPchip": _query_input_pchip_model_schema})

_query_input_polynomial_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a polynomial of the lowest possible degree passing trough the data points.",
  "enum" : [ "polynomial" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Query-InputPolynomial": _query_input_polynomial_model_schema
})

_query_input_quadratic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 2, which is a piecewise polynomial.",
  "enum" : [ "quadratic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputQuadratic": _query_input_quadratic_model_schema})

_query_input_slinear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 1, which is a piecewise polynomial.",
  "enum" : [ "slinear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputSlinear": _query_input_slinear_model_schema})

_query_input_spline_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of a user-specified order.",
  "enum" : [ "spline" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputSpline": _query_input_spline_model_schema})

_query_input_std_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the standard deviation of all observations in the sample interval.",
  "enum" : [ "std" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputStd": _query_input_std_model_schema})

_query_input_sum_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "The sum of all values summarizes the data for the sample interval.",
  "enum" : [ "sum" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputSum": _query_input_sum_model_schema})

_query_input_zero_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 0, which is a piecewise polynomial.",
  "enum" : [ "zero" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-InputZero": _query_input_zero_model_schema})

_query_list_hal_links_model_schema = json.loads(
    r"""{
  "title" : "QueryListHALLinks",
  "required" : [ "self" ],
  "type" : "object",
  "properties" : {
    "self" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "first" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "prev" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "next" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "last" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "additionalProperties" : true,
  "description" : "HAL Links for a query entity."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueryListHALLinks": _query_list_hal_links_model_schema})

_query_list_item_model_schema = json.loads(
    r"""{
  "title" : "QueryListItem",
  "required" : [ "_links", "attrs", "name" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/QueryHALLinks"
    },
    "attrs" : {
      "title" : "Query attributes",
      "type" : "object",
      "additionalProperties" : true,
      "description" : "System provided metadata for the query definition."
    },
    "name" : {
      "title" : "Query name",
      "type" : "string",
      "description" : "Name of the stored query definition."
    },
    "meta" : {
      "title" : "Query metadata",
      "type" : "object",
      "additionalProperties" : true,
      "description" : "User metadata for the query definition."
    }
  },
  "additionalProperties" : true,
  "description" : "Listing of a query definition item."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueryListItem": _query_list_item_model_schema})

_query_output_model_schema = json.loads(
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
      "$ref" : "#/components/schemas/Default_Interpolation"
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
    }
  },
  "additionalProperties" : true,
  "description" : "Query definition for a Waylay analytics query.\n\nSee also [api docs](https://docs.waylay.io/#/api/query/?id=data-query-json-representation)."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-Output": _query_output_model_schema})

_query_output_akima_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a non-smoothing spline of order 2, called Akima interpolation.",
  "enum" : [ "akima" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputAkima": _query_output_akima_model_schema})

_query_output_backfill_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Same as pad, but using the last observed value. This method also extrapolates",
  "enum" : [ "backfill" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputBackfill": _query_output_backfill_model_schema})

_query_output_count_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the count of observations in the sample interval.",
  "enum" : [ "count" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputCount": _query_output_count_model_schema})

_query_output_cubic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 3, which is a piecewise polynomial.",
  "enum" : [ "cubic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputCubic": _query_output_cubic_model_schema})

_query_output_first_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the first value (in time) to represent all data for the sample interval.",
  "enum" : [ "first" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputFirst": _query_output_first_model_schema})

_query_output_fixed_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a fixed, user-specified value. This method also extrapolates.",
  "enum" : [ "fixed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputFixed": _query_output_fixed_model_schema})

_query_output_from_derivatives_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the derivative of order 1.",
  "enum" : [ "from_derivatives" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Query-OutputFrom_derivatives": _query_output_from_derivatives_model_schema
})

_query_output_inferred_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "When `inferred` is specified, the frequency of aggregation will be inferred from the main/first time series. This can be used to regularize the time series",
  "enum" : [ "inferred" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputInferred": _query_output_inferred_model_schema})

_query_output_last_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the last value (in time) to represent all data for the sample interval.",
  "enum" : [ "last" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputLast": _query_output_last_model_schema})

_query_output_linear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates",
  "enum" : [ "linear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputLinear": _query_output_linear_model_schema})

_query_output_max_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the maximum of all values in the sample interval.",
  "enum" : [ "max" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputMax": _query_output_max_model_schema})

_query_output_mean_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the mean value: The sum of values divided by number of observations.",
  "enum" : [ "mean" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputMean": _query_output_mean_model_schema})

_query_output_median_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.",
  "enum" : [ "median" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputMedian": _query_output_median_model_schema})

_query_output_min_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the minimum of all values in the sample interval.",
  "enum" : [ "min" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputMin": _query_output_min_model_schema})

_query_output_nearest_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputNearest": _query_output_nearest_model_schema})

_query_output_pad_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the value of the first observed point. This method also extrapolates.",
  "enum" : [ "pad" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputPad": _query_output_pad_model_schema})

_query_output_pchip_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a piecewise cubic spline function.",
  "enum" : [ "pchip" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputPchip": _query_output_pchip_model_schema})

_query_output_polynomial_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a polynomial of the lowest possible degree passing trough the data points.",
  "enum" : [ "polynomial" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Query-OutputPolynomial": _query_output_polynomial_model_schema
})

_query_output_quadratic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 2, which is a piecewise polynomial.",
  "enum" : [ "quadratic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Query-OutputQuadratic": _query_output_quadratic_model_schema
})

_query_output_slinear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 1, which is a piecewise polynomial.",
  "enum" : [ "slinear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputSlinear": _query_output_slinear_model_schema})

_query_output_spline_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of a user-specified order.",
  "enum" : [ "spline" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputSpline": _query_output_spline_model_schema})

_query_output_std_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the standard deviation of all observations in the sample interval.",
  "enum" : [ "std" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputStd": _query_output_std_model_schema})

_query_output_sum_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "The sum of all values summarizes the data for the sample interval.",
  "enum" : [ "sum" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputSum": _query_output_sum_model_schema})

_query_output_zero_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 0, which is a piecewise polynomial.",
  "enum" : [ "zero" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Query-OutputZero": _query_output_zero_model_schema})

_query_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "attrs", "name", "query" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/QueryHALLinks"
    },
    "attrs" : {
      "title" : "Query attributes",
      "type" : "object",
      "additionalProperties" : true,
      "description" : "System provided metadata for the query definition."
    },
    "name" : {
      "title" : "Query name",
      "type" : "string",
      "description" : "Name of the stored query definition."
    },
    "meta" : {
      "title" : "Query metadata",
      "type" : "object",
      "additionalProperties" : true,
      "description" : "User metadata for the query definition."
    },
    "query" : {
      "$ref" : "#/components/schemas/Query-Output"
    },
    "messages" : {
      "title" : "Messages",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Message"
      }
    }
  },
  "additionalProperties" : true,
  "description" : "Represents a single named query."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueryResponse": _query_response_model_schema})

_query_result_model_schema = json.loads(
    r"""{
  "required" : [ "data", "messages", "query" ],
  "type" : "object",
  "properties" : {
    "data" : {
      "title" : "Response Data Sets",
      "type" : "array",
      "description" : "A list of data sets, each with their own time axis. There will be one dataset for each `role` specified in the query (by default a single `input` role).\n\nThe data is represented according to the `render`  options in the query (default `COMPACT_WS`).",
      "items" : {
        "$ref" : "#/components/schemas/Response_Data_Set"
      }
    },
    "query" : {
      "$ref" : "#/components/schemas/Query-Output"
    },
    "messages" : {
      "title" : "Messages and Warnings",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/QueryExecutionMessage"
      }
    }
  },
  "additionalProperties" : true,
  "description" : "A json data response.\n\nUses the format as specified by the\n`render` options of the request (defaults to `COMPACT_WS`).\n'"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueryResult": _query_result_model_schema})

_query_update_input_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "meta" : {
      "title" : "Query metadata",
      "type" : "object",
      "additionalProperties" : true,
      "description" : "User metadata for the query definition."
    },
    "query" : {
      "$ref" : "#/components/schemas/Query-Input"
    }
  },
  "additionalProperties" : true,
  "description" : "Input data to update a query definition."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueryUpdateInput": _query_update_input_model_schema})

_render_model_schema = json.loads(
    r"""{
  "title" : "Render",
  "type" : "object",
  "properties" : {
    "mode" : {
      "$ref" : "#/components/schemas/Render_mode"
    },
    "roll_up" : {
      "title" : "Roll Up",
      "type" : "boolean",
      "description" : "move up attributes on rows (or columns) that are the same for             all rows (or columns) to a table attribute.             Levels enumerated in 'hierarchical' are excluded."
    },
    "hierarchical" : {
      "$ref" : "#/components/schemas/Hierarchical"
    },
    "value_key" : {
      "title" : "Value Key",
      "type" : "string",
      "description" : "if set, use this key in the value object to report data values"
    },
    "show_levels" : {
      "title" : "Show Levels",
      "type" : "boolean",
      "description" : "if set, report the levels used in the data values (either hierarchical or flat)"
    },
    "iso_timestamp" : {
      "title" : "Iso Timestamp",
      "type" : "boolean",
      "description" : "if set, render timestamps in a row or column index with both epoch and iso representations"
    },
    "row_key" : {
      "title" : "Row Key",
      "type" : "string",
      "description" : "if set, use this key as name of the row-dimension for single-dimensional rows"
    },
    "column_key" : {
      "title" : "Column Key",
      "type" : "string",
      "description" : "if set, use this key as name of the column-dimension for single-dimensional columns"
    },
    "header_array" : {
      "$ref" : "#/components/schemas/HeaderArrayOption"
    },
    "data_axis" : {
      "$ref" : "#/components/schemas/DataAxisOption"
    },
    "key_seperator" : {
      "title" : "Key Seperator",
      "type" : "string",
      "description" : "character used to concatenate multi-key columns or rows when required"
    },
    "key_skip_empty" : {
      "title" : "Key Skip Empty",
      "type" : "boolean",
      "description" : "skip empty values in concatenating multi-key column or row headers"
    },
    "include_window_spec" : {
      "title" : "Include Window Spec",
      "type" : "boolean",
      "description" : "if set, include window specification in render modes that support it"
    }
  },
  "additionalProperties" : true,
  "description" : "Configures the representation of data sets returned by the query API."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Render": _render_model_schema})

_render_compact_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`",
  "enum" : [ "COMPACT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderCOMPACT": _render_compact_model_schema})

_render_compact_ws_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers. Show the time window attributes.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`\n- `include_window_spec`: `True`",
  "enum" : [ "COMPACT_WS" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderCOMPACT_WS": _render_compact_ws_model_schema})

_render_csv_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render in csv format with row headers.\n\n###### options\n- `iso_timestamp`: `False`",
  "enum" : [ "CSV" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderCSV": _render_csv_model_schema})

_render_flat_dict_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render an object for each observation. Uses flattened keys.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `False`\n- `show_levels`: `True`\n- `roll_up`: `False`",
  "enum" : [ "FLAT_DICT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderFLAT_DICT": _render_flat_dict_model_schema})

_render_header_column_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Renders row index in `rows`, and each series as a values array.\n\nThe series are prefixed by their series attributes.The `rows` index is prefixed by the labels for these attributes.\n\n###### options\n- `iso_timestamp`: `True`\n- `header_array`: `column`\n- `roll_up`: `False`\n- `data_axis`: `row`",
  "enum" : [ "HEADER_COLUMN" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderHEADER_COLUMN": _render_header_column_model_schema})

_render_header_row_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render rows of timestamp and values. Show column headers. Includes an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `header_array`: `row`\n- `roll_up`: `False`\n- `data_axis`: `column`",
  "enum" : [ "HEADER_ROW" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderHEADER_ROW": _render_header_row_model_schema})

_render_hier_dict_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render an hierarchical object for each observation. Shows an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `True`\n- `show_levels`: `True`\n- `roll_up`: `True`",
  "enum" : [ "HIER_DICT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderHIER_DICT": _render_hier_dict_model_schema})

_render_metric_flat_dict_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render an object with metric keys for each observation. Shows an iso timestamp.\n\n###### options\n- `iso_timestamp`: `True`\n- `hierarchical`: `['metric']`\n- `show_levels`: `False`\n- `roll_up`: `True`\n- `key_skip_empty`: `True`",
  "enum" : [ "METRIC_FLAT_DICT" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RenderMETRIC_FLAT_DICT": _render_metric_flat_dict_model_schema
})

_render_mode_model_schema = json.loads(
    r"""{
  "$ref" : "#/components/schemas/_RenderMode"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Render_mode": _render_mode_model_schema})

_render_series_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render timestamps and each series (column) as a values array. Show column headers.\n\n###### options\n- `iso_timestamp`: `False`\n- `header_array`: `row`\n- `data_axis`: `row`\n- `roll_up`: `True`\n- `include_window_spec`: `True`",
  "enum" : [ "SERIES" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderSERIES": _render_series_model_schema})

_render_upload_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Render in an object format compatible with the `/data/v1/events` upload.\n\n###### options\n- `iso_timestamp`: `False`\n- `hierarchical`: `False`\n- `show_levels`: `False`\n- `roll_up`: `True`",
  "enum" : [ "UPLOAD" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RenderUPLOAD": _render_upload_model_schema})

_response_data_set_model_schema = json.loads(
    r"""{
  "title" : "Response Data Set",
  "description" : "Result timeseries data set, with one time dimension.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/RowDataSet"
  }, {
    "$ref" : "#/components/schemas/SeriesDataSet"
  }, {
    "$ref" : "#/components/schemas/ColumnDataSet"
  }, {
    "$ref" : "#/components/schemas/ObjectDataSet"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Response_Data_Set": _response_data_set_model_schema})

_row_data_set_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"RowDataSet": _row_data_set_model_schema})

_row_data_set_data_axis_model_schema = json.loads(
    r"""{
  "title" : "RowDataSet_data_axis",
  "type" : "string",
  "default" : "column",
  "enum" : [ "column" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RowDataSet_data_axis": _row_data_set_data_axis_model_schema})

_row_header_model_schema = json.loads(
    r"""{
  "required" : [ "timestamp" ],
  "type" : "object",
  "properties" : {
    "timestamp" : {
      "$ref" : "#/components/schemas/Timestamp"
    },
    "timestamp_iso" : {
      "$ref" : "#/components/schemas/TimestampIso"
    }
  },
  "additionalProperties" : true,
  "description" : "Index entry attributes.\n\nAttributes for a timestamp index entry."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RowHeader": _row_header_model_schema})

_row_headers_inner_model_schema = json.loads(
    r"""{
  "title" : "Row_Headers_inner",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ColumnIndexRowHeader"
  }, {
    "$ref" : "#/components/schemas/RowHeader"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Row_Headers_inner": _row_headers_inner_model_schema})

_series_data_set_model_schema = json.loads(
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
      "$ref" : "#/components/schemas/ColumnDataSet_data_axis"
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
        "title" : "Series",
        "type" : "array",
        "description" : "All metric observation values for a single series.",
        "items" : {
          "$ref" : "#/components/schemas/Datum"
        }
      },
      "x-prefixItems" : [ {
        "items" : {
          "$ref" : "#/components/schemas/Timestamp"
        },
        "type" : "array",
        "title" : "Timestamp Index",
        "description" : "The timestamp index for this result data."
      } ]
    }
  },
  "additionalProperties" : true,
  "description" : "Column-oriented dataset.\n\nTimeseries data layout with a column header\nand a seperate data array for the time index and each series.\nResult for render options `data_axis=row` and `header_array=row`."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesDataSet": _series_data_set_model_schema})

_series_spec_model_schema = json.loads(
    r"""{
  "title" : "SeriesSpec",
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "Name",
      "type" : "string",
      "description" : "Optional alias name for the series. This name is used when exporting the dataset to CSV format.",
      "example" : "demoQuery"
    },
    "resource" : {
      "title" : "Resource",
      "type" : "string",
      "description" : "Resource id for the series, required unless it is specified as a query default.",
      "example" : "13efb488-75ac-4dac-828a-d49c5c2ebbfc"
    },
    "metric" : {
      "title" : "Metric",
      "type" : "string",
      "description" : "Metric name for the series, required unless it is specified as a query default.",
      "example" : "temperature"
    },
    "aggregration" : {
      "$ref" : "#/components/schemas/Aggregration"
    },
    "interpolation" : {
      "$ref" : "#/components/schemas/Interpolation"
    }
  },
  "additionalProperties" : true,
  "description" : "Query specification for a single series."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpec": _series_spec_model_schema})

_series_spec_akima_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a non-smoothing spline of order 2, called Akima interpolation.",
  "enum" : [ "akima" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecAkima": _series_spec_akima_model_schema})

_series_spec_backfill_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Same as pad, but using the last observed value. This method also extrapolates",
  "enum" : [ "backfill" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecBackfill": _series_spec_backfill_model_schema})

_series_spec_count_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the count of observations in the sample interval.",
  "enum" : [ "count" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecCount": _series_spec_count_model_schema})

_series_spec_cubic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 3, which is a piecewise polynomial.",
  "enum" : [ "cubic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecCubic": _series_spec_cubic_model_schema})

_series_spec_first_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the first value (in time) to represent all data for the sample interval.",
  "enum" : [ "first" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecFirst": _series_spec_first_model_schema})

_series_spec_fixed_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a fixed, user-specified value. This method also extrapolates.",
  "enum" : [ "fixed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecFixed": _series_spec_fixed_model_schema})

_series_spec_from_derivatives_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the derivative of order 1.",
  "enum" : [ "from_derivatives" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SeriesSpecFrom_derivatives": _series_spec_from_derivatives_model_schema
})

_series_spec_last_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the last value (in time) to represent all data for the sample interval.",
  "enum" : [ "last" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecLast": _series_spec_last_model_schema})

_series_spec_linear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates",
  "enum" : [ "linear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecLinear": _series_spec_linear_model_schema})

_series_spec_max_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the maximum of all values in the sample interval.",
  "enum" : [ "max" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecMax": _series_spec_max_model_schema})

_series_spec_mean_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the mean value: The sum of values divided by number of observations.",
  "enum" : [ "mean" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecMean": _series_spec_mean_model_schema})

_series_spec_median_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.",
  "enum" : [ "median" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecMedian": _series_spec_median_model_schema})

_series_spec_min_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the minimum of all values in the sample interval.",
  "enum" : [ "min" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecMin": _series_spec_min_model_schema})

_series_spec_nearest_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the value that is closest in time.",
  "enum" : [ "nearest" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecNearest": _series_spec_nearest_model_schema})

_series_spec_pad_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with the value of the first observed point. This method also extrapolates.",
  "enum" : [ "pad" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecPad": _series_spec_pad_model_schema})

_series_spec_pchip_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a piecewise cubic spline function.",
  "enum" : [ "pchip" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecPchip": _series_spec_pchip_model_schema})

_series_spec_polynomial_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a polynomial of the lowest possible degree passing trough the data points.",
  "enum" : [ "polynomial" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecPolynomial": _series_spec_polynomial_model_schema})

_series_spec_quadratic_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 2, which is a piecewise polynomial.",
  "enum" : [ "quadratic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecQuadratic": _series_spec_quadratic_model_schema})

_series_spec_slinear_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 1, which is a piecewise polynomial.",
  "enum" : [ "slinear" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecSlinear": _series_spec_slinear_model_schema})

_series_spec_spline_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of a user-specified order.",
  "enum" : [ "spline" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecSpline": _series_spec_spline_model_schema})

_series_spec_std_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Use the standard deviation of all observations in the sample interval.",
  "enum" : [ "std" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecStd": _series_spec_std_model_schema})

_series_spec_sum_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "The sum of all values summarizes the data for the sample interval.",
  "enum" : [ "sum" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecSum": _series_spec_sum_model_schema})

_series_spec_zero_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Interpolate with a spline function of order 0, which is a piecewise polynomial.",
  "enum" : [ "zero" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SeriesSpecZero": _series_spec_zero_model_schema})

_time_window_from_model_schema = json.loads(
    r"""{
  "title" : "Time Window From",
  "description" : "The start of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)  specifiers.",
  "oneOf" : [ {
    "title" : "ISO8601 absolute timestamp",
    "pattern" : "[0-9]{4}-[0-9]{2}-[0-9]{2}(T.*)?",
    "type" : "string",
    "description" : "A date or date-time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format. When no timezone is specified, the UTC timezone is assumed (`+00:00`)",
    "format" : "date-time",
    "example" : "2018-03-21T12:23:00+01:00"
  }, {
    "title" : "UNIX epoch milliseconds",
    "minimum" : 0,
    "type" : "integer",
    "description" : "Absolute timestamp milliseconds in unix epoch since 1970-01-01.",
    "example" : 1534836422284
  }, {
    "title" : "ISO8601 Period Before Now",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "Specifies a timestamp before _now_ as a period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Time_Window_From": _time_window_from_model_schema})

_time_window_until_model_schema = json.loads(
    r"""{
  "title" : "Time Window Until",
  "description" : "The end (not-inclusive) of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)specifiers.",
  "oneOf" : [ {
    "title" : "ISO8601 absolute timestamp",
    "pattern" : "[0-9]{4}-[0-9]{2}-[0-9]{2}(T.*)?",
    "type" : "string",
    "description" : "A date or date-time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format. When no timezone is specified, the UTC timezone is assumed (`+00:00`)",
    "format" : "date-time",
    "example" : "2018-03-21T12:23:00+01:00"
  }, {
    "title" : "UNIX epoch milliseconds",
    "minimum" : 0,
    "type" : "integer",
    "description" : "Absolute timestamp milliseconds in unix epoch since 1970-01-01.",
    "example" : 1534836422284
  }, {
    "title" : "ISO8601 Period Before Now",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "Specifies a timestamp before _now_ as a period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Time_Window_Until": _time_window_until_model_schema})

_validation_error_model_schema = json.loads(
    r"""{
  "title" : "ValidationError",
  "required" : [ "loc", "msg", "type" ],
  "type" : "object",
  "properties" : {
    "loc" : {
      "title" : "Location",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Location_inner"
      }
    },
    "msg" : {
      "title" : "Message",
      "type" : "string"
    },
    "type" : {
      "title" : "Error Type",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ValidationError": _validation_error_model_schema})

_window_model_schema = json.loads(
    r"""{
  "title" : "Window",
  "type" : "string",
  "description" : "The absolute size of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.",
  "oneOf" : [ {
    "title" : "ISO8601 period ",
    "pattern" : "^P([0-9]+Y)?([0-9]+M)?([0-9]+W)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\\.[0-9]*)?S)?)?$",
    "type" : "string",
    "description" : "A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.",
    "format" : "period",
    "example" : "PT3H15M"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Window": _window_model_schema})
