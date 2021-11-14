import sys
import os
import argparse

from prettytable import PrettyTable

from importing import startImport
from factory.datasetFactory import createDataset
from result import plotWordsCountForAllDocuments, plotTestResult
from saving import saveDataset, loadDataset
from dataloss import analyzeLostWords
from util.colors import bcolors
from models.test import Test

def loadOrCreateDataset(args):
    dataset = loadDataset(args.name[0])
    if dataset is None:
        dataset = createDataset(args.name[0])

    return dataset

def startLearning(args):
    if args.name is None:
        print(bcolors.FAIL + "Name must be provided!" + bcolors.ENDC)
        return
    dataset = loadOrCreateDataset(args)

    dataset.readDataset(args.stop_words, args.headers, args.fast_reading)
    dataset.createDictionary()
    saveDataset(dataset)
    print(bcolors.OKGREEN + "Done learning!" + bcolors.ENDC)

def printDatasets(args):
    dataDir = f"{sys.path[0]}/data"
    if os.path.isdir(dataDir) is False:
        print(bcolors.WARNING + "No datasets avaiable" + bcolors.ENDC)
        return
    table = PrettyTable()
    table.field_names = ["Datasets"]
    for file in os.listdir(dataDir):
        table.add_row([file])
    print(table)


def importData(args):
    if args.path is None:
        print(bcolors.FAIL + "Import path must be provided!" + bcolors.ENDC)
    dataPath = sys.path[0] + "/data"
    if os.path.isdir(dataPath) is False:
        os.mkdir(dataPath)

    x = PrettyTable()
    x.field_names = ["Category", "#dirs"]

    totData = 0
    print(args.path[0])
    for dir in os.listdir(args.path[0]):
        if os.path.isdir(f"{args.path[0]}/{dir}"):
            nData = len(os.listdir(f"{args.path[0]}/{dir}"))
            totData += nData
            x.add_row([dir, str(nData)])

    print(x)
    print("Dimension of dataset(in files):" + str(totData))
    startImport(args)
    print(bcolors.OKGREEN + "Data imported!" + bcolors.ENDC)

def startTesting(args):
    if args.name is None:
        print(bcolors.FAIL + "Name must be provided!" + bcolors.ENDC)
        return

    dataset = loadOrCreateDataset(args)

    if dataset.datasetReaded is False:
        print(bcolors.FAIL + f"Dataset must learned first!" + bcolors.ENDC)
        return
    
    testLengths = []
    if args.feature_length is None:
        testLengths.append(-1)
    else:
        testLengths = args.feature_length
    
    dataset.cleanTest()
    testResults = []

    i = 1
    for featureLength in testLengths:
        mbmTest, mmTest = dataset.startTest(featureLength, args.kl_feature)
        testResults.append(mbmTest)
        testResults.append(mmTest)
        print(bcolors.OKGREEN + f"Done testing {i}/{len(testLengths)}" + bcolors.ENDC)
        i += 1
    
    print(bcolors.OKGREEN + "Testing done!" + bcolors.ENDC)
    for test in testResults:
        print(str(test))
    
    saveDataset(dataset)

def plotResult(args):
    if args.name is None:
        print(bcolors.FAIL + "Name must be provided!" + bcolors.ENDC)
        return

    dataset = loadOrCreateDataset(args)
    plotTestResult(dataset)

   
commands = {
    'import-data': importData,
    'start-learning': startLearning,
    'show-datasets': printDatasets,
    'start-testing': startTesting,
    'plot-result': plotResult
}


def main():
    print('Welcome to Naive text classifier main program!')
    print('developed by Lorenzo Adreani')
    parser = argparse.ArgumentParser(prog='text-categorization', description="Text-categorization")

    parser.add_argument('command', choices=commands.keys(), metavar='command',
                        help=f'Commands avaiable: {str(commands.keys())}')
    parser.add_argument('-s', '--split', nargs='?', const=0.2, type=float, 
                        help='Split the dataset path into train and test default ratio 0.2 (80:20)')
    parser.add_argument('-p', '--path', nargs=1, type=str, metavar='dataset-path',
                        help='Path to the folder of the dataset destination')
    parser.add_argument('-n', '--name', nargs=1, type=str, metavar='dataset-name', 
                        help='Name of the dataset selected')
    parser.add_argument('-sw', '--stop-words', nargs='+', type=str, help='set the stop words for reading')
    parser.add_argument('-he', '--headers', nargs='+', type=str, help='set the headers to remove for reading')
    parser.add_argument('-fl', '--feature-length', nargs='+', type=int, metavar='feature-length', 
                        help='Choose the length of vocabulary for test')
    parser.add_argument('-fr', '--fast-reading', action="store_const", const=True, default=False, help='Set the fast reading when learning. This action remove tokenization')
    parser.add_argument('-kl', '--kl-feature', action="store_const", const=True, default=False, 
                        help="Use the kl feature selection for the multinomial model")

    args = parser.parse_args()

    command = commands.get(args.command)
    command(args)


main()
