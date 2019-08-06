from django.db import models
from django.forms import ModelForm
from django.core.validators import URLValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(validators=[MinLengthValidator(1)])
    author = models.CharField(max_length=255)
    draft = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return (f"{self.title} by {self.author}")

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ["title", "body", "author", "draft", "published_date"]

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')