from django.contrib import admin
from webapp.models import Article, Author, Book, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'created_at']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'full_name', 'birth_date', 'death_date']


class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'publish_year']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'book', 'text', 'created_at']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)
