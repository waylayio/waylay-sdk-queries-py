# ExecuteByNameInterpolationBackfill

Same as pad, but using the last observed value. This method also extrapolates

**Source:** `waylay.services.queries.models.execute_by_name_interpolation_backfill`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BACKFILL** | `'backfill'` |

## Example

```python
from waylay.services.queries.models.execute_by_name_interpolation_backfill import (
    ExecuteByNameInterpolationBackfill,
)

# Use enum by value
my_execute_by_name_interpolation_backfill = ExecuteByNameInterpolationBackfill.BACKFILL
print(my_execute_by_name_interpolation_backfill)  # Output: 'backfill'

# Or by string value
my_execute_by_name_interpolation_backfill = ExecuteByNameInterpolationBackfill(
    "backfill"
)
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


