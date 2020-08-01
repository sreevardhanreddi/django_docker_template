from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
from app.models import Book
from app.forms import BookForm

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from app.celery_tasks import heavy_task
from celery.result import AsyncResult


class BookCreateView(CreateView):
    template_name = "books/book_create.html"
    form_class = BookForm
    success_url = reverse_lazy(
        "app:book_list"
    )  # use reverse_lazy or override get_success_url method, using regular reverse throws an error because django reasons


class BookListView(ListView):
    template_name = "books/book_list.html"
    model = Book
    context_object_name = "books"


def trigger_celery_task(request):
    # you can pass any number of args or kwargs here
    args_list = [1, 2, 3]
    kwargs_list = {"a": 1, "b": 2, "c": 3}
    task_data = heavy_task.delay(*args_list, **kwargs_list)
    return JsonResponse({"task_id": task_data.id}, status=200)


def get_task_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return JsonResponse(result, status=200)
