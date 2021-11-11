"""SQLAlchemy-powered model definitions for bones."""

from sqlalchemy import Column
from sqlalchemy import String
from lxml import etree

from ....lib.utils import make_id
from ....lib.i18n import _
from ....models import DBDeclarativeClass, ID_LEN, LABEL_LEN
from ....models.dbbase import DBBaseClass
from ..relaxng import RELAXNG_CIOSKELETON


# =============================================================================
class DBBone(DBDeclarativeClass, DBBaseClass):
    """SQLAlchemy-powered bone class."""

    suffix = 'cioskt'
    attachments_dir = 'cioskt'
    _settings_tabs = (_('Information'),)

    __tablename__ = 'bones'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    bone_id = Column(String(ID_LEN), primary_key=True)
    label = Column(String(LABEL_LEN), nullable=False)
    attachments_key = Column(String(ID_LEN + 20))
    picture = Column(String(ID_LEN + 4))

    # -------------------------------------------------------------------------
    @classmethod
    def xml2db(cls, dbsession, bone_elt, error_if_exists=True, kwargs=None):
        """Load a bone from a XML element.

        :type  dbsession: sqlalchemy.orm.session.Session
        :param dbsession:
            SQLAlchemy session.
        :type  bone_elt: lxml.etree.Element
        :param bone_elt:
            Bone XML element.
        :param bool error_if_exists: (default=True)
            It returns an error if bone already exists.
        :param dict kwargs: (optional)
            Dictionary of keyword arguments.
        :rtype: :class:`pyramid.i18n.TranslationString` or ``None``
        :return:
            Error message or ``None``.
        """
        # pylint: disable = unused-argument
        # Check if already exists
        bone_id = make_id(bone_elt.get('id'), 'token', ID_LEN)
        dbbone = dbsession.query(cls).filter_by(bone_id=bone_id).first()
        if dbbone is not None:
            if error_if_exists:
                return _('Bone "${s}" already exists.', {'s': bone_id})
            return None

        # Create bone
        record = cls.record_from_xml(bone_id, bone_elt)
        error = cls.record_format(record)
        if error:
            return error
        dbsession.add(cls(**record))
        return None

    # -------------------------------------------------------------------------
    @classmethod
    def record_from_xml(cls, bone_id, bone_elt):
        """Convert a bone XML element into a dictionary.

        :param str bone_id:
            Bone ID.
        :type  bone_elt: lxml.etree.Element
        :param bone_elt:
            Bone XML element.
        :rtype: dict
        """
        namespace = RELAXNG_CIOSKELETON['namespace']
        attachments = bone_elt.find('{{{0}}}attachments'.format(namespace))
        return {
            'bone_id': bone_id,
            'label': bone_elt.findtext(
                '{{{0}}}label'.format(namespace)) or bone_id,
            'attachments_key': attachments is not None and attachments.get(
                'key') or None,
            'picture': attachments is not None and attachments.findtext(
                '{{{0}}}picture'.format(namespace)) or None}

    # -------------------------------------------------------------------------
    @classmethod
    def record_format(cls, record):
        """Check and possibly correct a record before inserting it in the
        database.

        :param dict record:
            Dictionary of values to check.
        :rtype: ``None`` or :class:`pyramid.i18n.TranslationString`
        :return:
            ``None`` or error message.
        """
        for k in [i for i in record if record[i] is None]:
            del record[k]

        # Bone ID
        if not record.get('bone_id'):
            return _('Bone without ID.')
        record['bone_id'] = make_id(record['bone_id'], 'token', ID_LEN)
        return None

    # -------------------------------------------------------------------------
    def db2xml(self):
        """Serialize a bone to a XML representation.

        :rtype: lxml.etree.Element
        """
        bone_elt = etree.Element('{{{0}}}bone'.format(
            RELAXNG_CIOSKELETON['namespace']))
        bone_elt.set('id', self.bone_id)
        etree.SubElement(bone_elt, 'label').text = self.label
        if self.attachments_key:
            elt = etree.SubElement(
                bone_elt, 'attachments', key=self.attachments_key)
            if self.picture:
                etree.SubElement(elt, 'picture').text = self.picture

        return bone_elt
