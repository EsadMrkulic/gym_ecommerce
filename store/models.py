from django.db import models
import datetime

# Create your models here.


# Model for categories of products
class Category(models.Model):
    name = models.CharField(max_length=50)

    # Method to allow the model to appear in the Django admin panel
    def __str__(self):
        return self.name

    # In the Django Admin Panel, Django makes all classes plural by adding an "s" at the end of it.
    # So, Category would be Categorys. But it should be Categories.
    # Therefore, this class Meta class fixes this.
    class Meta:
        verbose_name_plural = "Categories"


# Customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    # Show the model in admin panel
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# All products model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1
    )  # Foreign Key references this category value to the class Category
    description = models.CharField(max_length=250, default="", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/product/")

    # Sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    # Show the model in admin panel
    def __str__(self):
        return self.name


# Customer orders model
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=15, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    # Show the model in admin panel
    def __str__(self):
        return self.product
