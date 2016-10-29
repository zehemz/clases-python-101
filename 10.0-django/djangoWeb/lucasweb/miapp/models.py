from django.db import models
from django.utils.encoding import python_2_unicode_compatible
#https://docs.djangoproject.com/es/1.10/ref/models/fields/
# Create your models here.

from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/media/photos')

@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Contact(models.Model):
    GENDER = (('M', 'male'), ('F', 'female'))
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    photo = models.ImageField(storage=fs)
    birth_date = models.DateTimeField('bith date')

    def __str__(self):
        return self.email
