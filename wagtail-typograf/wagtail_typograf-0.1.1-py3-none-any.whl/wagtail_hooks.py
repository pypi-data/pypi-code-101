from wagtail.admin.rich_text.editors.draftail.features import EntityFeature
from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def register_typograf_feature(features):
    feature_name = 'typograf'
    type_ = 'TYPOGRAF'

    control = {
        'type': type_,
        'label': '¶',
        'description': 'Typograf',
    }

    features.register_editor_plugin(
        'draftail', feature_name, EntityFeature(
            control,
            js=['wagtail_typograf/js/typograf.js'],
            css={'all': []},
        )
    )

    features.default_features.insert(0, 'typograf')
