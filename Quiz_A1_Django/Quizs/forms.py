from django.forms import ModelForm
from .models import MyUser,Question,ImageQuestion,Soccer,Comment
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

		