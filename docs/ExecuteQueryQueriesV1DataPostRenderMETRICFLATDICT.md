# ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT

Render an object with metric keys for each observation. Shows an iso timestamp.  ###### options - `iso_timestamp`: `True` - `hierarchical`: `['metric']` - `show_levels`: `False` - `roll_up`: `True` - `key_skip_empty`: `True`

**Source:** `waylay.services.queries.models.execute_query_queries_v1_data_post_render_metricflatdict`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**METRIC_FLAT_DICT** | `'METRIC_FLAT_DICT'` |

## Example

```python
from waylay.services.queries.models.execute_query_queries_v1_data_post_render_metricflatdict import (
    ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT,
)

# Use enum by value
my_execute_query_queries_v1_data_post_render_metricflatdict = (
    ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT.METRIC_FLAT_DICT
)
print(
    my_execute_query_queries_v1_data_post_render_metricflatdict
)  # Output: 'METRIC_FLAT_DICT'

# Or by string value
my_execute_query_queries_v1_data_post_render_metricflatdict = (
    ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT("METRIC_FLAT_DICT")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


