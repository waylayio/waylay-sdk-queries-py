# AlignShift

Possible values for `align.shift`.  * 'backward': keep the window size of the original interval specification,    shifting back. * 'forward': keep the window size of the original interval specification,    shifting forward. * 'wrap': enlarge the window size to include all of the original interval.  When not specified, 'backward' is used.

**Source:** `waylay.services.queries.models.align_shift`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BACKWARD** | `'backward'` |
**FORWARD** | `'forward'` |
**WRAP** | `'wrap'` |

## Example

```python
from waylay.services.queries.models.align_shift import AlignShift

# Use enum by value
my_align_shift = AlignShift.BACKWARD
print(my_align_shift)  # Output: 'backward'

# Or by string value
my_align_shift = AlignShift("backward")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


