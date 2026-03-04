# ObjectData

Result data for a timestamp in object format.

**Source:** `waylay.services.queries.models.object_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** | Unix epoch milliseconds timestamp. | 
**timestamp_iso** | **datetime** | ISO8601 rendering of the timestamp, present when &#x60;render.iso_timestamp&#x3D;true&#x60; | [optional] 
**role** | **str** | The role of series specification that was used to compile this data set. | [optional] 
**resource** | **str** | Series resource id, if applicable for all values. | [optional] 
**metric** | **str** | Series metric, if applicable for all values. | [optional] 
**aggregation** | **str** | Series aggregation, if applicable for all values. | [optional] 
**levels** | **List[str]** | Attribute level names used to key the values for this observation.  Levels that are flattened have a dot-separated key.  If all observations have the same attribute for a level, that level might be omitted. | [optional] 


## Example

```python
from waylay.services.queries.models.object_data import ObjectData

object_data = ObjectData(
    timestamp=...,
    timestamp_iso=...,
    role=...,
    resource=...,
    metric=...,
    aggregation=...,
    levels=...,
)

# Create from JSON
object_data = ObjectData.from_json(
    '{ "timestamp": ..., "timestamp_iso": ..., "role": ..., "resource": ..., "metric": ..., "aggregation": ..., "levels": ... }'
)

# Export to dictionary
object_data_dict = object_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


