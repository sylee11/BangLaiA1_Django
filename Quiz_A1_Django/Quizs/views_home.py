from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . forms import MyUserForm, Question
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	formLogin = MyUserForm
	print(request.user)
	return render(request, 'home.html',{'form': formLogin})


@login_required()
def main(request):
	listQuestionRaw = Question.objects.all()
	listQuestion = []
	print(type(listQuestionRaw))
	# listQuestion = [list(x) for x in listQuestionRaw]
	for index,item in enumerate(listQuestionRaw, start=0):
		listTemp = [item.content, item.anserFirst, item.anserSecond, item.anserThird, item.anserFour,item.anser,item.id,index]
		listQuestion.append(listTemp)
	print(listQuestion)
	print(type(listQuestion))
	return render(request, 'main.html',{'listQuestion' :listQuestion})
