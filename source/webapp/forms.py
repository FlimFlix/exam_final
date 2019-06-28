from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'image':
                visible.field.widget.attrs['class'] = 'form-control-file'

    def clean(self):
        if not self.cleaned_data['text'] and not self.cleaned_data['image']:
            raise forms.ValidationError('Хотя бы одно из полей "Текст" и "Картинка" должно быть заполнено.')
        return super().clean()

    class Meta:
        model = Article
        fields = ['title', 'text', 'image']
