# Waylay Queries Service

Execute and store queries on the Waylay timeseries.

Protocol version: v1.

This Python package is automatically generated based on the 
Waylay Queries OpenAPI specification (API version: 0.6.5)
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
    api_response = await waylay_client.queries.execute_queries.execute(
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
    print("The response of queries.execute_queries.execute:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling queries.execute_queries.execute: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/?id=software-development-kits).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExecuteQueriesApi* | [**execute_by_name**](docs/ExecuteQueriesApi.md#execute_by_name) | **GET** /queries/v1/data/{query_name} | Execute Named Query
*ExecuteQueriesApi* | [**execute**](docs/ExecuteQueriesApi.md#execute) | **POST** /queries/v1/data | Execute Query
*NamedQueriesApi* | [**create**](docs/NamedQueriesApi.md#create) | **POST** /queries/v1/query | Create Query
*NamedQueriesApi* | [**get**](docs/NamedQueriesApi.md#get) | **GET** /queries/v1/query/{query_name} | Get Query
*NamedQueriesApi* | [**list**](docs/NamedQueriesApi.md#list) | **GET** /queries/v1/query | List Queries
*NamedQueriesApi* | [**remove**](docs/NamedQueriesApi.md#remove) | **DELETE** /queries/v1/query/{query_name} | Remove Query
*NamedQueriesApi* | [**update**](docs/NamedQueriesApi.md#update) | **PUT** /queries/v1/query/{query_name} | Update Query
*StatusApi* | [**get**](docs/StatusApi.md#get) | **GET** /queries/v1 | Get Version And Health


## Documentation For Models

 - [Aggregation](docs/Aggregation.md)
 - [AggregationByResourceAndMetricValue](docs/AggregationByResourceAndMetricValue.md)
 - [AggregationByResourceOrMetricValue](docs/AggregationByResourceOrMetricValue.md)
 - [AggregationOverride](docs/AggregationOverride.md)
 - [AggregationOverrideOneOf](docs/AggregationOverrideOneOf.md)
 - [AggregationOverrideOneOf1](docs/AggregationOverrideOneOf1.md)
 - [AggregationOverrideOneOf2](docs/AggregationOverrideOneOf2.md)
 - [AggregationOverrideOneOf3](docs/AggregationOverrideOneOf3.md)
 - [AggregationOverrideOneOf4](docs/AggregationOverrideOneOf4.md)
 - [AggregationOverrideOneOf5](docs/AggregationOverrideOneOf5.md)
 - [AggregationOverrideOneOf6](docs/AggregationOverrideOneOf6.md)
 - [AggregationOverrideOneOf7](docs/AggregationOverrideOneOf7.md)
 - [AggregationOverrideOneOf8](docs/AggregationOverrideOneOf8.md)
 - [AggregationsInner](docs/AggregationsInner.md)
 - [Aggregration](docs/Aggregration.md)
 - [AlignAt](docs/AlignAt.md)
 - [AlignShift](docs/AlignShift.md)
 - [Alignment](docs/Alignment.md)
 - [AlignmentAt](docs/AlignmentAt.md)
 - [AlignmentGridInterval](docs/AlignmentGridInterval.md)
 - [AlignmentShift](docs/AlignmentShift.md)
 - [AlignmentTimezone](docs/AlignmentTimezone.md)
 - [CauseException](docs/CauseException.md)
 - [ColumnDataSet](docs/ColumnDataSet.md)
 - [ColumnDataSetDataAxis](docs/ColumnDataSetDataAxis.md)
 - [ColumnHeader](docs/ColumnHeader.md)
 - [ColumnHeadersInner](docs/ColumnHeadersInner.md)
 - [Data](docs/Data.md)
 - [DataAxisOption](docs/DataAxisOption.md)
 - [DataSetAttributes](docs/DataSetAttributes.md)
 - [DataSetWindow](docs/DataSetWindow.md)
 - [Datum](docs/Datum.md)
 - [DefaultAggregation](docs/DefaultAggregation.md)
 - [DefaultInterpolation](docs/DefaultInterpolation.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [EmbeddingsValue](docs/EmbeddingsValue.md)
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
 - [InterpolationAnyOf](docs/InterpolationAnyOf.md)
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
 - [InterpolationParameter](docs/InterpolationParameter.md)
 - [InterpolationSpec](docs/InterpolationSpec.md)
 - [LinksValue](docs/LinksValue.md)
 - [LocationInner](docs/LocationInner.md)
 - [Message](docs/Message.md)
 - [MessageArguments](docs/MessageArguments.md)
 - [MessageLevel](docs/MessageLevel.md)
 - [MessageProperties](docs/MessageProperties.md)
 - [ObjectData](docs/ObjectData.md)
 - [ObjectDataSet](docs/ObjectDataSet.md)
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
 - [Render1AnyOf](docs/Render1AnyOf.md)
 - [RenderMode](docs/RenderMode.md)
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

