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
    def add(self, product):
        product_id = str(product.id)

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {"price": str(product.price)}

        self.session.modified = True

    # Create a filter that gives us a length
    def __len__(self):
        return len(self.cart)
