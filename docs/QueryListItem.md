# QueryListItem

Listing of a query definition item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**QueryHALLinks**](QueryHALLinks.md) |  | 
**attrs** | **Dict[str, object]** | System provided metadata for the query definition. | 
**name** | **str** | Name of the stored query definition. | 
**meta** | **Dict[str, object]** | User metadata for the query definition. | [optional] 

## Example

```python
from waylay.services.queries.models.query_list_item import QueryListItem

# TODO update the JSON string below
json = "{}"
# create an instance of QueryListItem from a JSON string
query_list_item_instance = QueryListItem.from_json(json)
# print the JSON string representation of the object
print QueryListItem.to_json()

# convert the object into a dict
query_list_item_dict = query_list_item_instance.to_dict()
# create an instance of QueryListItem from a dict
query_list_item_form_dict = query_list_item.from_dict(query_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


