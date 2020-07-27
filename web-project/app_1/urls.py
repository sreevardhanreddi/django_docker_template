from django.urls import path
from app_1.views import BookCreateView, BookListView

app_name = "app_1"

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("add-book/", BookCreateView.as_view(), name="add_book"),
]
