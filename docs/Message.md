# Message

Individual (info/warning/error) message in a response.

**Source:** `waylay.services.queries.models.message`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | 
**level** | [**MessageLevel**](MessageLevel.md) |  | [optional] [default to MessageLevel.INFO]
**args** | **Dict[str, object]** |  | [optional] 


## Example

```python
from waylay.services.queries.models.message import Message

message = Message(code=..., message=..., level=..., args=...)

# Create from JSON
message = Message.from_json(
    '{ "code": ..., "message": ..., "level": ..., "args": ... }'
)

# Export to dictionary
message_dict = message.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


