from wagtail.images.formats import Format, register_image_format

register_image_format(Format("small", "Small Right", "richtext-image right", "max-400x400"))

register_image_format(Format("smallleft", "Small Left", "richtext-image left", "max-400x400"))