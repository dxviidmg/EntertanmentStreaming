from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Payment(models.Model):
	now = datetime.datetime.now()

	month_choices = (
		('01' , 'January'),
		('02' , 'February'),
		('03' , 'March'),
		('04' , 'April'),
		('05' , 'May'),
		('06' , 'June'),
		('07' , 'July'),
		('08' , 'August'),
		('09' , 'September'),
		('10' , 'October'),
		('11' , 'November'),
		('12' , 'December'),
	)
	year = int(now.year)
	year_choices = [(i,str(i)) for i in range((year-1),(year+5))]

	method_choices = (
		('Cash' , 'Cash'),
		('Deposit' , 'Deposit'),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, )
	quantity = models.DecimalField(decimal_places=2, max_digits=7)
	validity_month = models.CharField(choices=month_choices, max_length=20)
	validity_year = models.IntegerField(choices=year_choices)
	method = models.CharField(choices=method_choices, default="Cash", max_length=20)
	created = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return 'Payment of {} {} until {} {} '.format(self.user.first_name, self.user.last_name, self.validity_month, self.validity_year)	