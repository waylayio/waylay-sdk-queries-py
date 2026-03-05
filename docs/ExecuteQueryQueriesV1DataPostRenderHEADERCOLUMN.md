# ExecuteQueryQueriesV1DataPostRenderHEADERCOLUMN

Renders row index in `rows`, and each series as a values array.  The series are prefixed by their series attributes.The `rows` index is prefixed by the labels for these attributes.  ###### options - `iso_timestamp`: `True` - `header_array`: `column` - `roll_up`: `False` - `data_axis`: `row`

**Source:** `waylay.services.queries.models.execute_query_queries_v1_data_post_render_headercolumn`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**HEADER_COLUMN** | `'HEADER_COLUMN'` |

## Example

```python
from waylay.services.queries.models.execute_query_queries_v1_data_post_render_headercolumn import (
    ExecuteQueryQueriesV1DataPostRenderHEADERCOLUMN,
)

# Use enum by value
my_execute_query_queries_v1_data_post_render_headercolumn = (
    ExecuteQueryQueriesV1DataPostRenderHEADERCOLUMN.HEADER_COLUMN
)
print(
    my_execute_query_queries_v1_data_post_render_headercolumn
)  # Output: 'HEADER_COLUMN'

# Or by string value
my_execute_query_queries_v1_data_post_render_headercolumn = (
    ExecuteQueryQueriesV1DataPostRenderHEADERCOLUMN("HEADER_COLUMN")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


