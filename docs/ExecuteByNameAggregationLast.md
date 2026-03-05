# ExecuteByNameAggregationLast

Use the last value (in time) to represent all data for the sample interval.

**Source:** `waylay.services.queries.models.execute_by_name_aggregation_last`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**LAST** | `'last'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_aggregation_last import (
    ExecuteByNameAggregationLast,
)

# Use enum by value
my_execute_by_name_aggregation_last = ExecuteByNameAggregationLast.LAST
print(my_execute_by_name_aggregation_last)  # Output: 'last'

# Or by string value
my_execute_by_name_aggregation_last = ExecuteByNameAggregationLast("last")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


