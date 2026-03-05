# ExecuteByNameRenderCOMPACTWS

Render rows of timestamp and values. Show column headers. Show the time window attributes.  ###### options - `iso_timestamp`: `False` - `header_array`: `row` - `roll_up`: `False` - `data_axis`: `column` - `include_window_spec`: `True`

**Source:** `waylay.services.queries.models.execute_by_name_render_compactws`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COMPACT_WS** | `'COMPACT_WS'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_render_compactws import (
    ExecuteByNameRenderCOMPACTWS,
)

# Use enum by value
my_execute_by_name_render_compactws = ExecuteByNameRenderCOMPACTWS.COMPACT_WS
print(my_execute_by_name_render_compactws)  # Output: 'COMPACT_WS'

# Or by string value
my_execute_by_name_render_compactws = ExecuteByNameRenderCOMPACTWS("COMPACT_WS")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


