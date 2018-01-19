from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = "categories"

class Channel(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	link = models.TextField()
	logo = models.ImageField(upload_to='channels/%Y/%m/%d/')
	slug = models.SlugField(max_length=200, unique=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
