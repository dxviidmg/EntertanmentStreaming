from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

now = datetime.now()

class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name

class Serie(models.Model):
	category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	image = models.TextField()
	synopsis = models.TextField()
	year = models.IntegerField(default=now.year)
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.name

class Season(models.Model):
	serie = models.ForeignKey(Serie, related_name="serie", on_delete=models.CASCADE)
	number = models.IntegerField()
	year = models.IntegerField()

	def __str__(self):
		return str(self.number) + " of " + self.serie.name

class Chapter(models.Model):
	link_status_choices = (
		('Functional','Functional'),
		('Broken or Misspelled','Broken or Misspelled'),
	)
	season = models.ForeignKey(Season, related_name="season", on_delete=models.CASCADE)
	number = models.IntegerField()
	name = models.CharField(max_length=50)
	link = models.TextField()
	synopsis = models.TextField()
	duration = models.DurationField()
	slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
	link_status = models.CharField(max_length=20, default="Functional", choices=link_status_choices)

	def __str__(self):
		return str(self.number) + "x" +str(self.season)

	def save(self, *args, **kwargs):
		print(self.season.number)
		self.slug= '-'.join((slugify(self.season.number), slugify(self.number), slugify(self.season.serie.name)))
		super(Chapter, self).save(*args, **kwargs)