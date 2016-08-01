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
                ('pageThumbWidth',
                'pageThumbHeight',),
            ]
        }),
        (_('Core'), {
            'classes': ['collapse', ],
            'fields': [
                'mode',
		'cssEasing',
                'easing',
                'speed',
                'height',
                'width',
                'addClass',
                'startClass',
                'backdropDuration',
                'hideBarsDelay',
                'useLeft',
                'closable',
                'loop',
                'escKey',
                'keyPress',
                'controls',
                'slideEndAnimation',
                'hideControlOnEnd',
                'mousewheel',
                'preload',
                'showAfterLoad',
                'nextHtml',
                'prevHtml',
                'index',
                'iframeMaxWidth',
                'download',
                'counter',
                'appendCounterTo',
                'swipeThreshold',
                'enableDrag',
                'enableTouch',
            ]
        }),
        (_('Gallery Thumbnails'), {
            'classes': ['collapse', ],
            'fields': [
                'thumbnails',
                'animateThumb',
                'currentPagerPosition',
                'thumbWidth',
                'thumbContHeight',
                'thumbMargin',
                'toggleThumb',
                'pullCaptionUp',
                'enableThumbDrag',
                'enableThumbSwipe',
                'swipeThreshold',
            ]
        }),
        (_('Fullscreen'), {
            'classes': ['collapse', ],
            'fields': [
                'fullscreen',
            ]
        }),
        (_('Zoom'), {
            'classes': ['collapse', ],
            'fields': [
                'zoom',
                'zoomScale',
                'zoomEnableZoomAfter',
                'zoomActualSize',
            ]
        }),
        (_('Pager'), {
            'classes': ['collapse', ],
            'fields': [
                'pager',
            ]
        }),
        (_('Hash'), {
            'classes': ['collapse', ],
            'fields': [
                'hash',
                'galleryId',
            ]
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'images': instance.get_folder_images(),
            'pageThumbWidthHeight': instance.parse_page_thumb_width_height(),
            'mode': instance.mode,
            'cssEasing': instance.cssEasing,
            'easing': instance.easing,
            'speed': instance.speed,
            'height': instance.height,
            'width': instance.width,
            'addClass': instance.addClass,
            'startClass': instance.startClass,
            'backdropDuration': instance.backdropDuration,
            'hideBarsDelay': instance.hideBarsDelay,
            'useLeft': instance.useLeft,
            'closable': instance.closable,
            'loop': instance.loop,
            'escKey': instance.escKey,
            'keyPress': instance.escKey,
            'controls': instance.controls,
            'slideEndAnimation': instance.slideEndAnimation,
            'hideControlOnEnd': instance.hideControlOnEnd,
            'mousewheel': instance.mousewheel,
            'preload': instance.preload,
            'showAfterLoad': instance.showAfterLoad,
            'nextHtml': instance.nextHtml,
            'nextHtml': instance.nextHtml,
            'index': instance.index,
            'iframeMaxWidth': instance.iframeMaxWidth,
            'download': instance.download,
            'counter': instance.counter,
            'appendCounterTo': instance.appendCounterTo,
            'swipeThreshold': instance.swipeThreshold,
            'enableDrag': instance.enableDrag,
            'enableTouch': instance.enableTouch,
            'thumbnails': instance.thumbnails,
            'animateThumb': instance.animateThumb,
            'currentPagerPosition': instance.currentPagerPosition,
            'thumbWidth': instance.thumbWidth,
            'thumbContHeight': instance.thumbContHeight,
            'thumbMargin': instance.thumbMargin,
            'toggleThumb': instance.toggleThumb,
            'pullCaptionUp': instance.pullCaptionUp,
            'enableThumbDrag': instance.enableThumbDrag,
            'enableThumbSwipe': instance.enableThumbSwipe,
            'swipeThreshold': instance.swipeThreshold,
            'id': instance.generate_id(),
            'fullscreen': instance.fullscreen,
            'zoom': instance.zoom,
            'zoomScale': instance.zoomScale,
            'zoomEnableZoomAfter': instance.zoomEnableZoomAfter,
            'zoomActualSize': instance.zoomActualSize,
            'pager': instance.pager,
            'hash': instance.hash,
            'galleryId': instance.galleryId,
        });
        return context

plugin_pool.register_plugin(LightGallery)
