# RenderHIERDICT

Render an hierarchical object for each observation. Shows an iso timestamp.  ###### options - `iso_timestamp`: `True` - `hierarchical`: `True` - `show_levels`: `True` - `roll_up`: `True`

**Source:** `waylay.services.queries.models.render_hierdict`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**HIER_DICT** | `'HIER_DICT'` |

## Example

```python
from waylay.services.queries.models.render_hierdict import RenderHIERDICT

# Use enum by value
my_render_hierdict = RenderHIERDICT.HIER_DICT
print(my_render_hierdict)  # Output: 'HIER_DICT'

# Or by string value
my_render_hierdict = RenderHIERDICT("HIER_DICT")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


