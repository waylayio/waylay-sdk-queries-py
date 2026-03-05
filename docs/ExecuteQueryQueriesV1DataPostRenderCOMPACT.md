# ExecuteQueryQueriesV1DataPostRenderCOMPACT

Render rows of timestamp and values. Show column headers.  ###### options - `iso_timestamp`: `False` - `header_array`: `row` - `roll_up`: `False` - `data_axis`: `column`

**Source:** `waylay.services.queries.models.execute_query_queries_v1_data_post_render_compact`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COMPACT** | `'COMPACT'` |

## Example

```python
from waylay.services.queries.models.execute_query_queries_v1_data_post_render_compact import (
    ExecuteQueryQueriesV1DataPostRenderCOMPACT,
)

# Use enum by value
my_execute_query_queries_v1_data_post_render_compact = (
    ExecuteQueryQueriesV1DataPostRenderCOMPACT.COMPACT
)
print(my_execute_query_queries_v1_data_post_render_compact)  # Output: 'COMPACT'

# Or by string value
my_execute_query_queries_v1_data_post_render_compact = (
    ExecuteQueryQueriesV1DataPostRenderCOMPACT("COMPACT")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


