# QueryOutputLinear

Linearly go from the first observed value of the gap to the last observed oneThis method also extrapolates

**Source:** `waylay.services.queries.models.query_output_linear`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**LINEAR** | `'linear'` |

## Example

```python
from waylay.services.queries.models.query_output_linear import QueryOutputLinear

# Use enum by value
my_query_output_linear = QueryOutputLinear.LINEAR
print(my_query_output_linear)  # Output: 'linear'

# Or by string value
my_query_output_linear = QueryOutputLinear("linear")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


