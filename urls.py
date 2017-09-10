from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/(.*)', admin.site.root),  # django==1.1.0
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/', include('cms.urls')),
)
