# ExecuteByNameInterpolationFromDerivatives

Interpolate with the derivative of order 1.

**Source:** `waylay.services.queries.models.execute_by_name_interpolation_from_derivatives`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FROM_DERIVATIVES** | `'from_derivatives'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_interpolation_from_derivatives import (
    ExecuteByNameInterpolationFromDerivatives,
)

# Use enum by value
my_execute_by_name_interpolation_from_derivatives = (
    ExecuteByNameInterpolationFromDerivatives.FROM_DERIVATIVES
)
print(my_execute_by_name_interpolation_from_derivatives)  # Output: 'from_derivatives'

# Or by string value
my_execute_by_name_interpolation_from_derivatives = (
    ExecuteByNameInterpolationFromDerivatives("from_derivatives")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


