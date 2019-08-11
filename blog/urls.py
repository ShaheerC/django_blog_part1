"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from blog.views import *
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', root),
    path('admin/', admin.site.urls),
    path('articles/', articles),
    path('articles/<int:id>', article_show, name='article_details'),
    path('articles/new', new_article, name='new_article'),
    path('articles/create', create_article, name='create_article'),
    path('comments/new', create_comment, name='create_comment'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('articles/<int:id>/edit', edit_article, name='edit_article'),
]