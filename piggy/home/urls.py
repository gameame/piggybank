from django.conf.urls.defaults import *

urlpatterns = patterns('django.views.generic.simple',
    # Example:
    (r'^$', 'direct_to_template', {'template': 'home.html'}),
    (r'^about', 'direct_to_template', {'template': 'about.html'}),
)
