from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

from . import views


urlpatterns = patterns('',
                       url(r'^(?P<movie_id>\d+)$', views.show_movie),
                       url(r'^', views.mainpage),
)