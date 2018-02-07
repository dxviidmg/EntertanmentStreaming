from django.db import models
from django.conf import settings
from payments.models import *
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	country_choices = (
		("MX", "Mexico"), #Yo
		("USA", "United States of America"),
	)

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True,  default="/userDefault.png")
	phone = models.CharField(max_length=13, blank=True, null=True)
	country = models.CharField(max_length=10, choices=country_choices, default="MX")
	locked = models.BooleanField(default=False)
	monthly_payment = models.DecimalField(decimal_places=2, max_digits=5)
	foreign_currency = models.CharField(max_length=10, default="MXN")
	is_internet_client = models.BooleanField(default=False)

	def __str__(self):
		return 'Perfil del usuario {} {}'.format(self.user.first_name, self.user.last_name)

	def UpdateLocking(self):
		if self.user.is_staff:
			self.locked = False
			self.save()
		else:
			now = datetime.datetime.now()
			last_payment = Payment.objects.filter(user=self.user).last()

			try:
				if last_payment.validity_year < now.year:
					self.locked = True
					self.save()
				elif last_payment.validity_year == now.year and int(last_payment.validity_month) < now.month:
					self.locked = True
					self.save()
				else:
					self.locked = False
					self.save()
			except:
				self.locked = True
				self.save()

	def save(self, *args, **kwargs):
		if self.country == "USA":
			self.foreign_currency = "USD"
			self.monthly_payment = 10
		elif self.country == "MX":
			self.foreign_currency = "MXN"
			if self.is_internet_client == False:
				self.monthly_payment = 150
			elif self.is_internet_client == True:
				self.monthly_payment = 100
		super(Profile, self).save(*args, **kwargs)

#You show complete name	
def get_full_name(self):
	return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_full_name)

class Visitor(models.Model):
	pupil = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
	session_key = models.CharField(null=False, max_length=40)

	def __str__(self):
		return 'Key of {}'.format(self.pupil)