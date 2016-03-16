from django import forms
from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            author=self.author,
        )
        return q


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def save(self):
        a = Answer.objects.create(
            text=self.cleaned_data['text'],
            question_id=self.cleaned_data['question'],
            author=self.author,
        )
        return a
