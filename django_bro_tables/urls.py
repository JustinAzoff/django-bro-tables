from django.conf.urls import patterns, url, include
from django_bro_tables import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'regex', views.RegexViewSet)
router.register(r'regexentry', views.RegexEntryViewSet)

router.register(r'table', views.TableViewSet)

urlpatterns = patterns('',
    url(r'api/regex/(?P<pk>[0-9]+)/$', views.RegexDetailView.as_view(), name='regex-detail'),
    url(r'api/regex/csv/(?P<name>\S+).csv$', views.RegexFlat.as_view(), name='regex-csv'),
    url(r'api/table/flat/(?P<name>\S+).csv$', views.TableFlat.as_view(), name='table-flat'),
    url(r'api/', include(router.urls)),
)
