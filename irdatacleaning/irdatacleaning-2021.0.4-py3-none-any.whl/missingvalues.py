import possible as possible

from encoder2 import Encoder
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
class MissingValues:
    def __init__(self, df, strategy = ["median"], columns = [],
                 columns_fill =[], fill_with = 0, round = True):
        self.df = df
        self.strategy = strategy
        self.columns = columns
        self.fill_with = fill_with
        self.column_location = {}
        self.round = round
        self.columns_fill = columns_fill
        self.column_check = lambda x: self.df[x].dtype !="object"
        self.rejected_columns = []
        self.size = [self.df[i].count() for i in self.df.columns]
    def check(self):
        self._filter()
    def _filter(self):
        count = 0
        possible_corrections = []
        max_size = max(self.size)
        for i in self.columns:
            if (self.column_check(i) is False):
                self.rejected_columns.append(i)
                self.columns.pop(count)
            count += 1
        for i in self.df.columns:
            if (self.column_check(i) is False and i is not self.columns and self.df[i].count() < max_size):
                possible_corrections.append(i)
        if (len(possible_corrections)>1):
            print("hello islander to help you out i have went ahead and looked through the rest of your dataset to check for\n"
                  "any other columns with missing values")
            user = input("enter yes to see what I have found")
if __name__ == "__main__":
    import pandas as pd
    from stringtodatetime import StringToDateTime
    data = pd.read_csv("/Users/williammckeon/Sync/youtube videos/novembers 2021/Parsing data/code/travel_times.csv",index_col=0)
    # data = pd.read_csv('https://raw.githubusercontent.com/jldbc/coffee-quality-database/master/data/arabica_data_cleaned.csv')
    # data = pd.read_csv("travel_times.csv")
    # print(type(data))
    # print(data.dtypes)
    stringtodate = StringToDateTime(data)
    data = stringtodate.check()
    # print(data.info())
    missing = MissingValues(data, columns=["AvgSpeed","FuelEconomy"])
    data = missing.check()

    # for i in data.columns:
    #     print(data[i].count())
    # # print(stringtodate.new_df.columns)