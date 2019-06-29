from django import forms
from .models import Article, Author, Book, Comment


class ArticleForm(forms.ModelForm):
    def clean(self):
        if not self.cleaned_data['text'] and not self.cleaned_data['image']:
            raise forms.ValidationError('Хотя бы одно из полей "Текст" и "Картинка" должно быть заполнено.')
        return super().clean()

    class Meta:
        model = Article
        fields = ['title', 'text', 'image']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'death_date', 'birth_date', 'biography', 'photo']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publish_year', 'file', 'cover', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
