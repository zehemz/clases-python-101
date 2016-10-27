from django.db import models
#https://docs.djangoproject.com/es/1.10/ref/models/fields/
# Create your models here.

from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/media/photos')

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Contact(models.Model):
    GENDER = (('M', 'male'), ('F', 'female'))
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    photo = models.ImageField(storage=fs)
    birth_date = models.DateTimeField('bith date')
