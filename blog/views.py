from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home_page(request):
    response = render(request, 'homepage.html')
    return HttpResponse(response)