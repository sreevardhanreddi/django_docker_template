from django.urls import path
from app.views import BookCreateView, BookListView, trigger_celery_task

app_name = "app"

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("add-book/", BookCreateView.as_view(), name="add_book"),
    path("task/", trigger_celery_task, name="trigger_celery_task"),
]
