# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class List(models.Model):
    title = models.CharField()
    order = models.IntegerField()


class Card(models.Model):
    title = models.CharField()
    description = models.CharField()
    list = models.ForeignKey(List)
