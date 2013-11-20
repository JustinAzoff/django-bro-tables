from django.db import models

class Regex(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    disabled = models.BooleanField(default=False)

class RegexEntry(models.Model):
    regex = models.ForeignKey(Regex)
    pattern = models.CharField(max_length=200)
    flags = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)
    date_added = models.DateTimeField('date added')
    disabled = models.BooleanField(default=False)
