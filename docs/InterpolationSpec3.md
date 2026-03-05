# InterpolationSpec3

Defines whether, and how to treat missing values.  This can occur in two circumstances when aggregating (setting a sample frequency): * missing values: if there are missing (or invalid) values stored for a given freq-interval, \"interpolation\" specifies how to compute these. * down-sampling: when the specified freq is smaller than the series’ actual frequency. \"interpolation\" specifies how to compute intermediate values.

**Source:** `waylay.services.queries.models.interpolation_spec3`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**InterpolationMethod3**](InterpolationMethod3.md) |  | 
**value** | [**InterpolationParameter**](InterpolationParameter.md) |  | [optional] 
**order** | **int** | Optional order parameter for the interpolation method (see method description). | [optional] 


## Example

```python
from waylay.services.queries.models.interpolation_spec3 import InterpolationSpec3

interpolation_spec3 = InterpolationSpec3(method=..., value=..., order=...)

# Create from JSON
interpolation_spec3 = InterpolationSpec3.from_json(
    '{ "method": ..., "value": ..., "order": ... }'
)

# Export to dictionary
interpolation_spec3_dict = interpolation_spec3.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


