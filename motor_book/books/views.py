from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404, render

from .models import Book, Category, CarModel
from .forms import OrderForm
from .utils import paginator_func


class MainView(TemplateView):
    template_name = "books/index.html"


class BookListView(ListView):
    context_object_name = "books"
    paginate_by = 2
    queryset = Book.objects.filter(republish=True)
    template_name = "books/homepage.html"
    extra_context = {"title": "Главная страница"}


def car_list(request, slug):
    template_name = "books/car_list.html"
    car = get_object_or_404(CarModel, slug=slug)
    car_list = Book.objects.filter(car_models=car)
    context = {"title": car, "page_obj": paginator_func(car_list, request)}
    return render(request, template_name, context)


def category_list(request, slug):
    template_name = "books/category_list.html"
    category = get_object_or_404(Category, slug=slug)
    category_list = Book.objects.filter(category=category)
    context = {
        "title": category,
        "page_obj": paginator_func(category_list, request),
    }
    return render(request, template_name, context)


def book_detail(request, slug):
    template_name = "books/book_detail.html"
    book = get_object_or_404(Book, slug=slug)
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.book = book
        order.save()
    context = {"book": book, "form": form}
    return render(request, template_name, context)
