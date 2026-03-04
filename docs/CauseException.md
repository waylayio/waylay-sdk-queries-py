# CauseException

Describes the exception that caused a message.

**Source:** `waylay.services.queries.models.cause_exception`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**message** | **str** |  | 
**stacktrace** | **List[str]** |  | 


## Example

```python
from waylay.services.queries.models.cause_exception import CauseException

cause_exception = CauseException(type=..., message=..., stacktrace=...)

# Create from JSON
cause_exception = CauseException.from_json(
    '{ "type": ..., "message": ..., "stacktrace": ... }'
)

# Export to dictionary
cause_exception_dict = cause_exception.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


