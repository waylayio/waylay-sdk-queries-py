# QueryInputCountNumeric

Use the count of numeric observations in the sample interval.

**Source:** `waylay.services.queries.models.query_input_count_numeric`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COUNT_MINUS_NUMERIC** | `'count-numeric'` |

## Example

```python
from waylay.services.queries.models.query_input_count_numeric import (
    QueryInputCountNumeric,
)

# Use enum by value
my_query_input_count_numeric = QueryInputCountNumeric.COUNT_MINUS_NUMERIC
print(my_query_input_count_numeric)  # Output: 'count-numeric'

# Or by string value
my_query_input_count_numeric = QueryInputCountNumeric("count-numeric")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


