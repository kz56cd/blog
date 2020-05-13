#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kz56cd'
SITENAME = 'yardsale'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Custom theme
THEME = './themes/nice-blog'

# Custom theme(for 'nice-blog')
THEME_COLOR = 'black'
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
SIDEBAR_ABOUT = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sequi quae hic dicta eius ad quam eligendi minima praesentium voluptatum? Quidem quaerat eaque libero velit impedit dicta, repudiandae sapiente. Deserunt, excepturi.'
COPYRIGHT = "© 2020 kz56cd"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True