from store.models import Product, Profile
import json


# Cart class
class Cart:
    def __init__(self, request):  # Request to view page
        self.session = request.session  # Sessions for users
        self.request = request  # Get request

        # Get current session key if it exists
        cart = self.session.get("session_key")

        # If user is new and no session key exists, create one
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # Make the cart available on all pages of the website
        self.cart = cart

        # ***Cart persistance***
        # When user logs back in, the user's cart gets updated with what's in their old cart
        if self.request.user.is_authenticated:
            # If the user is logged in, load cart from their profile
            profile = Profile.objects.filter(user=self.request.user).first()
            if profile and profile.old_cart:
                self.cart.update(json.loads(profile.old_cart))

    # Add function
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert to single quotes to double quotes for the dictionaries (dictionary -> JSON format)
            carty = str(self.cart)  # Converted to a string
            carty = carty.replace(
                "'", '"'
            )  # Replaces all single quotes to double quotes

            # Save carty to Profile model
            current_user.update(old_cart=str(carty))

    # Create a filter that gives us a length
    def __len__(self):
        return len(self.cart)

    # Function to see what's in the cart
    def get_products(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)

        # Return the looked up products
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    # Function to update quantity of products
    def update(self, product, quantity):
        product_id = str(
            product
        )  # Product ID is actually a string in the dictionary, so we want this to be a string
        product_qty = int(
            quantity
        )  # This is a integer in the dictionary, so we want this to be an integer

        # Get cart
        ourcart = self.cart

        # Update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        # Unnecessary, but always good to return something
        thing = self.cart
        return thing

    # Function to delete products
    def delete(self, product):
        product_id = str(product)

        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    # Total function
    def cart_total(self):
        # Get product ID's
        product_ids = self.cart.keys()

        # Look up the keys in product db model
        products = Product.objects.filter(id__in=product_ids)

        # Get quantities
        quantities = self.cart

        # Start counting at 0
        total = 0

        # Loop through products in cart, and add it up
        for key, value in quantities.items():

            # Convert key string into int so we can add it up
            key = int(key)
            for product in products:
                if product.id == key:
                    # First we need to check if the product is on sale
                    if product.is_sale:
                        total = total + (
                            product.sale_price * value
                        )  # If product is on sale, we add the product's sale price
                    else:
                        total = total + (
                            product.price * value
                        )  # If product is not on sale, obviously we just use the product's normal price

        return total
