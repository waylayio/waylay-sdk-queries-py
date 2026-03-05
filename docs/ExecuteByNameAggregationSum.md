# ExecuteByNameAggregationSum

The sum of all values summarizes the data for the sample interval.

**Source:** `waylay.services.queries.models.execute_by_name_aggregation_sum`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SUM** | `'sum'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_aggregation_sum import (
    ExecuteByNameAggregationSum,
)

# Use enum by value
my_execute_by_name_aggregation_sum = ExecuteByNameAggregationSum.SUM
print(my_execute_by_name_aggregation_sum)  # Output: 'sum'

# Or by string value
my_execute_by_name_aggregation_sum = ExecuteByNameAggregationSum("sum")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


