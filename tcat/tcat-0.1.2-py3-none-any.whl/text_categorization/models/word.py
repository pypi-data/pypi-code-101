class CountedWord:

    def __init__(self, text, counted=1):
        super().__init__()
        self.text = text
        self.counted = counted
    
    def __add__(self, newWord):
        if self.text == newWord.text:
            self.counted += newWord.counted
            return self

class GroupedWord(CountedWord):

    def __init__(self, text, group, counted=1, documents=1):
        super().__init__(text, counted=counted)
        self.documents = documents
        self.group = group
    
    def __add__(self, newWord):
        if self.text == newWord.text:
            self.counted += newWord.counted
            self.documents += newWord.documents
            return self
    
    def __str__(self):
        return f"text: {self.text}, group: {self.group}, counted: {self.counted}, documents: {self.documents}"
