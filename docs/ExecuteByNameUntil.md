# ExecuteByNameUntil


**Source:** `waylay.services.queries.models.execute_by_name_until`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
**datetime** | A date or date-time in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) format. When no timezone is specified, the UTC timezone is assumed (`+00:00`)
**int** | Absolute timestamp milliseconds in unix epoch since 1970-01-01.
**str** | Specifies a timestamp before _now_ as a period in [ISO8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) format.

## Example

```python
from waylay.services.queries.models.execute_by_name_until import ExecuteByNameUntil

# Use any of the accepted types (see table above)
my_execute_by_name_until: ExecuteByNameUntil = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


