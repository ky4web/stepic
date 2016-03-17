from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import auth
from models import Answer, Question
from forms import AskForm, AnswerForm, SignupForm, LoginForm
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
        'qa/question_list.html',
        {'page': page, 'title': 'new questions'}
    )


def popular_questions(request):
    q = Question.objects.all().order_by('-rating')
    page = paginate(request, q)
    return render(
        request,
        'qa/popular.html',
        {'page': page, 'title': 'popular'}
    )


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            url = '/question/%s/' % q.pk
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


@require_POST
def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        a = form.save()
        url = '/question/%s/' % a.question.pk
        return HttpResponseRedirect(url)
    return HttpResponseRedirect('/answer/')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.authuser()
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {'form': form})
