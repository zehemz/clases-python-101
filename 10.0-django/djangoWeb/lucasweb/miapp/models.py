from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
import os
import datetime


#https://docs.djangoproject.com/es/1.10/ref/models/fields/
# Create your models here.

# from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location='miapp/photo')

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


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/images/<filename>
    return 'images_{0}/{1}'.format(instance.submitter.id, filename)

class Contact(models.Model):
    submitter = models.ForeignKey(User)
    GENDER = (('M', 'male'), ('F', 'female'))
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.email

#'/media/miapp/photos/%Y/%m/%d'
# def get_image_path(instance, filename):
#     fn = filename.split(".")[0]
#     return os.path.join('miapp','photos', fn)
