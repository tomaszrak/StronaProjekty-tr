from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'zapisy.views.home', name='home'),


                       url(r'^$', 'projekty.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       )

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)