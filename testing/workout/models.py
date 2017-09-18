from django.db import models
from django.conf import settings

from website1.models import Person
# Create your models here.

class WorkOut(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL)
	sets 		= models.IntegerField(null = True)
	repeats		= models.IntegerField(null = True)