# ExecuteQueryQueriesV1DataPostFreqInferred

When `inferred` is specified, the frequency of aggregation will be inferred from the main/first time series. This can be used to regularize the time series

**Source:** `waylay.services.queries.models.execute_query_queries_v1_data_post_freq_inferred`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**INFERRED** | `'inferred'` |

## Example

```python
from waylay.services.queries.models.execute_query_queries_v1_data_post_freq_inferred import (
    ExecuteQueryQueriesV1DataPostFreqInferred,
)

# Use enum by value
my_execute_query_queries_v1_data_post_freq_inferred = (
    ExecuteQueryQueriesV1DataPostFreqInferred.INFERRED
)
print(my_execute_query_queries_v1_data_post_freq_inferred)  # Output: 'inferred'

# Or by string value
my_execute_query_queries_v1_data_post_freq_inferred = (
    ExecuteQueryQueriesV1DataPostFreqInferred("inferred")
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


