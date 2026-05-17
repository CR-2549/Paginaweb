from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Game(models.Model):

    title = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(upload_to='games/')

    release_date = models.DateTimeField()

    platform = models.CharField(max_length=50)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title