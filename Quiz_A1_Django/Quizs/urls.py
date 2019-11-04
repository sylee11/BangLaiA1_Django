from django.urls import path,include
from . import views_auth, views_home, views_cmt
from django.conf.urls import url
from django.contrib.auth import authenticate, logout

urlpatterns = [
	path('', views_home.home ),
	url(r'^home$', views_home.home, name = 'home'),
	url(r'^quiz$', views_home.main, name = 'main'),
	url(r'^register$', views_auth.regigter, name='register'),	
	url(r'^login$', views_auth.login, name='login'),
	url(r'^logout$', views_auth.logout, name='logout'),
	url(r'^examp$', views_home.examp, name='examp')	
]
