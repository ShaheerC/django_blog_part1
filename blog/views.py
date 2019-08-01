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

def create_comment(request):
    article_id = request.POST['article']
    article = Article.objects.filter(id=article_id)[0]
    name = request.POST['name']
    comment = request.POST['comment']
    new_comment = Comment(name=name, message=comment, article=article)
    new_comment.save()
    return HttpResponseRedirect(f'/articles/{article_id}')