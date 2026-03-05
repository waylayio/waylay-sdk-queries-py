# QueryExecutionMessage

A message object that informs or warns about a query execution issue.

**Source:** `waylay.services.queries.models.query_execution_message`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A human readable message. | 
**level** | [**QueryExecutionMessageLevel**](QueryExecutionMessageLevel.md) |  | 
**timestamp** | **datetime** |  | 
**action** | **str** | The request action that caused this message. | 
**category** | **str** | The subsystem that issued this message. | 
**properties** | [**MessageArguments**](MessageArguments.md) |  | [optional] 
**exception** | [**CauseException**](CauseException.md) |  | [optional] 


## Example

```python
from waylay.services.queries.models.query_execution_message import QueryExecutionMessage

query_execution_message = QueryExecutionMessage(
    message=...,
    level=...,
    timestamp=...,
    action=...,
    category=...,
    properties=...,
    exception=...,
)

# Create from JSON
query_execution_message = QueryExecutionMessage.from_json(
    '{ "message": ..., "level": ..., "timestamp": ..., "action": ..., "category": ..., "properties": ..., "exception": ... }'
)

# Export to dictionary
query_execution_message_dict = query_execution_message.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


