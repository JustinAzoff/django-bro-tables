=====
Bro Tables
=====


Quick start
-----------

1. Add "django_bro_tables" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'django_bro_tables',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^bro_tables/', include('django_bro_tables.urls')),

3. Run `python manage.py syncdb` to create the bro table models.
