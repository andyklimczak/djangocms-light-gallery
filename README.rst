|PyPI version|

DjangoCMS plugin for `Light Gallery
1.4.0 <https://github.com/sachinchoolur/lightGallery>`__

`Example with default
settings <https://andy-djangocms-test.herokuapp.com/light-gallery/>`__

Installation
============

First, add ``djangocms-light-gallery`` to your requirements.txt or install the plugin ::
    pip install djangocms-light-gallery


Then add the plugin to settings.py ::
    INSTALLED_APPS = [
    // ...
    'light_gallery',
    // ...


Finally, run the migrations ::
    python manage.py migrate


Should now see ``Light Gallery`` as a component in djangocms

.. |PyPI version| image:: https://badge.fury.io/py/djangocms-light-gallery.svg
   :target: https://badge.fury.io/py/djangocms-light-gallery
