# Waylay Queries Service

Execute and store queries on the Waylay timeseries.

Protocol version: v1.

This Python package is automatically generated based on the 
Waylay Queries OpenAPI specification (API version: 0.6.8)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/queries.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-queries` sub-package contains the Queries api methods.
- The `waylay-sdk-queries-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-queries`.

## Requirements.
This package requires Python 3.10+.

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
# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-queries-types` is installed
from waylay.services.queries.models.execute_query_queries_v1_data_post_interpolation_parameter import (
    ExecuteQueryQueriesV1DataPostInterpolationParameter,
)
from waylay.services.queries.models.execute_query_queries_v1_data_post_render_parameter import (
    ExecuteQueryQueriesV1DataPostRenderParameter,
)
from waylay.services.queries.models.query_input import QueryInput
from waylay.services.queries.models.query_result import QueryResult

try:
    # Execute Query
    # calls `POST /queries/v1/data`
    api_response = await waylay_client.queries.execute.execute(
        # query parameters:
        query={
            "resource": "13efb488-75ac-4dac-828a-d49c5c2ebbfc",
            "metric": "temperature",
            "interpolation": "pad",
            "render": "HEADER_ROW",
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json=waylay.services.queries.QueryInput(),  # QueryInput |
        headers={
            "accept": "accept_example",
        },
    )
    print(f"Response: {api_response}")
except ApiError as e:
    print("Exception when calling queries.execute.execute: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/sdk/waylay-sdk/).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

SDK Path | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
**waylay_client.queries.execute** | [**execute_by_name**](docs/ExecuteApi.md#execute_by_name) | **GET** /queries/v1/data/{query_name} | Execute Named Query
**waylay_client.queries.execute** | [**execute**](docs/ExecuteApi.md#execute) | **POST** /queries/v1/data | Execute Query
 | | |
**waylay_client.queries.manage** | [**get**](docs/ManageApi.md#get) | **GET** /queries/v1/query/{query_name} | Get Query
**waylay_client.queries.manage** | [**list**](docs/ManageApi.md#list) | **GET** /queries/v1/query | List Queries
**waylay_client.queries.manage** | [**post**](docs/ManageApi.md#post) | **POST** /queries/v1/query | Post Query
**waylay_client.queries.manage** | [**remove**](docs/ManageApi.md#remove) | **DELETE** /queries/v1/query/{query_name} | Remove Query
**waylay_client.queries.manage** | [**update**](docs/ManageApi.md#update) | **PUT** /queries/v1/query/{query_name} | Update Query
 | | |
**waylay_client.queries.status** | [**get**](docs/StatusApi.md#get) | **GET** /queries/v1 | Get Version And Health


## Documentation For Models

 - [Aggregation](docs/Aggregation.md)
 - [Aggregation1](docs/Aggregation1.md)
 - [AggregationByResourceAndMetricValue](docs/AggregationByResourceAndMetricValue.md)
 - [AggregationByResourceAndMetricValue1](docs/AggregationByResourceAndMetricValue1.md)
 - [AggregationByResourceOrMetricValue](docs/AggregationByResourceOrMetricValue.md)
 - [AggregationByResourceOrMetricValue1](docs/AggregationByResourceOrMetricValue1.md)
 - [AggregationsInner](docs/AggregationsInner.md)
 - [AggregationsInner1](docs/AggregationsInner1.md)
 - [Aggregration](docs/Aggregration.md)
 - [AlignAt](docs/AlignAt.md)
 - [AlignShift](docs/AlignShift.md)
 - [Alignment](docs/Alignment.md)
 - [AlignmentAt](docs/AlignmentAt.md)
 - [AlignmentBackward](docs/AlignmentBackward.md)
 - [AlignmentBoundary](docs/AlignmentBoundary.md)
 - [AlignmentForward](docs/AlignmentForward.md)
 - [AlignmentFrom](docs/AlignmentFrom.md)
 - [AlignmentGrid](docs/AlignmentGrid.md)
 - [AlignmentGridInterval](docs/AlignmentGridInterval.md)
 - [AlignmentInferred](docs/AlignmentInferred.md)
 - [AlignmentShift](docs/AlignmentShift.md)
 - [AlignmentTimezone](docs/AlignmentTimezone.md)
 - [AlignmentUntil](docs/AlignmentUntil.md)
 - [AlignmentWrap](docs/AlignmentWrap.md)
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
 - [DefaultAggregation1](docs/DefaultAggregation1.md)
 - [DefaultInterpolation](docs/DefaultInterpolation.md)
 - [DefaultInterpolation1](docs/DefaultInterpolation1.md)
 - [DefaultInterpolation1AnyOf](docs/DefaultInterpolation1AnyOf.md)
 - [DefaultInterpolationAnyOf](docs/DefaultInterpolationAnyOf.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [EmbeddingsValue](docs/EmbeddingsValue.md)
 - [ExecuteByNameAggregation](docs/ExecuteByNameAggregation.md)
 - [ExecuteByNameAggregationCount](docs/ExecuteByNameAggregationCount.md)
 - [ExecuteByNameAggregationCountNonNumeric](docs/ExecuteByNameAggregationCountNonNumeric.md)
 - [ExecuteByNameAggregationCountNumeric](docs/ExecuteByNameAggregationCountNumeric.md)
 - [ExecuteByNameAggregationFirst](docs/ExecuteByNameAggregationFirst.md)
 - [ExecuteByNameAggregationLast](docs/ExecuteByNameAggregationLast.md)
 - [ExecuteByNameAggregationMax](docs/ExecuteByNameAggregationMax.md)
 - [ExecuteByNameAggregationMean](docs/ExecuteByNameAggregationMean.md)
 - [ExecuteByNameAggregationMedian](docs/ExecuteByNameAggregationMedian.md)
 - [ExecuteByNameAggregationMin](docs/ExecuteByNameAggregationMin.md)
 - [ExecuteByNameAggregationStd](docs/ExecuteByNameAggregationStd.md)
 - [ExecuteByNameAggregationSum](docs/ExecuteByNameAggregationSum.md)
 - [ExecuteByNameFreq](docs/ExecuteByNameFreq.md)
 - [ExecuteByNameFreqInferred](docs/ExecuteByNameFreqInferred.md)
 - [ExecuteByNameFrom](docs/ExecuteByNameFrom.md)
 - [ExecuteByNameInterpolationAkima](docs/ExecuteByNameInterpolationAkima.md)
 - [ExecuteByNameInterpolationBackfill](docs/ExecuteByNameInterpolationBackfill.md)
 - [ExecuteByNameInterpolationCubic](docs/ExecuteByNameInterpolationCubic.md)
 - [ExecuteByNameInterpolationFixed](docs/ExecuteByNameInterpolationFixed.md)
 - [ExecuteByNameInterpolationFromDerivatives](docs/ExecuteByNameInterpolationFromDerivatives.md)
 - [ExecuteByNameInterpolationLinear](docs/ExecuteByNameInterpolationLinear.md)
 - [ExecuteByNameInterpolationNearest](docs/ExecuteByNameInterpolationNearest.md)
 - [ExecuteByNameInterpolationPad](docs/ExecuteByNameInterpolationPad.md)
 - [ExecuteByNameInterpolationPchip](docs/ExecuteByNameInterpolationPchip.md)
 - [ExecuteByNameInterpolationPolynomial](docs/ExecuteByNameInterpolationPolynomial.md)
 - [ExecuteByNameInterpolationQuadratic](docs/ExecuteByNameInterpolationQuadratic.md)
 - [ExecuteByNameInterpolationSlinear](docs/ExecuteByNameInterpolationSlinear.md)
 - [ExecuteByNameInterpolationSpline](docs/ExecuteByNameInterpolationSpline.md)
 - [ExecuteByNameInterpolationZero](docs/ExecuteByNameInterpolationZero.md)
 - [ExecuteByNameRenderCOMPACT](docs/ExecuteByNameRenderCOMPACT.md)
 - [ExecuteByNameRenderCOMPACTWS](docs/ExecuteByNameRenderCOMPACTWS.md)
 - [ExecuteByNameRenderCSV](docs/ExecuteByNameRenderCSV.md)
 - [ExecuteByNameRenderFLATDICT](docs/ExecuteByNameRenderFLATDICT.md)
 - [ExecuteByNameRenderHEADERCOLUMN](docs/ExecuteByNameRenderHEADERCOLUMN.md)
 - [ExecuteByNameRenderHEADERROW](docs/ExecuteByNameRenderHEADERROW.md)
 - [ExecuteByNameRenderHIERDICT](docs/ExecuteByNameRenderHIERDICT.md)
 - [ExecuteByNameRenderMETRICFLATDICT](docs/ExecuteByNameRenderMETRICFLATDICT.md)
 - [ExecuteByNameRenderSERIES](docs/ExecuteByNameRenderSERIES.md)
 - [ExecuteByNameRenderUPLOAD](docs/ExecuteByNameRenderUPLOAD.md)
 - [ExecuteByNameUntil](docs/ExecuteByNameUntil.md)
 - [ExecuteByNameWindow](docs/ExecuteByNameWindow.md)
 - [ExecuteQueryQueriesV1DataPostAggregation](docs/ExecuteQueryQueriesV1DataPostAggregation.md)
 - [ExecuteQueryQueriesV1DataPostAggregationCount](docs/ExecuteQueryQueriesV1DataPostAggregationCount.md)
 - [ExecuteQueryQueriesV1DataPostAggregationCountNonNumeric](docs/ExecuteQueryQueriesV1DataPostAggregationCountNonNumeric.md)
 - [ExecuteQueryQueriesV1DataPostAggregationCountNumeric](docs/ExecuteQueryQueriesV1DataPostAggregationCountNumeric.md)
 - [ExecuteQueryQueriesV1DataPostAggregationFirst](docs/ExecuteQueryQueriesV1DataPostAggregationFirst.md)
 - [ExecuteQueryQueriesV1DataPostAggregationLast](docs/ExecuteQueryQueriesV1DataPostAggregationLast.md)
 - [ExecuteQueryQueriesV1DataPostAggregationMax](docs/ExecuteQueryQueriesV1DataPostAggregationMax.md)
 - [ExecuteQueryQueriesV1DataPostAggregationMean](docs/ExecuteQueryQueriesV1DataPostAggregationMean.md)
 - [ExecuteQueryQueriesV1DataPostAggregationMedian](docs/ExecuteQueryQueriesV1DataPostAggregationMedian.md)
 - [ExecuteQueryQueriesV1DataPostAggregationMin](docs/ExecuteQueryQueriesV1DataPostAggregationMin.md)
 - [ExecuteQueryQueriesV1DataPostAggregationStd](docs/ExecuteQueryQueriesV1DataPostAggregationStd.md)
 - [ExecuteQueryQueriesV1DataPostAggregationSum](docs/ExecuteQueryQueriesV1DataPostAggregationSum.md)
 - [ExecuteQueryQueriesV1DataPostFreq](docs/ExecuteQueryQueriesV1DataPostFreq.md)
 - [ExecuteQueryQueriesV1DataPostFreqInferred](docs/ExecuteQueryQueriesV1DataPostFreqInferred.md)
 - [ExecuteQueryQueriesV1DataPostFrom](docs/ExecuteQueryQueriesV1DataPostFrom.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationAkima](docs/ExecuteQueryQueriesV1DataPostInterpolationAkima.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationBackfill](docs/ExecuteQueryQueriesV1DataPostInterpolationBackfill.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationCubic](docs/ExecuteQueryQueriesV1DataPostInterpolationCubic.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationFixed](docs/ExecuteQueryQueriesV1DataPostInterpolationFixed.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationFromDerivatives](docs/ExecuteQueryQueriesV1DataPostInterpolationFromDerivatives.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationLinear](docs/ExecuteQueryQueriesV1DataPostInterpolationLinear.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationNearest](docs/ExecuteQueryQueriesV1DataPostInterpolationNearest.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationPad](docs/ExecuteQueryQueriesV1DataPostInterpolationPad.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationParameter](docs/ExecuteQueryQueriesV1DataPostInterpolationParameter.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationPchip](docs/ExecuteQueryQueriesV1DataPostInterpolationPchip.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationPolynomial](docs/ExecuteQueryQueriesV1DataPostInterpolationPolynomial.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationQuadratic](docs/ExecuteQueryQueriesV1DataPostInterpolationQuadratic.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationSlinear](docs/ExecuteQueryQueriesV1DataPostInterpolationSlinear.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationSpline](docs/ExecuteQueryQueriesV1DataPostInterpolationSpline.md)
 - [ExecuteQueryQueriesV1DataPostInterpolationZero](docs/ExecuteQueryQueriesV1DataPostInterpolationZero.md)
 - [ExecuteQueryQueriesV1DataPostRenderCOMPACT](docs/ExecuteQueryQueriesV1DataPostRenderCOMPACT.md)
 - [ExecuteQueryQueriesV1DataPostRenderCOMPACTWS](docs/ExecuteQueryQueriesV1DataPostRenderCOMPACTWS.md)
 - [ExecuteQueryQueriesV1DataPostRenderCSV](docs/ExecuteQueryQueriesV1DataPostRenderCSV.md)
 - [ExecuteQueryQueriesV1DataPostRenderFLATDICT](docs/ExecuteQueryQueriesV1DataPostRenderFLATDICT.md)
 - [ExecuteQueryQueriesV1DataPostRenderHEADERCOLUMN](docs/ExecuteQueryQueriesV1DataPostRenderHEADERCOLUMN.md)
 - [ExecuteQueryQueriesV1DataPostRenderHEADERROW](docs/ExecuteQueryQueriesV1DataPostRenderHEADERROW.md)
 - [ExecuteQueryQueriesV1DataPostRenderHIERDICT](docs/ExecuteQueryQueriesV1DataPostRenderHIERDICT.md)
 - [ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT](docs/ExecuteQueryQueriesV1DataPostRenderMETRICFLATDICT.md)
 - [ExecuteQueryQueriesV1DataPostRenderParameter](docs/ExecuteQueryQueriesV1DataPostRenderParameter.md)
 - [ExecuteQueryQueriesV1DataPostRenderSERIES](docs/ExecuteQueryQueriesV1DataPostRenderSERIES.md)
 - [ExecuteQueryQueriesV1DataPostRenderUPLOAD](docs/ExecuteQueryQueriesV1DataPostRenderUPLOAD.md)
 - [ExecuteQueryQueriesV1DataPostUntil](docs/ExecuteQueryQueriesV1DataPostUntil.md)
 - [ExecuteQueryQueriesV1DataPostWindow](docs/ExecuteQueryQueriesV1DataPostWindow.md)
 - [GroupingInterval](docs/GroupingInterval.md)
 - [GroupingInterval1](docs/GroupingInterval1.md)
 - [HALLink](docs/HALLink.md)
 - [HALLinkMethod](docs/HALLinkMethod.md)
 - [HALLinkRole](docs/HALLinkRole.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HeaderArrayOption](docs/HeaderArrayOption.md)
 - [Hierarchical](docs/Hierarchical.md)
 - [InterpolationMethod](docs/InterpolationMethod.md)
 - [InterpolationMethod1](docs/InterpolationMethod1.md)
 - [InterpolationMethod2](docs/InterpolationMethod2.md)
 - [InterpolationMethod3](docs/InterpolationMethod3.md)
 - [InterpolationParameter](docs/InterpolationParameter.md)
 - [InterpolationSpec](docs/InterpolationSpec.md)
 - [InterpolationSpec1](docs/InterpolationSpec1.md)
 - [InterpolationSpec2](docs/InterpolationSpec2.md)
 - [InterpolationSpec3](docs/InterpolationSpec3.md)
 - [InterpolationSpecAkima](docs/InterpolationSpecAkima.md)
 - [InterpolationSpecBackfill](docs/InterpolationSpecBackfill.md)
 - [InterpolationSpecCubic](docs/InterpolationSpecCubic.md)
 - [InterpolationSpecFixed](docs/InterpolationSpecFixed.md)
 - [InterpolationSpecFromDerivatives](docs/InterpolationSpecFromDerivatives.md)
 - [InterpolationSpecLinear](docs/InterpolationSpecLinear.md)
 - [InterpolationSpecNearest](docs/InterpolationSpecNearest.md)
 - [InterpolationSpecPad](docs/InterpolationSpecPad.md)
 - [InterpolationSpecPchip](docs/InterpolationSpecPchip.md)
 - [InterpolationSpecPolynomial](docs/InterpolationSpecPolynomial.md)
 - [InterpolationSpecQuadratic](docs/InterpolationSpecQuadratic.md)
 - [InterpolationSpecSlinear](docs/InterpolationSpecSlinear.md)
 - [InterpolationSpecSpline](docs/InterpolationSpecSpline.md)
 - [InterpolationSpecZero](docs/InterpolationSpecZero.md)
 - [InterpolationSpecification](docs/InterpolationSpecification.md)
 - [InterpolationSpecificationAnyOf](docs/InterpolationSpecificationAnyOf.md)
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
 - [QueryInputAkima](docs/QueryInputAkima.md)
 - [QueryInputBackfill](docs/QueryInputBackfill.md)
 - [QueryInputCount](docs/QueryInputCount.md)
 - [QueryInputCountNonNumeric](docs/QueryInputCountNonNumeric.md)
 - [QueryInputCountNumeric](docs/QueryInputCountNumeric.md)
 - [QueryInputCubic](docs/QueryInputCubic.md)
 - [QueryInputFirst](docs/QueryInputFirst.md)
 - [QueryInputFixed](docs/QueryInputFixed.md)
 - [QueryInputFromDerivatives](docs/QueryInputFromDerivatives.md)
 - [QueryInputInferred](docs/QueryInputInferred.md)
 - [QueryInputLast](docs/QueryInputLast.md)
 - [QueryInputLinear](docs/QueryInputLinear.md)
 - [QueryInputMax](docs/QueryInputMax.md)
 - [QueryInputMean](docs/QueryInputMean.md)
 - [QueryInputMedian](docs/QueryInputMedian.md)
 - [QueryInputMin](docs/QueryInputMin.md)
 - [QueryInputNearest](docs/QueryInputNearest.md)
 - [QueryInputPad](docs/QueryInputPad.md)
 - [QueryInputPchip](docs/QueryInputPchip.md)
 - [QueryInputPolynomial](docs/QueryInputPolynomial.md)
 - [QueryInputQuadratic](docs/QueryInputQuadratic.md)
 - [QueryInputSlinear](docs/QueryInputSlinear.md)
 - [QueryInputSpline](docs/QueryInputSpline.md)
 - [QueryInputStd](docs/QueryInputStd.md)
 - [QueryInputSum](docs/QueryInputSum.md)
 - [QueryInputZero](docs/QueryInputZero.md)
 - [QueryListHALLinks](docs/QueryListHALLinks.md)
 - [QueryListItem](docs/QueryListItem.md)
 - [QueryOutput](docs/QueryOutput.md)
 - [QueryOutputAkima](docs/QueryOutputAkima.md)
 - [QueryOutputBackfill](docs/QueryOutputBackfill.md)
 - [QueryOutputCount](docs/QueryOutputCount.md)
 - [QueryOutputCountNonNumeric](docs/QueryOutputCountNonNumeric.md)
 - [QueryOutputCountNumeric](docs/QueryOutputCountNumeric.md)
 - [QueryOutputCubic](docs/QueryOutputCubic.md)
 - [QueryOutputFirst](docs/QueryOutputFirst.md)
 - [QueryOutputFixed](docs/QueryOutputFixed.md)
 - [QueryOutputFromDerivatives](docs/QueryOutputFromDerivatives.md)
 - [QueryOutputInferred](docs/QueryOutputInferred.md)
 - [QueryOutputLast](docs/QueryOutputLast.md)
 - [QueryOutputLinear](docs/QueryOutputLinear.md)
 - [QueryOutputMax](docs/QueryOutputMax.md)
 - [QueryOutputMean](docs/QueryOutputMean.md)
 - [QueryOutputMedian](docs/QueryOutputMedian.md)
 - [QueryOutputMin](docs/QueryOutputMin.md)
 - [QueryOutputNearest](docs/QueryOutputNearest.md)
 - [QueryOutputPad](docs/QueryOutputPad.md)
 - [QueryOutputPchip](docs/QueryOutputPchip.md)
 - [QueryOutputPolynomial](docs/QueryOutputPolynomial.md)
 - [QueryOutputQuadratic](docs/QueryOutputQuadratic.md)
 - [QueryOutputSlinear](docs/QueryOutputSlinear.md)
 - [QueryOutputSpline](docs/QueryOutputSpline.md)
 - [QueryOutputStd](docs/QueryOutputStd.md)
 - [QueryOutputSum](docs/QueryOutputSum.md)
 - [QueryOutputZero](docs/QueryOutputZero.md)
 - [QueryResponse](docs/QueryResponse.md)
 - [QueryResult](docs/QueryResult.md)
 - [QueryUpdateInput](docs/QueryUpdateInput.md)
 - [Render](docs/Render.md)
 - [RenderCOMPACT](docs/RenderCOMPACT.md)
 - [RenderCOMPACTWS](docs/RenderCOMPACTWS.md)
 - [RenderCSV](docs/RenderCSV.md)
 - [RenderFLATDICT](docs/RenderFLATDICT.md)
 - [RenderHEADERCOLUMN](docs/RenderHEADERCOLUMN.md)
 - [RenderHEADERROW](docs/RenderHEADERROW.md)
 - [RenderHIERDICT](docs/RenderHIERDICT.md)
 - [RenderMETRICFLATDICT](docs/RenderMETRICFLATDICT.md)
 - [RenderMode](docs/RenderMode.md)
 - [RenderSERIES](docs/RenderSERIES.md)
 - [RenderUPLOAD](docs/RenderUPLOAD.md)
 - [ResponseDataSet](docs/ResponseDataSet.md)
 - [RowDataSet](docs/RowDataSet.md)
 - [RowDataSetDataAxis](docs/RowDataSetDataAxis.md)
 - [RowHeader](docs/RowHeader.md)
 - [RowHeadersInner](docs/RowHeadersInner.md)
 - [SeriesDataSet](docs/SeriesDataSet.md)
 - [SeriesSpec](docs/SeriesSpec.md)
 - [SeriesSpecAkima](docs/SeriesSpecAkima.md)
 - [SeriesSpecBackfill](docs/SeriesSpecBackfill.md)
 - [SeriesSpecCount](docs/SeriesSpecCount.md)
 - [SeriesSpecCountNonNumeric](docs/SeriesSpecCountNonNumeric.md)
 - [SeriesSpecCountNumeric](docs/SeriesSpecCountNumeric.md)
 - [SeriesSpecCubic](docs/SeriesSpecCubic.md)
 - [SeriesSpecFirst](docs/SeriesSpecFirst.md)
 - [SeriesSpecFixed](docs/SeriesSpecFixed.md)
 - [SeriesSpecFromDerivatives](docs/SeriesSpecFromDerivatives.md)
 - [SeriesSpecLast](docs/SeriesSpecLast.md)
 - [SeriesSpecLinear](docs/SeriesSpecLinear.md)
 - [SeriesSpecMax](docs/SeriesSpecMax.md)
 - [SeriesSpecMean](docs/SeriesSpecMean.md)
 - [SeriesSpecMedian](docs/SeriesSpecMedian.md)
 - [SeriesSpecMin](docs/SeriesSpecMin.md)
 - [SeriesSpecNearest](docs/SeriesSpecNearest.md)
 - [SeriesSpecPad](docs/SeriesSpecPad.md)
 - [SeriesSpecPchip](docs/SeriesSpecPchip.md)
 - [SeriesSpecPolynomial](docs/SeriesSpecPolynomial.md)
 - [SeriesSpecQuadratic](docs/SeriesSpecQuadratic.md)
 - [SeriesSpecSlinear](docs/SeriesSpecSlinear.md)
 - [SeriesSpecSpline](docs/SeriesSpecSpline.md)
 - [SeriesSpecStd](docs/SeriesSpecStd.md)
 - [SeriesSpecSum](docs/SeriesSpecSum.md)
 - [SeriesSpecZero](docs/SeriesSpecZero.md)
 - [TimeWindowFrom](docs/TimeWindowFrom.md)
 - [TimeWindowUntil](docs/TimeWindowUntil.md)
 - [ValidationError](docs/ValidationError.md)
 - [Window](docs/Window.md)

