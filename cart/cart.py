from products.models import Product


class Cart:
    def __init__(self, request):
        """
        implementing the initialization method for the cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            self.session['cart'] = {}
            cart = self.session['cart']

        self.cart = cart

    def add(self, product, quantity=1):
        """
        implementing the add method for adding item into the cart
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id][quantity] += quantity

        self.save()

    def remove(self, product):
        """
        implementing the remove method for deleting item from the cart
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """
        implementing the save method for session to save changes
        """
        self.session.modified = True

    def __iter__(self):
        """
        implementation of making class instances iterable
        """
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)

        return sum(product.price for product in products)
