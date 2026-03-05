# MessageLevel


**Source:** `waylay.services.queries.models.message_level`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DEBUG** | `'debug'` |
**INFO** | `'info'` |
**WARNING** | `'warning'` |
**ERROR** | `'error'` |
**FATAL** | `'fatal'` |

## Example

```python
from waylay.services.queries.models.message_level import MessageLevel

# Use enum by value
my_message_level = MessageLevel.DEBUG
print(my_message_level)  # Output: 'debug'

# Or by string value
my_message_level = MessageLevel("debug")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


