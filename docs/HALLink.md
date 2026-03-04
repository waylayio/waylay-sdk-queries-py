# HALLink

A link target in a HAL response.

**Source:** `waylay.services.queries.models.hal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Target url for this link. | 
**type** | **str** | Type of the resource referenced by this link. | [optional] 
**method** | [**HALLinkMethod**](HALLinkMethod.md) |  | [optional] 


## Example

```python
from waylay.services.queries.models.hal_link import HALLink

hal_link = HALLink(href=..., type=..., method=...)

# Create from JSON
hal_link = HALLink.from_json('{ "href": ..., "type": ..., "method": ... }')

# Export to dictionary
hal_link_dict = hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


