from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

    # Examples:
urlpatterns = patterns('newapp.views',
    # url(r'^$', 'newsite.views.home', name='home'),
    # url(r'^newsite/', include('newsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)


urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
