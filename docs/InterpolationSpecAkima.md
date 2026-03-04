# InterpolationSpecAkima

Interpolate with a non-smoothing spline of order 2, called Akima interpolation.

**Source:** `waylay.services.queries.models.interpolation_spec_akima`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**AKIMA** | `'akima'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_akima import (
    InterpolationSpecAkima,
)

# Use enum by value
my_interpolation_spec_akima = InterpolationSpecAkima.AKIMA
print(my_interpolation_spec_akima)  # Output: 'akima'

# Or by string value
my_interpolation_spec_akima = InterpolationSpecAkima("akima")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


