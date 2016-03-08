from django.http import HttpResponse
from django.shortcuts import render


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question(request, id):
    return render(request, 'qa/question.html', {'id': id, })
