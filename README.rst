========================
django CMS Light Gallery
========================

|PyPI version|

django CMS plugin for `Light Gallery
1.4.0 <https://github.com/sachinchoolur/lightGallery>`__

Installation
============

First, add ``djangocms-light-gallery`` to your requirements.txt or install the plugin ::

    pip install djangocms-light-gallery


Then add the plugin to settings.py ::

    INSTALLED_APPS = [
      // ...
      'light_gallery',
      // ...


Run the migrations ::

    python manage.py migrate light_gallery

This plugin relies on javascript, ensure you have a js block in your template ::

    {% render_block "js" %}


Should now see ``Light Gallery`` as a component in django CMS

.. |PyPI version| image:: https://badge.fury.io/py/djangocms-light-gallery.svg
   :target: https://badge.fury.io/py/djangocms-light-gallery
