""" Handle Address endpoints"""
from .apirequest import APIRequest
from .decorators import endpoint
from abc import abstractmethod


class Addresses(APIRequest):
    """Addresses - class to handle the accounts endpoints"""

    ENDPOINT = ""
    METHOD = "GET"

    @abstractmethod
    def __init__(self):
        endpoint = self.ENDPOINT.format()
        super(Addresses, self).__init__(endpoint, method=self.METHOD)


@endpoint('address/deposit/')
class AddressesActiveFiatAddresses(Addresses):
    """AddressesActiveFiatAddresses - class to handle the active address endpoints"""
    def __init__(self, assetID, variant):
        super(AddressesActiveFiatAddresses, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(assetID) + "/" + str(variant) + "/"


# TODO: Determine where the network ID comes from. Status currently: Unknown
@endpoint('address/deposit/')
class AddressesActiveCryptoAddresses(Addresses):
    """AddressesActiveCryptoAddresses - class to handle the active address endpoints"""
    def __init__(self, assetID, networkId):
        super(AddressesActiveCryptoAddresses, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(assetID) + "/" + str(networkId) + "/"
        self.params = {'version': 2}


@endpoint('address/deposit/', "POST", 200)
class AddressesCreateDepositAddress(Addresses):
    """AddressesCreateDepositAddress - class to handle the active address endpoints"""
    def __init__(self, assetID, variant, name):
        super(AddressesCreateDepositAddress, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(assetID) + "/" + str(variant) + "/"
        self.data = {'address': {'name': name}}


@endpoint('address/withdraw/')
class AddressesActiveWithdrawAddresses(Addresses):
    """AddressesGetActiveWithdrawAddresses - class to handle the active address endpoints"""
    def __init__(self, asset_code):
        super(AddressesActiveWithdrawAddresses, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(assetID) + "/"


@endpoint('address/withdraw/', 'POST', 200)
class AddressesCreateWithdrawAddresses(Addresses):
    """AddressesCreateWithdrawAddresses - class to handle the active address endpoints"""
    def __init__(self, asset_code):
        super(AddressesCreateWithdrawAddresses, self).__init__()
        self.ENDPOINT = self.ENDPOINT + str(assetID) + "/"