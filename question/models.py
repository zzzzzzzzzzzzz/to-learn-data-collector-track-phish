# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Category(models.Model):

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        ordering = ('name', )


class Question(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='questions')
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = ('-created_at', )
