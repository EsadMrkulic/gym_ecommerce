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
        self.car = cart
