# QueryInputAkima

Interpolate with a non-smoothing spline of order 2, called Akima interpolation.

**Source:** `waylay.services.queries.models.query_input_akima`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**AKIMA** | `'akima'` |

## Example

```python
from waylay.services.queries.models.query_input_akima import QueryInputAkima

# Use enum by value
my_query_input_akima = QueryInputAkima.AKIMA
print(my_query_input_akima)  # Output: 'akima'

# Or by string value
my_query_input_akima = QueryInputAkima("akima")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


