from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from blog.models import Article
from datetime import datetime

def root(request):
    return HttpResponseRedirect('home')

def home_page(request):
    context ={'articles': Article.objects.all().order_by('-published_date'), 'time_now': datetime.now()}
    response = render(request, 'homepage.html', context)
    return HttpResponse(response)