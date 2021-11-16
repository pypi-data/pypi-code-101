# -*- coding: utf-8 -*-
from . import response
from . import client

class SimRequest(object):
    OPERATOR_CHINAMOBILE = 1
    OPERATOR_CHINAUNICOM = 2
    OPERATOR_CHINATELCOM = 3

    def __init__(self):
        return

    def get_package_list(self, page = 1, size = 20):
        params = client.RequestParam()
        params.method = params.GET
        params.payload = {
            "page": page,
            "size": size,
        }
        params.path = f"cardapi/package/list"
        return params

    def get_card_list(self, cardflag = 1, operator = None, order = None, page = 1, size = 20, sortfield = None, status = None):
        params = client.RequestParam()
        params.path = f"cardapi/card/list/"
        params.method = params.POST
        params.payload = {
            "cardFlag": cardflag,
            "operator": operator or self.OPERATOR_CHINAMOBILE,
            "order": order,
            "pageindex": page,
            "pagesize": size,
            "sortfield": sortfield,
        }
        return params

    def get_card(self, iccid = None):
        if iccid == None:
            return response.PARAM_ERROR

        params = client.RequestParam()
        params.method = params.GET
        params.path = f"cardapi/card/{iccid}/"

        return params

    def get_share_pool_list(self):
        params = client.RequestParam()
        params.path = f"cardapi/cardsharepool/list/"
        params.method = params.POST
        params.payload = {}
        return params

    def get_card_month_usage(self, iccid, month):
        params = client.RequestParam()
        params.path = f"cardapi/card_flow/month/"
        params.method = params.POST
        params.payload = {
            "iccid": iccid,
            "month": month,
        }
        return params