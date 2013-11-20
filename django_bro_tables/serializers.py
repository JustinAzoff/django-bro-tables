from django_bro_tables.models import Regex, RegexEntry
from rest_framework import serializers

class RegexSerializer(serializers.HyperlinkedModelSerializer):
    csv = serializers.HyperlinkedIdentityField(view_name='regex-csv', format='csv', lookup_field='name')
    class Meta:
        model = Regex
        fields = ( 'csv', 'url', 'name', 'comment', 'disabled')

class RegexEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegexEntry
        fields = ('pattern', 'flags', 'comment')
