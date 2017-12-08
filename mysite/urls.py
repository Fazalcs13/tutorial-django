# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from mysite.views import ChatterBotAppView

from . import views
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    #url(r'^', include('cms.urls')),
    url(r'^$', views.coursesTopic_view, name='index'),
    url(r'^logins', views.login_view, name='logins'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^createnewAccount', views.createAccount_view, name='createnewAccount'),
    url(r'^forgotPassword', views.forgotPassword_view, name='forgotPassword'),
    url(r'^resetPassword', views.resetPassword_view, name='resetPassword'),
    url(r'^(?P<course_name>[\w\-]+)/courses', views.courses_view, name='courses'),
    url(r'^(?P<course_name>[\w\-]+)/video/', views.video_view, name='video'),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^chatterbot/', views.ChatterBotAppView, name='chatterbot'),

)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
