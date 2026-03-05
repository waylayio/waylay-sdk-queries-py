# Datum

A single metric value for a timeseries.  A null value indicates that no (aggregated/interpolated) value  exists for the corresponding timestamp.

**Source:** `waylay.services.queries.models.datum`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**float** | -
**str** | -
**bool** | -

## Example

```python
from waylay.services.queries.models.datum import Datum

# Use any of the accepted types (see table above)
my_datum: Datum = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


