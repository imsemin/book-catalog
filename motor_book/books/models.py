from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
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
        return reverse("books:car_list", kwargs={"slug": self.slug})


class Category(models.Model):
    title = models.CharField("Категория", max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:category_list", kwargs={"slug": self.slug})


class Book(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextField("Описание", max_length=5000)
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
    republish = models.BooleanField("Переиздание", default=True)

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


class Order(models.Model):
    IN_PROGRESS = "IN"
    READY = "RD"
    NOTICE = "NT"
    CANCELING = "CAN"

    STATUS = [
        (IN_PROGRESS, "В работе"),
        (READY, "Исполнено"),
        (NOTICE, "Уведомить о поступлении"),
        (CANCELING, "Отменено"),
    ]

    status = models.CharField(
        "Статус заказа", choices=STATUS, default=IN_PROGRESS, max_length=20
    )
    order_date = models.DateTimeField("Дата создания", auto_now_add=True)
    comment = models.TextField(
        verbose_name="Комментарий к заказу",
        help_text="Комментарий к заказу",
        blank=True,
    )
    buyer_name = models.CharField("Имя", max_length=50)
    buyer_surname = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("E-mail")
    phone_number = models.CharField(
        "Телефон",
        validators=[RegexValidator(r"^\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$")],
        max_length=20,
    )
    book = models.ForeignKey(
        Book, blank=True, on_delete=models.DO_NOTHING, related_name="orders"
    )
    buyer_city = models.CharField("Город", max_length=100)

    class Meta:
        ordering = ["-order_date"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
