import matplotlib.pyplot as plt

from models.dataset import Dataset
from models.word import GroupedWord
from setting import Setting

# TODO: Need to be updated
def plotWordsCountForAllDocuments(dataset: Dataset):
    plt.style.use('dark_background')

    wordCounted = []
    wordDocument = []

    words = []
    maxCountedWord: GroupedWord
    maxDocumentWord: GroupedWord

    for group in dataset.trainGroups:
        print(f"group {group.name} words: {len(group.dictionary.words)}")

        for word in group.dictionary.words:
            words.append(word)

    maxCounted = 0
    maxDocument = 0
    for word in words:
        if maxCounted < word.counted:
            maxCounted = word.counted
            maxCountedWord = word
        if maxDocument < word.documents:
            maxDocument = word.documents
            maxDocumentWord = word
    
    for i in range(0, maxCounted + 1):
        wordCounted.append(0)
    
    for i in range(0, maxDocument + 1):
        wordDocument.append(0)

    for word in words:
        wordCounted[word.counted] += 1
        wordDocument[word.documents] += 1  
    
    print(f"most counted word: {maxCountedWord.text}, counted: {maxCountedWord.counted}, documents: {maxCountedWord.documents}")
    print(f"most document word: {maxDocumentWord.text}, counted: {maxDocumentWord.counted}, documents: {maxDocumentWord.documents}")
    
    plt.title("Results")

    plt.subplot(1, 2, 1)
    plt.plot(wordCounted, "bx")
    plt.ylabel('Number of words with x counted')
    plt.xlabel('Number of count')

    plt.subplot(1, 2, 2)
    plt.plot(wordDocument, "rx")
    plt.ylabel('Number of words with x documents')
    plt.xlabel('Number of document')
    plt.show()

    print("Plot created")

def plotTestResult(dataset):
    plt.style.use('dark_background')
    mbm = []
    for mbmTest in dataset.resultMBMTest:
        mbm.append([mbmTest.lenDictionary, mbmTest.accuracy])
    mm = []
    for mmTest in dataset.resultMMTest:
        mm.append([mmTest.lenDictionary, mmTest.accuracy])

    mbm.sort(key=lambda tup:tup[0])
    mm.sort(key=lambda tup:tup[0])

    mbmY = []
    mbmX = []
    mmY = []
    mmX = []

    for test in mbm:
        mbmX.append(test[0])
        mbmY.append(test[1] * 100)
    for test in mm:
        mmX.append(test[0])
        mmY.append(test[1] * 100)


    plt.plot(mbmX, mbmY, "ro-", label="Multi-variate Bernulli")
    plt.plot(mmX, mmY, "b^-", label="Multinomial")
    plt.ylim(0, 100)
    plt.title(dataset.name)
    plt.xlabel("Vocabulary Size")
    plt.ylabel("Classification Accuracy")
    plt.xscale("log")
    plt.legend()
    plt.show()