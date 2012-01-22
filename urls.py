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
    
    url(r'^$', include('cv.mycv.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/lechu/apps/cv/templates/'}),
)


urlpatterns += patterns('django.views.generic.simple',
    (r'^googled8194f9e4fb53fd6.html$', 'direct_to_template', {'template':'googled8194f9e4fb53fd6.html', 'mimetype':'text/plain'}),
    (r'^robots.txt$', 'direct_to_template', {'template':'robots.txt', 'mimetype':'text/plain'}),
    )