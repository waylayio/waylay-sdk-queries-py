# ExecuteByNameAggregationCountNumeric

Use the count of numeric observations in the sample interval.

**Source:** `waylay.services.queries.models.execute_by_name_aggregation_count_numeric`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COUNT_MINUS_NUMERIC** | `'count-numeric'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_aggregation_count_numeric import (
    ExecuteByNameAggregationCountNumeric,
)

# Use enum by value
my_execute_by_name_aggregation_count_numeric = (
    ExecuteByNameAggregationCountNumeric.COUNT_MINUS_NUMERIC
)
print(my_execute_by_name_aggregation_count_numeric)  # Output: 'count-numeric'

# Or by string value
my_execute_by_name_aggregation_count_numeric = ExecuteByNameAggregationCountNumeric(
    "count-numeric"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


