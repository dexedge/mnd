from wagtail.images.formats import Format, register_image_format

register_image_format(Format("small", "Small Right", "richtext-image small-right", "max-400x400"))

register_image_format(Format("smallleft", "Small Left", "richtext-image small-left", "max-400x400"))

register_image_format(Format("smallcenter", "Small Center", "richtext-image small-center", "max-400x400"))

register_image_format(Format("mediumcenter", "Medium Center", "richtext-image medium-center", "max-600x600"))
