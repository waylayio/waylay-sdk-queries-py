# LinksValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Target url for this link. | 
**type** | **str** | Type of the resource referenced by this link. | [optional] 
**method** | [**HALLinkMethod**](HALLinkMethod.md) |  | [optional] 

## Example

```python
from waylay.services.queries.models.links_value import LinksValue

# TODO update the JSON string below
json = "{}"
# create an instance of LinksValue from a JSON string
links_value_instance = LinksValue.from_json(json)
# print the JSON string representation of the object
print LinksValue.to_json()

# convert the object into a dict
links_value_dict = links_value_instance.to_dict()
# create an instance of LinksValue from a dict
links_value_form_dict = links_value.from_dict(links_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


