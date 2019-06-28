from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'image':
                visible.field.widget.attrs['class'] = 'form-control-file'

    class Meta:
        model = Article
        fields = ['title', 'text', 'image']
