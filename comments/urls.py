from django.conf.urls.defaults import *

urlpatterns = patterns('comments.views',
    url(r'^post/$',          'post_comment',       name='comment-post-comment'),
)
