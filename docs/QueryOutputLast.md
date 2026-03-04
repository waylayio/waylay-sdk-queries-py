# QueryOutputLast

Use the last value (in time) to represent all data for the sample interval.

**Source:** `waylay.services.queries.models.query_output_last`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**LAST** | `'last'` |

## Example

```python
from waylay.services.queries.models.query_output_last import QueryOutputLast

# Use enum by value
my_query_output_last = QueryOutputLast.LAST
print(my_query_output_last)  # Output: 'last'

# Or by string value
my_query_output_last = QueryOutputLast("last")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


