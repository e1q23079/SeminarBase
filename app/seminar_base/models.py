from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10000)
    content = MarkdownxField()
    
    def __str__(self):
        return self.title
