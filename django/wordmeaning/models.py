from __future__ import unicode_literals

from django.db import models

# Create your models here.
class words(models.Model):

    word = models.CharField(max_length=40,unique=True)
    meaning = models.CharField(max_length=1000)
    partOfSpeech = models.CharField(max_length=40)
    def __str__(self):
        return self.word

