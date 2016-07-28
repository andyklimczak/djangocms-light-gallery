from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from filer.fields.folder import FilerFolderField
from filer.models.imagemodels import Image
import uuid

class LightGallery(CMSPlugin):
    folder = FilerFolderField(
        verbose_name=_('Folder')
    )
    zoom = models.BooleanField(_("Enable Zoom"), default=False, help_text=_("Enable/disable zoom for this gallery"))
    zoomScale = models.PositiveIntegerField(_("Scale"), default=1, help_text=_("Value of zoom should be incremented/decremented"))

    fullscreen = models.BooleanField(_("Enable Fullscreen"), default=False, help_text=_("Enable/disable fullscreen for this gallery"))

    thumbnails = models.BooleanField(_("Enable Thumbnails"), default=False, help_text=_("Enable/disable thumbnails for this gallery"))

    def get_folder_images(self):
        images = self.folder.files.instance_of(Image)
        return images.filter(is_public=True)

    def generate_id(self):
        return str(uuid.uuid4().fields[-1])[:7]
