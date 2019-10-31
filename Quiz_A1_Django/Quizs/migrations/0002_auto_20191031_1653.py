# Generated by Django 2.1.12 on 2019-10-31 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quizs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=0, max_digits=10)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
            ],
        ),
        migrations.CreateModel(
            name='Soccer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soccer', models.DecimalField(decimal_places=0, max_digits=10)),
                ('time', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('idUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='imagequestion',
            name='idQuestion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Quizs.Question'),
        ),
    ]
