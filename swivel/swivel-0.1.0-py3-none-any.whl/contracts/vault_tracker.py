from swivel.constants.abi import VAULT_TRACKER
from swivel.abstracts import VaultTracker as base

class VaultTracker(base):
    def __init__(self, v):
        """
        Parameters:
            v (W3) Instance of a vendor W3 class (no other vendors are supported as of now)
        """
        self.vendor = v
        self.abi = VAULT_TRACKER

    def admin(self, opts=None):
        return self.contract.functions.admin(), opts

    def c_token_address(self, opts=None):
        return self.contract.functions.cTokenAddr(), opts

    def swivel(self, opts=None):
        return self.contract.functions.swivel(), opts

    def matured(self, opts=None):
        return self.contract.functions.matured(), opts

    def maturity(self, opts=None):
        return self.contract.functions.maturity(), opts

    def maturity_rate(self, opts=None):
        return self.contract.functions.maturityRate(), opts

    def vaults(self, o, opts=None):
        return self.contract.functions.vaults(o), opts
    
    def balances_of(self, o, opts=None):
        return self.contract.functions.balancesOf(o), opts
