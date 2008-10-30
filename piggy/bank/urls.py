from django.conf.urls.defaults import *

urlpatterns = patterns('piggy.bank.views',
    # Example:
    (r'^$', 'index'),
    (r'^(?P<piggy_id>\d+)$', 'detail'),
    (r'^(?P<piggy_id>\d+)/donate$', 'donate'),

)
