from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def login(request):
	return HttpResponse("Hello")


def logout(request):
	return HttpResponse("Hello")


def regigter(request):
	return HttpResponse("Hello")
