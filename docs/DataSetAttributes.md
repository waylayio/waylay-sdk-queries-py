# DataSetAttributes

Data Set Attributes.  Data attributes that apply to all data in this set.

**Source:** `waylay.services.queries.models.data_set_attributes`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role of series specification that was used to compile this data set. | [optional] 


## Example

```python
from waylay.services.queries.models.data_set_attributes import DataSetAttributes

data_set_attributes = DataSetAttributes(role=...)

# Create from JSON
data_set_attributes = DataSetAttributes.from_json('{ "role": ... }')

# Export to dictionary
data_set_attributes_dict = data_set_attributes.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


