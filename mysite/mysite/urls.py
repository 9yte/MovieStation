from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from . import views

urlpatterns = patterns('', url(r'^admin', include(admin.site.urls)),
                       url(r'^movieprofile/', include('movie.urls')),
                       url(r'^user', include('useraccount.urls')),
                       url(r'^home$', include('useraccount.urls')),
                       url(r'^profile/', include('useraccount.urls')),
                       url(r'^post', include('post.urls')),
                       url(r'^search$', views.show_searchResult),
                       url(r'^', views.mainpage)
)