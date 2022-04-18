from django.db import models

class Product(models.Model):
	Title = models.CharField(max_length=200)
	description = models.CharField(max_length=300)
	UpVotes= models.PositiveIntegerField(default=0)
	DownVotes= models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.Title

class User(models.Model):
	pass

