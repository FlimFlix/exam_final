# Generated by Django 2.1 on 2019-06-29 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_author_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('publish_year', models.CharField(max_length=200, verbose_name='Год издания')),
                ('file', models.FileField(blank=True, null=True, upload_to='book_file', verbose_name='Файл')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='book_cover', verbose_name='Обложка')),
                ('description', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Author')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
