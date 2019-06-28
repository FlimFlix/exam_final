from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleListView(ListView):
    template_name = 'article_list.html'
    model = Article
    ordering = ['-created_at']


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_create.html'
    form_class = ArticleForm
    model = Article

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)