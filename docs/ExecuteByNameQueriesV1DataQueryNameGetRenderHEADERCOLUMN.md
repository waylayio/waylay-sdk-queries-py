# ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERCOLUMN

Renders row index in `rows`, and each series as a values array.  The series are prefixed by their series attributes.The `rows` index is prefixed by the labels for these attributes.  ###### options - `iso_timestamp`: `True` - `header_array`: `column` - `roll_up`: `False` - `data_axis`: `row`

**Source:** `waylay.services.queries.models.execute_by_name_queries_v1_data_query_name_get_render_headercolumn`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**HEADER_COLUMN** | `'HEADER_COLUMN'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_queries_v1_data_query_name_get_render_headercolumn import (
    ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERCOLUMN,
)

# Use enum by value
my_execute_by_name_queries_v1_data_query_name_get_render_headercolumn = (
    ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERCOLUMN.HEADER_COLUMN
)
print(
    my_execute_by_name_queries_v1_data_query_name_get_render_headercolumn
)  # Output: 'HEADER_COLUMN'

# Or by string value
my_execute_by_name_queries_v1_data_query_name_get_render_headercolumn = (
    ExecuteByNameQueriesV1DataQueryNameGetRenderHEADERCOLUMN("HEADER_COLUMN")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


