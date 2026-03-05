# ExecuteByNameRenderHIERDICT

Render an hierarchical object for each observation. Shows an iso timestamp.  ###### options - `iso_timestamp`: `True` - `hierarchical`: `True` - `show_levels`: `True` - `roll_up`: `True`

**Source:** `waylay.services.queries.models.execute_by_name_render_hierdict`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**HIER_DICT** | `'HIER_DICT'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_render_hierdict import (
    ExecuteByNameRenderHIERDICT,
)

# Use enum by value
my_execute_by_name_render_hierdict = ExecuteByNameRenderHIERDICT.HIER_DICT
print(my_execute_by_name_render_hierdict)  # Output: 'HIER_DICT'

# Or by string value
my_execute_by_name_render_hierdict = ExecuteByNameRenderHIERDICT("HIER_DICT")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


