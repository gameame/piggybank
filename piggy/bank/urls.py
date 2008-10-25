from django.conf.urls.defaults import *
from piggy import settings

urlpatterns = patterns('',
    # Example:
    (r'^$', 'piggy.bank.views.index'),
    (r'^(?P<piggy_id>\d+)$', 'piggy.bank.views.detail'),
    (r'^(?P<piggy_id>\d+)/donate$', 'piggy.bank.views.donate'),
    
    
    # Development environment
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
