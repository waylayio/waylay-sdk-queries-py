# Interpolation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**InterpolationMethod**](InterpolationMethod.md) |  | 
**value** | [**InterpolationParameter**](InterpolationParameter.md) |  | [optional] 
**order** | **int** | Optional order parameter for the interpolation method (see method description). | [optional] 

## Example

```python
from waylay.services.queries.models.interpolation import Interpolation

# TODO update the JSON string below
json = "{}"
# create an instance of Interpolation from a JSON string
interpolation_instance = Interpolation.from_json(json)
# print the JSON string representation of the object
print Interpolation.to_json()

# convert the object into a dict
interpolation_dict = interpolation_instance.to_dict()
# create an instance of Interpolation from a dict
interpolation_form_dict = interpolation.from_dict(interpolation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


