# Generated by Django 2.1.12 on 2019-11-04 13:43

import Quizs.validator
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ImageQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('anserFirst', models.CharField(max_length=255)),
                ('anserSecond', models.CharField(max_length=255)),
                ('anserThird', models.CharField(max_length=255)),
                ('anserFour', models.CharField(max_length=255, null=True)),
                ('anser', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Soccer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soccer', models.DecimalField(decimal_places=0, max_digits=10)),
                ('time', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=255)),
                ('phoneNumber', models.DecimalField(decimal_places=0, max_digits=13, null=True, validators=[Quizs.validator.validate_phone])),
                ('gender', models.CharField(max_length=255, null=True)),
                ('old', models.DecimalField(decimal_places=0, max_digits=2, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='soccer',
            name='idUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagequestion',
            name='idQuestion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Quizs.Question'),
        ),
        migrations.AddField(
            model_name='comment',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
