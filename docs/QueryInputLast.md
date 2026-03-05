# QueryInputLast

Use the last value (in time) to represent all data for the sample interval.

**Source:** `waylay.services.queries.models.query_input_last`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**LAST** | `'last'` |

## Example

```python
from waylay.services.queries.models.query_input_last import QueryInputLast

# Use enum by value
my_query_input_last = QueryInputLast.LAST
print(my_query_input_last)  # Output: 'last'

# Or by string value
my_query_input_last = QueryInputLast("last")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


