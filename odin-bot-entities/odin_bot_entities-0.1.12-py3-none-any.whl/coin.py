
from pydantic import BaseModel


class Coin(BaseModel):
    name: str
    amount: float
    precision: int = 8

    def __add__(self, other):
        amount = round(self.amount + other.amount, self.precision)
        return Coin(name=self.name, amount=amount)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __rmul__(self, sign: int):
        return Coin(name=self.name, amount=self.amount * sign)

    def __abs__(self):
        return Coin(name=self.name, amount=abs(self.amount))

    def __str__(self):
        out = ""
        out += f"\t\t **{self.name}**: {self.amount} ({self.precision})"
        return out
