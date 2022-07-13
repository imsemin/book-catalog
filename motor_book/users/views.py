from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, DetailView

from .forms import CreationForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("books:homepage")
    template_name = "users/signup.html"


class ProfileDetailView(DetailView):
    model = User
    template_name = "users/profile.html"
