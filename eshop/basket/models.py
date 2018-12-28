from datetime import datetime

from django.db import models

# Create your models here.
from oscar.apps.basket.abstract_models import AbstractLine


class Line(AbstractLine):
    title_choices = (('price', 'price'), ('length', 'length'))
    title = models.CharField(choices=title_choices, max_length=20)
    comments = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)


from oscar.apps.basket.models import *
