from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from pyodbc import Connection

from . forms import MyUserForm, Question, ImageQuestion, Comment
from django.contrib.auth.decorators import login_required
import docx2txt
import re
from django.db import connection
from django.db import transaction
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
	listQuestionRaw = Question.objects.raw('SELECT TOP 20 tb.*,us.link from dbo.Quizs_question as tb Left Join dbo.Quizs_imagequestion as us on tb.id = us.idQuestion_id order by newid()')
	print('lllllllllllllllllllllllllllllllllllllll')

	# listQuestionRaw = Question.objects.select_related('idQuestion').all()
	print(listQuestionRaw)
	listQuestion2 = list(listQuestionRaw)
	strListQuestion = '‡'.join(str(x.id) + '†' + str(x.content) + '†' + str(x.anser) + '†' + str(x.anserFirst) + '†'  + str(x.anserSecond) + '†' + str(x.anserThird) + '†' + str(x.anserFour) + '†' + str(x.link) for x in listQuestionRaw)
	print(strListQuestion)
	request.session['listQuestionOld'] = strListQuestion
	listComment = list(Comment.objects.order_by('-id')[:10].select_related('idUser'))
	print(listComment)
	if request.method == "POST":
		return render(request, 'main.html',{'listQuestion' :listQuestion2})

	return render(request, 'main.html',{'listQuestion' :listQuestion2, 'listComment':'listComment'})


@login_required()
def examp(request):
	print(request.session['listQuestionOld'])
	strListQuestionOld = request.session['listQuestionOld']
	listQuestionOld = []
	for x in strListQuestionOld.split('‡'):
		listQuestionOld.append(x.split('†'))
	print(listQuestionOld)
	listAnserFromUser = []
	for x in request.POST:
		if 'valueAnser' in x:
			strValueAnserTemp = ','.join(request.POST.getlist(x))
			idValueAnser = x.split('valueAnser')[1].split('[]')[0]
			listAnserFromUser.append( [idValueAnser , strValueAnserTemp])
	print(request.POST)
	numQuestionTrue = 0
	print(listAnserFromUser)
	for x in listQuestionOld:
		for y in listAnserFromUser:
			if y[0] == x[0]:
				if y[1] == x[2]:
					x.append('true')
					numQuestionTrue += 1
				else:
					x.append('false')
	print(listQuestionOld)
	numQuestionFalse = 20 - numQuestionTrue
	kqFinal = 'Đạt' if numQuestionTrue >=16 else  'Không đạt'
	xxx = request.POST.getlist('valueAnser1[]')
	listComment = list(Comment.objects.order_by('-id')[:10].select_related('idUser'))
	# return HttpResponse(xxx)
	return render(request, 'exam.html',{'listComment':listComment, 'listQuestionOld':listQuestionOld,'numQuestionTrue' : numQuestionTrue, 'numQuestionFalse':numQuestionFalse,'kqFinal':kqFinal })


@transaction.atomic
def importdb(request):
	result = docx2txt.process("D:\Câu 1.docx")
	list = result.split('::')
	for x in list:
		if x == '':
			continue
		x = x.replace('\n','')
		print(x)
		ques = x.split('1-')[0]
		# print(x.split('?')[1])
		print(ques)
		an1 = x.split('1-')[1].split('2-')[0]
		if '3-' in x:
			an2 = x.split('1-')[1].split('2-')[1].split('3-')[0]
			if '4-' in x:
				an3 = x.split('1-')[1].split('2-')[1].split('3-')[1].split('4-')[0]
				an4 = x.split('1-')[1].split('2-')[1].split('3-')[1].split('4-')[1]
			else:
				an3 = x.split('1-')[1].split('2-')[1].split('3-')[1]
				an4 = ''
		else:
			an2 = an1 = x.split('1-')[1].split('2-')[1]
			an3 = ''
			an4 = ''
		print(an1)
		print(an2)
		print(an3)
		print(an4)
		with connection.cursor() as cursor:
			cursor.execute("Insert into dbo.Quizs_question (content, anserFirst, anserSecond, anserThird, anserFour, anser) values (%s,%s,%s,%s,%s, '1')",[ques,an1,an2,an3,an4])
	# print(list[1].replace('\n',''))
	# a = set(list[1].split('\n'))
	# a.remove("")
	# print(a)
	# aa = re.findall(r'\S{1:}', list[1])
	# print(aa)
	return HttpResponse("hehe")