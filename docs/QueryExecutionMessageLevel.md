# QueryExecutionMessageLevel


**Source:** `waylay.services.queries.models.query_execution_message_level`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DEBUG** | `'debug'` |
**INFO** | `'info'` |
**WARNING** | `'warning'` |
**ERROR** | `'error'` |

## Example

```python
from waylay.services.queries.models.query_execution_message_level import (
    QueryExecutionMessageLevel,
)

# Use enum by value
my_query_execution_message_level = QueryExecutionMessageLevel.DEBUG
print(my_query_execution_message_level)  # Output: 'debug'

# Or by string value
my_query_execution_message_level = QueryExecutionMessageLevel("debug")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


