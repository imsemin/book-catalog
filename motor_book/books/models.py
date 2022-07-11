from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class CarModel(models.Model):
    car_model = models.CharField("Модель авто", max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Модель авто"
        verbose_name_plural = "Модели авто"

    def __str__(self):
        return self.car_model

    def get_absolute_url(self):
        return reverse("books:car_models", kwargs={"slug": self.slug})


class Category(models.Model):
    title = models.CharField("Категория", max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField("Описание", max_length=2000)
    pages = models.PositiveSmallIntegerField("Количество страниц")
    price = models.PositiveIntegerField("Стоимость", help_text="руб.")
    available_in_stoke = models.PositiveSmallIntegerField(
        "Количество на складе", help_text="шт."
    )
    category = models.ManyToManyField(Category)
    car_models = models.ManyToManyField(CarModel)
    cover = models.CharField("Обложка", max_length=200, blank=True)
    publisher = models.CharField("Издалельство", max_length=200, blank=True)
    image = models.ImageField("Картинка", upload_to="books/", blank=True)
    pub_date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    book = models.ForeignKey(
        Book, blank=True, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    text = models.TextField(
        verbose_name="Текст комментария",
        help_text="Текст нового комментария",
        blank=True,
    )
    pub_date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text[:15]
