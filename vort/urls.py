from django.conf.urls import include, url
from django.contrib import admin
from larb import views
admin.autodiscover()

urlpatterns = [
    # prevent the extra are-you-sure-you-want-to-logout step on logout
    # (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    # url(r'^', include('larb.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
