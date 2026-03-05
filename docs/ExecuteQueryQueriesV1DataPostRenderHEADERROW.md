# ExecuteQueryQueriesV1DataPostRenderHEADERROW

Render rows of timestamp and values. Show column headers. Includes an iso timestamp.  ###### options - `iso_timestamp`: `True` - `header_array`: `row` - `roll_up`: `False` - `data_axis`: `column`

**Source:** `waylay.services.queries.models.execute_query_queries_v1_data_post_render_headerrow`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**HEADER_ROW** | `'HEADER_ROW'` |

## Example

```python
from waylay.services.queries.models.execute_query_queries_v1_data_post_render_headerrow import (
    ExecuteQueryQueriesV1DataPostRenderHEADERROW,
)

# Use enum by value
my_execute_query_queries_v1_data_post_render_headerrow = (
    ExecuteQueryQueriesV1DataPostRenderHEADERROW.HEADER_ROW
)
print(my_execute_query_queries_v1_data_post_render_headerrow)  # Output: 'HEADER_ROW'

# Or by string value
my_execute_query_queries_v1_data_post_render_headerrow = (
    ExecuteQueryQueriesV1DataPostRenderHEADERROW("HEADER_ROW")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


