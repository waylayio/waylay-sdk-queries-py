# AlignmentBackward

Shift both boundaries (`align.at=grid`) or first boundary (`align.at=until`) backward to align with the grid.

**Source:** `waylay.services.queries.models.alignment_backward`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BACKWARD** | `'backward'` |

## Example

```python
from waylay.services.queries.models.alignment_backward import AlignmentBackward

# Use enum by value
my_alignment_backward = AlignmentBackward.BACKWARD
print(my_alignment_backward)  # Output: 'backward'

# Or by string value
my_alignment_backward = AlignmentBackward("backward")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


