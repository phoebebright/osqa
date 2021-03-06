from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext as _
from django.conf import settings

urlpatterns = patterns('',
    (r'', include('forum.urls')),

)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns = patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    ) + urlpatterns

handler404 = 'forum.views.meta.page'
handler500 = 'forum.views.meta.error_handler'
