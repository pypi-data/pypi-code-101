# -*- coding: utf-8 -*-
# pylint: disable = import-outside-toplevel
"""Tests of ``modules.cioskeleton.models.dbbone`` class."""

from ....tests import DBUnitTestCase


# =============================================================================
class UModelsDBBoneDBBone(DBUnitTestCase):
    """Unit test class for
    :class:`modules.cioskeleton.models.dbbone.DBBone`."""

    # -------------------------------------------------------------------------
    def test_xml2db(self):
        """[u:modules.cioskeleton.models.dbbone.DBBone.xml2db]"""
        from lxml import etree
        from pyramid.i18n import TranslationString
        from ..models.dbbone import DBBone

        # pylint: disable = no-member
        dbsession = self.request.dbsession
        # pylint: enable = no-member
        dbbone = DBBone(bone_id='bone01', label='Bone n°1')
        dbsession.add(dbbone)

        # error_if_exists
        bone_elt = etree.XML(
            '<bone id="bone01" xmlns="http://ns.chrysal.io/cioskeleton">'
            '  <label>Bone n°1</label>'
            '</bone>')
        error = DBBone.xml2db(dbsession, bone_elt)
        self.assertIsInstance(error, TranslationString)
        error = DBBone.xml2db(
            dbsession, bone_elt, error_if_exists=False)
        self.assertIsNone(error)

        # Bad ID
        bone_elt = etree.XML(
            '<bone id="" xmlns="http://ns.chrysal.io/cioskeleton">'
            '  <label>Bone n°2</label>'
            '</bone>')
        error = DBBone.xml2db(dbsession, bone_elt)
        self.assertIsNotNone(error)

        # Correct bone
        bone_elt = etree.XML(
            '<bone id="bone02" xmlns="http://ns.chrysal.io/cioskeleton">'
            '  <label>Bone n°2</label>'
            '</bone>')
        error = DBBone.xml2db(dbsession, bone_elt)
        self.assertIsNone(error)
        dbbone = dbsession.query(DBBone).filter_by(
            bone_id='bone02').first()
        self.assertIsInstance(dbbone, DBBone)
        self.assertEqual(dbbone.label, 'Bone n°2')

    # -------------------------------------------------------------------------
    def test_db2xml(self):
        """[u:modules.cioskeleton.models.dbbone.DBBone.db2xml]"""
        from ..models.dbbone import DBBone

        dbbone = DBBone(
            bone_id='bone01', label='Bone n°1',
            attachments_key='Bone01', picture='bone01.png')
        bone_elt = dbbone.db2xml()
        self.assertEqual(bone_elt.findtext('label'), 'Bone n°1')
