from text_categorization.models.word import CountedWord

class Dictionary:
    def __init__(self):
        super().__init__()
        self.words = []

    def searchWord(self, text):
        if len(self.words) == 0:
            return False, 0

        l = 0
        r = len(self.words) - 1
        i = int((r + l) / 2)
        while l <= r:
            if self.words[i].text == text:
                return True, i
            elif self.words[i].text > text:
                r = i - 1
            else:
                l = i + 1
            i = int((r + l) / 2)

        if self.words[i].text < text:
            i += 1

        return False, i
    

    def searchAndAddWord(self, newWord: CountedWord):
        founded, index = self.searchWord(newWord.text)
        if founded:
            self.__addWord__(self.words[index], newWord)
        else:
            self.__insertWord__(index, newWord)

    def __addWord__(self, w1, w2):
        w1 = w1 + w2

    def __insertWord__(self, index, newWord):
        self.words.insert(index, newWord)

    def getSumOfCounted(self):
        ris = 0

        for word in self.words:
            ris += word.counted
        
        return ris

    def clean(self):
        self.words = []
    