from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Payment(models.Model):
	months_choices = [(i,i) for i in range((1),(13))]

	method_choices = (
		('Cash' , 'Cash'),
		('Deposit' , 'Deposit'),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
	quantity = models.DecimalField(decimal_places=2, max_digits=7)
	months = models.IntegerField(choices=months_choices, default=1)
	deadline = models.DateTimeField(null=True, blank=True)
	method = models.CharField(choices=method_choices, default="Cash", max_length=10)
	reference_number = models.CharField(max_length=30, null=True, blank=True)
	voucher = models.ImageField(upload_to="voucher/%Y/%m/%d", null=True, blank=True)	
	created = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author", default=1)

	def __str__(self):
		return 'Payment of {} {} until'.format(self.user.first_name, self.user.last_name)

	def save(self, *args, **kwargs):
		now = timezone.now()
		self.quantity = self.months * self.user.profile.monthly_payment
		self.deadline = now + relativedelta(months=self.months)
		super(Payment, self).save(*args, **kwargs)		