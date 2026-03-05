# HALLinkRole

Supported link and embedding roles in HAL representations.

**Source:** `waylay.services.queries.models.hal_link_role`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SELF** | `'self'` |
**FIRST** | `'first'` |
**PREV** | `'prev'` |
**NEXT** | `'next'` |
**LAST** | `'last'` |
**EXECUTE** | `'execute'` |

## Example

```python
from waylay.services.queries.models.hal_link_role import HALLinkRole

# Use enum by value
my_hal_link_role = HALLinkRole.SELF
print(my_hal_link_role)  # Output: 'self'

# Or by string value
my_hal_link_role = HALLinkRole("self")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


