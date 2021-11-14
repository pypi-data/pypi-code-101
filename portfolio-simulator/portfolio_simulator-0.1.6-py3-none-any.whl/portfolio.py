from dataclasses import dataclass
import pandas as pd


@dataclass
class Portfolio:
    assets: list
    mortgages: list

    def total_principal(self):
        s = pd.Series()
        for x in self.assets:
            s = s.add(x.single_events(), fill_value=0)
        for x in self.mortgages:
            s = s.add(x.single_events(), fill_value=0)
        s.index = pd.to_datetime(s.index)
        return s.reindex().resample("MS").sum().cumsum()


    def cashflows(self):
        s = pd.Series()
        for x in self.mortgages:
            s = s.add(x.cashflows(), fill_value=0)
        s.index = pd.to_datetime(s.index)
        return s.reindex().resample("MS").sum()

