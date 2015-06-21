from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
admin.autodiscover()

from . import views

urlpatterns = patterns('', url(r'^admin', include(admin.site.urls)),
                       url(r'^movieprofile/', include('movie.urls')),
                       url(r'^search', include('search.urls')),
                       url(r'^user', include('useraccount.urls')),
                       url(r'^home$', include('useraccount.urls')),
                       url(r'^profile', include('useraccount.urls')),
                       url(r'^post/', include('post.urls')),
                       url(r'^search$', views.show_searchResult),
                       url(r'^$', views.mainpage)
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))