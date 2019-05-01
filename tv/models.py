from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = "categories"

class Channel(models.Model):
	link_status_choices = (
		('Functional','Functional'),
		('Broken','Broken'),
		('Misspelled', 'Misspelled')
	)
	
	category = models.ForeignKey(Category, related_name="category",on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	link = models.TextField()
	image = models.TextField()
	link_status = models.CharField(max_length=10, default="Functional", choices=link_status_choices)
	slug = models.SlugField(max_length=200, unique=True)
	
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
