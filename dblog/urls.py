from django.conf.urls.defaults import *

urlpatterns = patterns('dblog.views',
    # Example:
    (r'^$', 'index'),
    (r'^(?P<blog_id>\d+)/$', 'readblog'),
    (r'^(?P<blog_id>\d+)/comment/$', 'comment'),
    (r'^(?P<blog_id>\d+)/comment/add/$', 'addComment'),
    (r'^(?P<blog_id>\d+)/postComment/$', 'postComment'),
    (r'^writeBlog/$', 'writeBlog'),
    (r'^postEntry/$', 'postEntry'),
)

