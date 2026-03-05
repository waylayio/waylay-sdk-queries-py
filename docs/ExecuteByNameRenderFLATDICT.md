# ExecuteByNameRenderFLATDICT

Render an object for each observation. Uses flattened keys.  ###### options - `iso_timestamp`: `True` - `hierarchical`: `False` - `show_levels`: `True` - `roll_up`: `False`

**Source:** `waylay.services.queries.models.execute_by_name_render_flatdict`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FLAT_DICT** | `'FLAT_DICT'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_render_flatdict import (
    ExecuteByNameRenderFLATDICT,
)

# Use enum by value
my_execute_by_name_render_flatdict = ExecuteByNameRenderFLATDICT.FLAT_DICT
print(my_execute_by_name_render_flatdict)  # Output: 'FLAT_DICT'

# Or by string value
my_execute_by_name_render_flatdict = ExecuteByNameRenderFLATDICT("FLAT_DICT")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


