
from abstract import *


class Node:
    """
    A class used to represent the node of localPeriodicPatternTree
    ...
    Attributes:
    ----------
        item : int
            storing item of a node
        parent : node
            To maintain the parent of every node
        child : list
            To maintain the children of node
        nodeLink : node
            To maintain the next node of node
        tidList : set
            To maintain timestamps of node

    Methods:
    -------
        getChild(itemName)
            storing the children to their respective parent nodes
    """
    
    def __init__(self):
        self.item = -1
        self.parent = None
        self.child = []
        self.nodeLink = None
        self.tidList = set()

    def getChild(self, item):
        """
        :param item:
        :return: if node have node of item, then return it. if node don't have return []
        """
        for child in self.child:
            if child.item == item:
                return child
        return []


class Tree:
    """
        A class used to represent the frequentPatternGrowth tree structure

        ...
        Attributes:
        ----------
            root : node
                Represents the root node of the tree
            nodeLinks : dictionary
                storing last node of each item
            firstNodeLink : dictionary
                storing first node of each item

        Methods:
        -------
            addTransaction(transaction,timeStamp)
                creating transaction as a branch in frequentPatternTree
            fixNodeLinks(itemName, newNode)
                add newNode link after last node of item
            deleteNode(itemName)
                delete all node of item
            createPrefixTree(path,timeStampList)
                create prefix tree by path

    """
    def __init__(self):
        self.root = Node()
        self.nodeLinks = {}
        self.firstNodeLink = {}

    def addTransaction(self, transaction, tid):
        """
        add transaction into tree
            :param transaction: it represents the one transactions in database
            :type transaction: list
            :param tid: represents the timestamp of transaction
            :type tid: list or int
        """
        current = self.root
        for item in transaction:
            child = current.getChild(item)
            if not child:
                newNode = Node()
                newNode.item = item
                newNode.parent = current
                current.child.append(newNode)
                current = newNode
                self.fixNodeLinks(item, newNode)
            else:
                current = child
            current.tidList.add(tid)

    def fixNodeLinks(self, item, newNode):
        """
        fix node link
            :param item: it represents item name of newNode
            :type item: string
            :param newNode: it represents node which is added
            :type newNode: Node
        """
        if item in self.nodeLinks:
            lastNode = self.nodeLinks[item]
            lastNode.nodeLink = newNode
        self.nodeLinks[item] = newNode
        if item not in self.firstNodeLink:
            self.firstNodeLink[item] = newNode

    def deleteNode(self, item):
        """
        delete the node from tree
            :param item: it represents the item name of node
            :type item: str
        """
        deleteNode = self.firstNodeLink[item]
        parentNode = deleteNode.parent
        parentNode.child.remove(deleteNode)
        parentNode.child += deleteNode.child
        parentNode.tidList |= deleteNode.tidList
        for child in deleteNode.child:
            child.parent = parentNode
        while deleteNode.nodeLink:
            deleteNode = deleteNode.nodeLink
            parentNode = deleteNode.parent
            parentNode.child.remove(deleteNode)
            parentNode.child += deleteNode.child
            parentNode.tidList |= deleteNode.tidList
            for child in deleteNode.child:
                child.parent = parentNode

    def createPrefixTree(self, path, tidList):
        """
        create prefix tree by path
            :param path: it represents path to root from prefix node
            :type path: list
            :param tidList: it represents tid of each item
            :type tidList: list
        """
        currentNode = self.root
        for item in path:
            child = currentNode.getChild(item)
            if not child:
                newNode = Node()
                newNode.item = item
                newNode.parent = currentNode
                currentNode.child.append(newNode)
                currentNode = newNode
                self.fixNodeLinks(item, newNode)
            else:
                currentNode = child
            currentNode.tidList |= tidList


