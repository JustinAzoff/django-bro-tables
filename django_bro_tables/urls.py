from django.conf.urls import patterns, url, include
from django_bro_tables import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'regex', views.RegexViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'regex/(?P<name>\S+).csv$', views.CSV.as_view(), name='csv')
)
