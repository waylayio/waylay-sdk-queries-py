# InterpolationSpecQuadratic

Interpolate with a spline function of order 2, which is a piecewise polynomial.

**Source:** `waylay.services.queries.models.interpolation_spec_quadratic`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**QUADRATIC** | `'quadratic'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_quadratic import (
    InterpolationSpecQuadratic,
)

# Use enum by value
my_interpolation_spec_quadratic = InterpolationSpecQuadratic.QUADRATIC
print(my_interpolation_spec_quadratic)  # Output: 'quadratic'

# Or by string value
my_interpolation_spec_quadratic = InterpolationSpecQuadratic("quadratic")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


