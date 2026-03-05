# Window

The absolute size of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.

**Source:** `waylay.services.queries.models.window`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**str** | A period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.

## Example

```python
from waylay.services.queries.models.window import Window

# Use any of the accepted types (see table above)
my_window: Window = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


