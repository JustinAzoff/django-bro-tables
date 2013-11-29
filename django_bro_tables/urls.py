from django.conf.urls import patterns, url, include
from django_bro_tables import views
from django.contrib.auth.decorators import login_required

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'regex', views.RegexViewSet)
router.register(r'regexentry', views.RegexEntryViewSet)

router.register(r'table', views.TableViewSet,'bro_table')

urlpatterns = patterns('',
    url(r'api/regex/(?P<pk>[0-9]+)/$', views.RegexDetailView.as_view(), name='regex-detail'),
    url(r'api/regex/csv/(?P<name>\S+).csv$', views.RegexFlat.as_view(), name='regex-csv'),
    url(r'api/table/flat/(?P<name>\S+).csv$', views.TableFlat.as_view(), name='bro_table-flat'),
    url(r'api/', include(router.urls)),
    url(r'^tables$', login_required(views.TableList.as_view()), name='tables-list')
)
