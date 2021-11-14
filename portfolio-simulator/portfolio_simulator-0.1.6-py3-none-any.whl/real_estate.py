import numpy_financial as npf
import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class Asset:
    name: int
    value: int
    purchase_date: str
    sale_date: str

    @property
    def date_index(self):
        return pd.date_range(self.purchase_date, self.sale_date, freq="MS")

    def to_series(self):
        return pd.Series(self.value, index=self.date_index, name="principal")

    def to_dataframe(self):
        return self.to_series().to_frame()

    def single_events(self):
        return pd.Series(
            data={self.purchase_date: self.value, self.sale_date: -self.value},
            index=[self.purchase_date, self.sale_date],
        )


@dataclass
class Mortgage:
    """Holds parameters about a given mortgage and provides
    properties and method to access future cashflows and other
    realated information.

    Args:
        principal (int): original amount borrowed.
        rate (float): yearly rate (e.g. 0.01 for a 1% yearly rate).
        start_date (str): format YYYY-MM-DD (e.g. 2021-12-31)
        months (int): number of months this mortgage runs for.
    """

    principal: int
    rate: float
    start_date: str
    months: int

    @property
    def years(self) -> int:
        return self.months / 12

    @property
    def periods(self) -> np.array:
        return np.arange(self.months) + 1

    @property
    def ipmt(self) -> np.array:
        """Computes the interest portion of a payment."""
        return -npf.ipmt(self.rate / 12, self.periods, self.months, self.principal)

    @property
    def ppmt(self) -> np.array:
        """Computes the payment against loan principal."""
        return -npf.ppmt(self.rate / 12, self.periods, self.months, self.principal)

    @property
    def payment(self) -> np.array:
        """Computes the monthly payments."""
        return self.ipmt + self.ppmt

    @property
    def date_index(self):
        return pd.date_range(self.start_date, periods=self.months, freq="MS")

    def single_events(self):
        s = pd.Series({self.start_date: -self.principal}, index=[self.start_date])
        s.index = pd.to_datetime(s.index)
        s = s.add(self.to_dataframe().principal, fill_value=0)
        return s.reindex()

    def cashflows(self):
        return -self.to_dataframe().payment

    def to_dataframe(self):
        df = pd.DataFrame(
            {"interests": self.ipmt, "principal": self.ppmt, "payment": self.payment},
            index=self.date_index,
        )
        df["amount_due"] = self.principal - df.principal.cumsum()
        return df
