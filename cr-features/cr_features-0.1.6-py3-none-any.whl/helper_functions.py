import numpy as np
import pandas as pd


def convert_to2d(input, windowLength, overlap=0):
    """Convert input into 2d matrix with width = numCols. The last row is padded with zeros to match the other rows.

    Overlap has to be smaller than window length

    :param input: the one dimensional array
    :param windowLength: window length, expressed in number of samples
    :param overlap: Amount of overlap
    :return: 2D matrix
    """

    if windowLength <= overlap:
        raise Exception("Overlap has to be smaller than window length")

    inputWasList = True
    if type(input) != list:
        inputWasList = False
        input = input.tolist()

    out = [input[i: i + windowLength] for i in range(0, len(input), windowLength - overlap)]
    out[-1].extend([0] * (windowLength - len(out[-1])))
    return out if inputWasList else np.asarray(out)


def convert_to2d_time(input, timeThreshold):
    """ Convert input array into 2D matrix by time interval. When the timeThreshold is reached in each row,
        the process continues in the next row.

    :param input: the pandas dataframe with rows "time" and "data"
    :param timeThreshold: the threshold with which the row width is defined
    :return: 2D matrix
    """
    outData = [[]]
    outTime = [[]]
    startTime = 0

    for index, row in input.iterrows():
        t = row["time"]
        data = row["data"]

        if t - startTime >= timeThreshold:
            startTime = t
            outData.append([])
            outTime.append([])

        outData[-1].append(data)
        outTime[-1].append(t)

    return outData, outTime


def empatica1d_to_array(pathToEmpaticaCsvFile):
    """ Convert 1D empatica file to array

    :param pathToEmpaticaCsvFile: path to Empatica csv file
    :return: array of data, starting timestamp of data, sample rate of data
    """
    df = pd.read_csv(pathToEmpaticaCsvFile, names=["name"])
    startTimeStamp = df.name[0]
    sampleRate = df.name[1]
    df.drop([0, 1], inplace=True)
    data = df.name.ravel()
    return data, startTimeStamp, sampleRate


def empatica3d_to_array(pathToEmpaticaCsvFile):
    """ Convert 3D empatica file to array

    :param pathToEmpaticaCsvFile: path to Empatica csv file
    :return: array of data, starting timestamp of data, sample rate of data
    """
    df = pd.read_csv(pathToEmpaticaCsvFile, names=["x", "y", "z"])
    startTimeStamp = df.x[0]
    sampleRate = df.x[1]
    df.drop([0, 1], inplace=True)
    data = np.vstack((df.x.ravel(), df.y.ravel(), df.z.ravel()))
    return data, startTimeStamp, sampleRate


def checkForFeature(featureName, featureNames):
    return featureNames is None or featureName in featureNames


def checkForFeatures(featureList, featureNames):
    return featureNames is None or len(set(featureList) & set(featureNames))


def resample(df, f_from, f_to):
    n_from = len(df.columns)
    n_to = n_from * (f_to / f_from)
    ratio = n_from / n_to
    #print(n_from, f_to, f_from, n_to, ratio)#
    indices = [df.columns[int(x)] for x in np.arange(0,n_from-1, ratio)]
    return df[indices].copy()

frequency_features = ["fqHighestPeakFreqs", "fqHighestPeaks", "fqEnergyFeat", "fqEntropyFeat", "fqHistogramBins",
                         "fqAbsMean", "fqSkewness", "fqKurtosis", "fqInterquart"]

generic_features = ["autocorrelations", "countAboveMean", "countBelowMean", "maximum", "minimum", "meanAbsChange",
                       "longestStrikeAboveMean", "longestStrikeBelowMean", "stdDev", "median", "meanChange",
                       "numberOfZeroCrossings", "absEnergy", "linearTrendSlope", "ratioBeyondRSigma", "binnedEntropy",
                       "numOfPeaksAutocorr", "numberOfZeroCrossingsAutocorr", "areaAutocorr",
                       "calcMeanCrossingRateAutocorr", "countAboveMeanAutocorr", "sumPer", "sumSquared",
                       "squareSumOfComponent", "sumOfSquareComponents"]

