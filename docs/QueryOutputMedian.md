# QueryOutputMedian

Aggregate data by the median value: The n/2-th value when ordered, the average of the (n-1)/2-th and (n+1)/2-th value when n is uneven.

**Source:** `waylay.services.queries.models.query_output_median`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MEDIAN** | `'median'` |

## Example

```python
from waylay.services.queries.models.query_output_median import QueryOutputMedian

# Use enum by value
my_query_output_median = QueryOutputMedian.MEDIAN
print(my_query_output_median)  # Output: 'median'

# Or by string value
my_query_output_median = QueryOutputMedian("median")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


