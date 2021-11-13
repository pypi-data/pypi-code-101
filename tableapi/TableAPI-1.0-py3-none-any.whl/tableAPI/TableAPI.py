# +-------------+------------------------+
# | Author      | Twitch                 |
# +-------------+------------------------+
# | Knuffeliger | twitch.tv/knufffeliger |
# +-------------+------------------------+

class ModernTable():

    def __init__(self, collumns: int, indexing: bool = False):
        if collumns < 1: raise ValueError('TableAPI: Collumns cannot be under 1')

        self.data = {
            'header': [],
            'rows': [],
            'y': 0,
            'x': collumns,
            'indexing': indexing,
            'indexing-type': 'programmer'
        }

        for i in range(collumns):
            self.data['header'].append('')

    def setIndexingType(self, iType: str):
        if iType == 'programmer':
            self.data['indexing-type'] = iType
        elif iType == 'normal':
            self.data['indexing-type'] = iType
        else: raise ValueError('TableAPI: Table#setIndexingType: Type not found! Only use "programmer" and "normal"')

    def readFromFile(self, path: str):
        try:
            f = open(path + '.table', 'r')
            f.close()
        except FileNotFoundError:
            raise ValueError('TableAPI: Table#readFromFile: File not found')
        
        f = open(path + '.table', 'r')

        self.data['y'] = 0
        self.data['rows'] = []

        locked = False

        for line in f.readlines():
            if not line.startswith('+'):
                line = line.replace(' | ', '|||').replace('| ', '').replace(' |', '').replace('\n', '')
                elements = line.split('|||')

                if not locked:
                    self.data['x'] = len(elements)
                    locked = True

                self.addRow(elements)

    def setHeader(self, *args):
        if len(args) == 0: raise ValueError('TableAPI: Table#addRow: You need at least one argument')
        list = type(args[0]) == type([1, 8, 7])

        if list:
            if len(args) != 1: raise ValueError('TableAPI: Table#addRow: In list mode you must have exactly one argument')
            l = args[0]
            if len(l) != self.data['x']: raise ValueError('TableAPI: Table#addRow: Argument length is not matching the collums length')
            rows = []

            for row in l:
                rows.append(row)
            
            self.data['header'] = args[0]

        else:
            if len(args) != self.data['x']: raise ValueError('TableAPI: Table#addRow: Argument length is not matching the collums length')
            rows = []

            for row in args:
                rows.append(row)
            
            self.data['header'] = args

    def addRow(self, *args):
        if len(args) == 0: raise ValueError('TableAPI: Table#addRow: You need at least one argument')
        list = type(args[0]) == type([1, 8, 7])

        if list:
            if len(args) != 1: raise ValueError('TableAPI: Table#addRow: In list mode you must have exactly one argument')
            l = args[0]
            if len(l) != self.data['x']: raise ValueError('TableAPI: Table#addRow: Argument length is not matching the collums length')
            rows = []

            for row in l:
                rows.append(row)
            
            self.data['rows'].append(rows)
            self.data['y'] += 1

        else:
            if len(args) != self.data['x']: raise ValueError('TableAPI: Table#addRow: Argument length is not matching the collums length')
            rows = []

            for row in args:
                rows.append(row)
            
            self.data['rows'].append(rows)
            self.data['y'] += 1
    
    def getRow(self, id: int):
        if id < 0 or id >= len(self.data['rows']): raise ValueError('TableAPI: Table#getRow: Row index not found (Remember the first object has the ID 0)')
        return self.data['rows'][id]
    
    def removeRow(self, id: int):
        if id < 0 or id >= len(self.data['rows']): raise ValueError('TableAPI: Table#getRow: Row index not found (Remember the first object has the ID 0)')
        del self.data['rows'][id]
        self.data['y'] -= 1
    
    def setItem(self, row: int, column: int, value: str):
        if row < 0 or row >= len(self.data['rows']): raise ValueError('TableAPI: Table#setItem: Row index not found (Remember the first object has the ID 0)')
        if column < 0 or column >= self.data['x']: raise ValueError('TableAPI: Table#setItem: Column index not found (Remember the first object has the ID 0)')

        self.data['rows'][row][column] = value

    def buildLine(self, length: int):
        s = ''
        for i in range(length): s += '-'
        return s

    def buildSpace(self, s: str, length: int):
        space = ''
        for i in range(length - len(s)):
            space += ' '
        return space

    def saveToFile(self, path: str):
        s = self.build(onlyString = True)
        f = open(path + '.table', 'w')
        f.write(s)
        f.close()

    def build(self, onlyString: bool = False):
        maxLens = []

        for x in range(self.data['x']):
            temp = 0
            for y in range(self.data['y']):
                row = self.getRow(y)[x]
                if len(row) > temp: temp = len(row)
            
            row = self.data['header'][x]
            if len(row) > temp: temp = len(row)

            maxLens.append(temp)

        table = []

        for item in self.data['rows']:
            itemS = ''
            i = 0

            for value in item:
                
                if i == 0: itemS += '| ' + value + self.buildSpace(value, maxLens[i])
                else: itemS += value + self.buildSpace(value, maxLens[i])

                if i + 1 != len(item):
                    itemS += ' | '
                    
                if i + 1 == len(item):
                    itemS += ' |'

                i += 1
            table.append(itemS)

        itemS = ''
        i = 0
        
        for value in self.data['header']:
                
            if i == 0: itemS += '| ' + value + self.buildSpace(value, maxLens[i])
            else: itemS += value + self.buildSpace(value, maxLens[i])

            if i + 1 != len(value):
                itemS += ' | '
                
            if i + 1 == len(value):
                itemS += ' |'

            i += 1

        header = itemS
        
        line = ''
        max_index_len = 0

        if self.data['indexing']:
            if len(str(self.data["y"])) > 2:
                line += f'+{self.buildLine(len(str(self.data["y"])) + 2)}'
                max_index_len = len(str(self.data["y"])) - 2
            else:
                line += f'+{self.buildLine(4)}'
                max_index_len = 0

            header = f'| ID{self.buildSpace("ID", max_index_len + 2)} {header}'


        for i in range(len(maxLens)):
            line += f'+{self.buildLine(maxLens[i] + 2)}'

            if i + 1 == len(maxLens): line += '+'

        indexing_index = 0

        if self.data['indexing-type'] == 'normal': indexing_index = 1
        if self.data['indexing-type'] == 'programmer': indexing_index = 0

        if onlyString:
            out = ''
            
            out += f'{line}\n'
            out += header
            out += f'{line}\n'

            for s in table:
                out += f'{s}\n'
            out += f'{line}'
            
            return out
        else:
            print(line)
            print(header)
            print(line)

            if self.data['indexing']:
                for s in table:
                    print(f'| {indexing_index}{self.buildSpace(str(indexing_index), max_index_len + 2)} {s}')
                    indexing_index += 1
            if not self.data['indexing']:
                for s in table:
                    print(s)
            if len(self.data['rows']) != 0: print(line)

