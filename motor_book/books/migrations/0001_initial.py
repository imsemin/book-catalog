# Generated by Django 4.0.5 on 2022-06-22 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('pages', models.PositiveSmallIntegerField(verbose_name='Количество страниц')),
                ('price', models.PositiveIntegerField(help_text='руб.', verbose_name='Стоимость')),
                ('available_in_stoke', models.PositiveSmallIntegerField(help_text='шт.', verbose_name='Количество на складе')),
                ('cover', models.CharField(blank=True, max_length=200, verbose_name='Обложка')),
                ('publisher', models.CharField(blank=True, max_length=200, verbose_name='Издалельство')),
                ('image', models.ImageField(blank=True, upload_to='books/', verbose_name='Картинка')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=200, verbose_name='Модель авто')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Модель авто',
                'verbose_name_plural': 'Модели авто',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, help_text='Текст нового комментария', verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('book', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='car_models',
            field=models.ManyToManyField(to='books.carmodel'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='books.category'),
        ),
    ]
