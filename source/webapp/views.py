from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from webapp.forms import ArticleForm, AuthorForm
from webapp.models import Article, Author, Book


class ArticleListView(ListView):
    template_name = 'article_list.html'
    model = Article
    ordering = ['-created_at']


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author

    def get_queryset(self):
        return Author.objects.filter(is_deleted=False)


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author


class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_create.html'
    form_class = ArticleForm
    model = Article

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'author_create.html'
    form_class = AuthorForm
    model = Author
    permission_required = 'administrations'


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'article_update.html'
    form_class = ArticleForm
    model = Article

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user == self.get_object().author


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'author_update.html'
    form_class = AuthorForm
    model = Author
    permission_required = 'administrations'


def soft_delete_author(request, pk):
    if request.user.is_superuser:
        author = get_object_or_404(Author, pk=pk)
        author.is_deleted = True
        author.save()
        return redirect('webapp:author_list')
    else:
        raise PermissionDenied
