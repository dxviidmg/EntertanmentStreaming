from django.db import models
from django.conf import settings
from payments.models import *
import datetime

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True,  default="/userDefault.png")
	phone = models.CharField(max_length=13, blank=True, null=True)
	looked = models.BooleanField(default=False)
	price_per_month = models.IntegerField()

	def __str__(self):
		return 'Perfil del usuario {} {}'.format(self.user.first_name, self.user.last_name)

	def UpdateLook(self):
		now = datetime.datetime.now()
		last_payment = Payment.objects.filter(user=self.user).last()

		if last_payment.validity_year < now.year:
			self.looked = True
			self.save()
		elif last_payment.validity_year == now.year and int(last_payment.validity_month) < now.month:
			self.looked = True
			self.save()
		else:
			self.looked = False
			self.save()

		print(self.looked)			
	