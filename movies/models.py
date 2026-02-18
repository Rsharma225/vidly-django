from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")
    release_year = models.PositiveIntegerField(default=2000)
    number_in_stock = models.PositiveIntegerField(default=0)
    daily_rental_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.title
