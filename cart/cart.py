from store.models import Product


# Cart class
class Cart:
    def __init__(self, request):  # Request to view page
        self.session = request.session  # Sessions for users

        # Get current session key if it exists
        cart = self.session.get("session_key")

        # If user is new and no session key exists, create one
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # Make the cart available on all pages of the website
        self.cart = cart

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
