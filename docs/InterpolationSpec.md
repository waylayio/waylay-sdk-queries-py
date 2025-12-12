# InterpolationSpec

Defines whether, and how to treat missing values.  This can occur in two circumstances when aggregating (setting a sample frequency): * missing values: if there are missing (or invalid) values stored for a given freq-interval, \"interpolation\" specifies how to compute these. * down-sampling: when the specified freq is smaller than the series’ actual frequency. \"interpolation\" specifies how to compute intermediate values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**InterpolationMethod**](InterpolationMethod.md) |  | 
**value** | [**InterpolationParameter**](InterpolationParameter.md) |  | [optional] 
**order** | **int** | Optional order parameter for the interpolation method (see method description). | [optional] 

## Example

```python
from waylay.services.queries.models.interpolation_spec import InterpolationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of InterpolationSpec from a JSON string
interpolation_spec_instance = InterpolationSpec.from_json(json)
# print the JSON string representation of the object
print InterpolationSpec.to_json()

# convert the object into a dict
interpolation_spec_dict = interpolation_spec_instance.to_dict()
# create an instance of InterpolationSpec from a dict
interpolation_spec_form_dict = interpolation_spec.from_dict(interpolation_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


