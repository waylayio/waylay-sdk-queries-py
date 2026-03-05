# SeriesSpecMean

Aggregate data by the mean value: The sum of values divided by number of observations.

**Source:** `waylay.services.queries.models.series_spec_mean`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**MEAN** | `'mean'` |

## Example

```python
from waylay.services.queries.models.series_spec_mean import SeriesSpecMean

# Use enum by value
my_series_spec_mean = SeriesSpecMean.MEAN
print(my_series_spec_mean)  # Output: 'mean'

# Or by string value
my_series_spec_mean = SeriesSpecMean("mean")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


