from django.db import models



# Create your models here.

class Blogs(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=64)
    data = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=32, default='admin')
    count_messages = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=100, null=False)
    main_text = models.CharField(max_length=500, null=False)

    def __str__(self):
        return f'{self.id}-{self.title}'


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True)
    price_sale = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id}-{self.name}'