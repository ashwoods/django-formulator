from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]


if 'grappelli' in settings.INSTALLED_APPS:
    urlpatterns = urlpatterns + [
        url(r'^grappelli/', include('grappelli.urls')),
    ]
