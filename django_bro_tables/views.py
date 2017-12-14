from rest_framework.settings import api_settings
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_csv import renderers as r

from django_bro_tables.models import (
    Regex, RegexEntry,
    Table,
)
from django_bro_tables.serializers import (
    RegexEntrySerializer, RegexDetailSerializer, RegexSerializer,
    TableSerializer
)
from django_bro_tables.renderers import BroTSVRenderer

class RegexViewSet(viewsets.ModelViewSet):
    queryset = Regex.objects.all()
    serializer_class = RegexSerializer

class RegexDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Regex.objects.all()
    serializer_class = RegexDetailSerializer

class RegexEntryViewSet(viewsets.ModelViewSet):
    queryset = RegexEntry.objects.all()
    serializer_class = RegexEntrySerializer

class RegexCsvRenderer(r.CSVRenderer):
    headers = ['pattern', 'flags', 'comment','date_added']

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class RegexFlat(APIView):
    model = Regex
    renderer_classes = [RegexCsvRenderer] + api_settings.DEFAULT_RENDERER_CLASSES
    queryset = Regex.objects.none() #Required for DjangoModelPermissions

    def get(self, request, name, format=None):
        regex = get_object_or_404(Regex, name=name)
        entries = [e for e in regex.entries.all() if not e.disabled]
        serializer = RegexEntrySerializer(entries, many=True, context={'request': request})
        return Response(serializer.data)

class TableFlat(APIView):
    model = Table
    renderer_classes = [BroTSVRenderer]
    queryset = Table.objects.none() #Required for DjangoModelPermissions

    def get(self, request, name, format=None):
        table = get_object_or_404(Table, name=name)
        entries = table.flat_entries
        return Response(entries)


class TableList(ListView):
    model = Table