class StaticTable():

    def __init__(self, collumns: int):
        if collumns < 1: raise ValueError('TableAPI: Collumns cannot be under 1')

        self.data = {
            'rows': [],
            'y': 0,
            'x': collumns
        }

    def readFromFile(self, path: str):
        try:
            f = open(path + '.table', 'r')
            f.close()
        except FileNotFoundError:
            raise ValueError('TableAPI: Table#readFromFile: File not found')
        
        f = open(path + '.table', 'r')

        self.data['y'] = 0
        self.data['rows'] = []

        locked = False

        for line in f.readlines():
            if not line.startswith('+'):
                line = line.replace(' | ', '|||').replace('| ', '').replace(' |', '').replace('\n', '')
                elements = line.split('|||')

                if not locked:
                    self.data['x'] = len(elements)
                    locked = True

                self.addRow(elements)


    def addRow(self, *args):
        if len(args) == 0: raise ValueError('TableAPI: Table#addRow: You need at least one argument')
        list = type(args[0]) == type([1, 8, 7])

        if list:
            if len(args) != 1: raise ValueError('TableAPI: Table#addRow: In list mode you must have exactly one argument')
            l = args[0]
            if len(l) != self.data['x']: raise ValueError('TableAPI: Table#addRow: Argument length is not matching the collums length')
            rows = []

            for row in l:
                rows.append(row)
            
            self.data['rows'].append(rows)
            self.data['y'] += 1

        else:
            if len(args) != self.data['x']: raise ValueError('TableAPI: Table#addRow: Argument length is not matching the collums length')
            rows = []

            for row in args:
                rows.append(row)
            
            self.data['rows'].append(rows)
            self.data['y'] += 1
    
    def getRow(self, id: int):
        if id < 0 or id >= len(self.data['rows']): raise ValueError('TableAPI: Table#getRow: Row index not found (Remember the first object has the ID 0)')
        return self.data['rows'][id]
    
    def removeRow(self, id: int):
        if id < 0 or id >= len(self.data['rows']): raise ValueError('TableAPI: Table#getRow: Row index not found (Remember the first object has the ID 0)')
        del self.data['rows'][id]
        self.data['y'] -= 1
    
    def setItem(self, row: int, column: int, value: str):
        if row < 0 or row >= len(self.data['rows']): raise ValueError('TableAPI: Table#setItem: Row index not found (Remember the first object has the ID 0)')
        if column < 0 or column >= self.data['x']: raise ValueError('TableAPI: Table#setItem: Column index not found (Remember the first object has the ID 0)')

        self.data['rows'][row][column] = value

    def buildLine(self, length: int):
        s = ''
        for i in range(length): s += '-'
        return s

    def buildSpace(self, s: str, length: int):
        space = ''
        for i in range(length - len(s)):
            space += ' '
        return space

    def saveToFile(self, path: str):
        s = self.build(onlyString = True)
        f = open(path + '.table', 'w')
        f.write(s)
        f.close()

    def build(self, onlyString: bool = False):
        maxLens = []

        for x in range(self.data['x']):
            temp = 0
            for y in range(self.data['y']):
                row = self.getRow(y)[x]
                if len(row) > temp: temp = len(row)

            maxLens.append(temp)

        table = []

        for item in self.data['rows']:
            itemS = ''
            i = 0

            for value in item:
                
                if i == 0: itemS += '| ' + value + self.buildSpace(value, maxLens[i])
                else: itemS += value + self.buildSpace(value, maxLens[i])

                if i + 1 != len(item):
                    itemS += ' | '
                    
                if i + 1 == len(item):
                    itemS += ' |'

                i += 1
            table.append(itemS)
        
        line = ''

        for i in range(len(maxLens)):
            line += f'+{self.buildLine(maxLens[i] + 2)}'

            if i + 1 == len(maxLens): line += '+'

        if onlyString:
            out = ''

            for s in table:
                out += f'{line}\n'
                out += f'{s}\n'
            out += f'{line}'
            
            return out
        else:
            for s in table:
                print(line)
                print(s)
            if len(self.data['rows']) != 0: print(line)

