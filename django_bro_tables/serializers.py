from django_bro_tables.models import (
    Regex, RegexEntry,
    Table,
)
from rest_framework import serializers

class RegexEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegexEntry
        fields = ('pattern', 'flags', 'comment', 'disabled', 'regex', 'date_added')

class RegexSerializer(serializers.HyperlinkedModelSerializer):
    csv = serializers.HyperlinkedIdentityField(view_name='regex-csv', format='csv', lookup_field='name')
    class Meta:
        model = Regex
        fields = ( 'csv', 'url', 'name', 'comment', 'disabled')

class RegexDetailSerializer(serializers.HyperlinkedModelSerializer):
    entries = RegexEntrySerializer(many=True, read_only=True)
    csv = serializers.HyperlinkedIdentityField(view_name='regex-csv', format='csv', lookup_field='name')
    class Meta:
        model = Regex
        fields = ( 'csv', 'url', 'name', 'comment', 'disabled', 'entries')

class TableSerializer(serializers.HyperlinkedModelSerializer):
    flat = serializers.HyperlinkedIdentityField(view_name='bro_table-csv', format='csv', lookup_field='name')
    class Meta:
        model = Table
        fields = ( 'flat', 'name','comment','num_fields','fields')
