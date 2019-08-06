from django.db import models
from django.forms import ModelForm
from django.core.validators import URLValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from datetime import datetime, date

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(validators=[MinLengthValidator(1)])
    author = models.CharField(max_length=255)
    draft = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return (f"{self.title} by {self.author}")

    def clean(self):
         if self.draft and self.published_date < date.today():
           raise ValidationError('If this is a draft, the publish date must be in the future.')
    #     if self.draft and self.published_date < date.today():
            # trigger model validation error


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ["title", "body", "author", "draft", "published_date"]
    
    # if the article has draft set to True, 
    #     the published_date must be in the future. 
    # If draft is set to False, 
    #     published_date must be in the past.

    # def clean(self): 
  
    #     # data from the form is fetched using super function 
    #     super(ArticleForm, self).clean() 
          
    #     published_date = self.cleaned_data.get('published_date') 
    #     draft = self.cleaned_data.get('draft') 
  
    #     # conditions to be met for the username length 
    #     if (draft == True) and (published_date.date() > date.today()):
    #         self._errors['published_date'] = self.error_class([ 
    #             'Published Date must be in the future']) 
        
    #     if (draft == False) and (published_date.date() < date.today()):
    #         self._errors['published_date'] = self.error_class([ 
    #             'Published Date must be in the future']) 
  
    #     return self.cleaned_data 
           


class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')