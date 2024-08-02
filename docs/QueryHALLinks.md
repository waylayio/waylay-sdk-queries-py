# QueryHALLinks

HAL Links for a query entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HALLink**](HALLink.md) |  | 
**execute** | [**HALLink**](HALLink.md) |  | 

## Example

```python
from waylay.services.queries.models.query_hal_links import QueryHALLinks

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHALLinks from a JSON string
query_hal_links_instance = QueryHALLinks.from_json(json)
# print the JSON string representation of the object
print QueryHALLinks.to_json()

# convert the object into a dict
query_hal_links_dict = query_hal_links_instance.to_dict()
# create an instance of QueryHALLinks from a dict
query_hal_links_form_dict = query_hal_links.from_dict(query_hal_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


