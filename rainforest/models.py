from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_in_cents = models.IntegerField()

    def __str__(self):
        return self.name

    def price_in_dollars(self):
        dollars = self.price_in_cents / 100
        return "${:.2f}".format(dollars)

class Review(models.Model):
    comment = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.comment