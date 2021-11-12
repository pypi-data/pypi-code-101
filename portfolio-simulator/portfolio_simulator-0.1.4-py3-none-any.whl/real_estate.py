import numpy_financial as npf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dataclasses import dataclass

@dataclass
class Mortgage:
  principal: int
  rate: float
  start_date: str
  years: int
  linked_asset_value: int

  @property
  def per(self):
    return np.arange(self.years*12) + 1

  @property
  def ipmt(self):
    return npf.ipmt(self.rate/12, self.per, self.years*12, self.principal)

  @property
  def ppmt(self):
    return npf.ppmt(self.rate/12, self.per, self.years*12, self.principal)

  @property
  def payment(self):
    return self.ipmt + self. ppmt

  @property
  def months(self):
    return pd.date_range(self.start_date, periods=self.years*20, freq='M')

  def to_dataframe(self):
    df = pd.DataFrame({'interests':self.ipmt, 'principal': self.ppmt, 'payment': self.payment}, index=self.months)
    df['principal_left'] = self.principal + df.principal.cumsum()
    return df

