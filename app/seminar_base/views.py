from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'seminar_base/index.html')

def article_detail(request, article_id):
    from .models import Article
    article = Article.objects.get(id=article_id)
    return render(request, 'seminar_base/article_detail.html', {'article': article})