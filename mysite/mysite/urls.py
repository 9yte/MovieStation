from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

import mysite.views as views

urlpatterns = patterns('', url(r'^admin', include(admin.site.urls)),
                       url(r'^home', views.homepage),
                       url(r'^profile', views.show_profile),
                       url(r'^movieprofile', views.show_movie),
                       url(r'^post', views.show_post),
                       url(r'^search', views.show_searchResult),
                       url(r'^', views.mainpage)
)