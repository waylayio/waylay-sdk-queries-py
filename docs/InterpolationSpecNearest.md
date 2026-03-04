# InterpolationSpecNearest

Use the value that is closest in time.

**Source:** `waylay.services.queries.models.interpolation_spec_nearest`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**NEAREST** | `'nearest'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_nearest import (
    InterpolationSpecNearest,
)

# Use enum by value
my_interpolation_spec_nearest = InterpolationSpecNearest.NEAREST
print(my_interpolation_spec_nearest)  # Output: 'nearest'

# Or by string value
my_interpolation_spec_nearest = InterpolationSpecNearest("nearest")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


