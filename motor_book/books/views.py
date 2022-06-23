from django.views.generic import DetailView, TemplateView, ListView

from .models import Book


class MainView(TemplateView):
    template_name = "books/index.html"


class BookListView(ListView):
    context_object_name = "books"
    queryset = Book.objects.all()
    template_name = "books/homepage.html"


class BookDetailView(DetailView):
    queryset = Book.objects.all()
