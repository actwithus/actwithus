from django.conf.urls.defaults import patterns, include, handler500
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

handler500 # Pyflakes


urlpatterns = patterns(
    '',
    (r'^admin/(.*)', include(admin.site.urls)),

    # Accounts
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),

    # (r'^contacts/', include('awucontacts.urls')),

    # Top-level index
    (r'^$', 'awuproject.views.index', {}, 'siteindex'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
