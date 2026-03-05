# MessageProperties

Additional message arguments.

**Source:** `waylay.services.queries.models.message_properties`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | [optional] 
**metric** | **str** |  | [optional] 


## Example

```python
from waylay.services.queries.models.message_properties import MessageProperties

message_properties = MessageProperties(resource=..., metric=...)

# Create from JSON
message_properties = MessageProperties.from_json('{ "resource": ..., "metric": ... }')

# Export to dictionary
message_properties_dict = message_properties.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


