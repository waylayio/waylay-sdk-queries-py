# ExecuteByNameAggregationMean

Aggregate data by the mean value: The sum of values divided by number of observations.

**Source:** `waylay.services.queries.models.execute_by_name_aggregation_mean`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MEAN** | `'mean'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_aggregation_mean import (
    ExecuteByNameAggregationMean,
)

# Use enum by value
my_execute_by_name_aggregation_mean = ExecuteByNameAggregationMean.MEAN
print(my_execute_by_name_aggregation_mean)  # Output: 'mean'

# Or by string value
my_execute_by_name_aggregation_mean = ExecuteByNameAggregationMean("mean")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


