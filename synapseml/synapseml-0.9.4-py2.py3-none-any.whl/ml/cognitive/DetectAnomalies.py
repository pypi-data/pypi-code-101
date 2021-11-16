# Copyright (C) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in project root for information.


import sys
if sys.version >= '3':
    basestring = str

from pyspark import SparkContext, SQLContext
from pyspark.sql import DataFrame
from pyspark.ml.param.shared import *
from pyspark import keyword_only
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from synapse.ml.core.serialize.java_params_patch import *
from pyspark.ml.wrapper import JavaTransformer, JavaEstimator, JavaModel
from pyspark.ml.evaluation import JavaEvaluator
from pyspark.ml.common import inherit_doc
from synapse.ml.core.schema.Utils import *
from pyspark.ml.param import TypeConverters
from synapse.ml.core.schema.TypeConversionUtils import generateTypeConverter, complexTypeConverter


@inherit_doc
class DetectAnomalies(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        customInterval (object):  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     
        errorCol (object): column to hold http errors
        granularity (object):  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     
        handler (object): Which strategy to use when handling requests
        maxAnomalyRatio (object):  Optional argument, advanced model parameter, max anomaly ratio in a time series.     
        outputCol (object): The name of the output column
        period (object):  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     
        sensitivity (object):  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     
        series (object):  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (object): Url of the service
    """

    concurrency = Param(Params._dummy(), "concurrency", "max number of concurrent calls", typeConverter=TypeConverters.toInt)
    
    concurrentTimeout = Param(Params._dummy(), "concurrentTimeout", "max number seconds to wait on futures if concurrency >= 1", typeConverter=TypeConverters.toFloat)
    
    customInterval = Param(Params._dummy(), "customInterval", " Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     ")
    
    errorCol = Param(Params._dummy(), "errorCol", "column to hold http errors")
    
    granularity = Param(Params._dummy(), "granularity", " Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     ")
    
    handler = Param(Params._dummy(), "handler", "Which strategy to use when handling requests")
    
    maxAnomalyRatio = Param(Params._dummy(), "maxAnomalyRatio", " Optional argument, advanced model parameter, max anomaly ratio in a time series.     ")
    
    outputCol = Param(Params._dummy(), "outputCol", "The name of the output column")
    
    period = Param(Params._dummy(), "period", " Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     ")
    
    sensitivity = Param(Params._dummy(), "sensitivity", " Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     ")
    
    series = Param(Params._dummy(), "series", " Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     ")
    
    subscriptionKey = Param(Params._dummy(), "subscriptionKey", "the API key to use")
    
    timeout = Param(Params._dummy(), "timeout", "number of seconds to wait before closing the connection", typeConverter=TypeConverters.toFloat)
    
    url = Param(Params._dummy(), "url", "Url of the service")

    
    @keyword_only
    def __init__(
        self,
        java_obj=None,
        concurrency=1,
        concurrentTimeout=None,
        customInterval=None,
        customIntervalCol=None,
        errorCol="DetectAnomalies_1e3954add237_error",
        granularity=None,
        granularityCol=None,
        handler=None,
        maxAnomalyRatio=None,
        maxAnomalyRatioCol=None,
        outputCol="DetectAnomalies_1e3954add237_output",
        period=None,
        periodCol=None,
        sensitivity=None,
        sensitivityCol=None,
        series=None,
        seriesCol=None,
        subscriptionKey=None,
        subscriptionKeyCol=None,
        timeout=60.0,
        url=None
        ):
        super(DetectAnomalies, self).__init__()
        if java_obj is None:
            self._java_obj = self._new_java_obj("com.microsoft.azure.synapse.ml.cognitive.DetectAnomalies", self.uid)
        else:
            self._java_obj = java_obj
        self._setDefault(concurrency=1)
        self._setDefault(errorCol="DetectAnomalies_1e3954add237_error")
        self._setDefault(outputCol="DetectAnomalies_1e3954add237_output")
        self._setDefault(timeout=60.0)
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
    
        if java_obj is None:
            for k,v in kwargs.items():
                if v is not None:
                    getattr(self, "set" + k[0].upper() + k[1:])(v)

    @keyword_only
    def setParams(
        self,
        concurrency=1,
        concurrentTimeout=None,
        customInterval=None,
        customIntervalCol=None,
        errorCol="DetectAnomalies_1e3954add237_error",
        granularity=None,
        granularityCol=None,
        handler=None,
        maxAnomalyRatio=None,
        maxAnomalyRatioCol=None,
        outputCol="DetectAnomalies_1e3954add237_output",
        period=None,
        periodCol=None,
        sensitivity=None,
        sensitivityCol=None,
        series=None,
        seriesCol=None,
        subscriptionKey=None,
        subscriptionKeyCol=None,
        timeout=60.0,
        url=None
        ):
        """
        Set the (keyword only) parameters
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.azure.synapse.ml.cognitive.DetectAnomalies"

    @staticmethod
    def _from_java(java_stage):
        module_name=DetectAnomalies.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".DetectAnomalies"
        return from_java(java_stage, module_name)

    def setConcurrency(self, value):
        """
        Args:
            concurrency: max number of concurrent calls
        """
        self._set(concurrency=value)
        return self
    
    def setConcurrentTimeout(self, value):
        """
        Args:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
        self._set(concurrentTimeout=value)
        return self
    
    def setCustomInterval(self, value):
        """
        Args:
            customInterval:  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.org.apache.spark.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setCustomInterval(value)
        return self
    
    def setCustomIntervalCol(self, value):
        """
        Args:
            customInterval:  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     
        """
        self._java_obj = self._java_obj.setCustomIntervalCol(value)
        return self
    
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
        self._set(errorCol=value)
        return self
    
    def setGranularity(self, value):
        """
        Args:
            granularity:  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.org.apache.spark.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setGranularity(value)
        return self
    
    def setGranularityCol(self, value):
        """
        Args:
            granularity:  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     
        """
        self._java_obj = self._java_obj.setGranularityCol(value)
        return self
    
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
        self._set(handler=value)
        return self
    
    def setMaxAnomalyRatio(self, value):
        """
        Args:
            maxAnomalyRatio:  Optional argument, advanced model parameter, max anomaly ratio in a time series.     
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.org.apache.spark.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setMaxAnomalyRatio(value)
        return self
    
    def setMaxAnomalyRatioCol(self, value):
        """
        Args:
            maxAnomalyRatio:  Optional argument, advanced model parameter, max anomaly ratio in a time series.     
        """
        self._java_obj = self._java_obj.setMaxAnomalyRatioCol(value)
        return self
    
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
        self._set(outputCol=value)
        return self
    
    def setPeriod(self, value):
        """
        Args:
            period:  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.org.apache.spark.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setPeriod(value)
        return self
    
    def setPeriodCol(self, value):
        """
        Args:
            period:  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     
        """
        self._java_obj = self._java_obj.setPeriodCol(value)
        return self
    
    def setSensitivity(self, value):
        """
        Args:
            sensitivity:  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.org.apache.spark.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setSensitivity(value)
        return self
    
    def setSensitivityCol(self, value):
        """
        Args:
            sensitivity:  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     
        """
        self._java_obj = self._java_obj.setSensitivityCol(value)
        return self
    
    def setSeries(self, value):
        """
        Args:
            series:  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.org.apache.spark.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setSeries(value)
        return self
    
    def setSeriesCol(self, value):
        """
        Args:
            series:  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     
        """
        self._java_obj = self._java_obj.setSeriesCol(value)
        return self
    
    def setSubscriptionKey(self, value):
        """
        Args:
            subscriptionKey: the API key to use
        """
        if isinstance(value, list):
            value = SparkContext._active_spark_context._jvm.org.apache.spark.ml.param.ServiceParam.toSeq(value)
        self._java_obj = self._java_obj.setSubscriptionKey(value)
        return self
    
    def setSubscriptionKeyCol(self, value):
        """
        Args:
            subscriptionKey: the API key to use
        """
        self._java_obj = self._java_obj.setSubscriptionKeyCol(value)
        return self
    
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
        """
        self._set(timeout=value)
        return self
    
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
        self._set(url=value)
        return self

    
    def getConcurrency(self):
        """
        Returns:
            concurrency: max number of concurrent calls
        """
        return self.getOrDefault(self.concurrency)
    
    
    def getConcurrentTimeout(self):
        """
        Returns:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
        return self.getOrDefault(self.concurrentTimeout)
    
    
    def getCustomInterval(self):
        """
        Returns:
            customInterval:  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     
        """
        return self.getOrDefault(self.customInterval)
    
    
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
        return self.getOrDefault(self.errorCol)
    
    
    def getGranularity(self):
        """
        Returns:
            granularity:  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     
        """
        return self.getOrDefault(self.granularity)
    
    
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
        return self.getOrDefault(self.handler)
    
    
    def getMaxAnomalyRatio(self):
        """
        Returns:
            maxAnomalyRatio:  Optional argument, advanced model parameter, max anomaly ratio in a time series.     
        """
        return self.getOrDefault(self.maxAnomalyRatio)
    
    
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
        return self.getOrDefault(self.outputCol)
    
    
    def getPeriod(self):
        """
        Returns:
            period:  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     
        """
        return self.getOrDefault(self.period)
    
    
    def getSensitivity(self):
        """
        Returns:
            sensitivity:  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     
        """
        return self.getOrDefault(self.sensitivity)
    
    
    def getSeries(self):
        """
        Returns:
            series:  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     
        """
        return self.getOrDefault(self.series)
    
    
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
        return self.getOrDefault(self.subscriptionKey)
    
    
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
        """
        return self.getOrDefault(self.timeout)
    
    
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
        return self.getOrDefault(self.url)

    

    
    def setLocation(self, value):
        self._java_obj = self._java_obj.setLocation(value)
        return self
    
    def setLinkedService(self, value):
        self._java_obj = self._java_obj.setLinkedService(value)
        return self
        