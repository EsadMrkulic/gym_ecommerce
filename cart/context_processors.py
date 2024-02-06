from .cart import Cart


# Create context processor so the cart can work on all pages
def cart(request):

    # Return default data from the cart
    return {"cart": Cart(request)}
