# QueryResult

A json data response.  Uses the format as specified by the `render` options of the request (defaults to `COMPACT_WS`). '

**Source:** `waylay.services.queries.models.query_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResponseDataSet]**](ResponseDataSet.md) | A list of data sets, each with their own time axis. There will be one dataset for each &#x60;role&#x60; specified in the query (by default a single &#x60;input&#x60; role).  The data is represented according to the &#x60;render&#x60;  options in the query (default &#x60;COMPACT_WS&#x60;). | 
**query** | [**QueryOutput**](QueryOutput.md) |  | 
**messages** | [**List[QueryExecutionMessage]**](QueryExecutionMessage.md) |  | 


## Example

```python
from waylay.services.queries.models.query_result import QueryResult

query_result = QueryResult(data=..., query=..., messages=...)

# Create from JSON
query_result = QueryResult.from_json('{ "data": ..., "query": ..., "messages": ... }')

# Export to dictionary
query_result_dict = query_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


