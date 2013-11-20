import csv
from six import StringIO, text_type, PY2

from rest_framework.renderers import BaseRenderer

#based on django-rest-framework-csv

class BroTSVRenderer(BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'

    def render(self, data, media_type=None, renderer_context=None):
        """
        Renders serialized *data* into CSV. For a dictionary:
        """
        if data is None:
            return ''

        csv_buffer = StringIO()
        csv_writer = csv.writer(csv_buffer, dialect='excel-tab')
        
        if data:
            header = list(data[0]._fields)
            header[0] = '#' + header[0]
            data = [header] + data

        for row in data:
            # Assume that strings should be encoded as UTF-8
            csv_writer.writerow([
                elem.encode('utf-8') if isinstance(elem, text_type) and PY2 else elem
                for elem in row
            ])

        return csv_buffer.getvalue()    
