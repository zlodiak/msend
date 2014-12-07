from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^mailsend/', include('mailsend.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
