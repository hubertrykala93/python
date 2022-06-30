import json

from menu import Menu
from exceptions import ProductUnavailableError, NegativeValueError, ProductUnavailable


class Ham:

    def __init__(self, name, quantity=1):
        """
        Creating ham object.
        :param name: str
        :param quantity: int
        """
        if name not in Menu().product_info(category='ham').keys():
            raise ProductUnavailableError(name=name)

        self.name = name
        self.price = Menu().product_info(category='ham')[name]

        if quantity < 0:
            raise NegativeValueError()
        else:
            self.quantity = quantity

        menu = Menu()._load_menu()

        for product in menu['ham']:
            if self.name in product.values():
                if product['quantity'] >= self.quantity:
                    product['quantity'] -= self.quantity
                else:
                    raise ProductUnavailable(name=name)

        with open(file='menu.json', mode='w') as file:
            json.dump(obj=menu, fp=file)

    def __repr__(self):
        """
        String representation of ham object.
        :return: str
        """
        return self.name
