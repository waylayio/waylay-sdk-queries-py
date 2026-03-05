# ExecuteByNameInterpolationQuadratic

Interpolate with a spline function of order 2, which is a piecewise polynomial.

**Source:** `waylay.services.queries.models.execute_by_name_interpolation_quadratic`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**QUADRATIC** | `'quadratic'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_interpolation_quadratic import (
    ExecuteByNameInterpolationQuadratic,
)

# Use enum by value
my_execute_by_name_interpolation_quadratic = (
    ExecuteByNameInterpolationQuadratic.QUADRATIC
)
print(my_execute_by_name_interpolation_quadratic)  # Output: 'quadratic'

# Or by string value
my_execute_by_name_interpolation_quadratic = ExecuteByNameInterpolationQuadratic(
    "quadratic"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


