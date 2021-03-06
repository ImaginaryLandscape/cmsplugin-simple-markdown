=========================
NOTE
=========================

This is a fork intended to make some duct tape quality fixes for newer versions of Django as an interim solution in an effort to upgrade a live site.
I don't recommend you use this if possible. In an ideal world, we would switch to/develop a new plugin, but time didn't permit.


=========================
cmsplugin-simple-markdown
=========================
.. contents:: Table of contents

Simple Markdown plugin is just a simple markdown plugin for django-cms.
It's brutally simple. Just a text area and you'll enter some markdown text and save it.
And the reason why I make this is that, I really couldn't find any simple as stupid plugin
for django-cms, all I've found was fancy with a lot of java script stuff.


Requirements
=============

- django-cms
- django-markdown

Installation
==============

PyPi
-----

**cmsplugin-simple-markdown** is available on PyPi:

http://pypi.python.org/pypi/cmsplugin-simple-markdown
::

    $ pip install cmsplugin-simple-markdown

Git
---

You can get latest stable changes from GitHub server:
::

    $ git clone https://github.com/Alir3z4/cmsplugin-simple-markdown.git
    $ cd cmsplugin-simple-markdown
    $ python setup.py install

Zip, Tarball
------------

You can grab the latest tarball.

*unix
------

Get the latest tarball & install
::

    $ wget https://github.com/Alir3z4/cmsplugin-simple-markdown/archive/master.tar.gz
    $ tar xvzf cmsplugin-simple-markdown-master.tar.gz && cd cmsplugin-simple-markdown-master
    $ python setup.py install

Windows
-------

Download latest ZIP archive.

https://github.com/Alir3z4/cmsplugin-simple-markdown/archive/master.zip

Extract the archive, and run the following command in root directory of cmsplugin-simple-markdown
::

    $ python setup.py install

Configuration & Usage
----------------------

1. Make sure ``django-markdown`` is configured as described in their `Setup
<https://github.com/klen/django_markdown#id5>`_ section.
2. Add ``cmsplugin_simple_markdown`` to  ``INSTALLED_APPS``.
3. If you are using Django 1.7 or higher add ``'cmsplugin_simple_markdown': 'cmsplugin_simple_markdown.migrations_django',`` to ``MIGRATION_MODULES`` in settings.
4. Create the database tables::

    $ python manage.py migrate
