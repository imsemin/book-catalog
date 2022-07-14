from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.MainView.as_view()),
    path("homepage.html", views.BookListView.as_view(), name="home"),
    path("car_list/<slug:slug>", views.car_list, name="car_list"),
    path(
        "category_list/<slug:slug>", views.category_list, name="category_list"
    ),
    path("book/<slug:slug>/", views.book_detail, name="book_detail"),
]
