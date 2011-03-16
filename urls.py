from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^blog/$', 'dblog.views.index'),
    (r'^blog/(?P<blog_id>\d+)/$', 'dblog.views.readblog'),
    (r'^blog/(?P<blog_id>\d+)/comment/$', 'dblog.views.comment'),
    (r'^blog/(?P<blog_id>\d+)/comment/add/$', 'dblog.views.addComment'),
    (r'^blog/(?P<blog_id>\d+)/postComment/$', 'dblog.views.postComment'),
    (r'^blog/writeBlog/$', 'dblog.views.writeBlog'),
    (r'^blog/postEntry/$', 'dblog.views.postEntry'),

   # (r'^simpleblog/$', 'simpleblog.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
