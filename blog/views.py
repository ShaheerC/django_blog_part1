from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from blog.models import *
from blog.forms import *
from datetime import datetime

def root(request):
    return HttpResponseRedirect('articles')

def articles(request):
    context ={'articles': Article.objects.all().order_by('-published_date'), 'time_now': datetime.now()}
    response = render(request, 'articles.html', context)
    return HttpResponse(response)

def article_show(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article, 'time_now': datetime.now()}
    return render(request, 'article.html', context)

def new_article(request):
    form = ArticleForm()
    context = {"form": form, "message": "Create new article", "action": "/articles/create", 'time_now': datetime.now()}
    return render(request, 'form.html', context)

def create_article(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save(commit=False)
        article.user = request.user
        article.save()
        return HttpResponseRedirect("/articles")
    else:
        context = {"form": form}
        return render(request, 'form.html', context)

def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.filter(id=article_id)[0]
    name = request.POST['name']
    comment = request.POST['comment']
    new_comment = Comment(name=name, message=comment, article=article)
    new_comment.save()
    return HttpResponseRedirect(f'/articles/{article_id}')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/articles')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/articles')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/articles')
    else:
        form = UserCreationForm()
    html_response = render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)

