# SeriesSpecAkima

Interpolate with a non-smoothing spline of order 2, called Akima interpolation.

**Source:** `waylay.services.queries.models.series_spec_akima`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**AKIMA** | `'akima'` |

## Example

```python
from waylay.services.queries.models.series_spec_akima import SeriesSpecAkima

# Use enum by value
my_series_spec_akima = SeriesSpecAkima.AKIMA
print(my_series_spec_akima)  # Output: 'akima'

# Or by string value
my_series_spec_akima = SeriesSpecAkima("akima")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


