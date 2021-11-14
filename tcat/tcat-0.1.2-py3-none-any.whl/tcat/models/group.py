from tcat.models.word import CountedWord, GroupedWord
from tcat.models.dictionary import Dictionary

class Group:
    def __init__(self, name, path, type):
        super().__init__()
        self.name = name
        self.path = path
        self.type = type

        self.dictionary = Dictionary()
        self.documents = []

        self.totalCountedWords = 0
    
    def readDocuments(self, stopWords=[], headers=[], fastReading=False):
        self.dictionary.clean()

        for document in self.documents:
            document.readWords(stopWords, headers, fastReading)

            for word in document.dictionary.words:
                self.dictionary.searchAndAddWord(GroupedWord(word.text, self, word.counted, 1))
            
            document.clearReadedWords()
        self.setTotalCountedWords()
        
    def setTotalCountedWords(self):
        self.totalCountedWords = 0
        for word in self.dictionary.words:
            self.totalCountedWords += word.counted

    def __str__(self):
        return f"Group: {self.name}"
