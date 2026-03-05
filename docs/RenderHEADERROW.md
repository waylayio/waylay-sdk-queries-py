# RenderHEADERROW

Render rows of timestamp and values. Show column headers. Includes an iso timestamp.  ###### options - `iso_timestamp`: `True` - `header_array`: `row` - `roll_up`: `False` - `data_axis`: `column`

**Source:** `waylay.services.queries.models.render_headerrow`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**HEADER_ROW** | `'HEADER_ROW'` |

## Example

```python
from waylay.services.queries.models.render_headerrow import RenderHEADERROW

# Use enum by value
my_render_headerrow = RenderHEADERROW.HEADER_ROW
print(my_render_headerrow)  # Output: 'HEADER_ROW'

# Or by string value
my_render_headerrow = RenderHEADERROW("HEADER_ROW")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


