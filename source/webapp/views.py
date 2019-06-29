from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from webapp.forms import ArticleForm, AuthorForm, BookForm
from webapp.models import Article, Author, Book
from django.urls import reverse


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


class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = Article


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book


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


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'book_create.html'
    form_class = BookForm
    model = Book
    permission_required = 'administrations'

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})


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


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'book_update.html'
    form_class = BookForm
    model = Book
    permission_required = 'administrations'

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})


def soft_delete_author(request, pk):
    if request.user.is_superuser:
        author = get_object_or_404(Author, pk=pk)
        author.is_deleted = True
        author.save()
        return redirect('webapp:author_list')
    else:
        raise PermissionDenied


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'book_detail.html'
    model = Book
    permission_required = 'administrations'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('webapp:book_list')
