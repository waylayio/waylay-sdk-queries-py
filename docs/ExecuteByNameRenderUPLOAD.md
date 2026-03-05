# ExecuteByNameRenderUPLOAD

Render in an object format compatible with the `/data/v1/events` upload.  ###### options - `iso_timestamp`: `False` - `hierarchical`: `False` - `show_levels`: `False` - `roll_up`: `True`

**Source:** `waylay.services.queries.models.execute_by_name_render_upload`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UPLOAD** | `'UPLOAD'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_render_upload import (
    ExecuteByNameRenderUPLOAD,
)

# Use enum by value
my_execute_by_name_render_upload = ExecuteByNameRenderUPLOAD.UPLOAD
print(my_execute_by_name_render_upload)  # Output: 'UPLOAD'

# Or by string value
my_execute_by_name_render_upload = ExecuteByNameRenderUPLOAD("UPLOAD")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


