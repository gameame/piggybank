from django.conf.urls.defaults import *
from piggy import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^(?P<language_code>[a-z]{2})/piggy/', include('piggy.bank.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^(?P<language_code>[a-z]{2})/', include('piggy.home.urls')),

    # Development environment
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
