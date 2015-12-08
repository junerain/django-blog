# -*- coding: utf-8 -*-
__author__ = 'junerain'
from django.conf.urls import patterns, include, url
from article.views import RSSFeed

urlpatterns = patterns('',
    url(r'^$', 'article.views.home', name='article_home'),
#    url(r'^detail/','west.views.detail'),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    #����?P<my_args>�����������ڱ�ʶƥ�������
#    url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
#    url(r'^(?P<my_args>\d+)/$', 'article.views.readdb', name='readdb'),
 #   url(r'^feed/','article.views.templay'),
    url(r'^aboutme/','article.views.about_me',name='aboutme'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
    url(r'^search/$','article.views.blog_search', name = 'search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"),  #����ӵ�urlconf, ����name����ΪRSS, ������ģ����ʹ��url
)
