from django.shortcuts import render
from markdownx.utils import markdownify
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'seminar_base/index.html')

@login_required
def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    article.content = markdownify(article.content)
    contents = {
        'article': article,
        'nextId': Article.objects.filter(id__gt=article_id).order_by('id').first() if Article.objects.filter(id__gt=article_id).exists() else None,
        'prevId': Article.objects.filter(id__lt=article_id).order_by('-id').first()

    }
    return render(request, 'seminar_base/article_detail.html', contents)

@login_required
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'seminar_base/article_list.html', {'articles': articles})