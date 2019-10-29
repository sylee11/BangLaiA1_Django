from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import MyUser
from django.contrib.auth import authenticate
# Create your views here.

def login(request):
	user = authenticate(username='syle',password='123456')
	print(user)
	return HttpResponse("Hello")


def logout(request):
	return HttpResponse("Hello")
	user = MyUser.authenticate

def regigter(request):
	user = MyUser.objects.create_user('abcdef@gmail.com','namnk','123456')
	return HttpResponse("Register done")
