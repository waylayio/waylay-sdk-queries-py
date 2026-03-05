# ExecuteByNameAggregationFirst

Use the first value (in time) to represent all data for the sample interval.

**Source:** `waylay.services.queries.models.execute_by_name_aggregation_first`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FIRST** | `'first'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_aggregation_first import (
    ExecuteByNameAggregationFirst,
)

# Use enum by value
my_execute_by_name_aggregation_first = ExecuteByNameAggregationFirst.FIRST
print(my_execute_by_name_aggregation_first)  # Output: 'first'

# Or by string value
my_execute_by_name_aggregation_first = ExecuteByNameAggregationFirst("first")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


