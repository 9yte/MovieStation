from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

from . import views


urlpatterns = patterns('',
                       url(r'^/register$', views.register),
                       url(r'^/login$', views.login),
                       url(r'^/logout$', views.logout),
                       url(r'^/follow$', views.follow),
                       url(r'^/unfollow$', views.unfollow),
                       url(r'^/(?P<username>\w+)$', views.show_profile),
                       url(r'^', views.homepage),
)