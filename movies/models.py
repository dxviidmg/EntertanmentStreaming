from django.db import models
import datetime

class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = "categories"

class Movie(models.Model):
	category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	link = models.TextField()
	image = models.TextField()
	synopsis = models.TextField()
	year = models.IntegerField()
	duration = models.DurationField()
	slug = models.SlugField(max_length=200, unique=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']