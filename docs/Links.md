# Links


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Target url for this link. | 
**type** | **str** | Type of the resource referenced by this link. | [optional] 
**method** | [**HALLinkMethod**](HALLinkMethod.md) |  | [optional] 

## Example

```python
from waylay.services.queries.models.links import Links

# TODO update the JSON string below
json = "{}"
# create an instance of Links from a JSON string
links_instance = Links.from_json(json)
# print the JSON string representation of the object
print Links.to_json()

# convert the object into a dict
links_dict = links_instance.to_dict()
# create an instance of Links from a dict
links_form_dict = links.from_dict(links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


