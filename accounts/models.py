from django.db import models
from django.contrib.auth.models import User
from payments.models import *
from dateutil.relativedelta import relativedelta

class Profile(models.Model):
	country_choices = (
		("MX", "Mexico"),
		("USA", "United States of America"),
	)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, default="/userDefault.png")
	phone = models.CharField(max_length=13, blank=True, null=True)
	country = models.CharField(max_length=10, choices=country_choices)
	locked = models.BooleanField(default=False)
	monthly_payment = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
	foreign_currency = models.CharField(max_length=10, null=True, blank=True)
	is_internet_client = models.BooleanField(default=False)
	free_trial_deadline = models.DateTimeField(null=True, blank=True)
	is_premium = models.BooleanField(default=False)

	def __str__(self):
		return 'Profile of {} {}'.format(self.user.first_name, self.user.last_name)

	def UpdateStatus(self):
		now = timezone.now()
		last_payment = Payment.objects.filter(user=self.user).last()

		if last_payment is None:
			if now > self.user.profile.free_trial_deadline:
				self.locked = True
			else:
				self.locked = False
			self.save()
		else:
			self.is_premium = True
			if now > last_payment.deadline:
				self.locked = True
			else:
				self.locked = False
			self.save()

	def save(self, *args, **kwargs):
		#Define foreign currency and monthly payment
		if self.user.is_staff == False:
			if self.country == "USA":
				self.foreign_currency = "USD"
				self.monthly_payment = 10
			elif self.country == "MX":
				self.foreign_currency = "MXN"
				if self.is_internet_client == False:
					self.monthly_payment = 150
				elif self.is_internet_client == True:
					self.monthly_payment = 100

				#Define free_trial_deadline
			self.free_trial_deadline = self.user.date_joined + relativedelta(months=1)
		super(Profile, self).save(*args, **kwargs)

#You show complete name	
def get_full_name(self):
	return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_full_name)

class Visitor(models.Model):
	pupil = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
	session_key = models.CharField(null=False, max_length=40)

	def __str__(self):
		return 'Key of {}'.format(self.pupil)