class LPPGrowth(localPeriodicPatterns):
    """

        Attributes:
        -----------
            iFile : str
                Input file name or path of the input file
            oFile : str
                Output file name or path of the output file
            maxPer : float
                User defined maxPer value.
            maxSoPer : float
                User defined maxSoPer value.
            minDur : float
                User defined minDur value.
            tsMin : int / date
                First time stamp of input data.
            tsMax : int / date
                Last time stamp of input data.
            startTime : float
                Time when start of execution the algorithm.
            endTime : float
                Time when end of execution the algorithm.
            finalPatterns : dict
                To store local periodic patterns and its PTL.
            tsList : dict
                To store items and its time stamp as bit vector.
            root : Tree
                It is root node of transaction tree of whole input data.
            PTL : dict
                Storing the item and its PTL.
            items : list
                Storing local periodic item list.
            sep: str
                separator used to distinguish items from each other. The default separator is tab space.


        Methods:
        -------
            findSeparator(line)
                Find the separator of the line which split strings.
            creteLPPlist()
                Create the local periodic patterns list from input data.
            createTSList()
                Create the tsList as bit vector from input data.
            generateLPP()
                Generate 1 length local periodic pattens by tsList and execute depth first search.
            createLPPTree()
                Create LPPTree of local periodic item from input data.
            patternGrowth(tree, prefix, prefixPFList)
                Execute pattern growth algorithm. It is important function in this program.
            calculatePTL(tsList)
                Calculate PTL from input tsList as integer list.
            calculatePTLbit(tsList)
                Calculate PTL from input tsList as bit vector.
            startMine()
                Mining process will start from here.
            getMemoryUSS()
                Total amount of USS memory consumed by the mining process will be retrieved from this function.
            getMemoryRSS()
                Total amount of RSS memory consumed by the mining process will be retrieved from this function.
            getRuntime()
                Total amount of runtime taken by the mining process will be retrieved from this function.
            getLocalPeriodicPatterns()
                return local periodic patterns and its PTL
            savePatterns(oFile)
                Complete set of local periodic patterns will be loaded in to a output file.
            getPatternsAsDataFrame()
                Complete set of local periodic patterns will be loaded in to a dataframe.

        Executing the code on terminal:
        ------------------------------
            Format:
                python3 LPPMGrowth.py <inputFile> <outputFile> <maxPer> <minSoPer> <minDur>
            Examples:
                python3 LPPMGrowth.py sampleDB.txt patterns.txt 0.3 0.4 0.5

                python3 LPPMGrowth.py sampleDB.txt patterns.txt 3 4 5

        Sample run of importing the code:
        --------------------------------

            from PAMI.localPeriodicPattern.basic import LPPGrowth as alg

            obj = alg.LPPGrowth(iFile, maxPer, maxSoPer, minDur)

            obj.startMine()

            localPeriodicPatterns = obj.getPatterns()

            print(f'Total number of local periodic patterns: {len(localPeriodicPatterns)}')

            obj.savePatterns(oFile)

            Df = obj.getPatternsAsDataFrame()

            memUSS = obj.getMemoryUSS()

            print(f'Total memory in USS: {memUSS}')

            memRSS = obj.getMemoryRSS()

            print(f'Total memory in RSS: {memRSS}')

            runtime = obj.getRuntime()

            print(f'Total execution time in seconds: {runtime})

        Credits:
        -------
            The complete program was written by So Nakamura under the supervision of Professor Rage Uday Kiran.
        """
    iFile = ' '
    oFile = ' '
    maxPer = str()
    maxSoPer = str()
    minDur = str()
    tsMin = 0
    tsMax = 0
    startTime = float()
    endTime = float()
    memoryUSS = float()
    memoryRSS = float()
    finalPatterns = {}
    tsList = {}
    root = Tree()
    PTL = {}
    items = []
    sep = ' '
    Database = []

    def creatingItemSets(self):
        """
            Storing the complete transactions of the database/input file in a database variable


        """
        self.Database = []
        if isinstance(self.iFile, pd.DataFrame):
            if self.iFile.empty:
                print("its empty..")
            i = self.iFile.columns.values.tolist()
            if 'Transactions' in i:
                self.Database = self.iFile['Transactions'].tolist()
            if 'Patterns' in i:
                self.Database = self.iFile['Patterns'].tolist()

        if isinstance(self.iFile, str):
            if validators.url(self.iFile):
                data = urlopen(self.iFile)
                for line in data:
                    line.strip()
                    line = line.decode("utf-8")
                    temp = [i.rstrip() for i in line.split(self.sep)]
                    temp = [x for x in temp if x]
                    self.Database.append(temp)
            else:
                try:
                    with open(self.iFile, 'r', encoding='utf-8') as f:
                        for line in f:
                            line.strip()
                            temp = [i.rstrip() for i in line.split(self.sep)]
                            temp = [x for x in temp if x]
                            self.Database.append(temp)
                except IOError:
                    print("File Not Found")
                    quit()

    def createLPPlist(self):
        """
        Create Local Periodic Pattern list from temporal data.
        """
        LPPList = {}
        PTL = {}
        start = {}
        tsPre = {}
        for line in self.Database:
            soPer = ' '
            self.tsMin = int(line.pop(0))
            ts = self.tsMin
            for item in line:
                if item in LPPList:
                    per = ts - tsPre[item]
                    if per <= self.maxPer and start == -1:
                        start = tsPre[item]
                        soPer = self.maxSoPer
                    if start != -1:
                        soPer = max(0, soPer + per - self.maxPer)
                        if soPer > self.maxSoPer:
                            if tsPre[item] - start[item] <= self.minDur:
                                PTL[item].add((start[item], tsPre[item]))
                                LPPList[item] = PTL[item]
                            start[item] = -1
                else:
                    tsPre[item] = ts
                    start[item] = -1
                    LPPList[item] = set()
            for line in self.Database:
                ts = int(line.pop(0))
                for item in line:
                    if item in LPPList:
                        per = ts - tsPre[item]
                        if per <= self.maxPer and start[item] == -1:
                            start[item] = tsPre[item]
                            soPer = self.maxSoPer
                        if start[item] != -1:
                            soPer = max(0, soPer + per - self.maxPer)
                            if soPer > self.maxSoPer:
                                PTL[item].add((start[item], tsPre[item]))
                                LPPList[item] = PTL[item]
                            start[item] = -1
                        tsPre[item] = ts
                    else:
                        tsPre[item] = ts
                        start[item] = -1
                        LPPList[item] = set()

    def createTSList(self):
        """
        Create tsList as bit vector from temporal data.
        """
        for line in self.Database:
            count = 1
            bitVector = 0b1 << count
            bitVector = bitVector | 0b1
            self.tsMin = int(line.pop(0))
            self.tsList = {item: bitVector for item in line}
            count += 1
            ts = ' '
            for line in self.Database:
                bitVector = 0b1 << count
                bitVector = bitVector | 0b1
                print(line)
                ts = line.pop(0)
                for item in line:
                    if self.tsList.get(item):
                        different = abs(bitVector.bit_length() - self.tsList[item].bit_length())
                        self.tsList[item] = self.tsList[item] << different
                        self.tsList[item] = self.tsList[item] | 0b1
                    else:
                        self.tsList[item] = bitVector
                count += 1
            self.tsMax = int(ts)
            for item in self.tsList:
                different = abs(bitVector.bit_length() - self.tsList[item].bit_length())
                self.tsList[item] = self.tsList[item] << different
            self.maxPer = (count - 1) * self.maxPer
            self.maxSoPer = (count - 1) * self.maxSoPer
            self.minDur = (count - 1) * self.minDur

    def generateLPP(self):
        """
        Generate local periodic items from bit vector tsList.
        """
        PTL = {}
        for item in self.tsList:
            PTL[item] = set()
            ts = list(bin(self.tsList[item]))
            ts = ts[2:]
            start = -1
            currentTs = 1
            soPer = ' '
            tsPre = ' '
            for t in ts[currentTs:]:
                if t == '0':
                    currentTs += 1
                    continue
                else:
                    tsPre = currentTs
                    currentTs += 1
                    break
            for t in ts[currentTs:]:
                if t == '0':
                    currentTs += 1
                    continue
                else:
                    per = currentTs - tsPre
                    if per <= self.maxPer and start == -1:
                        start = tsPre
                        soPer = self.maxSoPer
                    if start != -1:
                        soPer = max(0, soPer + per - self.maxPer)
                        if soPer > self.maxSoPer:
                            if tsPre - start >= self.minDur:
                                PTL[item].add((start, tsPre))
                            """else:
                                bitVector = 0b1 << currentTs
                                different = abs(self.tsList[item].bit_length() - bitVector.bit_length())
                                bitVector = bitVector | 0b1
                                bitVector = bitVector << different
                                self.tsList[item] = self.tsList[item] | bitVector"""
                            start = -1
                    tsPre = currentTs
                    currentTs += 1
            if start != -1:
                soPer = max(0, soPer + self.tsMax - tsPre - self.maxPer)
                if soPer > self.maxSoPer and tsPre - start >= self.minDur:
                    PTL[item].add((start, tsPre))
                """else:
                    bitVector = 0b1 << currentTs+1
                    different = abs(self.tsList[item].bit_length() - bitVector.bit_length())
                    bitVector = bitVector | 0b1
                    bitVector = bitVector << different
                    self.tsList[item] = self.tsList[item] | bitVector"""
                if soPer <= self.maxSoPer and self.tsMax - start >= self.minDur:
                    PTL[item].add((start, self.tsMax))
                """else:
                    bitVector = 0b1 << currentTs+1
                    different = abs(self.tsList[item].bit_length() - bitVector.bit_length())
                    bitVector = bitVector | 0b1
                    bitVector = bitVector << different
                    self.tsList[item] = self.tsList[item] | bitVector"""
        self.PTL = {k: v for k, v in PTL.items() if len(v) > 0}
        self.items = list(self.PTL.keys())

    def createLPPTree(self):
        """
        Create transaction tree of local periodic item from input data.
        """
        for line in self.Database:
            ts = int(line[0])
            tempTransaction = [item for item in line if item in self.items]
            transaction = sorted(tempTransaction, key=lambda x: len(self.PTL[x]), reverse=True)
            self.root.addTransaction(transaction, ts)
            for line in self.Database:
                tid = int(transaction.pop(0))
                tempTransaction = [item for item in transaction if item in self.items]
                transaction = sorted(tempTransaction, key=lambda x: len(self.PTL[x]), reverse=True)
                self.root.addTransaction(transaction, tid)

    def patternGrowth(self, tree, prefix, prefixPFList):
        """
        Create prefix tree and prefixPFList. Store finalPatterns and its PTL.
        :param tree: The root node of prefix tree.
        :type tree: Node or Tree
        :param prefix: Prefix item list.
        :type prefix: list
        :param prefixPFList: tsList of prefix patterns.
        :type prefixPFList: dict or list
        """
        items = list(prefixPFList)
        if not prefix:
            items = reversed(items)
        for item in items:
            prefixCopy = prefix.copy()
            prefixCopy.append(item)
            PFList = {}
            prefixTree = Tree()
            prefixNode = tree.firstNodeLink[item]
            tidList = prefixNode.tidList
            path = []
            currentNode = prefixNode.parent
            while currentNode.item != -1:
                path.insert(0, currentNode.item)
                currentNodeItem = currentNode.item
                if currentNodeItem in PFList:
                    PFList[currentNodeItem] |= tidList
                else:
                    PFList[currentNodeItem] = tidList
                currentNode = currentNode.parent
            prefixTree.createPrefixTree(path, tidList)
            while prefixNode.nodeLink:
                prefixNode = prefixNode.nodeLink
                tidList = prefixNode.tidList
                path = []
                currentNode = prefixNode.parent
                while currentNode.item != -1:
                    path.insert(0, currentNode.item)
                    currentNodeItem = currentNode.item
                    if currentNodeItem in PFList:
                        PFList[currentNodeItem] = PFList[currentNodeItem] | tidList
                    else:
                        PFList[currentNodeItem] = tidList
                    currentNode = currentNode.parent
                prefixTree.createPrefixTree(path, tidList)
            if len(prefixCopy) == 1:
                self.finalPatterns[prefixCopy[0]] = self.calculatePTLbit(self.tsList[item])
            else:
                self.finalPatterns[tuple(prefixCopy)] = self.calculatePTL(prefixPFList[item])
            candidateItems = list(PFList)
            for i in candidateItems:
                PTL = self.calculatePTL(PFList[i])
                if len(PTL) == 0:
                    prefixTree.deleteNode(i)
                    del PFList[i]
            if PFList:
                self.patternGrowth(prefixTree, prefixCopy, PFList)

    def calculatePTL(self, tsList):
        """
        Calculate PTL from input tsList as integer list/
        :param tsList: It is tsList which store time stamp as integer.
        :type tsList: list
        :return: PTL
        """
        start = -1
        PTL = set()
        tsList = sorted(tsList)
        tsPre = tsList[0]
        soPer = ' '
        for ts in tsList[1:]:
            per = ts - tsPre
            if per <= self.maxPer and start == -1:
                start = tsPre
                soPer = self.maxSoPer
            if start != -1:
                soPer = max(0, soPer + per - self.maxPer)
                if soPer > self.maxSoPer:
                    if tsPre - start >= self.minDur:
                        PTL.add((start, tsPre))
                    start = -1
            tsPre = ts
        if start != -1:
            soPer = max(0, soPer + self.tsMax - tsPre - self.maxPer)
            if soPer > self.maxSoPer and tsPre - start >= self.minDur:
                PTL.add((start, tsPre))
            if soPer <= self.maxSoPer and self.tsMax - start >= self.minDur:
                PTL.add((start, self.tsMax))
        return PTL

    def calculatePTLbit(self, tsList):
        """
        Calculate PTL from input tsList as bit vector.
        :param tsList: It is tsList which store time stamp as bit vector.
        :type tsList: list
        :return: PTL
        """
        tsList = list(bin(tsList))
        tsList = tsList[2:]
        start = -1
        currentTs = 1
        PTL = set()
        tsPre = ' '
        soPer = ' '
        for ts in tsList[currentTs:]:
            if ts == '0':
                currentTs += 1
                continue
            else:
                tsPre = currentTs
                currentTs += 1
                break
        for ts in tsList[currentTs:]:
            if ts == '0':
                currentTs += 1
                continue
            else:
                per = currentTs - tsPre
                if per <= self.maxPer and start == -1:
                    start = tsPre
                    soPer = self.maxSoPer
                if start != -1:
                    soPer = max(0, soPer + per - self.maxPer)
                    if soPer > self.maxSoPer:
                        if tsPre - start >= self.minDur:
                            PTL.add((start, tsPre))
                        start = -1
                tsPre = currentTs
                currentTs += 1
        if start != -1:
            soPer = max(0, soPer + self.tsMax - tsPre - self.maxPer)
            if soPer > self.maxSoPer and tsPre - start >= self.minDur:
                PTL.add((start, tsPre))
            if soPer <= self.maxSoPer and self.tsMax - start >= self.minDur:
                PTL.add((start, tsPre))
        return PTL

    def convert(self, value):
        """
        to convert the type of user specified minSup value
        :param value: user specified minSup value
        :return: converted type
        """
        if type(value) is int:
            value = int(value)
        if type(value) is float:
            value = (len(self.Database) * value)
        if type(value) is str:
            if '.' in value:
                value = float(value)
                value = (len(self.Database) * value)
            else:
                value = int(value)
        return value

    def startMine(self):
        """
        Mining process start from here.
        """
        self.startTime = time.time()
        self.finalPatterns = {}
        self.creatingItemSets()
        self.maxPer = self.convert(self.maxPer)
        self.maxSoPer = self.convert(self.maxSoPer)
        self.minDur = self.convert(self.minDur)
        self.createTSList()
        self.generateLPP()
        self.createLPPTree()
        self.patternGrowth(self.root, [], self.items)
        self.endTime = time.time()
        process = psutil.Process(os.getpid())
        self.memoryUSS = float()
        self.memoryRSS = float()
        self.memoryUSS = process.memory_full_info().uss
        self.memoryRSS = process.memory_info().rss

    def getMemoryUSS(self):
        """Total amount of USS memory consumed by the mining process will be retrieved from this function

        :return: returning USS memory consumed by the mining process
        :rtype: float
        """

        return self.memoryUSS

    def getMemoryRSS(self):
        """Total amount of RSS memory consumed by the mining process will be retrieved from this function

        :return: returning RSS memory consumed by the mining process
        :rtype: float
        """

        return self.memoryRSS

    def getRuntime(self):
        """Calculating the total amount of runtime taken by the mining process

        :return: returning total amount of runtime taken by the mining process
        :rtype: float
        """

        return self.endTime - self.startTime

    def getPatternsAsDataFrame(self):
        """Storing final local periodic patterns in a dataframe

        :return: returning local periodic patterns in a dataframe
        :rtype: pd.DataFrame
        """

        dataFrame = {}
        data = []
        for a, b in self.finalPatterns.items():
            data.append([a, b])
            dataFrame = pd.DataFrame(data, columns=['Patterns', 'PTL'])
        return dataFrame

    def savePatterns(self, outFile):
        """Complete set of local periodic patterns will be loaded in to a output file

        :param outFile: name of the output file
        :type outFile: file
        """
        self.oFile = outFile
        writer = open(self.oFile, 'w+')
        for x, y in self.finalPatterns.items():
            writer.write(f'{x} : {y}\n')
            # patternsAndPTL = x + ":" + y
            # writer.write("%s \n" % patternsAndPTL)

    def getPatterns(self):
        """ Function to send the set of local periodic patterns after completion of the mining process

        :return: returning frequent patterns
        :rtype: dict
        """
        return self.finalPatterns


