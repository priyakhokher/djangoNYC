from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey("auth.User")
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date= models.DateTimeField(default = timezone.now)
	published_data = models.DateTimeField(blank=True, null=True)

	def pubish(self):
		self.published_data = timezone.now()
		self.save()


	def __str__(self):
		return self.title	
# Create your models here.
