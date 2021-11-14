from sklearn.feature_extraction.text import CountVectorizer

from text_categorization.models.word import CountedWord
from text_categorization.models.dictionary import Dictionary

class Document:
    def __init__(self, name, path):
        super().__init__()
        self.name = name
        self.path = path
        self.dictionary = Dictionary()
        self.readedWords = []
        self.totalWords = 0
    
    def readWords(self, stopWords=[], headers=[], fastReading=False):
        self.dictionary.clean()

        file = open(self.path, 'r', encoding="ISO-8859-1")

        lines = file.readlines()

        if headers is not None:
            for line in lines:
                for header in headers:
                    if line.startswith(header):
                        lines.remove(line)

        if fastReading is False:
            vectorizer = CountVectorizer(stop_words=stopWords)
            x = vectorizer.fit_transform(lines)
            self.readedWords = vectorizer.get_feature_names()    
            self.totalWords = len(self.readedWords)
            
            for arrayLine in x.toarray():
                for i in range(0, len(arrayLine)):
                    if arrayLine[i] != 0:
                        self.dictionary.searchAndAddWord(CountedWord(self.readedWords[i], arrayLine[i]))
        else:
            words = []
            for line in lines:
                words += line.split()
            self.totalWords = len(words)
            for word in words:
                try:
                    wordInStopList = stopWords.index(word)
                except (ValueError, AttributeError):
                    self.dictionary.searchAndAddWord(CountedWord(word.lower()))
        
    
    def clearReadedWords(self):
        self.readedWords = []
