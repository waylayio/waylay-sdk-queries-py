# ExecuteByNameInterpolationAkima

Interpolate with a non-smoothing spline of order 2, called Akima interpolation.

**Source:** `waylay.services.queries.models.execute_by_name_interpolation_akima`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**AKIMA** | `'akima'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_interpolation_akima import (
    ExecuteByNameInterpolationAkima,
)

# Use enum by value
my_execute_by_name_interpolation_akima = ExecuteByNameInterpolationAkima.AKIMA
print(my_execute_by_name_interpolation_akima)  # Output: 'akima'

# Or by string value
my_execute_by_name_interpolation_akima = ExecuteByNameInterpolationAkima("akima")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


