# SeriesSpecPolynomial

Interpolate with a polynomial of the lowest possible degree passing trough the data points.

**Source:** `waylay.services.queries.models.series_spec_polynomial`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**POLYNOMIAL** | `'polynomial'` |

## Example

```python
from waylay.services.queries.models.series_spec_polynomial import SeriesSpecPolynomial

# Use enum by value
my_series_spec_polynomial = SeriesSpecPolynomial.POLYNOMIAL
print(my_series_spec_polynomial)  # Output: 'polynomial'

# Or by string value
my_series_spec_polynomial = SeriesSpecPolynomial("polynomial")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