def GUI():
    try:
        import os

        os.system('cls')

        c = input('Collumns: ')
        table = StaticTable(int(c))

        while True:
            try:
                os.system('cls')
                table.build()
                commands = """+--------+-------------------------------------+
| Name   | Description                         |
+--------+-------------------------------------+
| add    | Add a Row                           |
| set    | Set an Item in a Row                |
| remove | Remove a Row                        |
| save   | Save the Table in a .table File     |
| load   | Load a .table File                  |
| exit   | Exit without saving in BACKUP.table |
+--------+-------------------------------------+ """
                print(commands)
                command = input('> ')

                if command == 'add':

                    formatS = ''

                    for i in range(table.xCount):
                        formatS += 'Obj: VALUE'
                        if i + 1 != table.xCount: formatS += ', '

                    cmd = input(f'({formatS}): ')
                    objs = cmd.split(', ')

                    if len(objs) != table.xCount:
                        input(f'You need exactly {table.xCount} Objects')
                    else:
                        table.addRow(objs)

                if command == 'remove':
                    cmd = input(f'(int: ROW_ID): ')

                    if not cmd.isdigit():
                        input(f'You need and int object')
                    
                    table.removeRow(int(cmd))

                if command == 'exit':
                    os.system('cls')

                    print('Good bye!')
                    exit()

                if command == 'set':
                    cmd = input(f'(int: ROW_ID, int: COLLUMN_ID, str: VALUE): ')
                    objs = cmd.split(', ')

                    if not objs[0].isdigit(): input(f'You need and int object at (-> int <-, int, str)')
                    if not objs[1].isdigit(): input(f'You need and int object at (int, -> int <-, str)')
                    
                    table.setItem(int(objs[0]), int(objs[1]), objs[2])
                
                if command == 'save':
                    name = input(f'(str: NAME): ')
                    table.saveToFile(name)
                
                if command == 'load':
                    name = input(f'(str: NAME): ')
                    table.readFromFile(name)

            except KeyboardInterrupt:
                table.saveToFile('BACKUP')
                exit()

    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    GUI()