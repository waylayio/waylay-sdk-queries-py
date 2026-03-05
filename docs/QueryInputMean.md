# QueryInputMean

Aggregate data by the mean value: The sum of values divided by number of observations.

**Source:** `waylay.services.queries.models.query_input_mean`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MEAN** | `'mean'` |

## Example

```python
from waylay.services.queries.models.query_input_mean import QueryInputMean

# Use enum by value
my_query_input_mean = QueryInputMean.MEAN
print(my_query_input_mean)  # Output: 'mean'

# Or by string value
my_query_input_mean = QueryInputMean("mean")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


