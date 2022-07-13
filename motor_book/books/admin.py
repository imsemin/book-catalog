from django.contrib import admin
from django.utils.html import mark_safe


from .models import CarModel, Category, Comment, Book, Order


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = (
        "car_model",
        "slug",
    )
    list_display_links = ("car_model",)
    list_filter = ("car_model",)
    search_fields = ("car_model",)
    prepopulated_fields = {"slug": ("car_model",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    list_display_links = ("title",)
    list_filter = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "get_car_model",
        "get_category",
        "price",
        "available_in_stoke",
        "republish",
        "get_image",
    )
    list_display_links = ("title",)
    readonly_fields = ("get_image",)
    list_editable = ("price", "available_in_stoke", "republish")
    list_filter = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    def get_category(self, obj):
        return ",".join([c.title for c in obj.category.all()])

    def get_car_model(self, obj):
        return ",".join([c.car_model for c in obj.car_models.all()])

    get_image.short_description = "Изображение"
    get_category.short_description = "Категория"
    get_car_model.short_description = "Модель авто"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "author",
        "text",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "order_date", "book", "buyer")
