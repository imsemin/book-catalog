from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.MainView.as_view()),
    path("homepage.html", views.BookListView.as_view()),
    path(
        "book/<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"
    ),
]
