from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import MyUser, Comment
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def rating(request):
	if request.method == 'POST':
		strContentCmt = request.POST.get('valueContentCmt')
		strIdUserCmt = request.user.id
		Comment.objects.create(comment=strContentCmt,idUser_id=strIdUserCmt, rating = 1)
		listComment = list(Comment.objects.order_by('-id')[:10].select_related('myuser').values('idUser_id','comment','idUser__name'))
		return HttpResponse(json.dumps(listComment), content_type="application/json")
	return HttpResponse("Hello")
	