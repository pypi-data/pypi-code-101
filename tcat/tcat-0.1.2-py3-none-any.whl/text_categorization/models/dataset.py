import sys

from text_categorization.models.weightedDictionary import MBMWeightedDictionary, MMWeightedDictionary
from text_categorization.models.test import Test

class Dataset:

    def __init__(self, datasetName, pathTrain = "", pathTest = ""):
        super().__init__()
        self.name = datasetName

        if (pathTest == ""):
            self.testPath = f"{sys.path[0]}/data/{datasetName}/test"
        if (pathTrain == ""):
            self.trainPath = f"{sys.path[0]}/data/{datasetName}/train"

        self.trainGroups = []
        self.testGroups = []
        self.dictionaryWords = []
        self.fastReading = False
        self.datasetReaded = False
        self.mmWeightedDictionary: MMWeightedDictionary
        self.mbmWeightedDictionary: MBMWeightedDictionary

        self.resultMBMTest = []
        self.resultMMTest = []

    
    def readDataset(self, stopWords=[], headers=[], fastReading=False):
        if self.datasetReaded is False or fastReading != self.fastReading:
            for group in self.trainGroups:
                group.readDocuments(stopWords, headers, fastReading)
            for group in self.testGroups:
                group.readDocuments(stopWords, headers, fastReading)

            self.datasetReaded = True
            self.fastReading = fastReading
    
    def createDictionary(self):
        if self.datasetReaded is False:
            self.readDataset()

        self.mbmWeightedDictionary = MBMWeightedDictionary(self.trainGroups)
        self.mmWeightedDictionary = MMWeightedDictionary(self.trainGroups)

        for group in self.trainGroups:
            for word in group.dictionary.words:
                self.mbmWeightedDictionary.searchAndAddWord(word)
                self.mmWeightedDictionary.searchAndAddWord(word)

        self.mbmWeightedDictionary.cleanDictionary()
        self.mmWeightedDictionary.cleanDictionary()

        self.mbmWeightedDictionary.createParameters()
        self.mmWeightedDictionary.createParameters()

        self.mbmWeightedDictionary.setUpFeatureInformation()
        self.mmWeightedDictionary.setUpFeatureInformation()

    def startTest(self, maxLength = -1, kl = False):
        mbmDictionary, mmDictionary = self.__setSelectFeature__(maxLength, kl)

        currentTestedFiles = 0
        correctMBMPrediction = 0
        correctMMPrediction = 0

        for testGroup in self.testGroups:
            documentTested = 0
            for document in testGroup.documents:
                mbmWeights = mbmDictionary.classifyDictionary(document.dictionary)
                mmWeights = mmDictionary.classifyDictionary(document.dictionary)

                groupMBMPosition = 0
                groupMMPosition = 0
                minMBMWeight = mbmWeights[0]
                minMMWeight = mmWeights[0]

                for i in range(0, len(mbmWeights)):
                    if minMBMWeight > mbmWeights[i]:
                        minMBMWeight = mbmWeights[i]
                        groupMBMPosition = i
                    if minMMWeight > mmWeights[i]:
                        minMMWeight = mmWeights[i]
                        groupMMPosition = i
                    
                if self.trainGroups[groupMBMPosition].name == testGroup.name:
                    correctMBMPrediction += 1
                if self.trainGroups[groupMMPosition].name == testGroup.name:
                    correctMMPrediction += 1

                currentTestedFiles += 1
                documentTested += 1

        accuracyMBM = correctMBMPrediction / currentTestedFiles
        accuracyMM = correctMMPrediction / currentTestedFiles

        mbmTest = Test("MBM", len(mbmDictionary.words), accuracyMBM)
        self.resultMBMTest.append(mbmTest)

        mmTest = Test("MM", len(mmDictionary.words), accuracyMM)
        self.resultMMTest.append(mmTest)
        
        return mbmTest, mmTest 

    def __setSelectFeature__(self, maxLength, kl = False):
        if maxLength == -1:
            return self.mbmWeightedDictionary, self.mmWeightedDictionary

        cleanMBMDictionary = self.mbmWeightedDictionary.getCopy()
        cleanMMDictionary = self.mmWeightedDictionary.getCopy()

        cleanMMDictionary.klSelection = kl

        cleanMBMDictionary.featureSelection(maxLength)
        cleanMMDictionary.featureSelection(maxLength)

        cleanMBMDictionary.createParameters()
        cleanMMDictionary.createParameters()

        return cleanMBMDictionary, cleanMMDictionary

    def cleanTest(self):
        self.resultMBMTest = []
        self.resultMMTest = []
    
    def getTotalTrainDocuments(self):
        ris = 0
        for group in self.trainGroups:
            ris += len(group.documents)
        return ris
    
    def toString(self):
        string = f"Dataset: {self.name}\n"

        string += "Train Groups:\n"
        for trainGroup in self.trainGroups:
            string += trainGroup.toString()

        string += "Test Groups:\n"
        for testGroup in self.testGroups:
            string += testGroup.toString()
        
        return string

