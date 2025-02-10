#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CycleUsyer'
SITENAME = "GeoPyTool"
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Asia/Chongqing'
THEME = "cg"
DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (("Homepage","http://geopytool.com"), 
            ('Forum', 'https://github.com/GeoPyTool/GeoPyTool/issues'),   
            ("Discuss on Slack","https://geopytool.slack.com/"),  
            ("加入QQ群","http://geopytool.com/zhong-wen-jian-jie.html"),      
            ("Installation","http://geopytool.com/installation-expert.html"),   
            ("Templates","https://github.com/GeoPyTool/GeoPyTool/tree/master/DataFileSamples"),              
            ("Demo","http://geopytool.com/demonstration.html"),  
            ('Github', 'https://github.com/GeoPyTool/GeoPyTool'),  
            ("Archives","http://geopytool.com/archives.html"),      
		 )

# Blogroll
LINKS = (
        ("Introduction","http://geopytool.com/introduction.html"),  
        ("Functions","http://geopytool.com/functions.html"),                       
        ("Installation","http://geopytool.com/installation-expert.html"),       
        ("Demonstration","http://geopytool.com/demonstration.html"),  
        ("Download","http://geopytool.com/download.html"),  

        ("中文简介","http://geopytool.com/zhong-wen-jian-jie.html"),  
        ("功能列表","http://geopytool.com/gong-neng-lie-biao.html"),        
        ("安装指南","http://geopytool.com/an-zhuang-zhi-nan-jin-jie.html"),          
        ("功能演示","http://geopytool.com/yan-shi-shi-pin.html"),  
        ("下载链接","http://geopytool.com/download.html"),
        
        )

# Social widget
SOCIAL = (('github','https://github.com/GeoPyTool/GeoPyTool'),
		)

SHARE = (('twitter', 'http://twitter.com/share', '?text=', '&amp;url='),
         ('facebook', 'http://facebook.com/sharer.php', '?t=', '&amp;u='),
         ('google-plus', 'http://plus.google.com/share', '?text=', '&amp;url='))


DISQUS_SITENAME = "cycleuser"

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ["sitemap","neighbors","related_posts","tag_cloud", "related_posts"]
#sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.8,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
}
}
#相关文章
RELATED_POSTS_MAX = 1
