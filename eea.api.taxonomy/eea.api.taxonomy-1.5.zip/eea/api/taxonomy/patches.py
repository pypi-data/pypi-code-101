""" Monkey patches
"""
# pylint: disable = C0111, W0702, C1801

from plone import api
from collective.taxonomy import LEGACY_PATH_SEPARATOR
from collective.taxonomy import NODE
from collective.taxonomy import PATH_SEPARATOR
from collective.taxonomy import PRETTY_PATH_SEPARATOR
from collective.taxonomy.vocabulary import Vocabulary


def taxonomy_call(self, context):
    if not self.data:
        return Vocabulary(self.name, {}, {}, {}, 2)

    request = getattr(context, "REQUEST", None)
    if not request:
        language = 'en'
    else:
        language = self.getCurrentLanguage(request)

    return self.makeVocabulary(language)


def taxonomy_translate(
    self,
    msgid,
    mapping=None,
    context=None,
    target_language=None,
    default=None,
    msgid_plural=None,
    default_plural=None,
    number=None,
):
    if target_language is None or target_language not in self.inverted_data:
        try:
            target_language = str(api.portal.get_current_language())
        except:
            target_language = 'en'

        if target_language not in self.inverted_data:
            # might be a non standard language or the portal has
            # switched standard language after creating the taxonomy
            lngs = list(self.inverted_data.keys())
            if not len(lngs):
                # empty taxonomy
                return ""
            target_language = lngs[0]

    if msgid not in self.inverted_data[target_language]:
        return ""

    if self.version is not None and self.version.get(target_language) != 2:
        path_sep = LEGACY_PATH_SEPARATOR
    else:
        path_sep = PATH_SEPARATOR

    path = self.inverted_data[target_language][msgid]
    pretty_path = path[1:].replace(path_sep, PRETTY_PATH_SEPARATOR)

    if mapping is not None and mapping.get(NODE):
        pretty_path = pretty_path.rsplit(PRETTY_PATH_SEPARATOR, 1)[-1]

    return pretty_path
