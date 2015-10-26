from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from projekty.forms import Registration
from registration.backends.default.views import RegistrationView


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'zapisy.views.home', name='home'),


                       url(r'^$', 'projekty.views.home', name='home'),
                       url(r'kontakt/$', 'projekty.views.contact', name='contact'),
                       url(r'dane/$', 'projekty.views.your_data', name='your_data'),
                       url(r'projekty/$', 'projekty.views.projects', name='projects'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'accounts/register/$', RegistrationView.as_view(form_class=Registration),
                           name='registration_register'),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       )


if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

