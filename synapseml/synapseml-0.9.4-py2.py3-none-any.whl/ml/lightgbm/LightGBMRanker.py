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
from synapse.ml.lightgbm.LightGBMRankerModel import LightGBMRankerModel

@inherit_doc
class LightGBMRanker(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        baggingFraction (float): Bagging fraction
        baggingFreq (int): Bagging frequency
        baggingSeed (int): Bagging seed
        binSampleCount (int): Number of samples considered at computing histogram bins
        boostFromAverage (bool): Adjusts initial score to the mean of labels for faster convergence
        boostingType (object): Default gbdt = traditional Gradient Boosting Decision Tree. Options are: gbdt, gbrt, rf (Random Forest), random_forest, dart (Dropouts meet Multiple Additive Regression Trees), goss (Gradient-based One-Side Sampling). 
        categoricalSlotIndexes (list): List of categorical column indexes, the slot index in the features column
        categoricalSlotNames (list): List of categorical column slot names, the slot name in the features column
        chunkSize (int): Advanced parameter to specify the chunk size for copying Java data to native.  If set too high, memory may be wasted, but if set too low, performance may be reduced during data copy.If dataset size is known beforehand, set to the number of rows in the dataset.
        defaultListenPort (int): The default listen port on executors, used for testing
        driverListenPort (int): The listen port on a driver. Default value is 0 (random)
        dropRate (float): Dropout rate: a fraction of previous trees to drop during the dropout
        earlyStoppingRound (int): Early stopping round
        evalAt (list): NDCG and MAP evaluation positions, separated by comma
        featureFraction (float): Feature fraction
        featuresCol (object): features column name
        featuresShapCol (object): Output SHAP vector column name after prediction containing the feature contribution values
        fobj (object): Customized objective function. Should accept two parameters: preds, train_data, and return (grad, hess).
        groupCol (object): The name of the group column
        improvementTolerance (float): Tolerance to consider improvement in metric
        initScoreCol (object): The name of the initial score column, used for continued training
        isProvideTrainingMetric (bool): Whether output metric result over training dataset.
        labelCol (object): label column name
        labelGain (list): graded relevance for each label in NDCG
        lambdaL1 (float): L1 regularization
        lambdaL2 (float): L2 regularization
        leafPredictionCol (object): Predicted leaf indices's column name
        learningRate (float): Learning rate or shrinkage rate
        matrixType (object): Advanced parameter to specify whether the native lightgbm matrix constructed should be sparse or dense.  Values can be auto, sparse or dense. Default value is auto, which samples first ten rows to determine type.
        maxBin (int): Max bin
        maxBinByFeature (list): Max number of bins for each feature
        maxDeltaStep (float): Used to limit the max output of tree leaves
        maxDepth (int): Max depth
        maxDrop (int): Max number of dropped trees during one boosting iteration
        maxPosition (int): optimized NDCG at this position
        metric (object): Metrics to be evaluated on the evaluation data.  Options are: empty string or not specified means that metric corresponding to specified objective will be used (this is possible only for pre-defined objective functions, otherwise no evaluation metric will be added). None (string, not a None value) means that no metric will be registered, aliases: na, null, custom. l1, absolute loss, aliases: mean_absolute_error, mae, regression_l1. l2, square loss, aliases: mean_squared_error, mse, regression_l2, regression. rmse, root square loss, aliases: root_mean_squared_error, l2_root. quantile, Quantile regression. mape, MAPE loss, aliases: mean_absolute_percentage_error. huber, Huber loss. fair, Fair loss. poisson, negative log-likelihood for Poisson regression. gamma, negative log-likelihood for Gamma regression. gamma_deviance, residual deviance for Gamma regression. tweedie, negative log-likelihood for Tweedie regression. ndcg, NDCG, aliases: lambdarank. map, MAP, aliases: mean_average_precision. auc, AUC. binary_logloss, log loss, aliases: binary. binary_error, for one sample: 0 for correct classification, 1 for error classification. multi_logloss, log loss for multi-class classification, aliases: multiclass, softmax, multiclassova, multiclass_ova, ova, ovr. multi_error, error rate for multi-class classification. cross_entropy, cross-entropy (with optional linear weights), aliases: xentropy. cross_entropy_lambda, intensity-weighted cross-entropy, aliases: xentlambda. kullback_leibler, Kullback-Leibler divergence, aliases: kldiv. 
        minDataInLeaf (int): Minimal number of data in one leaf. Can be used to deal with over-fitting.
        minGainToSplit (float): The minimal gain to perform split
        minSumHessianInLeaf (float): Minimal sum hessian in one leaf
        modelString (object): LightGBM model to retrain
        negBaggingFraction (float): Negative Bagging fraction
        numBatches (int): If greater than 0, splits data into separate batches during training
        numIterations (int): Number of iterations, LightGBM constructs num_class * num_iterations trees
        numLeaves (int): Number of leaves
        numTasks (int): Advanced parameter to specify the number of tasks.  SynapseML tries to guess this based on cluster configuration, but this parameter can be used to override.
        numThreads (int): Number of threads for LightGBM. For the best speed, set this to the number of real CPU cores.
        objective (object): The Objective. For regression applications, this can be: regression_l2, regression_l1, huber, fair, poisson, quantile, mape, gamma or tweedie. For classification applications, this can be: binary, multiclass, or multiclassova. 
        parallelism (object): Tree learner parallelism, can be set to data_parallel or voting_parallel
        posBaggingFraction (float): Positive Bagging fraction
        predictionCol (object): prediction column name
        repartitionByGroupingColumn (bool): Repartition training data according to grouping column, on by default.
        skipDrop (float): Probability of skipping the dropout procedure during a boosting iteration
        slotNames (list): List of slot names in the features column
        timeout (float): Timeout in seconds
        topK (int): The top_k value used in Voting parallel, set this to larger value for more accurate result, but it will slow down the training speed. It should be greater than 0
        uniformDrop (bool): Set this to true to use uniform drop in dart mode
        useBarrierExecutionMode (bool): Barrier execution mode which uses a barrier stage, off by default.
        useSingleDatasetMode (bool): Use single dataset execution mode to create a single native dataset per executor (singleton) to reduce memory and communication overhead. Note this is disabled when running spark in local mode.
        validationIndicatorCol (object): Indicates whether the row is for training or validation
        verbosity (int): Verbosity where lt 0 is Fatal, eq 0 is Error, eq 1 is Info, gt 1 is Debug
        weightCol (object): The name of the weight column
        xgboostDartMode (bool): Set this to true to use xgboost dart mode
    """

    baggingFraction = Param(Params._dummy(), "baggingFraction", "Bagging fraction", typeConverter=TypeConverters.toFloat)
    
    baggingFreq = Param(Params._dummy(), "baggingFreq", "Bagging frequency", typeConverter=TypeConverters.toInt)
    
    baggingSeed = Param(Params._dummy(), "baggingSeed", "Bagging seed", typeConverter=TypeConverters.toInt)
    
    binSampleCount = Param(Params._dummy(), "binSampleCount", "Number of samples considered at computing histogram bins", typeConverter=TypeConverters.toInt)
    
    boostFromAverage = Param(Params._dummy(), "boostFromAverage", "Adjusts initial score to the mean of labels for faster convergence", typeConverter=TypeConverters.toBoolean)
    
    boostingType = Param(Params._dummy(), "boostingType", "Default gbdt = traditional Gradient Boosting Decision Tree. Options are: gbdt, gbrt, rf (Random Forest), random_forest, dart (Dropouts meet Multiple Additive Regression Trees), goss (Gradient-based One-Side Sampling). ")
    
    categoricalSlotIndexes = Param(Params._dummy(), "categoricalSlotIndexes", "List of categorical column indexes, the slot index in the features column", typeConverter=TypeConverters.toListInt)
    
    categoricalSlotNames = Param(Params._dummy(), "categoricalSlotNames", "List of categorical column slot names, the slot name in the features column", typeConverter=TypeConverters.toListString)
    
    chunkSize = Param(Params._dummy(), "chunkSize", "Advanced parameter to specify the chunk size for copying Java data to native.  If set too high, memory may be wasted, but if set too low, performance may be reduced during data copy.If dataset size is known beforehand, set to the number of rows in the dataset.", typeConverter=TypeConverters.toInt)
    
    defaultListenPort = Param(Params._dummy(), "defaultListenPort", "The default listen port on executors, used for testing", typeConverter=TypeConverters.toInt)
    
    driverListenPort = Param(Params._dummy(), "driverListenPort", "The listen port on a driver. Default value is 0 (random)", typeConverter=TypeConverters.toInt)
    
    dropRate = Param(Params._dummy(), "dropRate", "Dropout rate: a fraction of previous trees to drop during the dropout", typeConverter=TypeConverters.toFloat)
    
    earlyStoppingRound = Param(Params._dummy(), "earlyStoppingRound", "Early stopping round", typeConverter=TypeConverters.toInt)
    
    evalAt = Param(Params._dummy(), "evalAt", "NDCG and MAP evaluation positions, separated by comma", typeConverter=TypeConverters.toListInt)
    
    featureFraction = Param(Params._dummy(), "featureFraction", "Feature fraction", typeConverter=TypeConverters.toFloat)
    
    featuresCol = Param(Params._dummy(), "featuresCol", "features column name")
    
    featuresShapCol = Param(Params._dummy(), "featuresShapCol", "Output SHAP vector column name after prediction containing the feature contribution values")
    
    fobj = Param(Params._dummy(), "fobj", "Customized objective function. Should accept two parameters: preds, train_data, and return (grad, hess).")
    
    groupCol = Param(Params._dummy(), "groupCol", "The name of the group column")
    
    improvementTolerance = Param(Params._dummy(), "improvementTolerance", "Tolerance to consider improvement in metric", typeConverter=TypeConverters.toFloat)
    
    initScoreCol = Param(Params._dummy(), "initScoreCol", "The name of the initial score column, used for continued training")
    
    isProvideTrainingMetric = Param(Params._dummy(), "isProvideTrainingMetric", "Whether output metric result over training dataset.", typeConverter=TypeConverters.toBoolean)
    
    labelCol = Param(Params._dummy(), "labelCol", "label column name")
    
    labelGain = Param(Params._dummy(), "labelGain", "graded relevance for each label in NDCG", typeConverter=TypeConverters.toListFloat)
    
    lambdaL1 = Param(Params._dummy(), "lambdaL1", "L1 regularization", typeConverter=TypeConverters.toFloat)
    
    lambdaL2 = Param(Params._dummy(), "lambdaL2", "L2 regularization", typeConverter=TypeConverters.toFloat)
    
    leafPredictionCol = Param(Params._dummy(), "leafPredictionCol", "Predicted leaf indices's column name")
    
    learningRate = Param(Params._dummy(), "learningRate", "Learning rate or shrinkage rate", typeConverter=TypeConverters.toFloat)
    
    matrixType = Param(Params._dummy(), "matrixType", "Advanced parameter to specify whether the native lightgbm matrix constructed should be sparse or dense.  Values can be auto, sparse or dense. Default value is auto, which samples first ten rows to determine type.")
    
    maxBin = Param(Params._dummy(), "maxBin", "Max bin", typeConverter=TypeConverters.toInt)
    
    maxBinByFeature = Param(Params._dummy(), "maxBinByFeature", "Max number of bins for each feature", typeConverter=TypeConverters.toListInt)
    
    maxDeltaStep = Param(Params._dummy(), "maxDeltaStep", "Used to limit the max output of tree leaves", typeConverter=TypeConverters.toFloat)
    
    maxDepth = Param(Params._dummy(), "maxDepth", "Max depth", typeConverter=TypeConverters.toInt)
    
    maxDrop = Param(Params._dummy(), "maxDrop", "Max number of dropped trees during one boosting iteration", typeConverter=TypeConverters.toInt)
    
    maxPosition = Param(Params._dummy(), "maxPosition", "optimized NDCG at this position", typeConverter=TypeConverters.toInt)
    
    metric = Param(Params._dummy(), "metric", "Metrics to be evaluated on the evaluation data.  Options are: empty string or not specified means that metric corresponding to specified objective will be used (this is possible only for pre-defined objective functions, otherwise no evaluation metric will be added). None (string, not a None value) means that no metric will be registered, aliases: na, null, custom. l1, absolute loss, aliases: mean_absolute_error, mae, regression_l1. l2, square loss, aliases: mean_squared_error, mse, regression_l2, regression. rmse, root square loss, aliases: root_mean_squared_error, l2_root. quantile, Quantile regression. mape, MAPE loss, aliases: mean_absolute_percentage_error. huber, Huber loss. fair, Fair loss. poisson, negative log-likelihood for Poisson regression. gamma, negative log-likelihood for Gamma regression. gamma_deviance, residual deviance for Gamma regression. tweedie, negative log-likelihood for Tweedie regression. ndcg, NDCG, aliases: lambdarank. map, MAP, aliases: mean_average_precision. auc, AUC. binary_logloss, log loss, aliases: binary. binary_error, for one sample: 0 for correct classification, 1 for error classification. multi_logloss, log loss for multi-class classification, aliases: multiclass, softmax, multiclassova, multiclass_ova, ova, ovr. multi_error, error rate for multi-class classification. cross_entropy, cross-entropy (with optional linear weights), aliases: xentropy. cross_entropy_lambda, intensity-weighted cross-entropy, aliases: xentlambda. kullback_leibler, Kullback-Leibler divergence, aliases: kldiv. ")
    
    minDataInLeaf = Param(Params._dummy(), "minDataInLeaf", "Minimal number of data in one leaf. Can be used to deal with over-fitting.", typeConverter=TypeConverters.toInt)
    
    minGainToSplit = Param(Params._dummy(), "minGainToSplit", "The minimal gain to perform split", typeConverter=TypeConverters.toFloat)
    
    minSumHessianInLeaf = Param(Params._dummy(), "minSumHessianInLeaf", "Minimal sum hessian in one leaf", typeConverter=TypeConverters.toFloat)
    
    modelString = Param(Params._dummy(), "modelString", "LightGBM model to retrain")
    
    negBaggingFraction = Param(Params._dummy(), "negBaggingFraction", "Negative Bagging fraction", typeConverter=TypeConverters.toFloat)
    
    numBatches = Param(Params._dummy(), "numBatches", "If greater than 0, splits data into separate batches during training", typeConverter=TypeConverters.toInt)
    
    numIterations = Param(Params._dummy(), "numIterations", "Number of iterations, LightGBM constructs num_class * num_iterations trees", typeConverter=TypeConverters.toInt)
    
    numLeaves = Param(Params._dummy(), "numLeaves", "Number of leaves", typeConverter=TypeConverters.toInt)
    
    numTasks = Param(Params._dummy(), "numTasks", "Advanced parameter to specify the number of tasks.  SynapseML tries to guess this based on cluster configuration, but this parameter can be used to override.", typeConverter=TypeConverters.toInt)
    
    numThreads = Param(Params._dummy(), "numThreads", "Number of threads for LightGBM. For the best speed, set this to the number of real CPU cores.", typeConverter=TypeConverters.toInt)
    
    objective = Param(Params._dummy(), "objective", "The Objective. For regression applications, this can be: regression_l2, regression_l1, huber, fair, poisson, quantile, mape, gamma or tweedie. For classification applications, this can be: binary, multiclass, or multiclassova. ")
    
    parallelism = Param(Params._dummy(), "parallelism", "Tree learner parallelism, can be set to data_parallel or voting_parallel")
    
    posBaggingFraction = Param(Params._dummy(), "posBaggingFraction", "Positive Bagging fraction", typeConverter=TypeConverters.toFloat)
    
    predictionCol = Param(Params._dummy(), "predictionCol", "prediction column name")
    
    repartitionByGroupingColumn = Param(Params._dummy(), "repartitionByGroupingColumn", "Repartition training data according to grouping column, on by default.", typeConverter=TypeConverters.toBoolean)
    
    skipDrop = Param(Params._dummy(), "skipDrop", "Probability of skipping the dropout procedure during a boosting iteration", typeConverter=TypeConverters.toFloat)
    
    slotNames = Param(Params._dummy(), "slotNames", "List of slot names in the features column", typeConverter=TypeConverters.toListString)
    
    timeout = Param(Params._dummy(), "timeout", "Timeout in seconds", typeConverter=TypeConverters.toFloat)
    
    topK = Param(Params._dummy(), "topK", "The top_k value used in Voting parallel, set this to larger value for more accurate result, but it will slow down the training speed. It should be greater than 0", typeConverter=TypeConverters.toInt)
    
    uniformDrop = Param(Params._dummy(), "uniformDrop", "Set this to true to use uniform drop in dart mode", typeConverter=TypeConverters.toBoolean)
    
    useBarrierExecutionMode = Param(Params._dummy(), "useBarrierExecutionMode", "Barrier execution mode which uses a barrier stage, off by default.", typeConverter=TypeConverters.toBoolean)
    
    useSingleDatasetMode = Param(Params._dummy(), "useSingleDatasetMode", "Use single dataset execution mode to create a single native dataset per executor (singleton) to reduce memory and communication overhead. Note this is disabled when running spark in local mode.", typeConverter=TypeConverters.toBoolean)
    
    validationIndicatorCol = Param(Params._dummy(), "validationIndicatorCol", "Indicates whether the row is for training or validation")
    
    verbosity = Param(Params._dummy(), "verbosity", "Verbosity where lt 0 is Fatal, eq 0 is Error, eq 1 is Info, gt 1 is Debug", typeConverter=TypeConverters.toInt)
    
    weightCol = Param(Params._dummy(), "weightCol", "The name of the weight column")
    
    xgboostDartMode = Param(Params._dummy(), "xgboostDartMode", "Set this to true to use xgboost dart mode", typeConverter=TypeConverters.toBoolean)

    
    @keyword_only
    def __init__(
        self,
        java_obj=None,
        baggingFraction=1.0,
        baggingFreq=0,
        baggingSeed=3,
        binSampleCount=200000,
        boostFromAverage=True,
        boostingType="gbdt",
        categoricalSlotIndexes=[],
        categoricalSlotNames=[],
        chunkSize=10000,
        defaultListenPort=12400,
        driverListenPort=0,
        dropRate=0.1,
        earlyStoppingRound=0,
        evalAt=[1,2,3,4,5],
        featureFraction=1.0,
        featuresCol="features",
        featuresShapCol="",
        fobj=None,
        groupCol=None,
        improvementTolerance=0.0,
        initScoreCol=None,
        isProvideTrainingMetric=False,
        labelCol="label",
        labelGain=[],
        lambdaL1=0.0,
        lambdaL2=0.0,
        leafPredictionCol="",
        learningRate=0.1,
        matrixType="auto",
        maxBin=255,
        maxBinByFeature=[],
        maxDeltaStep=0.0,
        maxDepth=-1,
        maxDrop=50,
        maxPosition=20,
        metric="",
        minDataInLeaf=20,
        minGainToSplit=0.0,
        minSumHessianInLeaf=0.001,
        modelString="",
        negBaggingFraction=1.0,
        numBatches=0,
        numIterations=100,
        numLeaves=31,
        numTasks=0,
        numThreads=0,
        objective="lambdarank",
        parallelism="data_parallel",
        posBaggingFraction=1.0,
        predictionCol="prediction",
        repartitionByGroupingColumn=True,
        skipDrop=0.5,
        slotNames=[],
        timeout=1200.0,
        topK=20,
        uniformDrop=False,
        useBarrierExecutionMode=False,
        useSingleDatasetMode=False,
        validationIndicatorCol=None,
        verbosity=-1,
        weightCol=None,
        xgboostDartMode=False
        ):
        super(LightGBMRanker, self).__init__()
        if java_obj is None:
            self._java_obj = self._new_java_obj("com.microsoft.azure.synapse.ml.lightgbm.LightGBMRanker", self.uid)
        else:
            self._java_obj = java_obj
        self._setDefault(baggingFraction=1.0)
        self._setDefault(baggingFreq=0)
        self._setDefault(baggingSeed=3)
        self._setDefault(binSampleCount=200000)
        self._setDefault(boostFromAverage=True)
        self._setDefault(boostingType="gbdt")
        self._setDefault(categoricalSlotIndexes=[])
        self._setDefault(categoricalSlotNames=[])
        self._setDefault(chunkSize=10000)
        self._setDefault(defaultListenPort=12400)
        self._setDefault(driverListenPort=0)
        self._setDefault(dropRate=0.1)
        self._setDefault(earlyStoppingRound=0)
        self._setDefault(evalAt=[1,2,3,4,5])
        self._setDefault(featureFraction=1.0)
        self._setDefault(featuresCol="features")
        self._setDefault(featuresShapCol="")
        self._setDefault(improvementTolerance=0.0)
        self._setDefault(isProvideTrainingMetric=False)
        self._setDefault(labelCol="label")
        self._setDefault(labelGain=[])
        self._setDefault(lambdaL1=0.0)
        self._setDefault(lambdaL2=0.0)
        self._setDefault(leafPredictionCol="")
        self._setDefault(learningRate=0.1)
        self._setDefault(matrixType="auto")
        self._setDefault(maxBin=255)
        self._setDefault(maxBinByFeature=[])
        self._setDefault(maxDeltaStep=0.0)
        self._setDefault(maxDepth=-1)
        self._setDefault(maxDrop=50)
        self._setDefault(maxPosition=20)
        self._setDefault(metric="")
        self._setDefault(minDataInLeaf=20)
        self._setDefault(minGainToSplit=0.0)
        self._setDefault(minSumHessianInLeaf=0.001)
        self._setDefault(modelString="")
        self._setDefault(negBaggingFraction=1.0)
        self._setDefault(numBatches=0)
        self._setDefault(numIterations=100)
        self._setDefault(numLeaves=31)
        self._setDefault(numTasks=0)
        self._setDefault(numThreads=0)
        self._setDefault(objective="lambdarank")
        self._setDefault(parallelism="data_parallel")
        self._setDefault(posBaggingFraction=1.0)
        self._setDefault(predictionCol="prediction")
        self._setDefault(repartitionByGroupingColumn=True)
        self._setDefault(skipDrop=0.5)
        self._setDefault(slotNames=[])
        self._setDefault(timeout=1200.0)
        self._setDefault(topK=20)
        self._setDefault(uniformDrop=False)
        self._setDefault(useBarrierExecutionMode=False)
        self._setDefault(useSingleDatasetMode=False)
        self._setDefault(verbosity=-1)
        self._setDefault(xgboostDartMode=False)
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
        baggingFraction=1.0,
        baggingFreq=0,
        baggingSeed=3,
        binSampleCount=200000,
        boostFromAverage=True,
        boostingType="gbdt",
        categoricalSlotIndexes=[],
        categoricalSlotNames=[],
        chunkSize=10000,
        defaultListenPort=12400,
        driverListenPort=0,
        dropRate=0.1,
        earlyStoppingRound=0,
        evalAt=[1,2,3,4,5],
        featureFraction=1.0,
        featuresCol="features",
        featuresShapCol="",
        fobj=None,
        groupCol=None,
        improvementTolerance=0.0,
        initScoreCol=None,
        isProvideTrainingMetric=False,
        labelCol="label",
        labelGain=[],
        lambdaL1=0.0,
        lambdaL2=0.0,
        leafPredictionCol="",
        learningRate=0.1,
        matrixType="auto",
        maxBin=255,
        maxBinByFeature=[],
        maxDeltaStep=0.0,
        maxDepth=-1,
        maxDrop=50,
        maxPosition=20,
        metric="",
        minDataInLeaf=20,
        minGainToSplit=0.0,
        minSumHessianInLeaf=0.001,
        modelString="",
        negBaggingFraction=1.0,
        numBatches=0,
        numIterations=100,
        numLeaves=31,
        numTasks=0,
        numThreads=0,
        objective="lambdarank",
        parallelism="data_parallel",
        posBaggingFraction=1.0,
        predictionCol="prediction",
        repartitionByGroupingColumn=True,
        skipDrop=0.5,
        slotNames=[],
        timeout=1200.0,
        topK=20,
        uniformDrop=False,
        useBarrierExecutionMode=False,
        useSingleDatasetMode=False,
        validationIndicatorCol=None,
        verbosity=-1,
        weightCol=None,
        xgboostDartMode=False
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
        return "com.microsoft.azure.synapse.ml.lightgbm.LightGBMRanker"

    @staticmethod
    def _from_java(java_stage):
        module_name=LightGBMRanker.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".LightGBMRanker"
        return from_java(java_stage, module_name)

    def setBaggingFraction(self, value):
        """
        Args:
            baggingFraction: Bagging fraction
        """
        self._set(baggingFraction=value)
        return self
    
    def setBaggingFreq(self, value):
        """
        Args:
            baggingFreq: Bagging frequency
        """
        self._set(baggingFreq=value)
        return self
    
    def setBaggingSeed(self, value):
        """
        Args:
            baggingSeed: Bagging seed
        """
        self._set(baggingSeed=value)
        return self
    
    def setBinSampleCount(self, value):
        """
        Args:
            binSampleCount: Number of samples considered at computing histogram bins
        """
        self._set(binSampleCount=value)
        return self
    
    def setBoostFromAverage(self, value):
        """
        Args:
            boostFromAverage: Adjusts initial score to the mean of labels for faster convergence
        """
        self._set(boostFromAverage=value)
        return self
    
    def setBoostingType(self, value):
        """
        Args:
            boostingType: Default gbdt = traditional Gradient Boosting Decision Tree. Options are: gbdt, gbrt, rf (Random Forest), random_forest, dart (Dropouts meet Multiple Additive Regression Trees), goss (Gradient-based One-Side Sampling). 
        """
        self._set(boostingType=value)
        return self
    
    def setCategoricalSlotIndexes(self, value):
        """
        Args:
            categoricalSlotIndexes: List of categorical column indexes, the slot index in the features column
        """
        self._set(categoricalSlotIndexes=value)
        return self
    
    def setCategoricalSlotNames(self, value):
        """
        Args:
            categoricalSlotNames: List of categorical column slot names, the slot name in the features column
        """
        self._set(categoricalSlotNames=value)
        return self
    
    def setChunkSize(self, value):
        """
        Args:
            chunkSize: Advanced parameter to specify the chunk size for copying Java data to native.  If set too high, memory may be wasted, but if set too low, performance may be reduced during data copy.If dataset size is known beforehand, set to the number of rows in the dataset.
        """
        self._set(chunkSize=value)
        return self
    
    def setDefaultListenPort(self, value):
        """
        Args:
            defaultListenPort: The default listen port on executors, used for testing
        """
        self._set(defaultListenPort=value)
        return self
    
    def setDriverListenPort(self, value):
        """
        Args:
            driverListenPort: The listen port on a driver. Default value is 0 (random)
        """
        self._set(driverListenPort=value)
        return self
    
    def setDropRate(self, value):
        """
        Args:
            dropRate: Dropout rate: a fraction of previous trees to drop during the dropout
        """
        self._set(dropRate=value)
        return self
    
    def setEarlyStoppingRound(self, value):
        """
        Args:
            earlyStoppingRound: Early stopping round
        """
        self._set(earlyStoppingRound=value)
        return self
    
    def setEvalAt(self, value):
        """
        Args:
            evalAt: NDCG and MAP evaluation positions, separated by comma
        """
        self._set(evalAt=value)
        return self
    
    def setFeatureFraction(self, value):
        """
        Args:
            featureFraction: Feature fraction
        """
        self._set(featureFraction=value)
        return self
    
    def setFeaturesCol(self, value):
        """
        Args:
            featuresCol: features column name
        """
        self._set(featuresCol=value)
        return self
    
    def setFeaturesShapCol(self, value):
        """
        Args:
            featuresShapCol: Output SHAP vector column name after prediction containing the feature contribution values
        """
        self._set(featuresShapCol=value)
        return self
    
    def setFobj(self, value):
        """
        Args:
            fobj: Customized objective function. Should accept two parameters: preds, train_data, and return (grad, hess).
        """
        self._set(fobj=value)
        return self
    
    def setGroupCol(self, value):
        """
        Args:
            groupCol: The name of the group column
        """
        self._set(groupCol=value)
        return self
    
    def setImprovementTolerance(self, value):
        """
        Args:
            improvementTolerance: Tolerance to consider improvement in metric
        """
        self._set(improvementTolerance=value)
        return self
    
    def setInitScoreCol(self, value):
        """
        Args:
            initScoreCol: The name of the initial score column, used for continued training
        """
        self._set(initScoreCol=value)
        return self
    
    def setIsProvideTrainingMetric(self, value):
        """
        Args:
            isProvideTrainingMetric: Whether output metric result over training dataset.
        """
        self._set(isProvideTrainingMetric=value)
        return self
    
    def setLabelCol(self, value):
        """
        Args:
            labelCol: label column name
        """
        self._set(labelCol=value)
        return self
    
    def setLabelGain(self, value):
        """
        Args:
            labelGain: graded relevance for each label in NDCG
        """
        self._set(labelGain=value)
        return self
    
    def setLambdaL1(self, value):
        """
        Args:
            lambdaL1: L1 regularization
        """
        self._set(lambdaL1=value)
        return self
    
    def setLambdaL2(self, value):
        """
        Args:
            lambdaL2: L2 regularization
        """
        self._set(lambdaL2=value)
        return self
    
    def setLeafPredictionCol(self, value):
        """
        Args:
            leafPredictionCol: Predicted leaf indices's column name
        """
        self._set(leafPredictionCol=value)
        return self
    
    def setLearningRate(self, value):
        """
        Args:
            learningRate: Learning rate or shrinkage rate
        """
        self._set(learningRate=value)
        return self
    
    def setMatrixType(self, value):
        """
        Args:
            matrixType: Advanced parameter to specify whether the native lightgbm matrix constructed should be sparse or dense.  Values can be auto, sparse or dense. Default value is auto, which samples first ten rows to determine type.
        """
        self._set(matrixType=value)
        return self
    
    def setMaxBin(self, value):
        """
        Args:
            maxBin: Max bin
        """
        self._set(maxBin=value)
        return self
    
    def setMaxBinByFeature(self, value):
        """
        Args:
            maxBinByFeature: Max number of bins for each feature
        """
        self._set(maxBinByFeature=value)
        return self
    
    def setMaxDeltaStep(self, value):
        """
        Args:
            maxDeltaStep: Used to limit the max output of tree leaves
        """
        self._set(maxDeltaStep=value)
        return self
    
    def setMaxDepth(self, value):
        """
        Args:
            maxDepth: Max depth
        """
        self._set(maxDepth=value)
        return self
    
    def setMaxDrop(self, value):
        """
        Args:
            maxDrop: Max number of dropped trees during one boosting iteration
        """
        self._set(maxDrop=value)
        return self
    
    def setMaxPosition(self, value):
        """
        Args:
            maxPosition: optimized NDCG at this position
        """
        self._set(maxPosition=value)
        return self
    
    def setMetric(self, value):
        """
        Args:
            metric: Metrics to be evaluated on the evaluation data.  Options are: empty string or not specified means that metric corresponding to specified objective will be used (this is possible only for pre-defined objective functions, otherwise no evaluation metric will be added). None (string, not a None value) means that no metric will be registered, aliases: na, null, custom. l1, absolute loss, aliases: mean_absolute_error, mae, regression_l1. l2, square loss, aliases: mean_squared_error, mse, regression_l2, regression. rmse, root square loss, aliases: root_mean_squared_error, l2_root. quantile, Quantile regression. mape, MAPE loss, aliases: mean_absolute_percentage_error. huber, Huber loss. fair, Fair loss. poisson, negative log-likelihood for Poisson regression. gamma, negative log-likelihood for Gamma regression. gamma_deviance, residual deviance for Gamma regression. tweedie, negative log-likelihood for Tweedie regression. ndcg, NDCG, aliases: lambdarank. map, MAP, aliases: mean_average_precision. auc, AUC. binary_logloss, log loss, aliases: binary. binary_error, for one sample: 0 for correct classification, 1 for error classification. multi_logloss, log loss for multi-class classification, aliases: multiclass, softmax, multiclassova, multiclass_ova, ova, ovr. multi_error, error rate for multi-class classification. cross_entropy, cross-entropy (with optional linear weights), aliases: xentropy. cross_entropy_lambda, intensity-weighted cross-entropy, aliases: xentlambda. kullback_leibler, Kullback-Leibler divergence, aliases: kldiv. 
        """
        self._set(metric=value)
        return self
    
    def setMinDataInLeaf(self, value):
        """
        Args:
            minDataInLeaf: Minimal number of data in one leaf. Can be used to deal with over-fitting.
        """
        self._set(minDataInLeaf=value)
        return self
    
    def setMinGainToSplit(self, value):
        """
        Args:
            minGainToSplit: The minimal gain to perform split
        """
        self._set(minGainToSplit=value)
        return self
    
    def setMinSumHessianInLeaf(self, value):
        """
        Args:
            minSumHessianInLeaf: Minimal sum hessian in one leaf
        """
        self._set(minSumHessianInLeaf=value)
        return self
    
    def setModelString(self, value):
        """
        Args:
            modelString: LightGBM model to retrain
        """
        self._set(modelString=value)
        return self
    
    def setNegBaggingFraction(self, value):
        """
        Args:
            negBaggingFraction: Negative Bagging fraction
        """
        self._set(negBaggingFraction=value)
        return self
    
    def setNumBatches(self, value):
        """
        Args:
            numBatches: If greater than 0, splits data into separate batches during training
        """
        self._set(numBatches=value)
        return self
    
    def setNumIterations(self, value):
        """
        Args:
            numIterations: Number of iterations, LightGBM constructs num_class * num_iterations trees
        """
        self._set(numIterations=value)
        return self
    
    def setNumLeaves(self, value):
        """
        Args:
            numLeaves: Number of leaves
        """
        self._set(numLeaves=value)
        return self
    
    def setNumTasks(self, value):
        """
        Args:
            numTasks: Advanced parameter to specify the number of tasks.  SynapseML tries to guess this based on cluster configuration, but this parameter can be used to override.
        """
        self._set(numTasks=value)
        return self
    
    def setNumThreads(self, value):
        """
        Args:
            numThreads: Number of threads for LightGBM. For the best speed, set this to the number of real CPU cores.
        """
        self._set(numThreads=value)
        return self
    
    def setObjective(self, value):
        """
        Args:
            objective: The Objective. For regression applications, this can be: regression_l2, regression_l1, huber, fair, poisson, quantile, mape, gamma or tweedie. For classification applications, this can be: binary, multiclass, or multiclassova. 
        """
        self._set(objective=value)
        return self
    
    def setParallelism(self, value):
        """
        Args:
            parallelism: Tree learner parallelism, can be set to data_parallel or voting_parallel
        """
        self._set(parallelism=value)
        return self
    
    def setPosBaggingFraction(self, value):
        """
        Args:
            posBaggingFraction: Positive Bagging fraction
        """
        self._set(posBaggingFraction=value)
        return self
    
    def setPredictionCol(self, value):
        """
        Args:
            predictionCol: prediction column name
        """
        self._set(predictionCol=value)
        return self
    
    def setRepartitionByGroupingColumn(self, value):
        """
        Args:
            repartitionByGroupingColumn: Repartition training data according to grouping column, on by default.
        """
        self._set(repartitionByGroupingColumn=value)
        return self
    
    def setSkipDrop(self, value):
        """
        Args:
            skipDrop: Probability of skipping the dropout procedure during a boosting iteration
        """
        self._set(skipDrop=value)
        return self
    
    def setSlotNames(self, value):
        """
        Args:
            slotNames: List of slot names in the features column
        """
        self._set(slotNames=value)
        return self
    
    def setTimeout(self, value):
        """
        Args:
            timeout: Timeout in seconds
        """
        self._set(timeout=value)
        return self
    
    def setTopK(self, value):
        """
        Args:
            topK: The top_k value used in Voting parallel, set this to larger value for more accurate result, but it will slow down the training speed. It should be greater than 0
        """
        self._set(topK=value)
        return self
    
    def setUniformDrop(self, value):
        """
        Args:
            uniformDrop: Set this to true to use uniform drop in dart mode
        """
        self._set(uniformDrop=value)
        return self
    
    def setUseBarrierExecutionMode(self, value):
        """
        Args:
            useBarrierExecutionMode: Barrier execution mode which uses a barrier stage, off by default.
        """
        self._set(useBarrierExecutionMode=value)
        return self
    
    def setUseSingleDatasetMode(self, value):
        """
        Args:
            useSingleDatasetMode: Use single dataset execution mode to create a single native dataset per executor (singleton) to reduce memory and communication overhead. Note this is disabled when running spark in local mode.
        """
        self._set(useSingleDatasetMode=value)
        return self
    
    def setValidationIndicatorCol(self, value):
        """
        Args:
            validationIndicatorCol: Indicates whether the row is for training or validation
        """
        self._set(validationIndicatorCol=value)
        return self
    
    def setVerbosity(self, value):
        """
        Args:
            verbosity: Verbosity where lt 0 is Fatal, eq 0 is Error, eq 1 is Info, gt 1 is Debug
        """
        self._set(verbosity=value)
        return self
    
    def setWeightCol(self, value):
        """
        Args:
            weightCol: The name of the weight column
        """
        self._set(weightCol=value)
        return self
    
    def setXgboostDartMode(self, value):
        """
        Args:
            xgboostDartMode: Set this to true to use xgboost dart mode
        """
        self._set(xgboostDartMode=value)
        return self

    
    def getBaggingFraction(self):
        """
        Returns:
            baggingFraction: Bagging fraction
        """
        return self.getOrDefault(self.baggingFraction)
    
    
    def getBaggingFreq(self):
        """
        Returns:
            baggingFreq: Bagging frequency
        """
        return self.getOrDefault(self.baggingFreq)
    
    
    def getBaggingSeed(self):
        """
        Returns:
            baggingSeed: Bagging seed
        """
        return self.getOrDefault(self.baggingSeed)
    
    
    def getBinSampleCount(self):
        """
        Returns:
            binSampleCount: Number of samples considered at computing histogram bins
        """
        return self.getOrDefault(self.binSampleCount)
    
    
    def getBoostFromAverage(self):
        """
        Returns:
            boostFromAverage: Adjusts initial score to the mean of labels for faster convergence
        """
        return self.getOrDefault(self.boostFromAverage)
    
    
    def getBoostingType(self):
        """
        Returns:
            boostingType: Default gbdt = traditional Gradient Boosting Decision Tree. Options are: gbdt, gbrt, rf (Random Forest), random_forest, dart (Dropouts meet Multiple Additive Regression Trees), goss (Gradient-based One-Side Sampling). 
        """
        return self.getOrDefault(self.boostingType)
    
    
    def getCategoricalSlotIndexes(self):
        """
        Returns:
            categoricalSlotIndexes: List of categorical column indexes, the slot index in the features column
        """
        return self.getOrDefault(self.categoricalSlotIndexes)
    
    
    def getCategoricalSlotNames(self):
        """
        Returns:
            categoricalSlotNames: List of categorical column slot names, the slot name in the features column
        """
        return self.getOrDefault(self.categoricalSlotNames)
    
    
    def getChunkSize(self):
        """
        Returns:
            chunkSize: Advanced parameter to specify the chunk size for copying Java data to native.  If set too high, memory may be wasted, but if set too low, performance may be reduced during data copy.If dataset size is known beforehand, set to the number of rows in the dataset.
        """
        return self.getOrDefault(self.chunkSize)
    
    
    def getDefaultListenPort(self):
        """
        Returns:
            defaultListenPort: The default listen port on executors, used for testing
        """
        return self.getOrDefault(self.defaultListenPort)
    
    
    def getDriverListenPort(self):
        """
        Returns:
            driverListenPort: The listen port on a driver. Default value is 0 (random)
        """
        return self.getOrDefault(self.driverListenPort)
    
    
    def getDropRate(self):
        """
        Returns:
            dropRate: Dropout rate: a fraction of previous trees to drop during the dropout
        """
        return self.getOrDefault(self.dropRate)
    
    
    def getEarlyStoppingRound(self):
        """
        Returns:
            earlyStoppingRound: Early stopping round
        """
        return self.getOrDefault(self.earlyStoppingRound)
    
    
    def getEvalAt(self):
        """
        Returns:
            evalAt: NDCG and MAP evaluation positions, separated by comma
        """
        return self.getOrDefault(self.evalAt)
    
    
    def getFeatureFraction(self):
        """
        Returns:
            featureFraction: Feature fraction
        """
        return self.getOrDefault(self.featureFraction)
    
    
    def getFeaturesCol(self):
        """
        Returns:
            featuresCol: features column name
        """
        return self.getOrDefault(self.featuresCol)
    
    
    def getFeaturesShapCol(self):
        """
        Returns:
            featuresShapCol: Output SHAP vector column name after prediction containing the feature contribution values
        """
        return self.getOrDefault(self.featuresShapCol)
    
    
    def getFobj(self):
        """
        Returns:
            fobj: Customized objective function. Should accept two parameters: preds, train_data, and return (grad, hess).
        """
        return self.getOrDefault(self.fobj)
    
    
    def getGroupCol(self):
        """
        Returns:
            groupCol: The name of the group column
        """
        return self.getOrDefault(self.groupCol)
    
    
    def getImprovementTolerance(self):
        """
        Returns:
            improvementTolerance: Tolerance to consider improvement in metric
        """
        return self.getOrDefault(self.improvementTolerance)
    
    
    def getInitScoreCol(self):
        """
        Returns:
            initScoreCol: The name of the initial score column, used for continued training
        """
        return self.getOrDefault(self.initScoreCol)
    
    
    def getIsProvideTrainingMetric(self):
        """
        Returns:
            isProvideTrainingMetric: Whether output metric result over training dataset.
        """
        return self.getOrDefault(self.isProvideTrainingMetric)
    
    
    def getLabelCol(self):
        """
        Returns:
            labelCol: label column name
        """
        return self.getOrDefault(self.labelCol)
    
    
    def getLabelGain(self):
        """
        Returns:
            labelGain: graded relevance for each label in NDCG
        """
        return self.getOrDefault(self.labelGain)
    
    
    def getLambdaL1(self):
        """
        Returns:
            lambdaL1: L1 regularization
        """
        return self.getOrDefault(self.lambdaL1)
    
    
    def getLambdaL2(self):
        """
        Returns:
            lambdaL2: L2 regularization
        """
        return self.getOrDefault(self.lambdaL2)
    
    
    def getLeafPredictionCol(self):
        """
        Returns:
            leafPredictionCol: Predicted leaf indices's column name
        """
        return self.getOrDefault(self.leafPredictionCol)
    
    
    def getLearningRate(self):
        """
        Returns:
            learningRate: Learning rate or shrinkage rate
        """
        return self.getOrDefault(self.learningRate)
    
    
    def getMatrixType(self):
        """
        Returns:
            matrixType: Advanced parameter to specify whether the native lightgbm matrix constructed should be sparse or dense.  Values can be auto, sparse or dense. Default value is auto, which samples first ten rows to determine type.
        """
        return self.getOrDefault(self.matrixType)
    
    
    def getMaxBin(self):
        """
        Returns:
            maxBin: Max bin
        """
        return self.getOrDefault(self.maxBin)
    
    
    def getMaxBinByFeature(self):
        """
        Returns:
            maxBinByFeature: Max number of bins for each feature
        """
        return self.getOrDefault(self.maxBinByFeature)
    
    
    def getMaxDeltaStep(self):
        """
        Returns:
            maxDeltaStep: Used to limit the max output of tree leaves
        """
        return self.getOrDefault(self.maxDeltaStep)
    
    
    def getMaxDepth(self):
        """
        Returns:
            maxDepth: Max depth
        """
        return self.getOrDefault(self.maxDepth)
    
    
    def getMaxDrop(self):
        """
        Returns:
            maxDrop: Max number of dropped trees during one boosting iteration
        """
        return self.getOrDefault(self.maxDrop)
    
    
    def getMaxPosition(self):
        """
        Returns:
            maxPosition: optimized NDCG at this position
        """
        return self.getOrDefault(self.maxPosition)
    
    
    def getMetric(self):
        """
        Returns:
            metric: Metrics to be evaluated on the evaluation data.  Options are: empty string or not specified means that metric corresponding to specified objective will be used (this is possible only for pre-defined objective functions, otherwise no evaluation metric will be added). None (string, not a None value) means that no metric will be registered, aliases: na, null, custom. l1, absolute loss, aliases: mean_absolute_error, mae, regression_l1. l2, square loss, aliases: mean_squared_error, mse, regression_l2, regression. rmse, root square loss, aliases: root_mean_squared_error, l2_root. quantile, Quantile regression. mape, MAPE loss, aliases: mean_absolute_percentage_error. huber, Huber loss. fair, Fair loss. poisson, negative log-likelihood for Poisson regression. gamma, negative log-likelihood for Gamma regression. gamma_deviance, residual deviance for Gamma regression. tweedie, negative log-likelihood for Tweedie regression. ndcg, NDCG, aliases: lambdarank. map, MAP, aliases: mean_average_precision. auc, AUC. binary_logloss, log loss, aliases: binary. binary_error, for one sample: 0 for correct classification, 1 for error classification. multi_logloss, log loss for multi-class classification, aliases: multiclass, softmax, multiclassova, multiclass_ova, ova, ovr. multi_error, error rate for multi-class classification. cross_entropy, cross-entropy (with optional linear weights), aliases: xentropy. cross_entropy_lambda, intensity-weighted cross-entropy, aliases: xentlambda. kullback_leibler, Kullback-Leibler divergence, aliases: kldiv. 
        """
        return self.getOrDefault(self.metric)
    
    
    def getMinDataInLeaf(self):
        """
        Returns:
            minDataInLeaf: Minimal number of data in one leaf. Can be used to deal with over-fitting.
        """
        return self.getOrDefault(self.minDataInLeaf)
    
    
    def getMinGainToSplit(self):
        """
        Returns:
            minGainToSplit: The minimal gain to perform split
        """
        return self.getOrDefault(self.minGainToSplit)
    
    
    def getMinSumHessianInLeaf(self):
        """
        Returns:
            minSumHessianInLeaf: Minimal sum hessian in one leaf
        """
        return self.getOrDefault(self.minSumHessianInLeaf)
    
    
    def getModelString(self):
        """
        Returns:
            modelString: LightGBM model to retrain
        """
        return self.getOrDefault(self.modelString)
    
    
    def getNegBaggingFraction(self):
        """
        Returns:
            negBaggingFraction: Negative Bagging fraction
        """
        return self.getOrDefault(self.negBaggingFraction)
    
    
    def getNumBatches(self):
        """
        Returns:
            numBatches: If greater than 0, splits data into separate batches during training
        """
        return self.getOrDefault(self.numBatches)
    
    
    def getNumIterations(self):
        """
        Returns:
            numIterations: Number of iterations, LightGBM constructs num_class * num_iterations trees
        """
        return self.getOrDefault(self.numIterations)
    
    
    def getNumLeaves(self):
        """
        Returns:
            numLeaves: Number of leaves
        """
        return self.getOrDefault(self.numLeaves)
    
    
    def getNumTasks(self):
        """
        Returns:
            numTasks: Advanced parameter to specify the number of tasks.  SynapseML tries to guess this based on cluster configuration, but this parameter can be used to override.
        """
        return self.getOrDefault(self.numTasks)
    
    
    def getNumThreads(self):
        """
        Returns:
            numThreads: Number of threads for LightGBM. For the best speed, set this to the number of real CPU cores.
        """
        return self.getOrDefault(self.numThreads)
    
    
    def getObjective(self):
        """
        Returns:
            objective: The Objective. For regression applications, this can be: regression_l2, regression_l1, huber, fair, poisson, quantile, mape, gamma or tweedie. For classification applications, this can be: binary, multiclass, or multiclassova. 
        """
        return self.getOrDefault(self.objective)
    
    
    def getParallelism(self):
        """
        Returns:
            parallelism: Tree learner parallelism, can be set to data_parallel or voting_parallel
        """
        return self.getOrDefault(self.parallelism)
    
    
    def getPosBaggingFraction(self):
        """
        Returns:
            posBaggingFraction: Positive Bagging fraction
        """
        return self.getOrDefault(self.posBaggingFraction)
    
    
    def getPredictionCol(self):
        """
        Returns:
            predictionCol: prediction column name
        """
        return self.getOrDefault(self.predictionCol)
    
    
    def getRepartitionByGroupingColumn(self):
        """
        Returns:
            repartitionByGroupingColumn: Repartition training data according to grouping column, on by default.
        """
        return self.getOrDefault(self.repartitionByGroupingColumn)
    
    
    def getSkipDrop(self):
        """
        Returns:
            skipDrop: Probability of skipping the dropout procedure during a boosting iteration
        """
        return self.getOrDefault(self.skipDrop)
    
    
    def getSlotNames(self):
        """
        Returns:
            slotNames: List of slot names in the features column
        """
        return self.getOrDefault(self.slotNames)
    
    
    def getTimeout(self):
        """
        Returns:
            timeout: Timeout in seconds
        """
        return self.getOrDefault(self.timeout)
    
    
    def getTopK(self):
        """
        Returns:
            topK: The top_k value used in Voting parallel, set this to larger value for more accurate result, but it will slow down the training speed. It should be greater than 0
        """
        return self.getOrDefault(self.topK)
    
    
    def getUniformDrop(self):
        """
        Returns:
            uniformDrop: Set this to true to use uniform drop in dart mode
        """
        return self.getOrDefault(self.uniformDrop)
    
    
    def getUseBarrierExecutionMode(self):
        """
        Returns:
            useBarrierExecutionMode: Barrier execution mode which uses a barrier stage, off by default.
        """
        return self.getOrDefault(self.useBarrierExecutionMode)
    
    
    def getUseSingleDatasetMode(self):
        """
        Returns:
            useSingleDatasetMode: Use single dataset execution mode to create a single native dataset per executor (singleton) to reduce memory and communication overhead. Note this is disabled when running spark in local mode.
        """
        return self.getOrDefault(self.useSingleDatasetMode)
    
    
    def getValidationIndicatorCol(self):
        """
        Returns:
            validationIndicatorCol: Indicates whether the row is for training or validation
        """
        return self.getOrDefault(self.validationIndicatorCol)
    
    
    def getVerbosity(self):
        """
        Returns:
            verbosity: Verbosity where lt 0 is Fatal, eq 0 is Error, eq 1 is Info, gt 1 is Debug
        """
        return self.getOrDefault(self.verbosity)
    
    
    def getWeightCol(self):
        """
        Returns:
            weightCol: The name of the weight column
        """
        return self.getOrDefault(self.weightCol)
    
    
    def getXgboostDartMode(self):
        """
        Returns:
            xgboostDartMode: Set this to true to use xgboost dart mode
        """
        return self.getOrDefault(self.xgboostDartMode)

    def _create_model(self, java_model):
        try:
            model = LightGBMRankerModel(java_obj=java_model)
            model._transfer_params_from_java()
        except TypeError:
            model = LightGBMRankerModel._from_java(java_model)
        return model
    
    def _fit(self, dataset):
        java_model = self._fit_java(dataset)
        return self._create_model(java_model)

    
        