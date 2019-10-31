from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . forms import MyUserForm
# Create your views here.

def home(request):
	formLogin = MyUserForm
	return render(request, 'home.html',{'form': formLogin})

def main(request):
	return render(request, 'main.html')
