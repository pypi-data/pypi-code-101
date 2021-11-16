import json

from mirakl_api_client.utils import urljoin

class ResourcePool:
    def __init__(self, endpoint, session):
        """Initialize the ResourcePool to the given endpoint. Eg: products"""
        self._endpoint = endpoint
        self._session = session

    def get_url(self):
        return self._endpoint

class CreatableResource:
    def create_item(self, item, files=None):
        if files:
            self._session.headers.pop('Content-Type')
            self._session.headers.pop('Accept')
            print(self._session.headers)
            res = self._session.post(self._endpoint, files=files, data=item)
        else:
            res = self._session.post(self._endpoint, data=json.dumps(item))
        return res

class GettableResource:
    def fetch_item(self, code):
        url = urljoin(self._endpoint, code)
        res = self._session.get(url)
        return res

class ListableResource:
    def fetch_list(self, args=None):
        res = self._session.get(self._endpoint, params=args)
        return res

class SearchableResource:
    def search(self, query):
        params = {
            'query': query
        }
        res = self._session.get(self._endpoint, params=params)
        return res

class UpdatableResource:
    def update_create_item(self, item, code=None):
        if code is None:
            code = item.get('id')
        url = urljoin(self._endpoint, code) if code else self._endpoint
        res = self._session.put(url, data=json.dumps(item))
        return res

class DeletableResource:
    def delete_item(self, code):
        url = urljoin(self._endpoint, code)
        res = self._session.delete(url)
        return res

# Pools

# Invoices
class InvoicesPool(
    ResourcePool,
    GettableResource,
    ListableResource):
    pass

# sellerpayment Transactions
class TransactionsLogsPool(
    ResourcePool,
    ListableResource):
    pass

# Threads

class ThreadsPool(
    ResourcePool,
    GettableResource,
    ListableResource):
    
    def message(self, thread_id):
        return ThreadsMessagePool(
            urljoin(self._endpoint, thread_id, 'message'), self._session
        )

    def attachment(self, attachment_id):
        return ThreadsAttachmentPool(
            urljoin(self._endpoint, attachment_id, 'download'), self._session
        )

class ThreadsMessagePool(
    ResourcePool,
    CreatableResource):
    pass

class ThreadsAttachmentPool(
    ResourcePool,
    GettableResource):
    pass

# Shipments

class ShipmentsPool(
    ResourcePool,
    GettableResource,
    ListableResource):
    
    @property
    def tracking(self):
        return ShipmentsPool(
            urljoin(self._endpoint, 'tracking'), self._session
        )

    @property
    def ship(self):
        return ShipmentsShipPool(
            urljoin(self._endpoint, 'ship'), self._session
        )

class ShipmentsTrackingPool(
    ResourcePool,
    CreatableResource):
    pass

class ShipmentsShipPool(
    ResourcePool,
    UpdatableResource):
    pass

# Offers

class OffersPool(
    ResourcePool,
    CreatableResource,
    GettableResource,
    ListableResource
    ):

    @property
    def imports(self):
        return OffersImportsPool(
            urljoin(self._endpoint, 'imports'), self._session
        )

    @property
    def export(self):
        return OffersExportPool(
            urljoin(self._endpoint, 'export'), self._session
        )

    @property
    def states(self):
        return OffersStatesPool(
            urljoin(self._endpoint, 'states'), self._session
        )

class OffersImportsPool(
    ResourcePool,
    CreatableResource,
    GettableResource,
    ListableResource):
    
    def error_report(self, import_id):
        return OffersImportsErrorReportPool(
            urljoin(self._endpoint, import_id, 'error_report'), self._session
        )

class OffersImportsErrorReportPool(
    ResourcePool,
    ListableResource):
    pass

class OffersExportPool(
    ResourcePool, 
    ListableResource):
    pass

class OffersStatesPool(
    ResourcePool,
    ListableResource):
    pass

# Orders

