from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


# Mix the profile information and user information
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend the user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]


# In django, to get the Profile and User to be mixed together, you have to Unregister old way of having an account, and then register the new way.
admin.site.unregister(User)  # Unregister
admin.site.register(User, UserAdmin)  # Register
