from django.conf.urls import patterns, include, url

from comics.views import index, comics_detail, artist_detail, publisher_detail, article_detail, show_news
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bd.views.home', name='home'),
    # url(r'^bd/', include('bd.foo.urls')),

    url(r'^$', index),                   
    url(r'^comics/(?P<name>[\w|\W]+)/$', comics_detail),
    url(r'^artist/(?P<name>[\w|\W]+)/$', artist_detail),
    url(r'^publisher/(?P<name>[\w|\W]+)/$', publisher_detail),
    url(r'^article/(?P<title>[\w|\W]+)/$', article_detail),
    url(r'^news/$', show_news), 

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