class OrdersPool(
    ResourcePool,
    ListableResource,
    UpdatableResource):
    pass

    @property
    def shipping_from(self):
        return OrdersShippingFromPool(
            urljoin(self._endpoint, 'shipping_from'), self._session
        )

    @property
    def refund(self):
        return OrdersRefundPool(
            urljoin(self._endpoint, 'refund'), self._session
        )        

    @property
    def cancel_lines(self):
        return OrdersCancelPool(
            urljoin(self._endpoint, 'cancel'), self._session
        )
    
    @property
    def adjust(self):
        return OrdersAdjustPool(
            urljoin(self._endpoint, 'adjust'), self._session
        )

    @property
    def documents(self):
        return OrdersDocumentsPool(
            urljoin(self._endpoint, 'documents'), self._session
        )

    @property
    def taxes(self):
        return OrdersTaxesPool(
            urljoin(self._endpoint, 'taxes'), self._session
        )
    
    def accept(self, order_id):
        return OrdersAcceptPool(
            urljoin(self._endpoint, order_id, 'accept'), self._session
        )

    def tracking(self, order_id):
        return OrdersTrackingPool(
            urljoin(self._endpoint, order_id, 'tracking'), self._session
        )   

    def ship(self, order_id):
        return OrdersShipPool(
            urljoin(self._endpoint, order_id, 'ship'), self._session
        )

    def cancel(self, order_id):
        return OrdersCancelPool(
            urljoin(self._endpoint, order_id, 'cancel'), self._session
        )

    def additional_fields(self, order_id):
        return OrdersAdditionalFieldsPool(
            urljoin(self._endpoint, order_id, 'additional_fields'), self._session
        )

    def evaluation(self, order_id):
        return OrdersEvaluationPool(
            urljoin(self._endpoint, order_id, 'evaluation'), self._session
        )
    
    def lines(self, order_id):
        return OrdersLinesPool(
            urljoin(self._endpoint, order_id, 'lines'), self._session
        )

    def document_upload(self, order_id):
        return OrdersDocumentsUploadPool(
            urljoin(self._endpoint, order_id, 'documents'), self._session
        )

    def threads(self, order_id):
        return OrdersThreadsPool(
            urljoin(self._endpoint, order_id, 'threads'), self._session
        )


class OrdersShippingFromPool(
    ResourcePool,
    UpdatableResource
    ):
    pass

class OrdersAcceptPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersTrackingPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersShipPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersRefundPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersCancelPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersAdditionalFieldsPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersAdjustPool(
    ResourcePool,
    UpdatableResource):
    pass

class OrdersEvaluationPool(
    ResourcePool,
    ListableResource):
    pass

class OrdersLinesPool(
    ResourcePool, 
    GettableResource):
    
    def resolve_incident(self, line_id):
        return OrdersLinesResolveIncidentPool(
            urljoin(self._endpoint, line_id, 'resolve_incident'), self._session
        )

class OrdersLinesResolveIncidentPool(
    ResourcePool, 
    UpdatableResource):
    pass

class OrdersDocumentsPool(
    ResourcePool,
    ListableResource,
    DeletableResource):

    @property
    def download(self):
        return OrdersDocumentsDownloadPool(
            urljoin(self._endpoint, 'download'), self._session
        )

class OrdersDocumentsDownloadPool(
    ResourcePool, 
    ListableResource):
        pass

class OrdersDocumentsUploadPool(
    ResourcePool, 
    CreatableResource):
    pass

class OrdersTaxesPool(
    ResourcePool,
    ListableResource):
    pass

class OrdersThreadsPool(
    ResourcePool,
    CreatableResource):
    pass

# Settings

class SettingsPool(ResourcePool):
    @property
    def additional_fields(self):
        return SettingsAdditionalFieldsPool(
            urljoin(self._endpoint, 'additional_fields'), self._session
        )

    @property
    def channels(self):
        return SettingsChannelsPool(
            urljoin(self._endpoint, 'channels'), self._session
        )

    @property
    def documents(self):
        return SettingsDocumentsPool(
            urljoin(self._endpoint, 'documents'), self._session
        )

    @property    
    def locales(self):
        return SettingsLocalesPool(
            urljoin(self._endpoint, 'locales'), self._session
        )

    @property
    def reasons(self):
        return SettingsReasonsPool(
            urljoin(self._endpoint, 'reasons'), self._session
        )

    @property
    def version(self):
        return SettingsVersionPool(
            urljoin(self._endpoint, 'version'), self._session
        )

    @property
    def hierarchies(self):
        return SettingsHierarchiesPool(
            urljoin(self._endpoint, 'hierarchies'), self._session
        )

    @property
    def values_lists(self):
        return SettingsValuesListsPool(
            urljoin(self._endpoint, 'values_lists'), self._session
        )        

