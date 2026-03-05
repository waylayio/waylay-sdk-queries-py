# SeriesSpecCountNonNumeric

Use the count of non-numeric observations in the sample interval.

**Source:** `waylay.services.queries.models.series_spec_count_non_numeric`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COUNT_MINUS_NON_MINUS_NUMERIC** | `'count-non-numeric'` |

## Example

```python
from waylay.services.queries.models.series_spec_count_non_numeric import (
    SeriesSpecCountNonNumeric,
)

# Use enum by value
my_series_spec_count_non_numeric = (
    SeriesSpecCountNonNumeric.COUNT_MINUS_NON_MINUS_NUMERIC
)
print(my_series_spec_count_non_numeric)  # Output: 'count-non-numeric'

# Or by string value
my_series_spec_count_non_numeric = SeriesSpecCountNonNumeric("count-non-numeric")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


