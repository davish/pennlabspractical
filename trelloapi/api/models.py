# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class List(models.Model):
    """
    List Model: Is associated with one board and has many Cards.
    order parameter used to order lists on output.
    """
    title = models.CharField(max_length=500)
    order = models.IntegerField()


class Card(models.Model):
    """
    Cards are associated with one list and have a title and a description.
    """
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    list = models.ForeignKey(List, related_name='cards', on_delete=models.CASCADE)
