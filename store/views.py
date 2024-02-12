from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm
from django import forms

# Create your views here.


# Update password view
def update_password(request):
    # First check to see if user has a password, which they don't if they'r not logged in
    if request.user.is_authenticated:
        current_user = request.user

        # Check if they filled out the form
        if request.method == "POST":
            form = UpdatePasswordForm(current_user, request.POST)

            # Check if the form is valid
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been changed!")
                login(request, current_user)
                return redirect("update_user")

            # If form is not valid
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect("update_password")

        else:
            form = UpdatePasswordForm(current_user)
            return render(request, "update_password.html", {"form": form})
    else:
        messages.success(request, "Your must be logged in to access this page...")
        return redirect("home")


# Update user profile view
def update_user(request):
    # First check to make sure that user logged in
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)  # Get current user

        # When user goes to webpage for first time, it'll have all of their info already in the form
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "Your profile has been updated!")
            return redirect("home")
        return render(request, "update_user.html", {"user_form": user_form})
    else:
        messages.success(request, "You must be logged in to access this page...")
        return redirect("login")


# Category summary view
def category_summary(request):
    categories = Category.objects.all()
    return render(request, "category_summary.html", {"categories": categories})


# Product view
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})


# Homepage view
def home(request):

    # Store all product model objects to a vardiable
    products = Product.objects.all()

    return render(request, "home.html", {"products": products})


# About us view
def about(request):
    return render(request, "about.html", {})


# Category view
def category(request, foo):
    # If hyphen exists in string, it replace it for a space
    foo = foo.replace("-", " ")

    # Get category from url
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(
            request, "category.html", {"products": products, "category": category}
        )
    except:
        messages.success(request, ("That category doesn't exist..."))
        return redirect("home")


# Login view
def login_user(request):
    # Check if the submitted form is a POST
    if request.method == "POST":

        # Set username and password variables to the names given in html forl
        username = request.POST["username"]
        password = request.POST["password"]

        # Set user to valid credentials and log them in
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Django's built in login system
            messages.success(request, ("You have successfully logged in!"))
            return redirect("home")

        # Message and redirect for if the login failed
        else:
            messages.success(request, ("There was an error, please try again..."))
            return redirect("login")

    else:

        return render(request, "login.html", {})


# Logout view
def logout_user(request):
    logout(request)  # Django's built in logout system
    messages.success(request, ("You have successfully logged out!"))
    return redirect("home")


# Register view
def register_user(request):
    # Define form
    form = SignUpForm()
    if request.method == "POST":
        # Take typed information from user, and put it into the SignUpForm()
        form = SignUpForm(request.POST)
        if form.is_valid():  # Check if form is valid
            form.save()  # Save if valid
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            # Login the user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have successfully registered!"))
            return redirect("home")
        else:
            messages.success(
                request,
                "Oh no! Something went wrong when trying to register. Please try again.",
            )
            return redirect("register")
    else:
        return render(request, "register.html", {"form": form})
