class Test:
    def __init__(self, typeDictionary, lenDictionary, accuracy):
        super().__init__()
        self.typeDictionary = typeDictionary
        self.lenDictionary = lenDictionary
        self.accuracy = accuracy
    
    def __str__(self):
        return f"{self.typeDictionary} Test\nLength: {self.lenDictionary}\nAccuracy: {self.accuracy}"
