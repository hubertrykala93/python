from exceptions import NotExistingFile, CategoryUnavailableError, ProductUnavailableError, ProductAvailableError

import json
import os


class Menu:

    def __init__(self, file_path='menu.json'):
        """
        Creating menu object.
        :param file_path: str
        """
        self.filepath = file_path

    def _load_menu(self) -> dict:
        """
        Loading menu from json file.
        :return: dict
        """

        if os.path.isfile(path=self.filepath):
            with open(file=self.filepath, mode='r') as file:
                file = json.load(fp=file)

            return file

        raise NotExistingFile(file_name=self.filepath)

    def product_info(self, category: str) -> dict:
        """
        Displaying names and prices of the selected product category which are currently available in menu.
        :param category: str
        :return: dict
        """
        choose_product = {}

        for product in Menu(file_path=self.filepath)._load_menu().items():
            if product[0] == category:
                for item in product[1]:
                    choose_product[item['name']] = item['price']

        return choose_product

    def check_availability(self, category: str, name: str) -> dict:
        """
        Checking quantity for product
        :param category: str
        :param name: str
        :return: dict
        """
        menu = Menu(file_path=self.filepath)._load_menu()

        return {name: product['quantity'] for product in menu[category] if name in product.values()}

    def _add_product(self, category: str, **kwargs) -> None:
        """
        Protected method for admin of system. Adding new product to the menu and overwriting json file.
        :param category: str
        :param kwargs: str
        :return: None
        """
        menu = Menu(file_path=self.filepath)._load_menu()

        if not category in menu.keys():
            menu[category] = [kwargs]

        else:
            if kwargs not in menu[category]:
                menu[category].append(kwargs)
            else:
                raise ProductAvailableError(product=list(kwargs.values())[0])

        with open(file=self.filepath, mode='w') as file:
            json.dump(obj=menu, fp=file)

    def _remove_product(self, category: str, name: str) -> None:
        """
        Protected method for admin of system. Removing a product from the menu and overwriting json file.
        :param category: str
        :param name: str
        :return: None
        """
        menu = Menu(file_path=self.filepath)._load_menu()

        if not category in menu.keys():
            raise CategoryUnavailableError(category=category)

        else:
            for item in menu[category]:
                if item['name'] == name:
                    menu[category].remove(item)

                else:
                    raise ProductUnavailableError(name=name)

        if len(menu[category]) == 0:
            menu.pop(category)

        with open(file='menu.json', mode='w') as file:
            json.dump(obj=menu, fp=file)
