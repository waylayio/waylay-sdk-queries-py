# QueryOutputFirst

Use the first value (in time) to represent all data for the sample interval.

**Source:** `waylay.services.queries.models.query_output_first`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FIRST** | `'first'` |

## Example

```python
from waylay.services.queries.models.query_output_first import QueryOutputFirst

# Use enum by value
my_query_output_first = QueryOutputFirst.FIRST
print(my_query_output_first)  # Output: 'first'

# Or by string value
my_query_output_first = QueryOutputFirst("first")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


