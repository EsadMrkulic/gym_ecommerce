from django.shortcuts import render
from .models import Product

# Create your views here.


# Homepage view
def home(request):

    # Store all product model objects to a vardiable
    products = Product.objects.all()

    return render(request, "home.html", {"products": products})
