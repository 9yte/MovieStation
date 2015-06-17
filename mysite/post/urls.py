from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

from . import views


urlpatterns = patterns('',
                       url(r'^new_post/(?P<movie_id>\d+)$', views.post),
                       url(r'^(?P<id>\d+)$', views.show_post),
)