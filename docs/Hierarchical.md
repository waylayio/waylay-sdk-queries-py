# Hierarchical

if true, use hierarchical objects to represent multiple row (or column) dimensions, otherwise multi-keys get concatenated with a dot-delimiter. If the value is a list, only these levels are kept as separate levels, while remaining levels get concatenated keys

**Source:** `waylay.services.queries.models.hierarchical`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
**bool** | -
**List[str]** | -

## Example

```python
from waylay.services.queries.models.hierarchical import Hierarchical

# Use any of the accepted types (see table above)
my_hierarchical: Hierarchical = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


