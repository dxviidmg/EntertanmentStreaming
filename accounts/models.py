from django.db import models
from django.conf import settings
from payments.models import *
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True,  default="/userDefault.png")
	phone = models.CharField(max_length=13, blank=True, null=True)
	locked = models.BooleanField(default=False)
	is_internet_client = models.BooleanField(default=False)
	monthly_payment = models.DecimalField(decimal_places=2, max_digits=5, default=100)
	
	def __str__(self):
		return 'Perfil del usuario {} {}'.format(self.user.first_name, self.user.last_name)

	def UpdateLocking(self):
		now = datetime.datetime.now()
		last_payment = Payment.objects.filter(user=self.user).last()

		if last_payment.validity_year < now.year:
			self.locked = True
			self.save()
		elif last_payment.validity_year == now.year and int(last_payment.validity_month) < now.month:
			self.locked = True
			self.save()
		else:
			self.locked = False
			self.save()

	def save(self, *args, **kwargs):
		if self.is_internet_client == False:
			self.monthly_payment = 150
		super(Profile, self).save(*args, **kwargs)