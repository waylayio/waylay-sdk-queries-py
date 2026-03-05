# SeriesSpecBackfill

Same as pad, but using the last observed value. This method also extrapolates

**Source:** `waylay.services.queries.models.series_spec_backfill`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BACKFILL** | `'backfill'` |

## Example

```python
from waylay.services.queries.models.series_spec_backfill import SeriesSpecBackfill

# Use enum by value
my_series_spec_backfill = SeriesSpecBackfill.BACKFILL
print(my_series_spec_backfill)  # Output: 'backfill'

# Or by string value
my_series_spec_backfill = SeriesSpecBackfill("backfill")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


