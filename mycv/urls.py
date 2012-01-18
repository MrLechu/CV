from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('cv.mycv.views',
    url(r'^$', 'index')
)