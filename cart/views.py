from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.


# Cart summary view
def cart_summary(request):
    return render(request, "cart_summary.html", {})


# Adding to cart view
def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # Test for POST
    if request.POST.get("action") == "post":

        # Get stuff
        product_id = int(request.POST.get("product_id"))

        # Look up the product in database
        product = get_object_or_404(Product, id=product_id)

        # Save to the user's session
        cart.add(product=product)

        # Return response
        response = JsonResponse({"Product Name:": product.name})
        return response


# Deleting from cart view
def cart_delete(request):
    pass


# Updating cart view
def cart_update(request):
    pass
