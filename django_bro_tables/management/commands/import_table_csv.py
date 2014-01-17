import os
from django.core.management.base import BaseCommand, CommandError
from django_bro_tables.models import Table, TableEntry
import datetime

import csv

class Command(BaseCommand):
    args = 'filename'
    help = 'import filename as a Regex'
    
    def handle(self, *args, **options):
        for filename in args:
            self.do_import(filename)

    def do_import(self, filename):
        table_name = os.path.basename(filename).replace(".csv","")
        print filename, table_name
        data = list(csv.reader(open(filename), delimiter="\t"))

        fields = data.pop(0)[1:]
        fields_str = ",".join(fields).replace("timestamp","@timestamp")

        table, _ = Table.objects.get_or_create(name=table_name, defaults = {
            "name": table_name,
            "num_fields": len(data[0]),
            "fields": fields_str,
        })

        for rec in data:
            pairs = zip(fields, rec)
            obj = {}

            ts = None
            for col, (k,v) in enumerate(pairs):
                if k == "timestamp":
                    ts = datetime.datetime.fromtimestamp(int(v))
                else:
                    obj["c%d" % col] = v

            entry = table.entries.create(**obj)
            if ts:
                entry.timestamp = ts
                entry.save()
