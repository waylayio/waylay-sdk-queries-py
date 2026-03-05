# QueryInputBackfill

Same as pad, but using the last observed value. This method also extrapolates

**Source:** `waylay.services.queries.models.query_input_backfill`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BACKFILL** | `'backfill'` |

## Example

```python
from waylay.services.queries.models.query_input_backfill import QueryInputBackfill

# Use enum by value
my_query_input_backfill = QueryInputBackfill.BACKFILL
print(my_query_input_backfill)  # Output: 'backfill'

# Or by string value
my_query_input_backfill = QueryInputBackfill("backfill")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


