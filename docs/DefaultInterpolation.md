# DefaultInterpolation

Default Interpolation method for the series (if aggregated).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**InterpolationMethod**](InterpolationMethod.md) |  | 
**value** | **int** | Optional parameter value for the interpolation method (see method description). | [optional] 
**order** | **int** | Optional order parameter for the interpolation method (see method description). | [optional] 

## Example

```python
from waylay.services.queries.models.default_interpolation import DefaultInterpolation

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultInterpolation from a JSON string
default_interpolation_instance = DefaultInterpolation.from_json(json)
# print the JSON string representation of the object
print DefaultInterpolation.to_json()

# convert the object into a dict
default_interpolation_dict = default_interpolation_instance.to_dict()
# create an instance of DefaultInterpolation from a dict
default_interpolation_form_dict = default_interpolation.from_dict(default_interpolation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


