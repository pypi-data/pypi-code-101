import sys
import os
import pickle

from models.dataset import Dataset

def createDirIfNotExist(dir):

    if os.path.isdir(dir) is False:
        os.mkdir(dir)

def saveDataset(dataset: Dataset):

    dataPath = f"{sys.path[0]}/data/{dataset.name}/save/"
    datasetPath = f"{sys.path[0]}/data/{dataset.name}/save/{dataset.name}.pkl"

    createDirIfNotExist(dataPath)

    with open(datasetPath, "wb") as file:
        pickle.dump(dataset, file, pickle.HIGHEST_PROTOCOL)

def loadDataset(name):

    savedPath = f"{sys.path[0]}/data/{name}/save"
    if os.path.isdir(savedPath) is False:
        return None

    resultPath = f"{savedPath}/{name}.pkl"
    
    datasetFounded = False

    for datasetSaved in os.listdir(savedPath):
        if f"{name}.pkl" == datasetSaved:
            datasetFounded = True

    if datasetFounded == False:
        return None

    print(f"Loading dataset {name}")
    with open(resultPath, "rb") as file:
        return pickle.load(file)
