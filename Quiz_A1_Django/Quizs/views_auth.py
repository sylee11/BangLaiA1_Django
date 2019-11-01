from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import MyUser
from django.contrib.auth import authenticate
from django.db import models
from  django.contrib.auth.hashers import make_password
# Create your views here.

def login(request):
	if request.method == 'POST':
		strEmail = request.POST.get('email')
		strPass = request.POST.get('password')
	user = authenticate(email=strEmail,password=strPass)
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
		user = MyUser(name = strName,gender = strGender,old=22,email=strEmail,password=make_password(strPass))
		# user = MyUser.objects.create_user(strEmail,strName,strPass)
		# user = MyUser
		# user.gender = strGender
		# user.old = 20
		user.save()
		return HttpResponse("Register done")
