from django.conf.urls import patterns, url, include
from django_bro_tables import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'regex', views.RegexViewSet)
router.register(r'regexentry', views.RegexEntryViewSet)

urlpatterns = patterns('',
    url(r'regex/(?P<pk>[0-9]+)/$', views.RegexDetailView.as_view(), name='regex-detail'),
    url(r'regex/csv/(?P<name>\S+).csv$', views.CSV.as_view(), name='regex-csv'),
    url(r'^', include(router.urls)),
)
