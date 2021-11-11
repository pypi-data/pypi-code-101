"""XML manipulation."""

from logging import getLogger
from os.path import join, dirname, basename
from io import BytesIO
from textwrap import wrap
from filecmp import cmpfiles
from shutil import copy2
from json import loads

from lxml import etree

from pyramid.asset import abspath_from_asset_spec

from .i18n import _, translate
from .utils import normalize_spaces


LOG = getLogger(__name__)
XML_NS = '{http://www.w3.org/XML/1998/namespace}'


# =============================================================================
def load_xml(filename, relaxngs=None, data=None, noline=False, parser=None,
             xinclude=False):
    """Load an XML document and validate it against a Relax NG file.

    :param str filename:
        Path to XML file.
    :param dict relaxngs: (optional)
        Relax NG dictionary such as ``{<pattern>: <relax_ng_file>,...}``. If it
        is ``None``, no validation is performed.
    :type data: str, bytes or :class:`lxml.etree.ElementTree`
    :param data: (optional)
        Content of the XML document. If it is not ``None``, it is used in place
        of the content of the file ``filename``.
    :param bool noline: (default=False)
        If ``True``, the error message does not contain line numbers.
    :type parser: :class:`etree.XMLParser`
    :param parser: (optional)
        Specific parser for ``etree.parse`` function.
    :param bool xinclude: (default=False)
        If ``True``, activate XInclude.
    :rtype: str, :class:`TranslationString` or :class:`ElementTree`
    :return:
        An error message or an instance of :class:`lxml.etree.ElementTree`
        class.
    """
    # Read file
    # pylint: disable = protected-access
    if data is None or not isinstance(data, etree._ElementTree):
        if data is not None and not isinstance(data, bytes):
            data = bytes(data.encode())
        try:
            tree = etree.parse(
                filename if data is None else BytesIO(data), parser=parser)
        except IOError:
            return _('Unknown file "${n}"', {'n': basename(filename)})
        except etree.XMLSyntaxError as error:
            return str(error)
    else:
        tree = data
    # pylint: enable = protected-access

    # XInclude
    if xinclude:
        try:
            tree.xinclude()
        except etree.XIncludeError as error:
            return str(error)

    # Validate
    if relaxngs is None:
        return tree
    error = validate_xml(tree, relaxngs, noline)
    if error is not None:
        return error

    return tree


# =============================================================================
def validate_xml(tree, relaxngs, noline=False):
    """Load an XML document and validate it against a Relax NG file.

    :type  tree: lxml.etree.ElementTree
    :param tree:
        XML document.
    :param dict relaxngs:
        Relax NG dictionary such as ``{<pattern>: <relax_ng_file>,...}``.
    :param bool noline: (default=False)
        If ``True``, the error message does not contain line numbers.
    :rtype: str, :class:`TranslationString` or ``None``
    :return:
        An error message or ``None``.
    """
    # Find the right RelaxNG
    relaxng = None
    pattern = None
    root = tree.getroot()
    for pattern in relaxngs:
        chunks = pattern.split(',')
        chunk = chunks[0].strip()
        if root.tag != chunk:
            continue
        for chunk in chunks[1:]:
            chunk = chunk.strip().split('=')
            if root.get(chunk[0]) != chunk[1]:
                chunk = None
                break
        if chunk is not None:
            relaxng = relaxngs[pattern]
            break
    if relaxng is None:
        return _('${tag}: Relax NG not found', {'tag': tree.getroot().tag})

    # Load Relax NG
    if isinstance(relaxng, str):
        try:
            relaxng = etree.RelaxNG(etree.parse(relaxng))
        except IOError as error:
            return str(error)
        except (etree.XMLSyntaxError, etree.RelaxNGParseError) as error:
            return '"{0}": {1}'.format(relaxng, error)
        relaxngs[pattern] = relaxng

    # Validate
    if not relaxng.validate(tree):
        error = relaxng.error_log.last_error
        return error.message if noline else \
            _('Line ${l}: ${m}', {'l': error.line, 'm': error.message})
    return None


# =============================================================================
def relaxng4validation(relaxng, attributes=('version',)):
    """Transform a Relax NG dictionary with keys ``'root'``, ``'file'`` and
    possibly ``'namespace'`` and ``'version'`` into a dictionary compatible
    with :func:`validate_xml`.

    :param dict relaxng:
        A Chrysalio Relax NG dictionary.
    :param tuple attributes: (default=('version',))
        Attributes to take into account in the pattern.
    :rtype: :class:`dict` or ``None``
    """
    if not relaxng:
        return None
    if 'namespace' in relaxng:
        pattern = '{{{0}}}{1}'.format(
            relaxng['namespace'], relaxng['root'])
    else:
        pattern = relaxng['root']

    for attribute in attributes:
        if attribute in relaxng:
            pattern += ', {0}={1}'.format(attribute, relaxng[attribute])

    return {pattern: relaxng['file']}


# =============================================================================
def load_xslt(filename):
    """Load a XSL file and create a etree.XSLT object.

    :rtype: :class:`lxml.etree.XSLT` or :class:`str`
    """
    try:
        xslt = etree.XSLT(etree.parse(filename))
    except (IOError, etree.XSLTParseError, etree.XMLSyntaxError) as error:
        return str(error)
    return xslt


