from django.forms import ModelForm
from django import  forms
from .models import MyUser,Question,ImageQuestion,Soccer,Comment,ResetPass
class MyUserForm(ModelForm):
	class Meta:
		model = MyUser
		fields = ['email','name','password','phoneNumber', 'gender','old']
class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = '__all__'
class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment', 'rating']

class ResetPassForm(ModelForm):
	class Meta:
		model = ResetPass
		fields = ['email']
		widgets = {
			'email' : forms.TextInput(attrs={'class' : 'emailResetPass', 'required': 'required', 'type': 'email'})
		}

class RenewPassForm(forms.Form):
	passOld = forms.CharField(min_length=6,max_length=50, widget=forms.PasswordInput )
	passNew = forms.CharField(min_length=6,max_length=50, widget=forms.PasswordInput )
	# token = forms.CharField(min_length=100, max_length=100)