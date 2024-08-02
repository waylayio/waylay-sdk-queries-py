# QueryListHALLinks

HAL Links for a query entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HALLink**](HALLink.md) |  | 
**first** | [**HALLink**](HALLink.md) |  | [optional] 
**prev** | [**HALLink**](HALLink.md) |  | [optional] 
**next** | [**HALLink**](HALLink.md) |  | [optional] 
**last** | [**HALLink**](HALLink.md) |  | [optional] 

## Example

```python
from waylay.services.queries.models.query_list_hal_links import QueryListHALLinks

# TODO update the JSON string below
json = "{}"
# create an instance of QueryListHALLinks from a JSON string
query_list_hal_links_instance = QueryListHALLinks.from_json(json)
# print the JSON string representation of the object
print QueryListHALLinks.to_json()

# convert the object into a dict
query_list_hal_links_dict = query_list_hal_links_instance.to_dict()
# create an instance of QueryListHALLinks from a dict
query_list_hal_links_form_dict = query_list_hal_links.from_dict(query_list_hal_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


