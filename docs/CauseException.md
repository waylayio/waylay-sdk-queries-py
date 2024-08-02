# CauseException

Describes the exception that caused a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**message** | **str** |  | 
**stacktrace** | **List[str]** |  | 

## Example

```python
from waylay.services.queries.models.cause_exception import CauseException

# TODO update the JSON string below
json = "{}"
# create an instance of CauseException from a JSON string
cause_exception_instance = CauseException.from_json(json)
# print the JSON string representation of the object
print CauseException.to_json()

# convert the object into a dict
cause_exception_dict = cause_exception_instance.to_dict()
# create an instance of CauseException from a dict
cause_exception_form_dict = cause_exception.from_dict(cause_exception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


