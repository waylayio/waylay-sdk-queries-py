# SeriesSpecFromDerivatives

Interpolate with the derivative of order 1.

**Source:** `waylay.services.queries.models.series_spec_from_derivatives`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FROM_DERIVATIVES** | `'from_derivatives'` |

## Example

```python
from waylay.services.queries.models.series_spec_from_derivatives import (
    SeriesSpecFromDerivatives,
)

# Use enum by value
my_series_spec_from_derivatives = SeriesSpecFromDerivatives.FROM_DERIVATIVES
print(my_series_spec_from_derivatives)  # Output: 'from_derivatives'

# Or by string value
my_series_spec_from_derivatives = SeriesSpecFromDerivatives("from_derivatives")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


