from django.contrib.sessions.models import Session
from accounts.models import Visitor

class OneSessionPerUserMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_view(self, request, view_func, view_args, view_kwargs):
		if request.user.is_authenticated == True:
			current_key = request.session.session_key
			if hasattr(request.user, 'visitor'):
				active_key = request.user.visitor.session_key
				if active_key != current_key:
					Session.objects.filter(session_key=active_key).delete()
					request.user.visitor.session_key = current_key
					request.user.visitor.save()
			else:
				Visitor.objects.create(pupil=request.user, session_key=current_key)	