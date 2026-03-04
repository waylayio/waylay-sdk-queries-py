# InterpolationSpecSpline

Interpolate with a spline function of a user-specified order.

**Source:** `waylay.services.queries.models.interpolation_spec_spline`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SPLINE** | `'spline'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_spline import (
    InterpolationSpecSpline,
)

# Use enum by value
my_interpolation_spec_spline = InterpolationSpecSpline.SPLINE
print(my_interpolation_spec_spline)  # Output: 'spline'

# Or by string value
my_interpolation_spec_spline = InterpolationSpecSpline("spline")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


