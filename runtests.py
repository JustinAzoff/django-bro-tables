import os, sys
from django.conf import settings

settings.configure(DEBUG=True,
               USE_TZ=True,
               DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                    }
                },
               ROOT_URLCONF='django_bro_tables.urls',
               INSTALLED_APPS=('django.contrib.auth',
                              'django.contrib.contenttypes',
                              'django.contrib.sessions',
                              'django.contrib.admin',
                              'django_bro_tables',))

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['django_bro_tables', ])
if failures:
    sys.exit(failures)
