# ExecuteByNameInterpolationLinear

Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates

**Source:** `waylay.services.queries.models.execute_by_name_interpolation_linear`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**LINEAR** | `'linear'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_interpolation_linear import (
    ExecuteByNameInterpolationLinear,
)

# Use enum by value
my_execute_by_name_interpolation_linear = ExecuteByNameInterpolationLinear.LINEAR
print(my_execute_by_name_interpolation_linear)  # Output: 'linear'

# Or by string value
my_execute_by_name_interpolation_linear = ExecuteByNameInterpolationLinear("linear")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


