from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . forms import MyUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	formLogin = MyUserForm
	print(request.user)
	return render(request, 'home.html',{'form': formLogin})


@login_required()
def main(request):
	return render(request, 'main.html')
