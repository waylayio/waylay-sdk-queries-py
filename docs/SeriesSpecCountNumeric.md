# SeriesSpecCountNumeric

Use the count of numeric observations in the sample interval.

**Source:** `waylay.services.queries.models.series_spec_count_numeric`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COUNT_MINUS_NUMERIC** | `'count-numeric'` |

## Example

```python
from waylay.services.queries.models.series_spec_count_numeric import (
    SeriesSpecCountNumeric,
)

# Use enum by value
my_series_spec_count_numeric = SeriesSpecCountNumeric.COUNT_MINUS_NUMERIC
print(my_series_spec_count_numeric)  # Output: 'count-numeric'

# Or by string value
my_series_spec_count_numeric = SeriesSpecCountNumeric("count-numeric")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


