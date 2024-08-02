# HALLink

A link target in a HAL response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Target url for this link. | 
**type** | **str** | Type of the resource referenced by this link. | [optional] 
**method** | [**HALLinkMethod**](HALLinkMethod.md) |  | [optional] 

## Example

```python
from waylay.services.queries.models.hal_link import HALLink

# TODO update the JSON string below
json = "{}"
# create an instance of HALLink from a JSON string
hal_link_instance = HALLink.from_json(json)
# print the JSON string representation of the object
print HALLink.to_json()

# convert the object into a dict
hal_link_dict = hal_link_instance.to_dict()
# create an instance of HALLink from a dict
hal_link_form_dict = hal_link.from_dict(hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

