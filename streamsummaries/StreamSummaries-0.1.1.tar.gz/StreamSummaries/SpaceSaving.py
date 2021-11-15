class SpaceSaving:
    def __init__(self, size):
        self.size = size
        self.structure = []
        self.elements = {}

    def insert(self, element):
        if not self.is_full() and element not in self.elements:
            self.structure.append({'element': element, 'count': 1})
            self.elements[element] = len(self.structure) - 1
        elif self.is_full() and element not in self.elements:
            del self.elements[self.structure[-1]['element']]
            self.elements[element] = len(self.structure) - 1
            self.structure[-1] = {'element': element, 'count': self.structure[-1]['count'] + 1}
        elif element in self.elements:
            self.structure[self.elements[element]]['count'] += 1

        self.structure = sorted(self.structure, key=lambda x: x['count'], reverse=True)
        self.elements = {j['element']: i for i, j in enumerate(self.structure)}
        
    def is_full(self):
        return len(self.structure) == self.size

if __name__ == "__main__":
    ss = SpaceSaving(3)
    ss.insert('palavra1')
    ss.insert('palavra2')
    ss.insert('palavra3')
    ss.insert('palavra2')
    ss.insert('palavra3')
    ss.insert('palavra4')
    ss.insert('palavra5')
