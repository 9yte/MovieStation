from django.conf.urls import patterns, url

from django.contrib import admin

admin.autodiscover()

from . import views


urlpatterns = patterns('',
                       url(r'^/$', views.search),
                       url(r'^/result$', views.search_result),
)