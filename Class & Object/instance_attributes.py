class Shop:
    shopping_mall = 'Bushundha City'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute
    
    def add_to_cart(self,item):
        self.cart.append(item)


sushmoy = Shop('Sushmoy')
sushmoy.add_to_cart('shoe')
sushmoy.add_to_cart('Phone')
print(sushmoy.cart)


bappi = Shop('Bappi')
bappi.add_to_cart('hat')
bappi.add_to_cart('watch')
print(bappi.cart)