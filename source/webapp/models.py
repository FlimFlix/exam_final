from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class Author(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Автор")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    death_date = models.DateField(null=True, blank=True, verbose_name="Дата смерти")
    biography = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Биография автора")
    photo = models.ImageField(upload_to='author_images', blank=True, null=True, verbose_name="Фотография")
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('webapp:author_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    publish_year = models.CharField(max_length=200, verbose_name="Год издания")
    file = models.FileField(upload_to='book_file', blank=True, null=True, verbose_name="Файл")
    cover = models.ImageField(upload_to='book_cover', blank=True, null=True, verbose_name="Обложка")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")

    def get_absolute_url(self):
        return reverse('webapp:author_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    text = models.TextField(max_length=2000, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('webapp:author_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Текст статьи")
    author = models.ForeignKey(User, blank=True, verbose_name="Автор", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article_images', blank=True, null=True, verbose_name="Картинка")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время создания")

    def __str__(self):
        return f"{self.pk}. {self.title} | {self.author.username}"

    def get_absolute_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
