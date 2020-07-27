from django import forms

from app_1.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
