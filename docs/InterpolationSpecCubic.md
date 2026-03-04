# InterpolationSpecCubic

Interpolate with a spline function of order 3, which is a piecewise polynomial.

**Source:** `waylay.services.queries.models.interpolation_spec_cubic`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**CUBIC** | `'cubic'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_cubic import (
    InterpolationSpecCubic,
)

# Use enum by value
my_interpolation_spec_cubic = InterpolationSpecCubic.CUBIC
print(my_interpolation_spec_cubic)  # Output: 'cubic'

# Or by string value
my_interpolation_spec_cubic = InterpolationSpecCubic("cubic")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


