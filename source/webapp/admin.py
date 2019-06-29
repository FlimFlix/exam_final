from django.contrib import admin
from webapp.models import Article, Author


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'created_at']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'full_name', 'birth_date', 'death_date']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
