from django.contrib import admin

from .models import CarModel, Category, Comment, Book, Order


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
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
        "pk",
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
        "pk",
        "title",
        "price",
        "available_in_stoke",
        "cover",
        "publisher",
        "republish",
    )
    list_display_links = ("title",)
    list_editable = ("price", "available_in_stoke", "republish")
    list_filter = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "book",
        "author",
        "text",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("pk", "status", "order_date", "book", "buyer")
