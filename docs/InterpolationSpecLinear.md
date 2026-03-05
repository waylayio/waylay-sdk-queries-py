# InterpolationSpecLinear

Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates

**Source:** `waylay.services.queries.models.interpolation_spec_linear`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**LINEAR** | `'linear'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_linear import (
    InterpolationSpecLinear,
)

# Use enum by value
my_interpolation_spec_linear = InterpolationSpecLinear.LINEAR
print(my_interpolation_spec_linear)  # Output: 'linear'

# Or by string value
my_interpolation_spec_linear = InterpolationSpecLinear("linear")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


