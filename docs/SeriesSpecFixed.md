# SeriesSpecFixed

Interpolate with a fixed, user-specified value. This method also extrapolates.

**Source:** `waylay.services.queries.models.series_spec_fixed`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FIXED** | `'fixed'` |

## Example

```python
from waylay.services.queries.models.series_spec_fixed import SeriesSpecFixed

# Use enum by value
my_series_spec_fixed = SeriesSpecFixed.FIXED
print(my_series_spec_fixed)  # Output: 'fixed'

# Or by string value
my_series_spec_fixed = SeriesSpecFixed("fixed")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


