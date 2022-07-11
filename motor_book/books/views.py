from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import get_object_or_404, render

from .models import Book, Category, CarModel


class MainView(TemplateView):
    template_name = "books/index.html"


# class BookListView(ListView):
#     context_object_name = "books"
#     # queryset = Book.objects.all()
#     model = Book
#     template_name = "books/homepage.html"


def index(request):
    template_name = "books/homepage.html"
    books = Book.objects.all()
    categories = Category.objects.all()
    cars = CarModel.objects.all()
    context = {"books": books, "categories": categories, "cars": cars}
    return render(request, template_name, context)


def car_models(request, slug):
    template_name = "books/car_models.html"
    car = get_object_or_404(CarModel, slug=slug)
    car_list = Book.objects.filter(car_models=car)
    context = {"cars": car_list}
    return render(request, template_name, context)


class BookDetailView(DetailView):
    queryset = Book.objects.all()
