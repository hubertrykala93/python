import json

from menu import Menu
from exceptions import ProductUnavailableError, NegativeValueError, ZeroQuantityError, QuantityError, ProductUnavailable


class Roll:

    def __init__(self, name, quantity=1):
        if name not in Menu().product_info(category='roll').keys():
            raise ProductUnavailableError(name=name)

        self.name = name
        self.price = Menu().product_info(category='roll')[name]

        if quantity < 0:
            raise NegativeValueError()
        if quantity == 0:
            raise ZeroQuantityError(name=name)
        elif quantity > 1:
            raise QuantityError(name=name)

        else:
            self.quantity = quantity

        menu = Menu().load_menu()

        for product in menu['roll']:
            if self.name in product.values():
                if product['quantity'] >= self.quantity:
                    product['quantity'] -= self.quantity
                else:
                    raise ProductUnavailable(name=name)

        with open(file='menu.json', mode='w') as file:
            json.dump(obj=menu, fp=file)

    def __repr__(self):
        return self.name
