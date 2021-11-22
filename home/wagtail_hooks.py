import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler, BlockElementHandler
from wagtail.core import hooks

# Paragraph lede style
@hooks.register("register_rich_text_features")
def register_lede_styling(features):
    """Add lede style to richtext editor"""
    feature_name = "lede"
    type_ = "LEDE"

    control = {
        "type": type_,
        "label": "lede",
        "description": "Lede",
        "style": {
            "font-style": "italic",
            "font-weight": "bold"
        }
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        "from_database_format": {'span[class="paragraph-lede"]': InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_: 'span class="paragraph-lede"'}},
    }

    features.register_converter_rule("contentstate", feature_name, db_conversion)
    
    features.default_features.append(feature_name)

# Underline style
@hooks.register("register_rich_text_features")
def register_underline_styling(features):
    """Add inderline style to richtext editor"""
    feature_name = "underline"
    type_ = "UNDERLINE"

    control = {
        "type": type_,
        "label": "U",
        "description": "Underline",
        "style": {
            "text-decoration": "underline",
        }
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        "from_database_format": {'span[style="text-decoration: underline"]': InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_: 'span style="text-decoration: underline"'}},
    }

    features.register_converter_rule("contentstate", feature_name, db_conversion)
    
    features.default_features.append(feature_name)

# Smaller font-size style
@hooks.register("register_rich_text_features")
def register_small_styling(features):
    """Add smaller font-size to richtext editor"""
    feature_name = "small"
    type_ = "SMALL"

    control = {
        "type": type_,
        "label": "small",
        "description": "Smaller font size",
        "style": {
            "font-size": "smaller",
        }
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        "from_database_format": {'span[style="font-size: smaller"]': InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_: 'span style="font-size: smaller"'}},
    }

    features.register_converter_rule("contentstate", feature_name, db_conversion)
    
    features.default_features.append(feature_name)

# Block indent
@hooks.register("register_rich_text_features")
def register_blockindent_feature(features):
    """Add block indent feature to richtext editor"""

    feature_name = "blockindent"
    type_ = "blockindent"

    control = {
        "type": type_,
        "label": "⇥",
        "description": "Block Indent",
        "element": "div",
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.BlockFeature(control)
    )

    db_conversion = {
        "from_database_format": {'p[class=blockindent]': BlockElementHandler(type_)},
        "to_database_format": {
            "block_map": {
                type_: {
                    "element": "p",
                    "props": {"class": "blockindent"},
                }
            }
        },
    }

    features.register_converter_rule("contentstate", feature_name, db_conversion)

    features.default_features.append(feature_name)


# Center paragraph
@hooks.register("register_rich_text_features")
def register_center_feature(features):
    """Add block indent feature to richtext editor"""

    feature_name = "center"
    type_ = "center"

    control = {
        "type": type_,
        "label": "center",
        "description": "Center paragraph",
        "element": "div",
        "style": {
            "margin-left": "auto",
            "margin-right": "auto",
        }
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.BlockFeature(control)
    )

    db_conversion = {
        "from_database_format": {'p[class=center-paragraph]': BlockElementHandler(type_)},
        "to_database_format": {
            "block_map": {
                type_: {
                    "element": "p",
                    "props": {"class": "center-paragraph"},
                }
            }
        },
    }

    features.register_converter_rule("contentstate", feature_name, db_conversion)

    features.default_features.append(feature_name)