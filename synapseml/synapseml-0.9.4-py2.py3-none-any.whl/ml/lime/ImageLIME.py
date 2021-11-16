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
class ImageLIME(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        cellSize (float): Number that controls the size of the superpixels
        inputCol (object): The name of the input column
        model (object): Model to try to locally approximate
        modifier (float): Controls the trade-off spatial and color distance
        nSamples (int): The number of samples to generate
        outputCol (object): The name of the output column
        predictionCol (object): prediction column name
        regularization (float): regularization param for the lasso
        samplingFraction (float): The fraction of superpixels to keep on
        superpixelCol (object): The column holding the superpixel decompositions
    """

    cellSize = Param(Params._dummy(), "cellSize", "Number that controls the size of the superpixels", typeConverter=TypeConverters.toFloat)
    
    inputCol = Param(Params._dummy(), "inputCol", "The name of the input column")
    
    model = Param(Params._dummy(), "model", "Model to try to locally approximate")
    
    modifier = Param(Params._dummy(), "modifier", "Controls the trade-off spatial and color distance", typeConverter=TypeConverters.toFloat)
    
    nSamples = Param(Params._dummy(), "nSamples", "The number of samples to generate", typeConverter=TypeConverters.toInt)
    
    outputCol = Param(Params._dummy(), "outputCol", "The name of the output column")
    
    predictionCol = Param(Params._dummy(), "predictionCol", "prediction column name")
    
    regularization = Param(Params._dummy(), "regularization", "regularization param for the lasso", typeConverter=TypeConverters.toFloat)
    
    samplingFraction = Param(Params._dummy(), "samplingFraction", "The fraction of superpixels to keep on", typeConverter=TypeConverters.toFloat)
    
    superpixelCol = Param(Params._dummy(), "superpixelCol", "The column holding the superpixel decompositions")

    
    @keyword_only
    def __init__(
        self,
        java_obj=None,
        cellSize=16.0,
        inputCol=None,
        model=None,
        modifier=130.0,
        nSamples=900,
        outputCol=None,
        predictionCol="prediction",
        regularization=0.0,
        samplingFraction=0.3,
        superpixelCol="superpixels"
        ):
        super(ImageLIME, self).__init__()
        if java_obj is None:
            self._java_obj = self._new_java_obj("com.microsoft.azure.synapse.ml.lime.ImageLIME", self.uid)
        else:
            self._java_obj = java_obj
        self._setDefault(cellSize=16.0)
        self._setDefault(modifier=130.0)
        self._setDefault(nSamples=900)
        self._setDefault(predictionCol="prediction")
        self._setDefault(regularization=0.0)
        self._setDefault(samplingFraction=0.3)
        self._setDefault(superpixelCol="superpixels")
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
        cellSize=16.0,
        inputCol=None,
        model=None,
        modifier=130.0,
        nSamples=900,
        outputCol=None,
        predictionCol="prediction",
        regularization=0.0,
        samplingFraction=0.3,
        superpixelCol="superpixels"
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
        return "com.microsoft.azure.synapse.ml.lime.ImageLIME"

    @staticmethod
    def _from_java(java_stage):
        module_name=ImageLIME.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".ImageLIME"
        return from_java(java_stage, module_name)

    def setCellSize(self, value):
        """
        Args:
            cellSize: Number that controls the size of the superpixels
        """
        self._set(cellSize=value)
        return self
    
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
        self._set(inputCol=value)
        return self
    
    def setModel(self, value):
        """
        Args:
            model: Model to try to locally approximate
        """
        self._set(model=value)
        return self
    
    def setModifier(self, value):
        """
        Args:
            modifier: Controls the trade-off spatial and color distance
        """
        self._set(modifier=value)
        return self
    
    def setNSamples(self, value):
        """
        Args:
            nSamples: The number of samples to generate
        """
        self._set(nSamples=value)
        return self
    
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
        self._set(outputCol=value)
        return self
    
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
        self._set(predictionCol=value)
        return self
    
    def setRegularization(self, value):
        """
        Args:
            regularization: regularization param for the lasso
        """
        self._set(regularization=value)
        return self
    
    def setSamplingFraction(self, value):
        """
        Args:
            samplingFraction: The fraction of superpixels to keep on
        """
        self._set(samplingFraction=value)
        return self
    
    def setSuperpixelCol(self, value):
        """
        Args:
            superpixelCol: The column holding the superpixel decompositions
        """
        self._set(superpixelCol=value)
        return self

    
    def getCellSize(self):
        """
        Returns:
            cellSize: Number that controls the size of the superpixels
        """
        return self.getOrDefault(self.cellSize)
    
    
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
        return self.getOrDefault(self.inputCol)
    
    
    def getModel(self):
        """
        Returns:
            model: Model to try to locally approximate
        """
        return JavaParams._from_java(self._java_obj.getModel())
    
    
    def getModifier(self):
        """
        Returns:
            modifier: Controls the trade-off spatial and color distance
        """
        return self.getOrDefault(self.modifier)
    
    
    def getNSamples(self):
        """
        Returns:
            nSamples: The number of samples to generate
        """
        return self.getOrDefault(self.nSamples)
    
    
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
        return self.getOrDefault(self.outputCol)
    
    
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
        return self.getOrDefault(self.predictionCol)
    
    
    def getRegularization(self):
        """
        Returns:
            regularization: regularization param for the lasso
        """
        return self.getOrDefault(self.regularization)
    
    
    def getSamplingFraction(self):
        """
        Returns:
            samplingFraction: The fraction of superpixels to keep on
        """
        return self.getOrDefault(self.samplingFraction)
    
    
    def getSuperpixelCol(self):
        """
        Returns:
            superpixelCol: The column holding the superpixel decompositions
        """
        return self.getOrDefault(self.superpixelCol)

    

    
        