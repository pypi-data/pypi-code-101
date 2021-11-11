# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioskeleton.models.populate`` functions."""

from ....tests import DBUnitTestCase


# =============================================================================
class UModelsPopulateXml2Db(DBUnitTestCase):
    """Unit test class for
    :func:`modules.cioskeleton.models.populate.xml2db`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:modules.cioskeleton.models.populate.xml2db]"""
        from lxml import etree
        from ..models.populate import xml2db

        tree = etree.XML(
            '<cioskeleton'
            '    xmlns="http://ns.chrysal.io/cioskeleton" version="1.0">'
            '  <bones>'
            '    <bone id="hand">'
            '      <label>Hand</label>'
            '      <foo/>'
            '    </bone>'
            '  </bones>'
            '</cioskeleton>')
        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member

        self.assertEqual(len(xml2db(dbsession, tree, None, True)), 0)


# =============================================================================
class UModelsPopulateDb2Xml(DBUnitTestCase):
    """Unit test class for
    :func:`modules.cioskeleton.models.populate.db2xml`."""

    # -------------------------------------------------------------------------
    def test_it(self):
        """[u:modules.cioskeleton.models.populate.db2xml]"""
        from lxml import etree
        from ..models.populate import db2xml
        from ..models.dbbone import DBBone

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        dbsession.add(DBBone(bone_id='hand', label='Hand'))
        namespace = 'http://ns.chrysal.io/cioskeleton'
        root_elt = etree.Element(
            '{{{0}}}cioskeleton'.format(namespace),
            nsmap={None: namespace}, version='1.0')

        db2xml(dbsession, root_elt)
        self.assertEqual(len(root_elt), 1)
