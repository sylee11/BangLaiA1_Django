from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import MyUser, VefriAccount, ResetPass
from django.contrib.auth import authenticate,login as log_in, logout as log_out
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
import random
import string
import datetime
from  django.views import  View
from .forms import ResetPassForm,RenewPassForm
# Create your views here.
from django.contrib.sessions.models import  Session

def login(request):
	sessions = Session.objects.filter(expire_date__gte=datetime.datetime.now(datetime.timezone.utc))
	uid_list = []

	# Build a list of user ids from that query
	for session in sessions:
		data = session.get_decoded()
		uid_list.append(data.get('_auth_user_id', None))

	# Query all logged in users based on id list
	for x in MyUser.objects.filter(id__in=uid_list):
		print(x.id)
		print(x.email)
	print(len(MyUser.objects.filter(id__in=uid_list)))
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
		if len(checkUser) > 0:
			return render(request, 'home.html',{'messageError': 'User has exists'})
		# user = MyUser(name = strName,gender = strGender,old=22,email=strEmail,password=make_password(strPass),phoneNumber=strPhone)
		# user.save()
		letters = string.ascii_letters
		string_random = ''.join(random.choice(letters) for i in range(100))
		print(string_random)
		defaults = {'name': strName,'gender': strGender,'old': 22,'email': strEmail,'password': make_password(strPass),'phoneNumber': strPhone, 'token': string_random}
		userVefri = VefriAccount.objects.update_or_create(email=strEmail, defaults=defaults)
		# userVefri = VefriAccount(name=strName, gender=strGender, old=22, email=strEmail, password=make_password(strPass),phoneNumber=strPhone, token=string_random)
		# userVefri.save()
		linkVerfiAccount = "http://192.168.1.246:5000/vefriaccount/" + string_random
		subject = 'Xác nhận tài khoản của bạn trên ThiLaiXeA1 Online'
		message = 'Cảm ơn bạn đã đăng kí site Thi bằng lái xe A1 Online của chúng tôi. Vui lòng truy cập vào link sau để xác minh tài khoản'+linkVerfiAccount+ '.<br> @@@@@@'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [strEmail, ]
		send_mail(subject, message, email_from, recipient_list)
		return render(request, 'home.html',{'message': 'Register susscessfull !!!'})

def vefriaccount(request,tok):
	print(tok)
	if VefriAccount.objects.filter(token = tok).exists():
		timeCheck = VefriAccount.objects.filter(token = tok)[0].created_at
		diffDate = datetime.datetime.now(datetime.timezone.utc) - timeCheck
		millisec = diffDate.total_seconds()/60
		if millisec > 10 :
			VefriAccount.objects.get(token=tok).delete()
			return HttpResponse("<h2><center>Time exprited</center></h2>")
		else:
			userVer = VefriAccount.objects.get(token=tok)
			user = MyUser(name = userVer.name,gender = userVer.gender,old=userVer.old,email=userVer.email,password=userVer.password,phoneNumber=userVer.phoneNumber)
			user.save()
			userVer.delete()
			return HttpResponse("<h2><center>Đăng kí  Thành công. <a href = '/' >Đăng nhập tại đây </a></center></h2>")
	return HttpResponse("404")

class ResetPassClass(View):
	def get(self,request):
		formReset = ResetPassForm()
		return render(request, 'forgotpass.html', {'form': formReset})
	def post(self,request):
		formReset = ResetPassForm()
		if ResetPassForm(request.POST).is_valid():
			strEmail = request.POST['email']
		else:
			return render(request, 'forgotpass.html', {'form': formReset,'message': 'Sai định dạng Mail, vui lòng thử lại'})
		if MyUser.objects.filter(email__contains=strEmail).exists():
			letters = string.ascii_letters
			string_random = ''.join(random.choice(letters) for i in range(100))
			defaults = {'email': strEmail, 'token': string_random}
			objReset = ResetPass.objects.update_or_create(email=strEmail,defaults= defaults)
			linkVerfiAccount = "http://192.168.1.246:5000/renewpass/" + string_random
			subject = 'Email lấy lại mật khẩu tài khoản của bạn trên ThiLaiXeA1 Online'
			message = 'Vui lòng truy cập vào link sau để lấy lại mật khẩu tài khoản của bạn' + linkVerfiAccount
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [strEmail, ]
			send_mail(subject, message, email_from, recipient_list)
			return render(request, 'forgotpass.html', {'form': formReset,'message' : 'Gửi thành công, vui lòng check Mail'})
		# return HttpResponse("<h2>Gửi thành công . Vui lòng check Mail của bạn !!</h2>")
		pass

class RenewPassClass(View):
	def get(self, request, tok):
		if ResetPass.objects.filter(token=tok).exists():
			timeCreate = ResetPass.objects.get(token= tok).created_at
			timeCheckExprite = (datetime.datetime.now(datetime.timezone.utc) - timeCreate).total_seconds()/60
			if timeCheckExprite < 10 :
				formRenew = RenewPassForm()
				return render(request, 'renew.html', {'formRenew':formRenew,'token':tok})
			else:
				ResetPass.objects.get(token=tok).delete()
				return HttpResponse("Timeexprite")
		else:
			return HttpResponse("404")
	def post(self, request, tok):
		value = RenewPassForm(request.POST)
		formRenew = RenewPassForm()
		if value.is_valid():
			passNew = value.cleaned_data['passOld']
			passNewRepeat = value.cleaned_data['passNew']
			if passNew != passNewRepeat :
				return render(request, 'renew.html', {'formRenew':formRenew,'token':tok,'message':'Mật khẩu không trùng nhau, vui lòng nhập lại!'})
			try:
				strEmail = ResetPass.objects.get(token = tok).email
				objNewPass = MyUser.objects.filter(email=strEmail).update(password = make_password(passNew))
				return HttpResponse("<h2><center>Đặt lại mật khẩu thành công. <a href='/'> Đăng nhập tại đây </a></center></h2>")
			except:
				return HttpResponse("Fail")

		pass