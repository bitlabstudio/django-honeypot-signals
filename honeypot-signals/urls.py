"""URLs for honeypot-signals application."""

from django.conf.urls.defaults import *


urlpatterns = patterns('honeypot-signals.views',
    url(r'^$', view='index', name='honeypot-signals_index'),
)
