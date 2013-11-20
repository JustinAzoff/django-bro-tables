from django.db import models

class Regex(models.Model):
    name = models.CharField(max_length=100, unique=True)
    comment = models.CharField(max_length=100)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class RegexEntry(models.Model):
    regex = models.ForeignKey(Regex, related_name='entries')
    pattern = models.CharField(max_length=200, unique=True)
    flags = models.CharField(max_length=10, default='e')
    comment = models.CharField(max_length=100)
    date_added = models.DateTimeField('date added', auto_now_add=True)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.pattern

class Table(models.Model):
    name = models.CharField(max_length=100, unique=True)
    comment = models.CharField(max_length=100)
    num_fields = models.SmallIntegerField()
    #comma seprated list of field names
    fields = models.CharField(max_length=200)

class TableEntry(models.Model):
    table = models.ForeignKey(Table, related_name='entries')
    date_added = models.DateTimeField('date added', auto_now_add=True)
    c0 = models.CharField(max_length=200)
    c1 = models.CharField(max_length=200, blank=True)
    c2 = models.CharField(max_length=200, blank=True)
    c3 = models.CharField(max_length=200, blank=True)
    c4 = models.CharField(max_length=200, blank=True)
    c5 = models.CharField(max_length=200, blank=True)
