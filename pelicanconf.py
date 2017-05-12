#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brad Miller'
SITENAME = 'A Reputable Journal'
SITEURL = 'http://localhost:8000'

PATH = 'content'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_youtube', 'gallery', 'thumbnailer', 'tag_cloud', 'sitemap', 
'liquid_tags.notebook', 'render_math', 'share_post'
]

STATIC_PATHS=['images','static']
TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

MARKUP = ('rst', 'md', 'ipynb')

ADDTHIS_PROFILE='ra-553bcb107aed7add'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
BOOTSTRAP_THEME = 'flatly'

MATH_JAX = {'process_escapes':True}
# Blogroll
LINKS = (('Runestone Interactive', 'http://runestoneinteractive.org'),
         ('Python Books', 'http://interactivepython.org/'),
         ('Everyday Python', 'http://everydaypython.org/'),
         ('Luther College', 'http://www.cs.luther.edu'),
         ('Buy My House', 'http://millerdreamhome.com'),
         )


THEME='themes/pelican-bootstrap3'
#THEME='themes/notmyidea-cms'


TAG_CLOUD_STEPS=4
TAG_CLOUD_MAX_ITEMS=100

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/bnmnetp'),
          ('Github', 'http://github.com/bnmnetp'),)

DEFAULT_PAGINATION = 10

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

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


YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

BANNER='/images/banner.jpg'
BANNER_SUBTITLE='Travel, Cooking, Teaching, Hacking...'
DISPLAY_ARTICLE_INFO_ON_INDEX=True
