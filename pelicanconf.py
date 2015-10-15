#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brad Miller'
SITENAME = 'A Reputable Journal'
SITEURL = 'http://reputablejournal.com'

PATH = 'content'
PLUGINS = ['pelican_youtube', 'gallery', 'thumbnailer', 'ipynb', 'tag_cloud',
]
STATIC_PATHS=['images','static']
TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

MARKUP = ('rst', 'md', 'ipynb')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Runestone Interactive', 'http://runestoneinteractive.org'),
         ('Python Books', 'http://interactivepython.org/'),
         ('Luther College', 'http://www.cs.luther.edu'),)


THEME='themes/Responsive-Pelican'
#THEME='themes/notmyidea-cms'


TAG_CLOUD_STEPS=4
TAG_CLOUD_MAX_ITEMS=100

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/bnmnetp'),
          ('Github', 'http://github.com/bnmnetp'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Thumbnailer and Gallery Conf

RESIZE = [
    ('gallery', False, 200, 200),
]

IMAGE_PATH = 'images/gallery'
THUMBNAIL_DIR = 'images'
THUMBNAIL_SIZES = {'200x200' : 'gallery200x200'}
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_KEEP_TREE = True


