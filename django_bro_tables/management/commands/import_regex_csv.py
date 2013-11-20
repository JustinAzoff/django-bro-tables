import os
from django.core.management.base import BaseCommand, CommandError
from django_bro_tables.models import Regex, RegexEntry

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
        regex, _ = Regex.objects.get_or_create(name=table_name, defaults = { "name": table_name } )

        for rec in csv.reader(open(filename)):
            padded = rec + ['','']
            pattern,flags,comment = padded[0:3]
            regex.entries.create(pattern=pattern, flags=flags, comment=comment)
