from django.db import models

class Regex(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class RegexEntry(models.Model):
    regex = models.ForeignKey(Regex, related_name='entries')
    pattern = models.CharField(max_length=200)
    flags = models.CharField(max_length=10, default='e')
    comment = models.CharField(max_length=100)
    date_added = models.DateTimeField('date added', auto_now_add=True)
    disabled = models.BooleanField(default=False)
