from django.db import models

from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.title)


class Buy(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    date_buy = models.DateField()


class Supply(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='supply')
    shop = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='supply')
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
