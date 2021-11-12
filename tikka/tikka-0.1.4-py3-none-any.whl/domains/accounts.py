# Copyright 2021 Vincent Texier <vit@free.fr>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
from pathlib import Path
from typing import Optional

from mnemonic import Mnemonic

from tikka.adapters.database import Database
from tikka.adapters.wallets import Wallet, Wallets
from tikka.data.account import TABLE_NAME, Account
from tikka.data.constants import MNEMONIC_LANGUAGES
from tikka.data.pubkey import PublicKey
from tikka.data.signing_key import TikkaSigningKey
from tikka.libs.dewif import DEWIF_CURRENCY_CODE_G1, DEWIF_CURRENCY_CODE_G1_TEST


class Accounts:

    list: list = []
    current_account: Optional[Account] = None

    """
    Account domain class
    """

    def __init__(self, database: Database, wallets: Wallets, language: str):
        """
        Init Accounts domain

        :param database: Database adapter instance
        :param wallets: Wallets adapter instance
        :param language: Language for mnemonic

        """
        self.database = database
        self.wallets = wallets
        self.language = language

        # init account list from database
        self.init_accounts()

    def init_accounts(self, database: Optional[Database] = None):
        """
        Init accounts from currency database connection

        :param database: New currency Database instance (default=None)
        :return:
        """
        if database is not None:
            self.database = database
        # reset current account
        self.current_account = None

        # get accounts from database
        result_set = self.database.select("SELECT * FROM accounts")
        self.list = []
        for row in result_set:
            self.list.append(Account(*row))

        # set current selected account
        for account in self.list:
            if account.selected:
                self.current_account = account

    def unselect_all(self):
        """
        Unselect all accounts

        :return:
        """
        # unselect other accounts
        for other_account in self.list:
            other_account.selected = False

        self.database.update(TABLE_NAME, "1", selected=False)

    def add_account(self, account: Account):
        """
        Add account action

        :param account: Account instance
        :return:
        """
        # add account
        self.list.append(account)
        self.current_account = account

        # insert only non hidden fields
        self.database.insert(
            TABLE_NAME,
            **{
                key: value
                for (key, value) in account.__dict__.items()
                if not key.startswith("_")
            },
        )

    def update_account(self, account: Account):
        """
        Update account in database

        :param account: Account instance
        :return:
        """
        # update only non hidden fields
        self.database.update(
            TABLE_NAME,
            f"pubkey='{account.pubkey}'",
            **{
                key: value
                for (key, value) in account.__dict__.items()
                if not key.startswith("_")
            },
        )

    def select_account_by_index(self, index: int) -> Account:
        """
        Select and return account instance

        :param index: Index in account list
        :return:
        """
        result = self.list[0]

        # unselect all applications accounts
        for account in self.list:
            if account == self.list[index]:
                account.selected = True
                self.current_account = account
                self.unselect_all()
                self.update_account(account)
                result = account
            else:
                account.selected = False

        return result

    def delete_account(self, account: Account):
        """
        Delete account in list and database

        :param account: Account instance to delete
        :return:
        """
        index = self.list.index(account)
        del self.list[index]

        if account == self.current_account:
            if len(self.list) > 0:
                self.select_account_by_index(0)
            else:
                self.current_account = None

        self.database.delete(TABLE_NAME, pubkey=account.pubkey)

    def unlock_account(
        self, account: Account, passphrase: str, password: Optional[str] = None
    ) -> bool:
        """
        Unlock account if credentials match pubkey, if not, return False

        :param account: Account instance
        :param passphrase: Passphrase
        :param password: Password
        :return:
        """
        # create signing_key from credentials
        if password is None:
            signing_key = TikkaSigningKey.from_dubp_mnemonic(
                passphrase
            )  # type: TikkaSigningKey
            # store mnemonic entropy needed to save wallet
            account.entropy = Mnemonic(MNEMONIC_LANGUAGES[self.language]).to_entropy(
                passphrase
            )
        else:
            signing_key = TikkaSigningKey.from_credentials(passphrase, password)

        # create pubkey instance
        account_pubkey = PublicKey.from_pubkey(account.pubkey)

        if signing_key is not None and account_pubkey == PublicKey.from_pubkey(
            signing_key.pubkey
        ):
            # save keypair in account instance
            account.signing_key = signing_key
            return True

        return False

    def lock_account(self, account: Account):
        """
        Lock account by removing signing_key

        :param account: Account instance
        :return:
        """
        account.signing_key = None

    def load_wallet(self, wallet: Wallet) -> Optional[Account]:
        """
        Create/Update an account from a wallet instance

        :param wallet: Wallet instance
        :return:
        """
        if wallet.signing_key is None:
            return None

        for account in self.list:
            # if account exists in list...
            if account.pubkey == wallet.signing_key.pubkey:
                account.signing_key = wallet.signing_key
                return account

        # create pubkey instance
        pubkey = PublicKey.from_pubkey(wallet.signing_key.pubkey)
        # create account instance
        account = Account(pubkey.base58)
        self.add_account(account)

        return account

    def save_wallet(
        self, account: Account, path: str, password: str, currency: str
    ) -> bool:
        """
        Save account on disk as DEWIF Wallet

        :param account: Account instance
        :param path: Path of the wallet on disk
        :param password: Wallet password
        :param currency: Currency codename
        :return:
        """
        if account.signing_key is None:
            return False

        if Path(path).suffix == ".dewif":
            if currency == "g1":
                currency_code = DEWIF_CURRENCY_CODE_G1
            else:
                currency_code = DEWIF_CURRENCY_CODE_G1_TEST
            try:
                # save dewif wallet file
                account.signing_key.save_dewif_v1_file(path, password, currency_code)
            except Exception as exception:
                logging.error(exception)
                return False
        else:
            try:
                # save ewif wallet file
                account.signing_key.save_ewif_file(path, password)
            except Exception as exception:
                logging.error(exception)
                return False

        self.update_account(account)
        return True
