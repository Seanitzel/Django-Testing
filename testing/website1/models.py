from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from . import validators

User = settings.AUTH_USER_MODEL

class Weight(models.Model):
	Owner = models.ForeignKey(User) #Django Models Unleashed joincfe.com
	name = models.CharField(max_length = 120, null = True)
	workout = models.CharField(max_length = 120, null = True, validators = [validators.validate_workout])
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = False, null = True)
	weight = models.FloatField(max_length = 5, null = True)
	slug = models.SlugField(blank = True, null = True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return f"/weight/{self.slug}"
		return reverse('weight:detail', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.name

def rl_pre_save_reciever(sender, instance, *args, **kwargs):
	instance.workout = instance.workout.capitalize()
	if not instance.slug: 
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_reciever, sender = Weight)