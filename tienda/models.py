from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

class Customer(models.Model):
    names = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    birthdate = models.DateField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.names