from django.db import models
from customers.models import Customer
from movies.models import Movie

class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="rentals")
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="rentals")
    date_out = models.DateField()
    date_returned = models.DateField(null=True, blank=True)
    rental_fee = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer} -> {self.movie}"
