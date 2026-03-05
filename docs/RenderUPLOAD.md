# RenderUPLOAD

Render in an object format compatible with the `/data/v1/events` upload.  ###### options - `iso_timestamp`: `False` - `hierarchical`: `False` - `show_levels`: `False` - `roll_up`: `True`

**Source:** `waylay.services.queries.models.render_upload`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UPLOAD** | `'UPLOAD'` |

## Example

```python
from waylay.services.queries.models.render_upload import RenderUPLOAD

# Use enum by value
my_render_upload = RenderUPLOAD.UPLOAD
print(my_render_upload)  # Output: 'UPLOAD'

# Or by string value
my_render_upload = RenderUPLOAD("UPLOAD")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


