from django.shortcuts import render
from markdownx.utils import markdownify
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'seminar_base/index.html', {'articles': articles})

def article_detail(request, article_id):
    
    article = Article.objects.get(id=article_id)
    article.content = markdownify(article.content)
    return render(request, 'seminar_base/article_detail.html', {'article': article})