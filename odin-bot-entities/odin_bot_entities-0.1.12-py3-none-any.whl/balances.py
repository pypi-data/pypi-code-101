import time
from datetime import datetime
from typing import Dict, List
from pydantic import BaseModel

from .wallet import Wallet
from .coin import Coin


class Balance(BaseModel):
    balance: Dict[str, Dict[str, float]]
    wallets: List[Wallet]
    time: float
    date: datetime
    name: str = "OdinBalance"

    @classmethod
    def from_wallets(cls, balance_coins: List[str],  wallets: List[Wallet], precision_dict: Dict[str, float]):
        try:
            balance_dict = {}
            for coin in balance_coins:
                balance_dict[coin] = {}
                coin_balances = [wallet[coin] for wallet in wallets]
                total = sum(coin_balances)
                balance_dict[coin]["Total"] = round(
                    total.amount, precision_dict[coin])

            return cls(
                balance=balance_dict,
                time=time.time(),
                date=datetime.now(),
                wallets=wallets,
            )
        except Exception as err:
            raise err

    def __str__(self):
        out = ""
        for name, value in self.balance.items():
            out += f"\t**{name}**: {value}"

        return out

    def is_unbalanced(self, balance_coins: List[str], minimum_to_trade_dict: Dict[str, float], rename_coin_dict: Dict[str, float]) -> List[Coin]:
        try:
            non_stable_coins = {
                coin_name: amount
                for coin_name, amount in self.balance.items()
                if coin_name in balance_coins
            }

            unbalanced = dict(
                filter(
                    lambda elem: abs(elem[1])
                    > minimum_to_trade_dict[
                        rename_coin_dict[elem[0]]
                    ],
                    non_stable_coins.items(),
                )
            )
            out = ""
            for name, amount in unbalanced.items():
                out += f"\t\t **{name}**: __{amount}__"
            return out

        except Exception as err:
            raise err
