# RenderMode

Render mode configuration keys.

**Source:** `waylay.services.queries.models.render_mode`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**HEADER_ROW** | `'HEADER_ROW'` |
**COMPACT** | `'COMPACT'` |
**SERIES** | `'SERIES'` |
**HEADER_COLUMN** | `'HEADER_COLUMN'` |
**FLAT_DICT** | `'FLAT_DICT'` |
**HIER_DICT** | `'HIER_DICT'` |
**METRIC_FLAT_DICT** | `'METRIC_FLAT_DICT'` |
**UPLOAD** | `'UPLOAD'` |
**COMPACT_WS** | `'COMPACT_WS'` |
**CSV** | `'CSV'` |

## Example

```python
from waylay.services.queries.models.render_mode import RenderMode

# Use enum by value
my_render_mode = RenderMode.HEADER_ROW
print(my_render_mode)  # Output: 'HEADER_ROW'

# Or by string value
my_render_mode = RenderMode("HEADER_ROW")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