if __name__ == '__main__':
    ap = str()
    if len(sys.argv) == 6 or len(sys.argv) == 7:
        if len(sys.argv) == 7:
            ap = LPPGrowth(sys.argv[1], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
        if len(sys.argv) == 6:
            ap = LPPGrowth(sys.argv[1], sys.argv[3], sys.argv[4], sys.argv[5])
        ap.startMine()
        Patterns = ap.getPatterns()
        print("Total number of Frequent Patterns:", len(Patterns))
        ap.savePatterns(sys.argv[2])
        memUSS = ap.getMemoryUSS()
        print("Total Memory in USS:", memUSS)
        memRSS = ap.getMemoryRSS()
        print("Total Memory in RSS", memRSS)
        run = ap.getRuntime()
        print("Total ExecutionTime in ms:", run)
    else:
        l = [0.004, 0.005, 0.006, 0.007, 0.008]
        for i in l:
            ap = LPPGrowth('https://www.u-aizu.ac.jp/~udayrage/datasets/temporalDatabases/temporal_T10I4D100K.csv'
                           , i, 0.01, 0.01)
            ap.startMine()
            Patterns = ap.getPatterns()
            print("Total number of Frequent Patterns:", len(Patterns))
            ap.savePatterns('/Users/Likhitha/Downloads/output')
            memUSS = ap.getMemoryUSS()
            print("Total Memory in USS:", memUSS)
            memRSS = ap.getMemoryRSS()
            print("Total Memory in RSS", memRSS)
            run = ap.getRuntime()
            print("Total ExecutionTime in ms:", run)
        print("Error! The number of input parameters do not match the total number of parameters provided")
