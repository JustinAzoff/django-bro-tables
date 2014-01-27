import datetime
from django.utils.timezone import utc
from django.test import TestCase
from django_bro_tables.models import Table

from django.contrib.auth.models import User

import json

EXPECTED_TABLE_CSV = """
#fields	ip	port	comment	timestamp
1.2.3.4	22	very bad	1383264000
5.6.7.8	80	very bad	1383264000
""".lstrip()


class CSVTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('admin', 'temporary@gmail.com', 'admin')
        self.client.login(username='admin', password='admin')
        a_day = datetime.datetime(2013,11,1,0,0,0).replace(tzinfo=utc)

        tab = Table.objects.create(name="test", comment="test table", num_fields=3, fields='ip,port,comment,@timestamp')
        e = tab.entries.create(c0="1.2.3.4", c1=22, c2="very bad")
        e.timestamp=a_day
        e.save()

        e = tab.entries.create(c0="5.6.7.8", c1=80, c2="very bad")
        e.timestamp=a_day
        e.save()


    def test_bro_tables_api(self):
        """Bro tables API"""
        #use a hardcoded url, not reverse. need to know if external clients would break
        response = self.client.get('/bro/api/table/')
        data = json.loads(response.content)
        self.assertEqual(data[0]['name'], 'test')
        self.assertEqual(data[0]['comment'], 'test table')

    def test_bro_table_as_csv(self):
        response = self.client.get('/bro/api/table/flat/test.csv')
        self.assertMultiLineEqual(response.content, EXPECTED_TABLE_CSV)