accelerometer_features = ["meanLow", "areaLow", "totalAbsoluteAreaBand", "totalMagnitudeBand", "entropyBand",
                             "skewnessBand", "kurtosisBand", "postureDistanceLow", "absoluteMeanBand",
                             "absoluteAreaBand", "quartilesBand", "interQuartileRangeBand",
                             "varianceBand", "coefficientOfVariationBand", "amplitudeBand", "totalEnergyBand",
                             "dominantFrequencyEnergyBand", "meanCrossingRateBand", "correlationBand",
                             "quartilesMagnitudesBand",
                             "interQuartileRangeMagnitudesBand", "areaUnderAccelerationMagnitude", "peaksDataLow",
                             "sumPerComponentBand", "velocityBand", "meanKineticEnergyBand",
                             "totalKineticEnergyBand", "squareSumOfComponent", "sumOfSquareComponents",
                             "averageVectorLength", "averageVectorLengthPower", "rollAvgLow", "pitchAvgLow",
                             "rollStdDevLow", "pitchStdDevLow",
                             "rollMotionAmountLow", "rollMotionRegularityLow", "manipulationLow", "rollPeaks",
                             "pitchPeaks",
                             "rollPitchCorrelation"]

gyroscope_features = ["meanLow", "areaLow", "totalAbsoluteAreaLow", "totalMagnitudeLow", "entropyLow", "skewnessLow",
                         "kurtosisLow",
                         "quartilesLow", "interQuartileRangeLow", "varianceLow", "coefficientOfVariationLow",
                         "amplitudeLow",
                         "totalEnergyLow", "dominantFrequencyEnergyLow", "meanCrossingRateLow", "correlationLow",
                         "quartilesMagnitudeLow", "interQuartileRangeMagnitudesLow", "areaUnderMagnitude",
                         "peaksCountLow",
                         "averageVectorLengthLow", "averageVectorLengthPowerLow"]

gsr_features = ['mean', 'std', 'q25', 'q75', 'qd', 'deriv', 'power', 'numPeaks', 'ratePeaks', 'powerPeaks',
                   'sumPosDeriv', 'propPosDeriv', 'derivTonic', 'sigTonicDifference', 'freqFeats',
                   'maxPeakAmplitudeChangeBefore', 'maxPeakAmplitudeChangeAfter',
                   'avgPeakAmplitudeChangeBefore', 'avgPeakAmplitudeChangeAfter', 'avgPeakChangeRatio',
                   'maxPeakIncreaseTime', 'maxPeakDecreaseTime', 'maxPeakDuration', 'maxPeakChangeRatio',
                   'avgPeakIncreaseTime', 'avgPeakDecreaseTime', 'avgPeakDuration', 'maxPeakResponseSlopeBefore',
                   'maxPeakResponseSlopeAfter', 'signalOverallChange', 'changeDuration', 'changeRate',
                   'significantIncrease', 'significantDecrease']

hrv_features = ['meanHr', 'ibi', 'sdnn', 'sdsd', 'rmssd', 'pnn20', 'pnn50', 'sd', 'sd2', 'sd1/sd2', 'numRR']

slow_features = ["numberOfZeroCrossingsAutocorr", "areaAutocorr", "calcMeanCrossingRateAutocorr", "countAboveMeanAutocorr",
        "numOfPeaksAutocorr"]

medium_features = ["entropyBand", "dominantFrequencyEnergyBand", "totalEnergyBand", "peaksDataLow", "rollAvgLow",
          "rollStdDevLow", "rollMotionAmountLow", "rollMotionRegularityLow", "manipulationLow", "rollPeaks",
          "rollPitchCorrelation", "pitchAvgLow", "pitchStdDevLow", "pitchPeaks", "autocorrelations",
          "longestStrikeAboveMean", "longestStrikeBelowMean", "peaksCountLow", "dominantFrequencyEnergyLow",
          "totalEnergyLow", "entropyLow"]