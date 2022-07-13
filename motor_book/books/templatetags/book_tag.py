from django import template

from books.models import Category, CarModel

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_car_model():
    return CarModel.objects.all()
