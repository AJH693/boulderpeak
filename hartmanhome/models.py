from __future__ import unicode_literals

from django.db import models


class flat_data(models.Model):
    i_d = models.IntegerField(primary_key=True)
    count = models.IntegerField()
    free_text = models.CharField(max_length=30)