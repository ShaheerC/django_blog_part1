from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import *
from datetime import datetime

def root(request):
    return HttpResponseRedirect('articles')

def articles(request):
    context ={'articles': Article.objects.all().order_by('-published_date'), 'time_now': datetime.now()}
    response = render(request, 'articles.html', context)
    return HttpResponse(response)

def article_show(request, id):
    article = Article.objects.get(pk=id)
    context = {'article': article}
    return render(request, 'article.html', context)