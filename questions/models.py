from __future__ import unicode_literals

from django.db import models


class Question(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
