from django.urls import path, include
from .views import ArticleListView


app_name = 'webapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
]