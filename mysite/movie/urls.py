from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

from . import views


urlpatterns = patterns('',
                       url(r'^movieprofile/(?P<id>\d+)$', views.show_movie),
)