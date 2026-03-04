# QueryOutputFromDerivatives

Interpolate with the derivative of order 1.

**Source:** `waylay.services.queries.models.query_output_from_derivatives`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FROM_DERIVATIVES** | `'from_derivatives'` |

## Example

```python
from waylay.services.queries.models.query_output_from_derivatives import (
    QueryOutputFromDerivatives,
)

# Use enum by value
my_query_output_from_derivatives = QueryOutputFromDerivatives.FROM_DERIVATIVES
print(my_query_output_from_derivatives)  # Output: 'from_derivatives'

# Or by string value
my_query_output_from_derivatives = QueryOutputFromDerivatives("from_derivatives")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


