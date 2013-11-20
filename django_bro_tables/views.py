from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_csv import renderers as r

from django_bro_tables.models import Regex
from django_bro_tables.serializers import RegexEntrySerializer, RegexSerializer

class RegexViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Regex.objects.all()
    serializer_class = RegexSerializer


class RegexCsvRenderer(r.CSVRenderer):
    headers = ['pattern', 'flags', 'comment']

class CSV(APIView):
    model = Regex
    renderer_classes = [RegexCsvRenderer]

    def get(self, request, name, format=None):
        regex = get_object_or_404(Regex, name=name)
        entries = [e for e in regex.entries.all() if not e.disabled]
        serializer = RegexEntrySerializer(entries, many=True)
        return Response(serializer.data)
