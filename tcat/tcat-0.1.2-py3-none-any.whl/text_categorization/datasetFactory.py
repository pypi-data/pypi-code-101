import os
import sys

from threading import Thread, Lock, Event
from time import time, sleep
from queue import Queue

from text_categorization.models.dataset import Dataset
from text_categorization.models.group import Group
from text_categorization.models.document import Document

def createDataset(datasethName):
    dataset = Dataset(datasethName)
    groupQueue = Queue()

    for groupName in os.listdir(dataset.trainPath):
        trainGroup = Group(groupName, f"{dataset.trainPath}/{groupName}" , "train")
        testGroup = Group(groupName, f"{dataset.testPath}/{groupName}", "test")

        dataset.trainGroups.append(trainGroup)
        dataset.testGroups.append(testGroup)

        groupQueue.put(trainGroup)
        groupQueue.put(testGroup)
    
    threads = []
    maxThreads = 16

    for i in range(0, maxThreads):
        t = Thread(target=createDocumentsForGroup, args=(groupQueue,))
        t.start()
        threads.append(t)

    for i in range(0, maxThreads):
        threads[i].join()
    
    print("dataset created")
    
    return dataset
    
def createDocumentsForGroup(groupQueue: Queue):
    while not groupQueue.empty():
        group = groupQueue.get()
        print(f"Creating group {group.name} for {group.type}...")
        nameDirs = os.listdir(group.path)
        print(f"Total documents for {group.name}-{group.type}: {len(nameDirs)}")
        for fileName in nameDirs:
            doc = Document(fileName, f"{group.path}/{fileName}")
            group.documents.append(doc)
        print(f"Done creating group {group.name}-{group.type}!\nDocument size:{len(group.documents)}")

