# RenderCOMPACT

Render rows of timestamp and values. Show column headers.  ###### options - `iso_timestamp`: `False` - `header_array`: `row` - `roll_up`: `False` - `data_axis`: `column`

**Source:** `waylay.services.queries.models.render_compact`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COMPACT** | `'COMPACT'` |

## Example

```python
from waylay.services.queries.models.render_compact import RenderCOMPACT

# Use enum by value
my_render_compact = RenderCOMPACT.COMPACT
print(my_render_compact)  # Output: 'COMPACT'

# Or by string value
my_render_compact = RenderCOMPACT("COMPACT")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


