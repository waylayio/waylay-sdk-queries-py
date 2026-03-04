# InterpolationSpecFromDerivatives

Interpolate with the derivative of order 1.

**Source:** `waylay.services.queries.models.interpolation_spec_from_derivatives`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FROM_DERIVATIVES** | `'from_derivatives'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_from_derivatives import (
    InterpolationSpecFromDerivatives,
)

# Use enum by value
my_interpolation_spec_from_derivatives = (
    InterpolationSpecFromDerivatives.FROM_DERIVATIVES
)
print(my_interpolation_spec_from_derivatives)  # Output: 'from_derivatives'

# Or by string value
my_interpolation_spec_from_derivatives = InterpolationSpecFromDerivatives(
    "from_derivatives"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


