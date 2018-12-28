from datetime import datetime

from django.db import models

# Create your models here.
from oscar.apps.address.abstract_models import AbstractShippingAddress


class ShippingAddress(AbstractShippingAddress):

    EVENT_CHOICES = (('Bridal', 'Bridal'), ('Causual', 'Causual'), ('Party', 'Party'))
    MARKTEING_CHOICES = (('FB', 'FB'), ('Twitter', 'Twitter'), ('News', 'News'))
    event = models.CharField(choices=EVENT_CHOICES, max_length=20, default='Casual', null=True, blank=True)
    event_date = models.CharField(max_length=30, null=True, blank=True)
    marketing_source = models.CharField(choices=MARKTEING_CHOICES, max_length=20, default='FB', null=True, blank=True)

from oscar.apps.address.models import *
