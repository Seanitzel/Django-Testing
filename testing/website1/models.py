import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Weight(models.Model):
	Gym = models.BooleanField(default = False)
	date = models.DateTimeField(auto_now = False, auto_now_add = False, null = True)
	weight = models.FloatField(max_length = 5, null = True)