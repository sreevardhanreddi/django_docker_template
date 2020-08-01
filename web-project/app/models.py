from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    pages = models.IntegerField()
    cover_image = models.ImageField(upload_to="uploads/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
