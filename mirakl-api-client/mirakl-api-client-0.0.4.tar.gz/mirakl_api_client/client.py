import requests as rq

from mirakl_api_client import (
    resources,
    utils
)

class MirakleClient:
    def __init__(self, hostname, api_key):
        self._session = rq.Session()
        self._hostname = hostname
        self._api_key = api_key   

        self._base_url = utils.urljoin('https://' + self._hostname, 'api')
        self._resources = {
            'invoices': resources.InvoicesPool(
                utils.urljoin(self._base_url, 'invoices'), self._session),
            'transactions_logs': resources.TransactionsLogsPool(
                utils.urljoin(self._base_url, 'sellerpayment/transactions_logs'), self._session),
            'threads': resources.ThreadsPool(
                utils.urljoin(self._base_url, 'threads'), self._session),
            'shipments': resources.ShipmentsPool(
                utils.urljoin(self._base_url, 'shipments'), self._session),
            'offers': resources.OffersPool(
                utils.urljoin(self._base_url, 'offers'), self._session),
            'orders': resources.OrdersPool(
                utils.urljoin(self._base_url, 'orders'), self._session),
            'settings': resources.SettingsPool(
                self._base_url, self._session),
            'shipping': resources.ShippingPool(
                utils.urljoin(self._base_url, 'shipping'), self._session),
            'products': resources.ProductsPool(
                utils.urljoin(self._base_url, 'products'), self._session),
            'promotions': resources.PromotionsPool(
                utils.urljoin(self._base_url, 'promotions'), self._session),
            'account': resources.AccountPool(
                utils.urljoin(self._base_url, 'account'), self._session),
            'shops': resources.ShopsPool(
                utils.urljoin(self._base_url, 'shops'), self._session),
        }        

        self._authenticate()

    def _authenticate(self):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': self._api_key
        }
        self._session.headers = headers

    @property
    def resources(self):
        return self._resources

    @property
    def invoices(self):
        return self.resources.get('invoices')

    @property
    def transactions_logs(self):
        return self.resources.get('transactions_logs')

    @property
    def threads(self):
        return self.resources.get('threads')

    @property
    def shipments(self):
        return self.resources.get('shipments')

    @property
    def offers(self):
        return self.resources.get('offers')

    @property
    def orders(self):
        return self.resources.get('orders')

    @property
    def settings(self):
        return self.resources.get('settings')

    @property
    def shipping(self):
        return self.resources.get('shipping')

    @property
    def products(self):
        return self.resources.get('products')

    @property
    def promotions(self):
        return self.resources.get('promotions')

    @property
    def accounts(self):
        return self.resources.get('account')

    @property
    def shops(self):
        return self.resources.get('shops')
