class Shop:
    cart = [] # cart is a class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


sushmoy = Shop('Sushmoy Nandi')
sushmoy.add_to_cart('shoes')
sushmoy.add_to_cart('phone')
print(sushmoy.cart)


bappi = Shop('Bappi')
bappi.add_to_cart('cap')
bappi.add_to_cart('watch')
print(bappi.cart)
