""" Control Panel RestAPI endpoint
"""
from eea.api.taxonomy.interfaces import IEeaApiTaxonomyLayer
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface


@adapter(Interface, IEeaApiTaxonomyLayer)
class TaxonomyControlPanel(RegistryConfigletPanel):
    """ Control Panel endpoint
    """
    schema = Interface
    configlet_id = "taxonomies"
    configlet_category_id = "Products"
    title = "Taxonomy settings"
    group = ""
