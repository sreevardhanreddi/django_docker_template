from django.shortcuts import render, reverse, redirect
from app_1.models import Book
from app_1.forms import BookForm

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView


class BookCreateView(CreateView):
    template_name = "books/book_create.html"
    form_class = BookForm
    success_url = reverse_lazy(
        "app_1:book_list"
    )  # use reverse_lazy or override get_success_url method, using regular reverse throws an error because django reasons


class BookListView(ListView):
    template_name = "books/book_list.html"
    model = Book
    context_object_name = "books"

