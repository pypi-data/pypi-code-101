# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.models.paginated_galaxy_collection_version_response_list import PaginatedGalaxyCollectionVersionResponseList  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestPaginatedGalaxyCollectionVersionResponseList(unittest.TestCase):
    """PaginatedGalaxyCollectionVersionResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedGalaxyCollectionVersionResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.paginated_galaxy_collection_version_response_list.PaginatedGalaxyCollectionVersionResponseList()  # noqa: E501
        if include_optional :
            return PaginatedGalaxyCollectionVersionResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    pulpcore.client.pulp_ansible.models.galaxy_collection_version_response.GalaxyCollectionVersionResponse(
                        version = '0', 
                        href = '0', 
                        namespace = pulpcore.client.pulp_ansible.models.namespace.namespace(), 
                        collection = pulpcore.client.pulp_ansible.models.collection.collection(), 
                        artifact = pulpcore.client.pulp_ansible.models.artifact.artifact(), 
                        metadata = pulpcore.client.pulp_ansible.models.collection_metadata_response.CollectionMetadataResponse(
                            authors = [
                                '0'
                                ], 
                            contents = pulpcore.client.pulp_ansible.models.contents.contents(), 
                            dependencies = pulpcore.client.pulp_ansible.models.dependencies.dependencies(), 
                            description = '0', 
                            documentation = '0', 
                            homepage = '0', 
                            issues = '0', 
                            license = [
                                '0'
                                ], 
                            repository = '0', 
                            tags = [
                                '0'
                                ], ), )
                    ]
            )
        else :
            return PaginatedGalaxyCollectionVersionResponseList(
        )

    def testPaginatedGalaxyCollectionVersionResponseList(self):
        """Test PaginatedGalaxyCollectionVersionResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
