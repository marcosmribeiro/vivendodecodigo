# codding: utf-8

from django.conf.urls import patterns, url


urlpatterns = patterns('vdc.core.views',
    url(r'^$', 'home', name='home'),
)