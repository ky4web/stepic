from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django import forms
from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            author=getattr(self, '_user', None),
        )
        return q


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def save(self):
        a = Answer.objects.create(
            text=self.cleaned_data['text'],
            question_id=self.cleaned_data['question'],
            author=getattr(self, '_user', None),
        )
        return a


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        return authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    def authuser(self):
        return authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
