# QueryOutputCountNumeric

Use the count of numeric observations in the sample interval.

**Source:** `waylay.services.queries.models.query_output_count_numeric`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COUNT_MINUS_NUMERIC** | `'count-numeric'` |

## Example

```python
from waylay.services.queries.models.query_output_count_numeric import (
    QueryOutputCountNumeric,
)

# Use enum by value
my_query_output_count_numeric = QueryOutputCountNumeric.COUNT_MINUS_NUMERIC
print(my_query_output_count_numeric)  # Output: 'count-numeric'

# Or by string value
my_query_output_count_numeric = QueryOutputCountNumeric("count-numeric")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


