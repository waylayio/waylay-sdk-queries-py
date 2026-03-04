# ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian

Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.

**Source:** `waylay.services.queries.models.execute_by_name_queries_v1_data_query_name_get_aggregation_median`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MEDIAN** | `'median'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_queries_v1_data_query_name_get_aggregation_median import (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian,
)

# Use enum by value
my_execute_by_name_queries_v1_data_query_name_get_aggregation_median = (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian.MEDIAN
)
print(
    my_execute_by_name_queries_v1_data_query_name_get_aggregation_median
)  # Output: 'median'

# Or by string value
my_execute_by_name_queries_v1_data_query_name_get_aggregation_median = (
    ExecuteByNameQueriesV1DataQueryNameGetAggregationMedian("median")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


