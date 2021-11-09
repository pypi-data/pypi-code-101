from swivel.constants.abi import MARKET_PLACE
from swivel.abstracts import MarketPlace as base

class MarketPlace(base):
    def __init__(self, v):
        """
        Parameters:
            v (W3) Instance of a vendor W3 class (no other vendors are supported as of now)
        """
        self.vendor = v
        self.abi = MARKET_PLACE

    def admin(self, opts=None):
        return self.contract.functions.admin(), opts

    def swivel(self, opts=None):
        return self.contract.functions.swivel(), opts

    def set_swivel_address(self, a, opts=None):
        return self.contract.functions.setSwivelAddress(a), self.tx_opts(opts)

    def c_token_address(self, u, m, opts=None):
        return self.contract.functions.cTokenAddress(u, m), opts

    def create_market(self, u, m, c, n, s, d, opts=None):
        return self.contract.functions.createMarket(u, m, c, n, s, d), self.tx_opts(opts)

    def markets(self, u, m, opts=None):
        return self.contract.functions.markets(u, m), opts

    def mature_market(self, u, m, opts=None):
        return self.contract.functions.matureMarket(u, m), self.tx_opts(opts)

    def mature(self, u, m, opts=None):
        return self.contract.functions.mature(u, m), opts

    def maturity_rate(self, u, m, opts=None):
        return self.contract.functions.maturityRate(u, m), opts

    def transfer_vault_notional(self, u, m, t, a, opts=None):
        return self.contract.functions.transferVaultNotional(u, m, t, a), self.tx_opts(opts)
