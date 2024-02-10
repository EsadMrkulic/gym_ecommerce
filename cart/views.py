from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.


# Cart summary view
def cart_summary(request):
    # Get the car
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quants
    totals = cart.cart_total()

    return render(
        request,
        "cart_summary.html",
        {"cart_products": cart_products, "quantities": quantities, "totals": totals},
    )


# Adding to cart view
def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # Test for POST
    if request.POST.get("action") == "post":

        # Get id and quantity of product
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))

        # Look up the product in database
        product = get_object_or_404(Product, id=product_id)

        # Save to the user's session
        cart.add(product=product, quantity=product_qty)

        # Get the quantity of the car
        cart_quantity = cart.__len__()
        # Return response
        # response = JsonResponse({"Product Name:": product.name})
        response = JsonResponse({"qty": cart_quantity})
        messages.success(
            request, (product.name + " has been added to your shopping cart!")
        )
        return response


# Deleting from cart view
def cart_delete(request):
    cart = Cart(request)

    # Using part of the code from cart_add view
    if request.POST.get("action") == "post":

        # Get id and quantity of product
        product_id = int(request.POST.get("product_id"))

        # Retrieve product instance for the success message
        product = get_object_or_404(Product, id=product_id)

        # Call delete function in cart
        cart.delete(product=product_id)
        messages.success(
            request, (product.name + " has been removed from your shopping cart!")
        )
        response = JsonResponse({"product": product_id})

        return response


# Updating cart view
def cart_update(request):
    cart = Cart(request)
    # Using part of the code from cart_add view
    if request.POST.get("action") == "post":

        # Get id and quantity of product
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({"qty": product_qty})
        messages.success(request, ("Your cart has been updated!"))
        return response
        # return redirect('cart_summary')
