# Alignment

Aggregation Alignment Options.  Specifies how the aggregation grid is aligned.

**Source:** `waylay.services.queries.models.alignment`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | [**AlignmentAt**](AlignmentAt.md) |  | [optional] 
**shift** | [**AlignmentShift**](AlignmentShift.md) |  | [optional] 
**freq** | [**AlignmentGridInterval**](AlignmentGridInterval.md) |  | [optional] 
**timezone** | [**AlignmentTimezone**](AlignmentTimezone.md) |  | [optional] 


## Example

```python
from waylay.services.queries.models.alignment import Alignment

alignment = Alignment(at=..., shift=..., freq=..., timezone=...)

# Create from JSON
alignment = Alignment.from_json(
    '{ "at": ..., "shift": ..., "freq": ..., "timezone": ... }'
)

# Export to dictionary
alignment_dict = alignment.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


