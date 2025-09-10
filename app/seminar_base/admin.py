from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.register(Article)

admin.site.site_header = "SeminarBase管理画面"
admin.site.site_title = "SeminarBase管理画面"
admin.site.index_title = "SeminarBase管理"