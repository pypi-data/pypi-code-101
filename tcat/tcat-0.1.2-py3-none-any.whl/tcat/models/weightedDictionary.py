import math

from tcat.models.dictionary import Dictionary
from tcat.models.word import GroupedWord
from tcat.models.wordVector import WeightedWordVector, MBMWeightedWordVector, MMWeightedWordVector

# Abstract class not intended for direct usage
class WeightedDictionary(Dictionary):
    def __init__(self, groups):
        super().__init__()
        self.groups = groups
        self.startWeights = [0] * len(groups)

        self.activeInformation = []
        self.totalDocuments = 0
        self.totalClassDocuments = [0] * len(groups)
        self.totalWords = 0
        self.totalClassWords = [0] * len(groups)
    
    # for dictionary base class
    def __addWord__(self, w1, w2):
        w1.addWeight(w2)
        return w1
    
    def __insertWord__(self, index, newWord):
        self.words.insert(index, WeightedWordVector(self, newWord))

    # Training
    def createParameters(self):
        self.__setUpTotalWordsCount__()
        self.resetStartWeight()
        self.__setUpTotalWordsCount__()
        for word in self.words:
            word.updateWeights()
            self.__updateStartWeights__(word)
    
    def setUpFeatureInformation(self):
        return

    def __setUpTotalWordsCount__(self):
        self.totalDocuments = 0
        for i in range(0, len(self.groups)):
            self.totalDocuments += len(self.groups[i].documents)
            self.totalClassDocuments[i] = len(self.groups[i].documents)

        self.totalWords = 0
        self.totalClassWords = [0] * len(self.groups)
        for wordVector in self.words:
            for i in range(0, len(wordVector.groupVector)):
                groupedWord = wordVector.groupVector[i]
                if groupedWord != None:
                    self.totalWords += groupedWord.counted
                    self.totalClassWords[i] += groupedWord.counted

    def __getMutualInformationArray__(self):
        return []
        
    def resetStartWeight(self):        
        for i in range(0, len(self.startWeights)):
            self.startWeights[i] = 0
    
    def __updateStartWeights__(self, wordVector: WeightedWordVector):
        return

    def cleanDictionary(self):
        cleanedWords = []
        for i in range(0, len(self.words)):
            wordInDocuments = 0
            for groupedWord in self.words[i].groupVector:
                if groupedWord != None:
                    wordInDocuments += self.__cleanValueWord__(groupedWord)
            
            if wordInDocuments > 1:
                cleanedWords.append(self.words[i])
        removedWords = len(self.words) - len(cleanedWords)
        self.words = cleanedWords

    def __cleanValueWord__(self, groupedWord):
        return 0

    # Testing
    def featureSelection(self, maxLength):
        remainingWords = []

        print(f"Selecting feature for {self.__strTypeDictionary__()}")
        if len(self.activeInformation) < maxLength:
            maxLength = len(self.activeInformation)
        for i in range(0, maxLength):
            remainingWords.append(self.activeInformation[i][1])
        self.__setNewWordsVectors__(remainingWords)
    
    def __setNewWordsVectors__(self, words):
        self.words = []
        for word in words:
            exist, index = self.searchWord(word.text)
            self.words.insert(index, word)
            self.words[index].weightedDictionary = self

    def classifyDictionary(self, dictionary: Dictionary):
        resultWeights = []

        for i in range(0, len(self.groups)):
            resultWeights.append(self.startWeights[i])

        for word in dictionary.words:
            wordExist, index = self.searchWord(word.text)

            #TODO: Add here speed improvement
            if wordExist:
                for i in range(0, len(resultWeights)):
                    wordVector = self.words[index]
                    resultWeights[i] -= self.__getWeightOfClass__(wordVector, word, i)

        return resultWeights
    
    def __getWeightOfClass__(self, wordVector: WeightedWordVector, word:GroupedWord, classIndex):
        return 

    # Utils
    def getCopy(self):
        newDictionary = self.__createNewInstance__()
        for wordVector in self.words:
            newVector = wordVector.getCopy()
            newVector.weightedDictionary = newDictionary
            newDictionary.words.append(newVector)
        newDictionary.startWeights = self.startWeights
        newDictionary.activeInformation = self.activeInformation
        newDictionary.totalDocuments = self.totalDocuments
        newDictionary.totalClassDocuments = self.totalClassDocuments
        newDictionary.totalWords = self.totalWords
        newDictionary.totalWords = self.totalClassWords
        return newDictionary
    
    def __createNewInstance__(self):
        return WeightedDictionary(self.groups)

    def getSumOfCounted(self):
        ris = 0

        for word in self.words:
            ris += word.getSumOfCounted()
        
        return ris
    
    def __strTypeDictionary__(self):
        return "dictonary"

