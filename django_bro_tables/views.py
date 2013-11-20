from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_csv import renderers as r

from django_bro_tables.models import Regex, RegexEntry
from django_bro_tables.serializers import RegexEntrySerializer, RegexDetailSerializer, RegexSerializer

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

class CSV(APIView):
    model = Regex
    renderer_classes = [RegexCsvRenderer]

    def get(self, request, name, format=None):
        regex = get_object_or_404(Regex, name=name)
        entries = [e for e in regex.entries.all() if not e.disabled]
        serializer = RegexEntrySerializer(entries, many=True, context={'request': request})
        return Response(serializer.data)
