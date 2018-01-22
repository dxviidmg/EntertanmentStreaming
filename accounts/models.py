from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True,  default="/userDefault.png")
	phone = models.CharField(max_length=13, blank=True, null=True)

	def __str__(self):
		return 'Perfil del usuario {} {}'.format(self.user.first_name, self.user.last_name)