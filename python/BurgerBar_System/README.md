BurgerBar System. Config your own burger!

This project includes:

- menu.json - BurgerBar menu in JSON file,
- menu.py - initialization Menu class,
- roll.py - initialization Roll class,
- meat.py - initialization Meat class,
- main.py - run BurgerBar System,
- vegetable.py - initialization Vegetable class,
- fruit.py - initialization Fruit class,
- cheese.py - initialization Cheese class,
- ham.py - initialization Ham class,
- sauce.py - initialization Sauce class,
- shopping_card.py - initialization ShoppingCard class,
- exceptions.py - exceptions for whole project.


Module menu.py:

In this module class Menu was created.

At the top of this module have been imported exceptions like NotExistingFile, CategoryUnavailableError, ProductUnavailableError, ProductAvailableError from exceptions.py module.
Have been imported also libraries like json and os.

Class Menu constructor has following attributes:

- self.file_path as string this attribute has default value as path to file.json,

Class Menu has following methods:

- def load_menu - loading menu from json file, returns dictionary. In method body validation have been implemented. Using os library is checking if file_path is correct, if yes method returns menu as dictionary, if not method returns exception named NotExistingFile.
- def product_info - takes category parameter as string, returns dictionary. User can display names and prices of the selected product category e.g. meat or vegetable which are currently available in menu.
- def add_product - takes category parameter as string and keywords arguments, returns None. Admin has the option to add new product to the menu. Method overwrites and updates menu.json file with new products. Method also raising ProductAvailableError exception when product being added already exists in menu.
- def remove_product - takes category and name parameters as string, returns None. Admin has the option to remove any product from menu. Method overwrites and updates menu.json file after removing product. Method also raising CategoryUnavailableError or ProductUnavailableError exception when product being removed doesn't exist in menu. Method overwrites and updates menu.json file with without removed product.
- def check_availability - takes category and name parameters as string, returns dictionary. User can check the availability of given product.


Module roll.py:

In this module class Roll was created.

At the top of this module have been imported exceptions like ProductUnavailableError, NegativeValueError, ZeroQuantityError, QuantityError, ProductUnavailable from exceptions.py module.
Have been imported also json library and class Menu from menu.py module.

Class roll constructor has following attributes:

- self.name (name of roll that the user wants to order) as string,
- self.quantity (quantity name of roll that the user wants to order) as integer with default parameter equal to 1.

In the init method has been implemented validation for quantity attribute. If user will choose quantity less than 0, system will raise exception named NegativeValueError, if user will choose quantity equal to 0, system will raise exception named ZeroQuantityError, if user will choose quantity more than 1, system will raise exception named QuantityError.

After placing the order by user quantity of chosen product will be reduced in menu. menu.json file will be updated.
