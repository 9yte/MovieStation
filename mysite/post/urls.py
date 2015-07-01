from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

from . import views


urlpatterns = patterns('',
                       url(r'^new_post/(?P<movie_id>\d+)$', views.post),
                       url(r'^get_post$', views.get_post),
                       url(r'^(?P<post_id>\d+)/like$', views.like),
                       url(r'^(?P<post_id>\d+)/comment', views.comment),
                       url(r'^get_notif/$', views.getNotif),
                       url(r'^(?P<post_id>\d+)$', views.show_post),
)