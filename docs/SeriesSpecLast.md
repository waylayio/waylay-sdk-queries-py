# SeriesSpecLast

Use the last value (in time) to represent all data for the sample interval.

**Source:** `waylay.services.queries.models.series_spec_last`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**LAST** | `'last'` |

## Example

```python
from waylay.services.queries.models.series_spec_last import SeriesSpecLast

# Use enum by value
my_series_spec_last = SeriesSpecLast.LAST
print(my_series_spec_last)  # Output: 'last'

# Or by string value
my_series_spec_last = SeriesSpecLast("last")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


