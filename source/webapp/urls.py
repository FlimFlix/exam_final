from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, \
    UserDetailView, AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, \
    soft_delete_author, BookListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, \
    CommentCreateView

app_name = 'webapp'

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/comment', CommentCreateView.as_view(), name='comment_create'),
    path('books/<int:pk>/edit', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/edit', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete', soft_delete_author, name='author_delete')
]