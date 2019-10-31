from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser)

#Create your models here.

class MyUserManager(BaseUserManager):
	def  create_user(self, email, name, password=None):
		if not email:
			raise ValueError("This iss not Email")
		user = self.model(
			email=self.normalize_email(email),
			name = name,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self, email,name, password):
		user = self.create_user(
			email,
			password=password,
			name =name)
		user.is_admin = True
		user.save(using=self._db)
		return user
class MyUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email',
		max_length=255,
		unique = True,
		)
	name = models.CharField(max_length =255)
	phoneNumber = models.DecimalField(max_digits=13,decimal_places=0,null=True)
	gender = models.CharField(max_length=255,null=True)
	old = models.DecimalField(max_digits=2,decimal_places=0,null=True)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	def __str__(self):
		return self.email
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_admin

class Question(models.Model):
	content = models.CharField(max_length=255)
	anserFirst = models.CharField(max_length=255)
	anserSecond = models.CharField(max_length=255)
	anserThird = models.CharField(max_length=255)
	anserFour = models.CharField(max_length=255, null = True)

	def __str__(self):
		return self.content

class ImageQuestion(models.Model):
	link = models.CharField(max_length=255)
	idQuestion = models.OneToOneField(Question,on_delete=models.CASCADE)
		
	def __str__(self):
		return self.link

class Soccer(models.Model):
	soccer = models.DecimalField(max_digits=10,decimal_places=0)
	idUser = models.OneToOneField(MyUser,on_delete=models.CASCADE)
	time = models.DecimalField(max_digits=10,decimal_places=0,null = True)
		

class Comment(models.Model):
	idUser = models.ForeignKey(MyUser,on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	rating = models.DecimalField(max_digits=10, decimal_places=0)	