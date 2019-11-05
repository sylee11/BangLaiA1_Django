from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import MyUser
from django.contrib.auth import authenticate,login as log_in, logout as log_out
from django.db import models
from  django.contrib.auth.hashers import make_password
# Create your views here.

def login(request):
	if request.method == 'POST':
		strEmail = request.POST.get('email')
		strPass = request.POST.get('password')
		user = authenticate(request, email = strEmail, password=strPass)
		if user is not None:
			log_in(request,user)
			return HttpResponseRedirect('/home')
		else:
			return render(request, 'home.html', {'messageError': 'UserLoginFail'})
	return render(request, 'home.html', {'messageError' : 'requireLogin'})


def logout(request):
	log_out(request)
	return HttpResponseRedirect('/home')
def regigter(request):
	if request.method == 'POST':
		strName = request.POST.get('name')
		strGender = request.POST.get('gender')
		strOld = request.POST.get('dateOfBirth')
		strEmail = request.POST.get('email')
		strPass = request.POST.get('password')
		strPhone = request.POST.get('phoneNumber')
		checkUser = MyUser.objects.filter(email = strEmail)
		print(checkUser)
		return render(request, 'home.html',{'messageError': 'User has exists'})
		# try:
		# 	checkUser = MyUser.objects.filter(email = strEmail)
		# 	return render(request, 'home.html',{'messageError': 'User has exists'})
		# except Exception as e:
		user = MyUser(name = strName,gender = strGender,old=22,email=strEmail,password=make_password(strPass),phoneNumber=strPhone)
		user.save()
			
		return render(request, 'home.html',{'message': 'Register susscessfull !!!'})
