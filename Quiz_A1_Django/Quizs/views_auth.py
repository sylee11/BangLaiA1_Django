from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import MyUser
from django.contrib.auth import authenticate
# Create your views here.

def login(request):
	user = authenticate(email='abcdef@gmail.com',password='123456')
	print(user)
	return HttpResponse(user)


def logout(request):
	return HttpResponse("Hello")
	user = MyUser.authenticate

def regigter(request):
	if request.method == 'POST':
		strName = request.POST.get('name')
		strGender = request.POST.get('gender')
		strOld = request.POST.get('dateOfBirth')
		strEmail = request.POST.get('email')
		strPass = request.POST.get('password')
		user = MyUser(strName,strGender,strOld,strEmail,strPass)
		user.save()
		user = MyUser.objects.create_user(strEmail,strName,strPass)
		return HttpResponse("Register done")
