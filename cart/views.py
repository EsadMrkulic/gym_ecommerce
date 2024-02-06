from django.shortcuts import render

# Create your views here.


# Cart summary view
def cart_summary(request):
    return render(request, "cart_summary.html", {})


# Adding to cart view
def cart_add(request):
    pass


# Deleting from cart view
def cart_delete(request):
    pass


# Updating cart view
def cart_update(request):
    pass
