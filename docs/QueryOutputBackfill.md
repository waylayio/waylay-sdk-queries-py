# QueryOutputBackfill

Same as pad, but using the last observed value. This method also extrapolates

**Source:** `waylay.services.queries.models.query_output_backfill`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BACKFILL** | `'backfill'` |

## Example

```python
from waylay.services.queries.models.query_output_backfill import QueryOutputBackfill

# Use enum by value
my_query_output_backfill = QueryOutputBackfill.BACKFILL
print(my_query_output_backfill)  # Output: 'backfill'

# Or by string value
my_query_output_backfill = QueryOutputBackfill("backfill")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


