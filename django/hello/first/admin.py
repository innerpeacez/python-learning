from django.contrib import admin
from .models import Article, Reporter


# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'headline')
