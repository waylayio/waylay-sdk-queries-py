# RenderSERIES

Render timestamps and each series (column) as a values array. Show column headers.  ###### options - `iso_timestamp`: `False` - `header_array`: `row` - `data_axis`: `row` - `roll_up`: `True` - `include_window_spec`: `True`

**Source:** `waylay.services.queries.models.render_series`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SERIES** | `'SERIES'` |

## Example

```python
from waylay.services.queries.models.render_series import RenderSERIES

# Use enum by value
my_render_series = RenderSERIES.SERIES
print(my_render_series)  # Output: 'SERIES'

# Or by string value
my_render_series = RenderSERIES("SERIES")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


