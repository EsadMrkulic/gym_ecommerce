from django.shortcuts import render

# Create your views here.


# Payment success view
def payment_success(request):
    return render(request, "payment/payment_success.html")
