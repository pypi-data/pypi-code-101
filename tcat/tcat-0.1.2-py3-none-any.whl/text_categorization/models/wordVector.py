from text_categorization.models.word import GroupedWord

# Abstract class not intended for direct usage
class WeightedWordVector:

    def __init__(self, weightedDictionary, word: GroupedWord = None):
        super().__init__()
        if word is not None:
            self.text = word.text 
        self.groupVector = [None] * len(weightedDictionary.groups)
        self.weights = [0] * len(weightedDictionary.groups)
        self.weightedDictionary = weightedDictionary

        if word is not None:
            self.addWeight(word)

    def addWeight(self, word: GroupedWord):
        for i in range(0, len(self.weightedDictionary.groups)):
            if word.group == self.weightedDictionary.groups[i]:
                if self.groupVector[i] == None:
                    self.groupVector[i] = word
                else:
                    self.groupVector[i] += word

    def updateWeights(self):
        for i in range(0, len(self.groupVector)):
            self.weights[i] = self.__createWordWeight__(self.groupVector[i], i)

    def getCopy(self):
        copy = self.__createNewInstance__()
        copy.text = self.text
        copy.groupVector = self.groupVector
        copy.weights = self.weights
        return copy


    def __createNewInstance__(self):
        return WeightedWordVector(self.weightedDictionary)
    
    def __createWordWeight__(self, groupedWord: GroupedWord, groupIndex):
        return 0
        
    def __str__(self):
        
        ris = f"word: {self.text}, weights: ["
        for group in self.groupVector:
            ris += f"{str(group)},"
        ris += "]"

        return ris

    def getSumOfDocuments(self):
        ris = 0
        for word in self.groupVector:
            if word is not None:
                ris += word.documents
        return ris

    def getSumOfCounted(self):
        ris = 0
        for word in self.groupVector:
            if word is not None:
                ris += word.counted
        return ris

class MBMWeightedWordVector(WeightedWordVector):
    def __init__(self, dictionary, word = None):
        super().__init__(dictionary, word)
    
    def __createNewInstance__(self):
        return MBMWeightedWordVector(self.weightedDictionary)

    def __createWordWeight__(self, groupedWord: GroupedWord, groupIndex):
        denominator = 2 + self.weightedDictionary.totalClassDocuments[groupIndex]
        if groupedWord != None:
            return (1 + groupedWord.documents) / denominator
        else:
            return 1 / denominator

class MMWeightedWordVector(WeightedWordVector):
    def __init__(self, dictionary, word = None):
        super().__init__(dictionary, word)

    def __createNewInstance__(self):
        return MMWeightedWordVector(self.weightedDictionary)

    def __createWordWeight__(self, groupedWord: GroupedWord, groupIndex):
        denominator = len(self.weightedDictionary.words) + self.weightedDictionary.totalClassWords[groupIndex]
        if groupedWord != None:
            return (1 + groupedWord.counted) / denominator
        else:
            return 1 / denominator