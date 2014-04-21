from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmscanner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('lectorbarras.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
