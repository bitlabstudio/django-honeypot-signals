from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^example/', include('honeypot-signals.urls')),
)
