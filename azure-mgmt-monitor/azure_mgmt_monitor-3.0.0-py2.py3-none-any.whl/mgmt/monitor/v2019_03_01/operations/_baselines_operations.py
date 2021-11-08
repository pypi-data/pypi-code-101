# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class BaselinesOperations(object):
    """BaselinesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~$(python-base-namespace).v2019_03_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        resource_uri,  # type: str
        metricnames=None,  # type: Optional[str]
        metricnamespace=None,  # type: Optional[str]
        timespan=None,  # type: Optional[str]
        interval=None,  # type: Optional[datetime.timedelta]
        aggregation=None,  # type: Optional[str]
        sensitivities=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        result_type=None,  # type: Optional[Union[str, "_models.ResultType"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.MetricBaselinesResponse"]
        """**Lists the metric baseline values for a resource**.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param metricnames: The names of the metrics (comma separated) to retrieve. Special case: If a
         metricname itself has a comma in it then use %2 to indicate it. Eg: 'Metric,Name1' should be
         **'Metric%2Name1'**.
        :type metricnames: str
        :param metricnamespace: Metric namespace to query metric definitions for.
        :type metricnamespace: str
        :param timespan: The timespan of the query. It is a string with the following format
         'startDateTime_ISO/endDateTime_ISO'.
        :type timespan: str
        :param interval: The interval (i.e. timegrain) of the query.
        :type interval: ~datetime.timedelta
        :param aggregation: The list of aggregation types (comma separated) to retrieve.
        :type aggregation: str
        :param sensitivities: The list of sensitivities (comma separated) to retrieve.
        :type sensitivities: str
        :param filter: The **$filter** is used to reduce the set of metric data returned. Example:
         Metric contains metadata A, B and C. - Return all time series of C where A = a1 and B = b1 or
         b2 **$filter=A eq 'a1' and B eq 'b1' or B eq 'b2' and C eq '*'** - Invalid variant: **$filter=A
         eq 'a1' and B eq 'b1' and C eq '*' or B = 'b2'** This is invalid because the logical or
         operator cannot separate two different metadata names. - Return all time series where A = a1, B
         = b1 and C = c1: **$filter=A eq 'a1' and B eq 'b1' and C eq 'c1'** - Return all time series
         where A = a1 **$filter=A eq 'a1' and B eq '\ *' and C eq '*\ '**. Special case: When dimension
         name or dimension value uses round brackets. Eg: When dimension name is **dim (test) 1**
         Instead of using $filter= "dim (test) 1 eq '\ *' " use **$filter= "dim %2528test%2529 1 eq '*\
         ' "\ ** When dimension name is **\ dim (test) 3\ ** and dimension value is **\ dim3 (test) val\
         ** Instead of using $filter= "dim (test) 3 eq 'dim3 (test) val' " use **\ $filter= "dim
         %2528test%2529 3 eq 'dim3 %2528test%2529 val' "**.
        :type filter: str
        :param result_type: Allows retrieving only metadata of the baseline. On data request all
         information is retrieved.
        :type result_type: str or ~$(python-base-namespace).v2019_03_01.models.ResultType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MetricBaselinesResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~$(python-base-namespace).v2019_03_01.models.MetricBaselinesResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MetricBaselinesResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-03-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceUri': self._serialize.url("resource_uri", resource_uri, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if metricnames is not None:
                    query_parameters['metricnames'] = self._serialize.query("metricnames", metricnames, 'str')
                if metricnamespace is not None:
                    query_parameters['metricnamespace'] = self._serialize.query("metricnamespace", metricnamespace, 'str')
                if timespan is not None:
                    query_parameters['timespan'] = self._serialize.query("timespan", timespan, 'str')
                if interval is not None:
                    query_parameters['interval'] = self._serialize.query("interval", interval, 'duration')
                if aggregation is not None:
                    query_parameters['aggregation'] = self._serialize.query("aggregation", aggregation, 'str')
                if sensitivities is not None:
                    query_parameters['sensitivities'] = self._serialize.query("sensitivities", sensitivities, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if result_type is not None:
                    query_parameters['resultType'] = self._serialize.query("result_type", result_type, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('MetricBaselinesResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/{resourceUri}/providers/Microsoft.Insights/metricBaselines'}  # type: ignore
