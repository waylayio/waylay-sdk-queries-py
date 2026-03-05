# QueryInputMedian

Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.

**Source:** `waylay.services.queries.models.query_input_median`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MEDIAN** | `'median'` |

## Example

```python
from waylay.services.queries.models.query_input_median import QueryInputMedian

# Use enum by value
my_query_input_median = QueryInputMedian.MEDIAN
print(my_query_input_median)  # Output: 'median'

# Or by string value
my_query_input_median = QueryInputMedian("median")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


