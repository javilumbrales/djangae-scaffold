from django.conf.urls import patterns, include, url

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
router = routers.DefaultRouter()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scaffold.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^csp/', include('cspreports.urls')),
)
