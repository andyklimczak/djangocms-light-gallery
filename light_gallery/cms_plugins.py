from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import LightGallery

class LightGallery(CMSPluginBase):
    model = LightGallery
    name = _("Light Gallery")
    render_template = "light_gallery.html"
    cache = False

    fieldsets = (
        (None, {
            'fields': [
                'folder',
            ]
        }),
        (_('Fullscreen'), {
            'classes': ['collapse', ],
            'fields': [
                'fullscreen',
            ]
        }),
        (_('Thumbnails'), {
            'classes': ['collapse', ],
            'fields': [
                'thumbnails',
            ]
        }),
        (_('Zoom'), {
            'classes': ['collapse', ],
            'fields': [
                'zoom',
                'zoomScale',
            ]
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'images': instance.get_folder_images(),
            'id': instance.generate_id(),
            'fullscreen': instance.fullscreen,
            'thumbnails': instance.thumbnails,
            'zoom': instance.zoom,
            'zoomScale': instance.zoomScale,
        });
        return context

plugin_pool.register_plugin(LightGallery)
