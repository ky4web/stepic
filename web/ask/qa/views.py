from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Answer, Question
from helpers import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question(request, id):
    q = get_object_or_404(Question, pk=id)
    a = q.answer_set.all()
    return render(
        request,
        'qa/question.html',
        {'title': q.title, 'text': q.text, 'answer': a}
    )


def new_question(request):
    q = Question.objects.all().order_by('-added_at')
    page = paginate(request, q)
    return render(
        request,
        'question_list.html',
        {'page': page, 'title': 'new questions'}
    )


def popular_questions(request):
    q = Question.objects.all().order_by('-rating')
    page = paginate(request, q)
    return render(
        request,
        'popular.html',
        {'page': page, 'title': 'popular'}
    )
