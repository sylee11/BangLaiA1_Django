from django.urls import path,include
from . import views_auth, views_home, views_cmt
from django.conf.urls import url

urlpatterns = [
	path('', views_home.home ),
	url(r'^home$', views_home.home, name = 'home'),	
]
