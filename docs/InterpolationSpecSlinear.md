# InterpolationSpecSlinear

Interpolate with a spline function of order 1, which is a piecewise polynomial.

**Source:** `waylay.services.queries.models.interpolation_spec_slinear`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SLINEAR** | `'slinear'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_slinear import (
    InterpolationSpecSlinear,
)

# Use enum by value
my_interpolation_spec_slinear = InterpolationSpecSlinear.SLINEAR
print(my_interpolation_spec_slinear)  # Output: 'slinear'

# Or by string value
my_interpolation_spec_slinear = InterpolationSpecSlinear("slinear")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


