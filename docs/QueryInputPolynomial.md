# QueryInputPolynomial

Interpolate with a polynomial of the lowest possible degree passing trough the data points.

**Source:** `waylay.services.queries.models.query_input_polynomial`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**POLYNOMIAL** | `'polynomial'` |

## Example

```python
from waylay.services.queries.models.query_input_polynomial import QueryInputPolynomial

# Use enum by value
my_query_input_polynomial = QueryInputPolynomial.POLYNOMIAL
print(my_query_input_polynomial)  # Output: 'polynomial'

# Or by string value
my_query_input_polynomial = QueryInputPolynomial("polynomial")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


