from django_bro_tables.models import Regex, RegexEntry
from rest_framework import serializers

class RegexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regex
        fields = ('name', 'comment', 'disabled')

class RegexEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegexEntry
        fields = ('pattern', 'flags', 'comment')
