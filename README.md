# Waylay Queries Service

Execute and store queries on the Waylay timeseries.

Protocol version: v1.

This Python package is automatically generated based on the 
Waylay Queries OpenAPI specification (API version: 0.5.0)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/queries.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-queries` sub-package contains the Queries api methods.
- The `waylay-sdk-queries-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-queries`.

## Requirements.
This package requires Python 3.9+.

## Installation

Normally this package is installed together with support for other services using the [waylay-sdk](https://pypi.org/project/waylay-sdk/) umbrella package:
* `pip install waylay-sdk` will install `waylay-sdk-queries` together with the SDK api packages for other services.
* `pip install waylay-sdk[types-queries]` will additionally install the types package `waylay-sdk-queries-types`.
* `pip install waylay-sdk[types]` will install the types packages for this and all other services.

Alternatively, you can install support for this _queries_ service only, installing or extending an existing [waylay-sdk-core](https://pypi.org/project/waylay-sdk-core/):

- `pip install waylay-sdk-queries` to only install api support for _queries_.
- `pip install waylay-sdk-queries[types]` to additionally install type support for _queries_.

## Usage

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.query_input import QueryInput
from waylay.services.queries.models.query_result import QueryResult
try:
    # Execute Query
    # calls `POST /queries/v1/data`
    api_response = await waylay_client.queries.execute.execute(
        # query parameters:
        query = {
            'resource': '13efb488-75ac-4dac-828a-d49c5c2ebbfc'
            'metric': 'temperature'
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.queries.QueryInput() # QueryInput | 
        headers = {
            'accept': 'accept_example',
        },
    )
    print("The response of queries.execute.execute:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.execute.execute: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/?id=software-development-kits).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExecuteApi* | [**execute_by_name**](docs/ExecuteApi.md#execute_by_name) | **GET** /queries/v1/data/{query_name} | Execute Named Query
*ExecuteApi* | [**execute**](docs/ExecuteApi.md#execute) | **POST** /queries/v1/data | Execute Query
*ManageApi* | [**create**](docs/ManageApi.md#create) | **POST** /queries/v1/query | Post Query
*ManageApi* | [**get**](docs/ManageApi.md#get) | **GET** /queries/v1/query/{query_name} | Get Query
*ManageApi* | [**list**](docs/ManageApi.md#list) | **GET** /queries/v1/query | List Queries
*ManageApi* | [**remove**](docs/ManageApi.md#remove) | **DELETE** /queries/v1/query/{query_name} | Remove Query
*ManageApi* | [**update**](docs/ManageApi.md#update) | **PUT** /queries/v1/query/{query_name} | Update Query
*StatusApi* | [**get**](docs/StatusApi.md#get) | **GET** /queries/v1 | Get Version And Health


## Documentation For Models

 - [AggregationByResourceAndMetric](docs/AggregationByResourceAndMetric.md)
 - [AggregationByResourceOrMetric](docs/AggregationByResourceOrMetric.md)
 - [AggregationMethod](docs/AggregationMethod.md)
 - [AggregationMethodOneOf](docs/AggregationMethodOneOf.md)
 - [AggregationMethodOneOf1](docs/AggregationMethodOneOf1.md)
 - [AggregationMethodOneOf2](docs/AggregationMethodOneOf2.md)
 - [AggregationMethodOneOf3](docs/AggregationMethodOneOf3.md)
 - [AggregationMethodOneOf4](docs/AggregationMethodOneOf4.md)
 - [AggregationMethodOneOf5](docs/AggregationMethodOneOf5.md)
 - [AggregationMethodOneOf6](docs/AggregationMethodOneOf6.md)
 - [AggregationMethodOneOf7](docs/AggregationMethodOneOf7.md)
 - [AggregationMethodOneOf8](docs/AggregationMethodOneOf8.md)
 - [AggregationsInner](docs/AggregationsInner.md)
 - [AlignAt](docs/AlignAt.md)
 - [AlignShift](docs/AlignShift.md)
 - [Alignment](docs/Alignment.md)
 - [AlignmentGridInterval](docs/AlignmentGridInterval.md)
 - [AlignmentTimezone](docs/AlignmentTimezone.md)
 - [CauseException](docs/CauseException.md)
 - [ColumnDataSet](docs/ColumnDataSet.md)
 - [ColumnDataSetDataAxis](docs/ColumnDataSetDataAxis.md)
 - [ColumnHeader](docs/ColumnHeader.md)
 - [ColumnHeadersInner](docs/ColumnHeadersInner.md)
 - [DataAxisOption](docs/DataAxisOption.md)
 - [DataSetAttributes](docs/DataSetAttributes.md)
 - [DataSetWindow](docs/DataSetWindow.md)
 - [Datum](docs/Datum.md)
 - [DefaultAggregation](docs/DefaultAggregation.md)
 - [DefaultInterpolation](docs/DefaultInterpolation.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [Embeddings](docs/Embeddings.md)
 - [FromOverride](docs/FromOverride.md)
 - [GroupingInterval](docs/GroupingInterval.md)
 - [GroupingIntervalOverride](docs/GroupingIntervalOverride.md)
 - [GroupingIntervalOverrideOneOf](docs/GroupingIntervalOverrideOneOf.md)
 - [HALLink](docs/HALLink.md)
 - [HALLinkMethod](docs/HALLinkMethod.md)
 - [HALLinkRole](docs/HALLinkRole.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HeaderArrayOption](docs/HeaderArrayOption.md)
 - [Hierarchical](docs/Hierarchical.md)
 - [Interpolation](docs/Interpolation.md)
 - [InterpolationMethod](docs/InterpolationMethod.md)
 - [InterpolationMethodOneOf](docs/InterpolationMethodOneOf.md)
 - [InterpolationMethodOneOf1](docs/InterpolationMethodOneOf1.md)
 - [InterpolationMethodOneOf10](docs/InterpolationMethodOneOf10.md)
 - [InterpolationMethodOneOf11](docs/InterpolationMethodOneOf11.md)
 - [InterpolationMethodOneOf12](docs/InterpolationMethodOneOf12.md)
 - [InterpolationMethodOneOf13](docs/InterpolationMethodOneOf13.md)
 - [InterpolationMethodOneOf2](docs/InterpolationMethodOneOf2.md)
 - [InterpolationMethodOneOf3](docs/InterpolationMethodOneOf3.md)
 - [InterpolationMethodOneOf4](docs/InterpolationMethodOneOf4.md)
 - [InterpolationMethodOneOf5](docs/InterpolationMethodOneOf5.md)
 - [InterpolationMethodOneOf6](docs/InterpolationMethodOneOf6.md)
 - [InterpolationMethodOneOf7](docs/InterpolationMethodOneOf7.md)
 - [InterpolationMethodOneOf8](docs/InterpolationMethodOneOf8.md)
 - [InterpolationMethodOneOf9](docs/InterpolationMethodOneOf9.md)
 - [InterpolationSpec](docs/InterpolationSpec.md)
 - [Links](docs/Links.md)
 - [LocationInner](docs/LocationInner.md)
 - [Message](docs/Message.md)
 - [MessageArguments](docs/MessageArguments.md)
 - [MessageLevel](docs/MessageLevel.md)
 - [MessageProperties](docs/MessageProperties.md)
 - [ObjectData](docs/ObjectData.md)
 - [ObjectDataSet](docs/ObjectDataSet.md)
 - [ObjectDataValue](docs/ObjectDataValue.md)
 - [QueriesListResponse](docs/QueriesListResponse.md)
 - [QueryDefinition](docs/QueryDefinition.md)
 - [QueryEntityInput](docs/QueryEntityInput.md)
 - [QueryExecutionMessage](docs/QueryExecutionMessage.md)
 - [QueryExecutionMessageLevel](docs/QueryExecutionMessageLevel.md)
 - [QueryHALLinks](docs/QueryHALLinks.md)
 - [QueryInput](docs/QueryInput.md)
 - [QueryListHALLinks](docs/QueryListHALLinks.md)
 - [QueryListItem](docs/QueryListItem.md)
 - [QueryOutput](docs/QueryOutput.md)
 - [QueryResponse](docs/QueryResponse.md)
 - [QueryResult](docs/QueryResult.md)
 - [QueryUpdateInput](docs/QueryUpdateInput.md)
 - [Render](docs/Render.md)
 - [Render1](docs/Render1.md)
 - [RenderMode](docs/RenderMode.md)
 - [RenderModeOneOf](docs/RenderModeOneOf.md)
 - [RenderModeOneOf1](docs/RenderModeOneOf1.md)
 - [RenderModeOneOf2](docs/RenderModeOneOf2.md)
 - [RenderModeOneOf3](docs/RenderModeOneOf3.md)
 - [RenderModeOneOf4](docs/RenderModeOneOf4.md)
 - [RenderModeOneOf5](docs/RenderModeOneOf5.md)
 - [RenderModeOneOf6](docs/RenderModeOneOf6.md)
 - [RenderModeOneOf7](docs/RenderModeOneOf7.md)
 - [RenderModeOneOf8](docs/RenderModeOneOf8.md)
 - [RenderModeOneOf9](docs/RenderModeOneOf9.md)
 - [ResponseDataSet](docs/ResponseDataSet.md)
 - [RowDataSet](docs/RowDataSet.md)
 - [RowDataSetDataAxis](docs/RowDataSetDataAxis.md)
 - [RowHeader](docs/RowHeader.md)
 - [RowHeadersInner](docs/RowHeadersInner.md)
 - [SeriesDataSet](docs/SeriesDataSet.md)
 - [SeriesSpec](docs/SeriesSpec.md)
 - [TimeWindowFrom](docs/TimeWindowFrom.md)
 - [TimeWindowUntil](docs/TimeWindowUntil.md)
 - [ValidationError](docs/ValidationError.md)
 - [Window](docs/Window.md)
 - [WindowOverride](docs/WindowOverride.md)

