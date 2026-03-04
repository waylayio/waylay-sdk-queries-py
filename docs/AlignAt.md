# AlignAt

Possible values for `align.at`.  * 'grid' Align to a fixed grid (possibly using timezone information) * 'from' Align a the `from` boundary * 'until' Align a the `until` boundary * 'boundary' Align a the `from` boundary if specified,    otherwise the `until` boundary.  When not specified, 'grid' is used.

**Source:** `waylay.services.queries.models.align_at`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**GRID** | `'grid'` |
**BOUNDARY** | `'boundary'` |
**FROM** | `'from'` |
**UNTIL** | `'until'` |

## Example

```python
from waylay.services.queries.models.align_at import AlignAt

# Use enum by value
my_align_at = AlignAt.GRID
print(my_align_at)  # Output: 'grid'

# Or by string value
my_align_at = AlignAt("grid")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


