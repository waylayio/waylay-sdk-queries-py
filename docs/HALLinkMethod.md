# HALLinkMethod

An http method that can be specified in a HAL link.

**Source:** `waylay.services.queries.models.hal_link_method`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**GET** | `'GET'` |
**POST** | `'POST'` |
**PUT** | `'PUT'` |
**DELETE** | `'DELETE'` |
**PATCH** | `'PATCH'` |

## Example

```python
from waylay.services.queries.models.hal_link_method import HALLinkMethod

# Use enum by value
my_hal_link_method = HALLinkMethod.GET
print(my_hal_link_method)  # Output: 'GET'

# Or by string value
my_hal_link_method = HALLinkMethod("GET")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


