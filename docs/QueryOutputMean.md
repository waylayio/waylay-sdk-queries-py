# QueryOutputMean

Aggregate data by the mean value: The sum of values divided by number of observations.

**Source:** `waylay.services.queries.models.query_output_mean`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MEAN** | `'mean'` |

## Example

```python
from waylay.services.queries.models.query_output_mean import QueryOutputMean

# Use enum by value
my_query_output_mean = QueryOutputMean.MEAN
print(my_query_output_mean)  # Output: 'mean'

# Or by string value
my_query_output_mean = QueryOutputMean("mean")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


