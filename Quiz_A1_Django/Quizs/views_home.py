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
	# listQuestionRaw = ImageQuestion.objects.select_related('idQuestion').filter(Question = Question_id)
	# # listQuestionRaw = Question.objects.select_related('idQuestion').all()

	# listQuestion = []
	# listQuestion2 = list(listQuestionRaw)
	# # listQuestion = [list(x) for x in listQuestionRaw]
	# for index,item in enumerate(listQuestionRaw, start=0):
	# 	print(item)
	# 	listTemp = [item.idQuestion.content, item.idQuestion.anserFirst, item.idQuestion.anserSecond, item.idQuestion.anserThird, item.idQuestion.anserFour,item.idQuestion.anser,item.idQuestion.id,index,item.link]
	# 	listQuestion.append(listTemp)
	# listComment = list(Comment.objects.order_by('-id')[:10].select_related('idUser'))
	# print(listComment)
	# return render(request, 'main.html',{'listQuestion' :listQuestion, 'listComment':listComment})
	# if request.method == "POST":
	# 	return render(request, 'main.html',{'listQuestion' :listQuestion})
	listQuestionRaw = Question.objects.raw('SELECT TOP 20 tb.*,us.link from dbo.Quizs_question as tb Left Join dbo.Quizs_imagequestion as us on tb.id = us.idQuestion_id')
	# listQuestionRaw = Question.objects.select_related('idQuestion').all()
	print(list(listQuestionRaw))
	listQuestion2 = list(listQuestionRaw)
	# request.session['listx'] = listQuestion2
	listComment = list(Comment.objects.order_by('-id')[:10].select_related('idUser'))
	print(listComment)
	if request.method == "POST":
		return render(request, 'main.html',{'listQuestion' :listQuestion2})

	return render(request, 'main.html',{'listQuestion' :listQuestion2, 'listComment':listComment})


@login_required()
def examp(request):
	print(request.session['listx'])
	aaa = request.POST
	for x in request.POST:
		if 'valueAnser' in x:
			a = request.POST.getlist(x)
	xxx = request.POST.getlist('valueAnser1[]')
	print(aaa)
	return HttpResponse(xxx)
	return render(request, 'exam.html',{})