# -*- coding: UTF-8 -*-
"""API client dedicated to PasswordsDatabase.com for searching for default credentials.

"""
from ....core.utils.api import *


__all__ = ["PasswordDatabaseAPI"]


class PasswordDatabaseAPI(SearchAPI):
    """
    Class for communicating with the website of PasswordsDatabase.com.
    
    :param kwargs: HTTPBot / API keyword-arguments
    """
    url = "https://www.passwordsdatabase.com"
    
    def __init__(self, **kwargs):
        kwargs['kind'] = "http"
        super(PasswordDatabaseAPI, self).__init__(None, **kwargs)
    
    @cache(86400)
    def _request(self, vendor):
        """
        PasswordDatabaseAPI list get method for a defined vendor.
        """
        super(PasswordDatabaseAPI, self)._request("/vendor/%s" % vendor.lower().replace(" ", "_"), "get")
        if self._soup is None:
            raise APIError("bad URL")
        for table in self._soup.findAll('table'):
            if "Defaut Password List" in table.text:
                break
        if "No default password found" in table.find('td').text:
            raise APIError("this vendor does not exist")
        row, self._API__bot.json = {}, {'data': []}  # fake the result of a JSON bot
        for td in table.findAll('tr'):
            if td.find('h1') and td.find('h1').text == "Defaut Password List":
                continue
            if len(row) > 1:
                row = {}
            if td.find('h2'):
                if td.find('h2').text == "Navigation":
                    continue
                n = td.find('h2').text.split("-", 1)[1].replace("default password", "")
                if n.lower().lstrip().startswith(vendor.lower()):
                    n = n[n.lower().index(vendor.lower())+len(vendor)+1:]
                row['name'] = API._sanitize("", n)[1]
            else:
                for p in td.findAll('p'):
                    k, v = API._sanitize(p.find('span').text, p.text.split(":", 1)[1])
                    if k == "product":
                        continue
                    elif k == "method":
                        if v.lower() == "multi":
                            v = ""
                        v = list(filter(lambda x: x != "", map(lambda s: s.strip().lower(), v.split(","))))
                    row[k] = v
            if len(row) > 1:
                self._json['data'].append(row)
        return self._json
    
    @cache(86400)
    def _vendors(self):
        """
        PasswordDatabaseAPI get method for the list of all vendors.
        """
        super(PasswordDatabaseAPI, self)._request("/", "get")
        if self._soup is None:
            raise APIError("bad URL")
        t = self._soup.find('table')
        while "Vendors" in t.text:
            if len(t.findAll('table')) == 0:
                break
            for st in t.findAll('table'):
                if "Vendors" in st.text:
                    t = st
                    break
        return [a.text for a in t.findAll('a')]
    
    @apicall
    def credentials(self, vendor):
        """
        Search for default credentials for a given vendor.
        
        :param vendor: vendor name
        """
        return self._request(vendor)
    
    @apicall
    def search(self, query, vendor=None):
        """
        Search for something in the PasswordDatabaseAPI list.
        
        :param vendor: vendor name
        :param query: anything to be searched for in the list
        """
        data = {'data': []}
        for v in (self.vendors if vendor is None else [vendor]):
            r = self._request(v)
            if vendor is None:
                r['vendor'] = v
            data['data'].append(r)
        self._json = data
        return super(PasswordDatabaseAPI, self)._search(query)
    
    @property
    def vendors(self):
        """
        List of vendors
        """
        return self._vendors()

