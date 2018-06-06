#!/usr/bin/env python2
# vim:fileencoding=utf-8
from __future__ import unicode_literals, division, absolute_import, print_function
from calibre.web.feeds.news import BasicNewsRecipe

class AdvancedUserRecipe1528300023(BasicNewsRecipe):
    #api doc:  https://blog.csdn.net/mycc/article/details/50808935
    title          = 'Raku\u9171\u7684\u8ba2\u9605'
    __author__     = 'Nagisa'
    oldest_article = 2
    max_articles_per_feed = 10
    auto_cleanup   = True

    feeds          = [
        ('\u73c2\u5b66\u677e\u9f20\u4f1a', 'http://songshuhui.net/feed'),
        ('\u962e\u4e00\u5cf0', 'http://www.ruanyifeng.com/blog/atom.xml'),
        ('\u77e5\u4e4e\u6bcf\u65e5\u7cbe\u9009', 'https://www.zhihu.com/rss'),
        ('\u597d\u5947\u5fc3\u65e5\u62a5', 'http://www.qdaily.com/feed.xml'),
        ('\u9177\u58f3-\u9648\u7693', 'https://coolshell.cn/feed'),
        ('Laruence-\u98ce\u96ea\u4e4b\u9685', 'http://www.laruence.com/feed'),
    ]
