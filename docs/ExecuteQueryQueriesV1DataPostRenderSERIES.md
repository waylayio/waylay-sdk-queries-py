# ExecuteQueryQueriesV1DataPostRenderSERIES

Render timestamps and each series (column) as a values array. Show column headers.  ###### options - `iso_timestamp`: `False` - `header_array`: `row` - `data_axis`: `row` - `roll_up`: `True` - `include_window_spec`: `True`

**Source:** `waylay.services.queries.models.execute_query_queries_v1_data_post_render_series`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SERIES** | `'SERIES'` |

## Example

```python
from waylay.services.queries.models.execute_query_queries_v1_data_post_render_series import (
    ExecuteQueryQueriesV1DataPostRenderSERIES,
)

# Use enum by value
my_execute_query_queries_v1_data_post_render_series = (
    ExecuteQueryQueriesV1DataPostRenderSERIES.SERIES
)
print(my_execute_query_queries_v1_data_post_render_series)  # Output: 'SERIES'

# Or by string value
my_execute_query_queries_v1_data_post_render_series = (
    ExecuteQueryQueriesV1DataPostRenderSERIES("SERIES")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


