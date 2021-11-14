from models.dataset import Dataset

def analyzeLostWords(dataset: Dataset):
    readedWordsCounted = 0
    wordCounted = 0
    groupedCounted = 0
    weightCounted = dataset.weightedDictionary.getSumOfCounted()

    for group in dataset.trainGroups:
        for document in group.documents:
            readedWordsCounted += document.totalWords
            wordCounted += document.dictionary.getSumOfCounted()
        
        groupedCounted += group.dictionary.getSumOfCounted()
    
    accuracy_in_1 = readedWordsCounted  /   wordCounted
    accuracy_at_2 = readedWordsCounted  /   groupedCounted
    accuracy_in_2 = wordCounted         /   groupedCounted       
    accuracy_at_3 = readedWordsCounted  /   weightCounted
    accuracy_in_3 = groupedCounted      /   weightCounted    

    print(f"losses in and at stage 1:   {(1 - accuracy_in_1) * 100}%")
    print(f"losses at stage 2:          {(1 - accuracy_at_2) * 100}%")
    print(f"losses in stage 2:          {(1 - accuracy_in_2) * 100}%")
    print(f"losses at stage 3:          {(1 - accuracy_at_3) * 100}%")
    print(f"losses in stage 3:          {(1 - accuracy_in_3) * 100}%")

    print(f"******************************************************************")
    print(f"Sp {readedWordsCounted}; Wc {wordCounted}; Gc {groupedCounted}; F {weightCounted}")
    print(f"******************************************************************")