# SeriesSpecPad

Interpolate with the value of the first observed point. This method also extrapolates.

**Source:** `waylay.services.queries.models.series_spec_pad`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**PAD** | `'pad'` |

## Example

```python
from waylay.services.queries.models.series_spec_pad import SeriesSpecPad

# Use enum by value
my_series_spec_pad = SeriesSpecPad.PAD
print(my_series_spec_pad)  # Output: 'pad'

# Or by string value
my_series_spec_pad = SeriesSpecPad("pad")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


