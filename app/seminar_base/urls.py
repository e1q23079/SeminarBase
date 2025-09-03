from django.urls import path
from . import views

app_name = 'seminar_base'

urlpatterns = [
    path('', views.index, name='index'),
]