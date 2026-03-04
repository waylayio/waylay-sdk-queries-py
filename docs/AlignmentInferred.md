# AlignmentInferred

When `inferred` is specified, the frequency of aggregation will be inferred from the main/first time series. This can be used to regularize the time series

**Source:** `waylay.services.queries.models.alignment_inferred`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**INFERRED** | `'inferred'` |

## Example

```python
from waylay.services.queries.models.alignment_inferred import AlignmentInferred

# Use enum by value
my_alignment_inferred = AlignmentInferred.INFERRED
print(my_alignment_inferred)  # Output: 'inferred'

# Or by string value
my_alignment_inferred = AlignmentInferred("inferred")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


