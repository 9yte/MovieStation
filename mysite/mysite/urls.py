from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

import mysite.views as views
import mysite.useraccount.views as useraccount_view

urlpatterns = patterns('', url(r'^admin', include(admin.site.urls)),
                       url(r'^home', views.homepage),
                       url(r'^profile', views.show_profile),
                       url(r'^movieprofile', views.show_movie),
                       url(r'^post', views.show_post),
                       url(r'^register', useraccount_view.register),
                       url(r'^search', views.show_searchResult),
                       url(r'^', views.mainpage)
)