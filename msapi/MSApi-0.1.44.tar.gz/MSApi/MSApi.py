import inspect

import requests
from MSApi.ObjectMS import ObjectMS

from MSApi.MSLowApi import MSLowApi, error_handler, caching

from MSApi.Meta import Meta
from MSApi.Organization import Organization
from MSApi.Template import Template
from MSApi.Product import Product
from MSApi.Service import Service
from MSApi.ProductFolder import ProductFolder
from MSApi.Discount import Discount, SpecialPriceDiscount, AccumulationDiscount
from MSApi.PriceType import PriceType
from MSApi.CompanySettings import CompanySettings
from MSApi.Bundle import Bundle
from MSApi.Variant import Variant
from MSApi.documents.CustomerOrder import CustomerOrder
from MSApi.exceptions import *
import MSApi as MSApi_module


class MSApi(MSLowApi):

    @classmethod
    def get_company_settings(cls) -> CompanySettings:
        """Запрос на получение Настроек компании."""
        response = cls.auch_get('context/companysettings')
        error_handler(response)
        return CompanySettings(response.json())

    @classmethod
    def get_default_price_type(cls) -> PriceType:
        """Получить тип цены по умолчанию"""
        response = cls.auch_get('context/companysettings/pricetype/default')
        error_handler(response)
        return PriceType(response.json())

    @classmethod
    def get_object_type(cls, obj_type_name) -> type:
        for member in inspect.getmembers(MSApi_module):
            if type(member[1]) is not type:
                continue
            if not issubclass(member[1], ObjectMS):
                continue
            if not hasattr(member[1], "_type_name"):
                continue
            if member[1].get_typename() == obj_type_name:
                return member[1]
        raise MSApiException("Object type \"{}\" not found".format(obj_type_name))

    @classmethod
    def get_object_by_meta(cls, meta: Meta):
        return cls.get_object_type(meta.get_type())

    @classmethod
    def get_object_by_json(cls, json_data):
        meta = Meta(json_data.get('meta'))
        return cls.get_object_type(meta.get_type())

    @classmethod
    def get_object_by_href(cls, href):
        response = cls._auch_get_by_href(href)
        error_handler(response)
        return cls.get_object_by_json(response.json())

    @classmethod
    @caching
    def gen_organizations(cls, **kwargs):
        return cls.gen_objects('entity/organization', Organization, **kwargs)

    @classmethod
    @caching
    def gen_variants(cls, **kwargs):
        return cls.gen_objects('entity/variant', Variant, **kwargs)

    @classmethod
    @caching
    def gen_services(cls, **kwargs):
        return cls.gen_objects('entity/service', Service, **kwargs)

    @classmethod
    @caching
    def gen_bundles(cls, **kwargs):
        return cls.gen_objects('entity/bundle', Bundle, **kwargs)

    @classmethod
    @caching
    def gen_assortment(cls, **kwargs):
        return cls.gen_objects('entity/assortment', lambda row_json: cls.get_object_by_json(row_json), **kwargs)

    @classmethod
    @caching
    def gen_customtemplates(cls, **kwargs):
        return cls.gen_objects('entity/assortment/metadata/customtemplate', Template, **kwargs)

    @classmethod
    @caching
    def gen_products(cls, **kwargs):
        return cls.gen_objects('entity/product', Product, **kwargs)

    @classmethod
    @caching
    def gen_productfolders(cls, **kwargs):
        return cls.gen_objects('entity/productfolder', ProductFolder, **kwargs)

    @classmethod
    @caching
    def gen_discounts(cls, **kwargs):
        return cls.gen_objects('entity/discount', Discount, **kwargs)

    @classmethod
    @caching
    def gen_special_price_discounts(cls, **kwargs):
        return cls.gen_objects('entity/specialpricediscount', SpecialPriceDiscount, **kwargs)

    @classmethod
    @caching
    def gen_accumulation_discounts(cls, **kwargs):
        return cls.gen_objects('entity/accumulationdiscount', AccumulationDiscount, **kwargs)

    @classmethod
    @caching
    def gen_customer_orders(cls, **kwargs):
        return cls.gen_objects('entity/customerorder', CustomerOrder, **kwargs)

    @classmethod
    def get_product_by_id(cls, product_id, **kwargs):
        response = cls.auch_get(f'entity/product/{product_id}', **kwargs)
        error_handler(response)
        return Product(response.json())

    @classmethod
    def set_products(cls, json_data):
        response = cls.auch_post(f'entity/product/', json=json_data)
        error_handler(response)

    @classmethod
    def load_label(cls, product: Product, organization: Organization, template: Template, sale_price=None, **kwargs):

        if not sale_price:
            sale_price = next(product.gen_sale_prices(), None)
            if not sale_price:
                raise MSApiException(f"Sale prices is empty in {product}")

        request_json = {
            'organization': {
                'meta': organization.get_meta().get_json()
            },
            'count': 1,
            'salePrice': sale_price.get_json(),
            'template': {
                'meta': template.get_meta().get_json()
            }

        }

        response = cls.auch_post(f"/entity/product/{product.get_id()}/export", json=request_json, **kwargs)
        if response.status_code == 303:
            url = response.json().get('Location')
            file_response = requests.get(url)
            data = file_response.content
        elif response.status_code == 200:
            data = response.content
        else:
            raise MSApiHttpException(response)

        return data