class SettingsAdditionalFieldsPool(
    ResourcePool,
    ListableResource):
    pass

class SettingsChannelsPool(
    ResourcePool,
    ListableResource):
    pass

class SettingsDocumentsPool(
    ResourcePool,
    ListableResource):
    pass

class SettingsLocalesPool(
    ResourcePool,
    ListableResource):
    pass

class SettingsReasonsPool(
    ResourcePool, 
    GettableResource):
    pass

class SettingsVersionPool(
    ResourcePool,
    ListableResource):
    pass

class SettingsHierarchiesPool(
    ResourcePool,
    ListableResource):
    pass

class SettingsValuesListsPool(
    ResourcePool,
    ListableResource,
    GettableResource):
    pass

# Shipping

class ShippingPool(ResourcePool):
    @property
    def zones(self):
        return ShippingZonesPool(
            urljoin(self._endpoint, 'zones'), self._session
        )

    @property
    def types(self):
        return ShippingTypesPool(
            urljoin(self._endpoint, 'types'), self._session
        )

    @property
    def carriers(self):
        return ShippingCarriersPool(
            urljoin(self._endpoint, 'carriers'), self._session
        )        

    @property
    def logistic_classes(self):
        return ShippingLogisticClassesPool(
            urljoin(self._endpoint, 'logistic_classes'), self._session
        )                

class ShippingZonesPool(
    ResourcePool, 
    ListableResource):
    pass

class ShippingTypesPool(
    ResourcePool, 
    ListableResource):
    pass

class ShippingCarriersPool(
    ResourcePool, 
    ListableResource):
    pass

class ShippingLogisticClassesPool(
    ResourcePool,
    ListableResource):
    pass
# Products 

class ProductsPool(
    ResourcePool, 
    ListableResource):

    @property
    def imports(self):
        return ProductsImportsPool(
            urljoin(self._endpoint, 'imports'), self._session
        )

    @property
    def attributes(self):
        return ProductsAttributesPool(
            urljoin(self._endpoint, 'attributes'), self._session
        )

    @property
    def offers(self):
        return ProductsOffersPool(
            urljoin(self._endpoint, 'offers'), self._session
        )

class ProductsImportsPool(
    ResourcePool,
    CreatableResource,
    GettableResource,
    ListableResource):
    
    def error_report(self, import_id):
        return ProductsImportsErrorReportPool(
            urljoin(self._endpoint, import_id, 'error_report'), self._session
        )

    def new_product_report(self, import_id):
        return ProductsImportsNewProductReportPool(
            urljoin(self._endpoint, import_id, 'new_product_report'), self._session
        )

    def transformed_file(self, import_id):
        return ProductsImportsTransformedFilePool(
            urljoin(self._endpoint, import_id, 'transformed_file'), self._session
        )

    def transformation_error_report(self, import_id):
        return ProductsImportsTransformationErrorReportPool(
            urljoin(self._endpoint, import_id, 'transformation_error_report'), self._session
        )

class ProductsImportsErrorReportPool(
    ResourcePool,
    ListableResource):
    pass

class ProductsImportsNewProductReportPool(
    ResourcePool,
    ListableResource):
    pass

class ProductsImportsTransformedFilePool(
    ResourcePool,
    ListableResource):
    pass

class ProductsImportsTransformationErrorReportPool(
    ResourcePool,
    ListableResource):
    pass

class ProductsAttributesPool(
    ResourcePool, 
    ListableResource):
    pass

class ProductsOffersPool(
    ResourcePool, 
    ListableResource):
    pass

# Promitions

class PromotionsPool(
    ResourcePool,
    ListableResource):
    pass

# Account

class AccountPool(
    ResourcePool,
    ListableResource):
    pass

# Shops

class ShopsPool(ResourcePool):

    @property
    def documents(self):
        return ShopsDocumentsPool(
            urljoin(self._endpoint, 'documents'), self._session
        )


class ShopsDocumentsPool(
    ResourcePool,
    ListableResource,
    CreatableResource,
    DeletableResource):

    @property
    def download(self):
        return ShopsDocumentsDownloadPool(
            urljoin(self._endpoint, 'download'), self._session
        )

class ShopsDocumentsDownloadPool(
    ResourcePool,
    ListableResource):
    pass