from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from ..useraccount.views import *
from .views import *

urlpatterns = patterns('', url(r'^admin', include(admin.site.urls)),
                       url(r'^home', homepage),
                       url(r'^profile', show_profile),
                       url(r'^movieprofile', show_movie),
                       url(r'^post', show_post),
                       url(r'^register', register),
                       url(r'^search', show_searchResult),
                       url(r'^', mainpage)
)