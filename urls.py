from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^blog/$', 'index'),
    #(r'^blog/(?P<blog_id>\d+)/$', 'readblog'),
    #(r'^blog/(?P<blog_id>\d+)/comment/$', 'comment'),
    #(r'^blog/(?P<blog_id>\d+)/comment/add/$', 'addComment'),
    #(r'^blog/(?P<blog_id>\d+)/postComment/$', 'postComment'),
    #(r'^blog/writeBlog/$', 'writeBlog'),
    #(r'^blog/postEntry/$', 'postEntry'),

    # (r'^simpleblog/$', 'simpleblog.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^blog/', include('dblog.urls')),
    (r'^admin/', include(admin.site.urls)),
)

#urlpatterns += patterns('',
#    (r'^admin/', include(admin.site.urls)),
#)
