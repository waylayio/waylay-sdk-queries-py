# QueryExecutionMessage

A message object that informs or warns about a query execution issue.

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

# TODO update the JSON string below
json = "{}"
# create an instance of QueryExecutionMessage from a JSON string
query_execution_message_instance = QueryExecutionMessage.from_json(json)
# print the JSON string representation of the object
print QueryExecutionMessage.to_json()

# convert the object into a dict
query_execution_message_dict = query_execution_message_instance.to_dict()
# create an instance of QueryExecutionMessage from a dict
query_execution_message_form_dict = query_execution_message.from_dict(query_execution_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