# =============================================================================
def create_entire_xml(relaxng, elements, validation=True):
    """Create an entire XML document composed of all ``elements``.

    :param dict relaxng:
        A dictionary with the name of the root element, the value of attribute
        version and path to the Relax NG file to validate the result.
    :param list elements:
        A list of :class:`lxml.etree._Element` objects.
    :param bool validation: (default=True)
        Validate the result.
    :rtype: :class:`~pyramid.i18n.TranslationString` or
        :class:`lxml.etree._Element`
    :return:
        An error message or an object :class:`lxml.etree._Element`.
    """
    def _label(elt):
        """Get label or name of ``elt``."""
        label = elt.get('{0}id'.format(XML_NS)) or elt.get('id') \
            or (elt.findtext('login') is not None and elt.findtext('login')) \
            or (elt.findtext('label') is not None and elt.findtext('label')) \
            or (elt.findtext('title') is not None and elt.findtext('title')) \
            or '~'
        return normalize_spaces(label)

    # Create XML root
    if 'namespace' in relaxng:
        root = '{{{0}}}{1}'.format(relaxng['namespace'], relaxng['root'])
        root_elt = etree.Element(
            root, version=relaxng['version'],
            nsmap={None: relaxng['namespace']})
    else:
        root = relaxng['root']
        root_elt = etree.Element(relaxng['root'], version=relaxng['version'])

    # Single export
    if len(elements) == 1 and 'namespace' not in relaxng:
        root_elt.append(elements[0])
    # Multiple export or namepsace
    else:
        tag = None
        for elt in elements:
            if tag != elt.tag:
                tag = elt.tag
                if tag.endswith('s'):
                    root_elt.append(etree.Comment(' {0} '.format('=' * 68)))
                    root_elt.append(etree.Comment('{0:^70}'.format(tag)))
                    root_elt.append(etree.Comment(' {0} '.format('=' * 68)))
                    group_elt = root_elt
                else:
                    root_elt.append(etree.Comment(' {0} '.format('=' * 68)))
                    root_elt.append(etree.Comment('{0:^70}'.format(
                        '{0}s'.format(tag))))
                    root_elt.append(etree.Comment(' {0} '.format('=' * 68)))
                    group_elt = etree.SubElement(root_elt, '{0}s'.format(tag))
            if tag.endswith('s'):
                group_elt.append(elt)
            else:
                group_elt.append(etree.Comment(' {0:~^66} '.format(
                    ' {0} '.format(_label(elt)))))
                group_elt.append(elt)

    # Validate the result
    error = None
    if validation:
        if 'namespace' in relaxng:
            root_elt = etree.XML(etree.tostring(root_elt, encoding='utf-8'))
        error = validate_xml(
            etree.ElementTree(root_elt), relaxng4validation(relaxng), True)

    return root_elt if error is None else translate(error)


# =============================================================================
def i18n_xml_text(root_elt, xpath, namespaces=None):
    """Return a dictionary with the localized texts contained in an XML
    element.

    :type  root_elt: lxml.etree.Element
    :param root_elt:
        XML root element of the localized text.
    :param str xpath:
        XPath expression to select localized texts.
    :param dict namespaces: (optional)
        Dictionary of possible name spaces.
    :rtype: dict
    :return:
        A dictionary such ``{lang1: text_in_lang1,...}``
    """
    i18n = {}
    for elt in root_elt.xpath(xpath, namespaces=namespaces):
        lang = elt.get('{0}lang'.format(XML_NS))
        if lang and elt.text:
            i18n[lang] = normalize_spaces(elt.text)
    return i18n


# =============================================================================
def db2xml_i18n_labels(dbitem, root_elt, depth):
    """Serialize i18n label and descriptio.

    :param dbitem:
        SQLAlchemy item.
    :type  root_elt: lxml.etree.Element
    :param root_elt:
        Root XML element.
    :param int depth:
        Depth of the parent element in the entire XML structure.
    """
    i18n = loads(dbitem.i18n_label)
    for lang in sorted(i18n):
        elt = etree.SubElement(root_elt, 'label')
        elt.set('{0}lang'.format(XML_NS), lang)
        elt.text = i18n[lang]

    if hasattr(dbitem, 'i18n_description'):
        i18n = dbitem.i18n_description
        if i18n:
            for lang in sorted(i18n):
                elt = etree.SubElement(root_elt, 'description')
                elt.set('{0}lang'.format(XML_NS), lang)
                elt.text = xml_wrap(i18n[lang], depth)


# =============================================================================
def xml_wrap(text, depth):
    """Wrap a text according to the depth of the parent element.

    :param str text:
        Text to wrap and indent.
    :param int depth:
        Depth of the parent element in the entire XML structure.
    :rtype: str
    """
    indent = ' ' * 2 * (depth + 1)
    return '\n{0}\n{1}'.format(
        '\n'.join(
            ['{0}{1}'.format(indent, k)
             for k in wrap(text, 79 - 2 * (depth + 1))]), ' ' * 2 * depth)


# =============================================================================
def check_chrysalio_rng(relaxng_dir):
    """Check if the Relax NG files in ``relaxng_dir`` directory is the last
    version and possibly update them.

    :param str relaxng_dir:
        Directory for Relax NG files.
    """
    relaxng_dir = abspath_from_asset_spec(relaxng_dir)
    cio_relaxng_dir = join(dirname(__file__), '..', 'RelaxNG')
    for name in cmpfiles(cio_relaxng_dir, relaxng_dir,
                         ('chrysalio.rnc', 'chrysalio.rng'))[1]:
        try:
            copy2(join(cio_relaxng_dir, name), relaxng_dir)
        except IOError:  # pragma: nocover
            LOG.warning('"%s" is not up to date.', name)
