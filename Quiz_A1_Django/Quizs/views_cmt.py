from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import MyUser, Comment
import json
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
@csrf_exempt
def rating(request):
	if request.method == 'POST':
		strContentCmt = request.POST.get('valueContentCmt')
		strIdUserCmt = request.user.id
		print(datetime.datetime.now().strftime('%Y-%m-%d'))
		# print(datetime.datetime.date())

		Comment.objects.create(comment=strContentCmt,idUser_id=strIdUserCmt, rating = 1, time =datetime.datetime.now().strftime('%Y-%m-%d'))
		# listComment = list(Comment.objects.order_by('-id')[:10].select_related('myuser').values('idUser_id','comment','idUser__name','time'))
		listComment = list(Comment.objects.order_by('-id')[:10].select_related('idUser').values('idUser__id','comment','idUser__name','time'))
		return HttpResponse(json.dumps(listComment,cls=DjangoJSONEncoder), content_type="application/json")
	return HttpResponse("Hello")
	