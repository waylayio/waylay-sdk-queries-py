# RenderCOMPACTWS

Render rows of timestamp and values. Show column headers. Show the time window attributes.  ###### options - `iso_timestamp`: `False` - `header_array`: `row` - `roll_up`: `False` - `data_axis`: `column` - `include_window_spec`: `True`

**Source:** `waylay.services.queries.models.render_compactws`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COMPACT_WS** | `'COMPACT_WS'` |

## Example

```python
from waylay.services.queries.models.render_compactws import RenderCOMPACTWS

# Use enum by value
my_render_compactws = RenderCOMPACTWS.COMPACT_WS
print(my_render_compactws)  # Output: 'COMPACT_WS'

# Or by string value
my_render_compactws = RenderCOMPACTWS("COMPACT_WS")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


