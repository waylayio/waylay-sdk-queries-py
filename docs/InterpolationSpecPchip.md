# InterpolationSpecPchip

Interpolate with a piecewise cubic spline function.

**Source:** `waylay.services.queries.models.interpolation_spec_pchip`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**PCHIP** | `'pchip'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_pchip import (
    InterpolationSpecPchip,
)

# Use enum by value
my_interpolation_spec_pchip = InterpolationSpecPchip.PCHIP
print(my_interpolation_spec_pchip)  # Output: 'pchip'

# Or by string value
my_interpolation_spec_pchip = InterpolationSpecPchip("pchip")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


