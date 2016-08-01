from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from filer.fields.folder import FilerFolderField
from filer.models.imagemodels import Image
import uuid

MODES = [['lg-slide', 'lg-slide'], ['lg-fade', 'lg-fade'], ['lg-zoom-in', 'lg-zoom-in'], ['lg-zoom-in-big', 'lg-zoom-in-big'], ['lg-zoom-out', 'lg-zoom-out'], ['lg-zoom-out-big', 'lg-zoom-out-big'], ['lg-zoom-out-in', 'lg-zoom-out-in'], ['lg-zoom-in-out', 'lg-zoom-in-out'], ['lg-soft-zoom', 'lg-soft-zoom'], ['lg-scale-up', 'lg-scale-up'], ['lg-slide-circular', 'lg-slide-circular'], ['lg-slide-circular-vertical', 'lg-slide-circular-vertical'], ['lg-slide-vertical', 'lg-slide-vertical'], ['lg-slide-vertical-growth', 'lg-slide-vertical-growth'], ['lg-slide-skew-only', 'lg-slide-skew-only'], ['lg-slide-skew-only-rev', 'lg-slide-skew-only-rev'], ['lg-slide-skew-only-y', 'lg-slide-skew-only-y'], ['lg-slide-skew-only-y-rev', 'lg-slide-skew-only-y-rev'], ['lg-slide-skew', 'lg-slide-skew'], ['lg-slide-skew-rev', 'lg-slide-skew-rev'], ['lg-slide-skew-cross', 'lg-slide-skew-cross'], ['lg-slide-skew-cross-rev', 'lg-slide-skew-cross-rev'], ['lg-slide-skew-ver', 'lg-slide-skew-ver'], ['lg-slide-skew-ver-rev', 'lg-slide-skew-ver-rev'], ['lg-slide-skew-ver-cross', 'lg-slide-skew-ver-cross'], ['lg-slide-skew-ver-cross-rev', 'lg-slide-skew-ver-cross-rev'], ['lg-lollipop', 'lg-lollipop'], ['lg-lollipop-rev', 'lg-lollipop-rev'], ['lg-rotate', 'lg-rotate'], ['lg-rotate-rev', 'lg-rotate-rev'], ['lg-tube', 'lg-tube']]
CURRENT_PAGER_POSITIONS = [['left', 'Left'], ['middle', 'Middle'], ['right', 'Right']]

