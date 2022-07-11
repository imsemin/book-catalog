from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.MainView.as_view()),
    # path("homepage.html", views.BookListView.as_view()),
    path("homepage.html", views.index),
    path("book/car_models/<slug:slug>", views.car_models, name="car_models"),
    path(
        "book/<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"
    ),
]
