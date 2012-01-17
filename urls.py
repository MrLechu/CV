from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cv.views.home', name='home'),
    # url(r'^cv/', include('cv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^mycv/$', 'cv.mycv.views.index'),
    (r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/lechu/apps/cv/templates/'}),
    
)

