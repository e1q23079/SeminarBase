from django.urls import path
from . import views

app_name = 'seminar_base'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/print/', views.article_print, name='article_print'),
]