import pandas as pd

def getFile(fileName):
    '''
    Get file from the directory.
    '''
    return pd.read_csv(fileName)


file = getFile('players_21.csv')


def ages(file):
    ages = file['age']
    return ages.value_counts()


common_ages_count = ages(file)
common_ages_count.columns = ['Ages', 'Count']

