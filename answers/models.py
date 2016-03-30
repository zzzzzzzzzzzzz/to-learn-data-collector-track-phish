# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Answer(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey('question.Question', related_name='answers')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = ('-created_at', )
