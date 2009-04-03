from django.conf.urls.defaults import *

urlpatterns = patterns('tagging.views',
    url(r'^(?P<slug>[-\w]+)/$', 'tag_view', name = 'tag-view'),
)