class MBMWeightedDictionary(WeightedDictionary):
    def __init__(self, groups):
        super().__init__(groups)

    def __insertWord__(self, index, newWord):
        self.words.insert(index, MBMWeightedWordVector(self, newWord))

    def __getWeightOfClass__(self, wordVector: WeightedWordVector, word:GroupedWord, classIndex):
        return math.log(wordVector.weights[classIndex]) - math.log(1 - wordVector.weights[classIndex])

    def setUpFeatureInformation(self):
        self.activeInformation = self.__getMutualInformationArray__()

    def __getMutualInformationArray__(self):
        mutualInformation = []

        for wordVector in self.words:
            mi = 0
            B = wordVector.getSumOfDocuments()

            for i in range(0, len(wordVector.groupVector)):
                groupedWord = wordVector.groupVector[i]
                A = 0
                if groupedWord is not None:
                    A = groupedWord.documents

                C = self.totalClassDocuments[i]
    
                n1 = A * self.totalDocuments
                n0 = (C - A) * self.totalDocuments
                d1 = B * C
                d0 = (self.totalDocuments - B) * C
                if A != 0:
                    mi += (A/self.totalDocuments) * math.log(n1/d1) 
                if C - A != 0:
                    mi += ((C-A) / self.totalDocuments) * math.log(n0/d0)

            mutualInformation.append([mi, wordVector])

        mutualInformation.sort(reverse=True, key=lambda tup:tup[0])
        return mutualInformation

    def __updateStartWeights__(self, wordVector: WeightedWordVector):
        for j in range(0, len(self.startWeights)):
            self.startWeights[j] -= math.log(1 - wordVector.weights[j])

    def __strTypeDictionary__(self):
        return "MBM dictonary"

    def __cleanValueWord__(self, groupedWord):
        return groupedWord.documents
    
    def __createNewInstance__(self):
        return MBMWeightedDictionary(self.groups)

class MMWeightedDictionary(WeightedDictionary):
    def __init__(self, groups):
        super().__init__(groups)
        self.klInformations = []
        self.klSelection = False
        self.mutualInformation = []

    def __insertWord__(self, index, newWord):
        self.words.insert(index, MMWeightedWordVector(self, newWord))

    def __getWeightOfClass__(self, wordVector: WeightedWordVector, word:GroupedWord, classIndex):
        wordCount = word.counted
        return wordCount * math.log(wordVector.weights[classIndex]) - math.log(math.factorial(wordCount)) 

    def setUpFeatureInformation(self):
        self.mutualInformation = self.__getMutualInformationArray__()
        self.klInformations = self.__getdKlArray__()

    def featureSelection(self, maxLength, personalizedInformation=None):
        if self.klSelection:
            self.activeInformation = self.klInformations
        else:
            self.activeInformation = self.mutualInformation

        return super().featureSelection(maxLength)

    def __getdKlArray__(self):
        dKL = []

        print(f"Calculating kl information for {self.__strTypeDictionary__()}")
        for wordVector in self.words:
            KLt = 0

            pOfWord = 0
            argLogKt = 0

            for i in range(0, len(wordVector.groupVector)):
                # KLt
                pOfC = self.totalClassDocuments[i] / self.totalDocuments
                groupedWord = wordVector.groupVector[i]
                # Kt
                pOfWord += pOfC * wordVector.weights[i]

                if groupedWord is not None:
                    KLt -= pOfC * wordVector.weights[i] * math.log(groupedWord.documents / self.totalClassDocuments[i])
                    argLogKt += groupedWord.documents / self.totalDocuments

            Kt = - pOfWord * math.log(argLogKt)
            KL = Kt - KLt
            dKL.append([KL, wordVector])

        dKL.sort(reverse=True, key=lambda tup:tup[0])
        return dKL


    def __getMutualInformationArray__(self):
        mutualInformation = []

        print(f"Calculating mutual information for {self.__strTypeDictionary__()}")
        for wordVector in self.words:
            mi = 0
            B = wordVector.getSumOfCounted()

            for i in range(0, len(wordVector.groupVector)):
                groupedWord = wordVector.groupVector[i]
                A = 0
                if groupedWord is not None:
                    A = groupedWord.counted

                C = self.totalClassWords[i]
    
                n = A * self.totalWords
                d = B * C
                if A != 0:
                    mi += (A/self.totalWords) * math.log(n/d) 
                
                n0 = (C - A) * self.totalWords
                d0 = (self.totalWords - B) * C
                if C - A != 0:
                    mi += ((C - A) / self.totalWords) * math.log(n0/d0)

            mutualInformation.append([mi, wordVector])
        
        mutualInformation.sort(reverse=True, key=lambda tup:tup[0])
        return mutualInformation


    def getCopy(self):
        mmDictionary = super().getCopy()
        mmDictionary.mutualInformation = self.mutualInformation
        mmDictionary.klInformations = self.klInformations
        mmDictionary.klSelection = self.klSelection
        return mmDictionary

    def __strTypeDictionary__(self):
        return "MM dictonary"

    def __cleanValueWord__(self, groupedWord):
        return groupedWord.counted

    def __createNewInstance__(self):
        return MMWeightedDictionary(self.groups)