class LightGallery(CMSPlugin):
    folder = FilerFolderField(
        verbose_name=_('Folder')
    )
    pageThumbWidth = models.CharField(_("Page Thumb Width"), max_length=255, default="150", help_text=_("Width of thumbnail on page"))
    pageThumbHeight = models.CharField(_("Page Thumb Height"), max_length=255, default="150", help_text=_("Height of thumbnail on page"))

    mode = models.CharField(_("Mode"), choices=MODES, default=MODES[0], help_text=_("Type of transition between images"), max_length=255)
    cssEasing = models.CharField(_("CSS Easing"), max_length=255, default="ease", help_text=_("Type of easing to be used for css animations"))
    easing = models.CharField(_("Easing"), max_length=255, default="linear", help_text=_("Type of easing to be used for jquery animations"))
    speed = models.PositiveIntegerField(_("Speed"), default=600, help_text=_("Transition duration (in ms)"))
    height = models.CharField(_("Height"), max_length=255, default="100%", help_text=_("Height of the gallery"))
    width = models.CharField(_("Width"), max_length=255, default="100%", help_text=_("Width of the gallery"))
    addClass = models.CharField(_("Add Class"), max_length=255, default="", help_text=_("Add custom class for gallery, can be used to set different style for different gallery"), blank=True)
    startClass = models.CharField(_("Add Class"), max_length=255, default="lg-start-zoom", help_text=_("Starting animation class for the gallery"))
    backdropDuration = models.PositiveIntegerField(_("Backdrop Duration"), default=150, help_text=_("Lightgallery backdrop transtion duration. Do not change the value of backdrop via css"))
    hideBarsDelay = models.PositiveIntegerField(_("Hide Bars Delay"), default=6000, help_text=_("Delay for hiding gallery controls in ms"))
    useLeft = models.BooleanField(_("Use Left"), default=False, help_text=_("Force lightgallery to use css left property instead of transform"))
    closable = models.BooleanField(_("Closable"), default=True, help_text=_("Allows clicks on dimmer to close gallery"))
    loop = models.BooleanField(_("Loop"), default=True, help_text=_("If false, will disable the ability to loop back to the beginning of the gallery when on the last element"))
    escKey = models.BooleanField(_("ESC Key"), default=True, help_text=_("Whether the LightGallery could be closed by pressing the 'Esc' key"))
    keyPress = models.BooleanField(_("Key Press"), default=True, help_text=_("Enable keyboard navigation"))
    controls = models.BooleanField(_("Controls"), default=True, help_text=_("If false, prev/next buttons will not be displayed"))
    slideEndAnimation = models.BooleanField(_("Slide End Animation"), default=True, help_text=_("Enable slideEnd animation"))
    hideControlOnEnd = models.BooleanField(_("Hide Control On End"), default=False, help_text=_("If true, prev/next button will be hidden on first/last image"))
    mousewheel = models.BooleanField(_("Mousewheel"), default=True, help_text=_("Change slide on mousewheel"))
    preload = models.PositiveIntegerField(_("Preload"), default=1, help_text=_("Number of preload slides. will execute only after the current slide is fully loaded"))
    showAfterLoad = models.BooleanField(_("Show After Load"), default=True, help_text=_("Show Content once it is fully loaded"))
    nextHtml = models.CharField(_("Next Html"), max_length=255, default="", help_text=_("Custom html for next control"), blank=True)
    prevHtml = models.CharField(_("Prev Html"), max_length=255, default="", help_text=_("Custom html for prev control"), blank=True)
    index = models.PositiveIntegerField(_("Index"), default=0, help_text=_("Allows to set which image/video should load initially"))
    iframeMaxWidth = models.CharField(_("IFrame Max Width"), max_length=255, default="100%", help_text=_("Set maximum width for iframe."))
    download = models.BooleanField(_("Download"), default=True, help_text=_("Enable download button"))
    counter = models.BooleanField(_("Counter"), default=True, help_text=_("Whether to show total number of images and index number of currently displayed image"))
    appendCounterTo = models.CharField(_("Append Counter To"), max_length=255, default=".lg-toolbar", help_text=_("Where the counter should be appended"))
    swipeThreshold = models.PositiveIntegerField(_("Swipe Threshold"), default=50, help_text=_("By setting the swipeThreshold (in px) you can set how far the user must swipe for the next/prev image"))
    enableDrag = models.BooleanField(_("Enable Drag"), default=True, help_text=_("Enables desktop mouse drag support"))
    enableTouch = models.BooleanField(_("Enable Touch"), default=True, help_text=_("Enables touch support"))

    thumbnails = models.BooleanField(_("Enable Thumbnails"), default=True, help_text=_("Enable/disable thumbnails for this gallery"))
    animateThumb = models.BooleanField(_("Enable Thumbnail Animation "), default=True)
    currentPagerPosition = models.CharField(_("Current Pager Position"), choices=CURRENT_PAGER_POSITIONS, max_length=255, default=CURRENT_PAGER_POSITIONS[1][0], help_text=_("Position of selected thumbnail"))
    thumbWidth = models.PositiveIntegerField(_("Thumb Width"), default=100, help_text=_("Width of each thumbnails"))
    thumbContHeight = models.PositiveIntegerField(_("Thumb Container Height"), default=100, help_text=_("Height of the thumbnail container including padding and border"))
    thumbMargin = models.PositiveIntegerField(_("Thumb Margin"), default=5, help_text=_("Spacing between each thumbnails"))
    toggleThumb = models.BooleanField(_("Toggle Thumbnail Button"), default=True, help_text=_("Whether to display thumbnail toggle button"))
    pullCaptionUp = models.BooleanField(_("Pull Captions Up"), default=True, help_text=_("Pull captions above thumbnails"))
    enableThumbDrag = models.BooleanField(_("Enable Thumbnail Drag"), default=True, help_text=_("Enables desktop mouse drag support for thumbnails"))
    enableThumbSwipe = models.BooleanField(_("Enable Thumbnail Swipe"), default=True, help_text=_("Enables thumbnail touch/swipe support for touch devices"))
    swipeThreshold = models.PositiveIntegerField(_("Swipe Threshold"), default=50, help_text=_("By setting the swipeThreshold (in px) you can set how far the user must swipe for the next/prev slide"))

    zoom = models.BooleanField(_("Enable Zoom"), default=False, help_text=_("Enable/disable zoom for this gallery"))
    zoomScale = models.PositiveIntegerField(_("Scale"), default=1, help_text=_("Value of zoom should be incremented/decremented"))
    zoomEnableZoomAfter = models.PositiveIntegerField(_("Enable Zoom After"), default=50, help_text=_("Number in ms"))
    zoomActualSize = models.BooleanField(_("Actual Size"), default=False, help_text=_("Enable actual pixel icon"))

    fullscreen = models.BooleanField(_("Enable Fullscreen"), default=False, help_text=_("Enable/disable fullscreen for this gallery"))

    pager = models.BooleanField(_("Enable Pager"), default=False, help_text=_("Enable/disable pager for this gallery"))

    hash = models.BooleanField(_("Enable Hash"), default=False, help_text=_("Enable/Disable hash plugin"))
    galleryId = models.PositiveIntegerField(_("Gallery Id"), default=1, help_text=("Unique id for each gallery. It is mandatory when you use hash plugin for multiple galleries on the same page"))

    def get_folder_images(self):
        images = self.folder.files.instance_of(Image)
        return images.filter(is_public=True)

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]

    def parse_page_thumb_width_height(self):
        return "%sx%s" % (self.pageThumbWidth, self.pageThumbHeight)
