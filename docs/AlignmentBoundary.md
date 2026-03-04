# AlignmentBoundary

Align a the `from` boundary if specified, otherwise use the `until` boundary (specfied or computed)

**Source:** `waylay.services.queries.models.alignment_boundary`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BOUNDARY** | `'boundary'` |

## Example

```python
from waylay.services.queries.models.alignment_boundary import AlignmentBoundary

# Use enum by value
my_alignment_boundary = AlignmentBoundary.BOUNDARY
print(my_alignment_boundary)  # Output: 'boundary'

# Or by string value
my_alignment_boundary = AlignmentBoundary("boundary")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


