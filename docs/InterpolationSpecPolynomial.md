# InterpolationSpecPolynomial

Interpolate with a polynomial of the lowest possible degree passing trough the data points.

**Source:** `waylay.services.queries.models.interpolation_spec_polynomial`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**POLYNOMIAL** | `'polynomial'` |

## Example

```python
from waylay.services.queries.models.interpolation_spec_polynomial import (
    InterpolationSpecPolynomial,
)

# Use enum by value
my_interpolation_spec_polynomial = InterpolationSpecPolynomial.POLYNOMIAL
print(my_interpolation_spec_polynomial)  # Output: 'polynomial'

# Or by string value
my_interpolation_spec_polynomial = InterpolationSpecPolynomial("polynomial")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


