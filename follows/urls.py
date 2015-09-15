from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from Person.views import ListaFollow, AddFollow, RemoveFollow

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListaFollow.as_view(), name="lista_follow"),
    url(r'^add_follow/(?P<id>\d{1,})/$', AddFollow.as_view(), name='add_follow'),
    url(r'^remove_follow/(?P<id>\d{1,})/$', RemoveFollow.as_view(), name='remove_follow')
]
