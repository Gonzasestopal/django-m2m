from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Tweet(models.Model):
	user = models.ForeignKey(User)
	tweet = models.CharField(max_length=140)

class MyUser(models.Model):
	user = models.ForeignKey(User)
	username = models.CharField(max_length=200)
	follow = models.ManyToManyField('self', blank=True)

	def __unicode__(self):
		return self.username