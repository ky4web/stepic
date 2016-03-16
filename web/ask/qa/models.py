from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name="liked_qs")
    rating = models.IntegerField(default=0)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
