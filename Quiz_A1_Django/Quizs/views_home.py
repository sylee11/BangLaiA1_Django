from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . forms import MyUserForm, Question, ImageQuestion, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	formLogin = MyUserForm
	return render(request, 'home.html',{'form': formLogin})


@login_required()
def main(request):
	listQuestionRaw = Question.objects.all().select_related('imagequestion')

	listQuestion = []
	listQuestion2 = list(listQuestionRaw)
	# listQuestion = [list(x) for x in listQuestionRaw]
	for index,item in enumerate(listQuestionRaw, start=0):
		# print(item.imagequestion.link)
		listTemp = [item.content, item.anserFirst, item.anserSecond, item.anserThird, item.anserFour,item.anser,item.id,index]
		listQuestion.append(listTemp)
	# print(listQuestion)
	# print(type(listQuestion))
	listComment = list(Comment.objects.order_by('-id')[:10].select_related('idUser'))
	print(listComment)
	return render(request, 'main.html',{'listQuestion' :listQuestion, 'listComment':listComment})

	if request.method == "POST":
		return render(request, 'main.html',{'listQuestion' :listQuestion})

@login_required()
def examp(request):

	return render(request, 'main,html',{})
	pass