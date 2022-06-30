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
- shopping_cart.py - initialization ShoppingCart class,
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

Class Roll constructor has following attributes:

- self.name - name of roll that the user wants to order as string,
- self.quantity - quantity name of roll that the user wants to order as integer with default parameter equal to 1.

In the init method has been implemented validation for checking if product is available in menu, if not raise ProductUnavailableError.
In the init method has been implemented another validation for quantity attribute. If user will choose quantity less than 0, system will raise exception named NegativeValueError, if user will choose quantity equal to 0, system will raise exception named ZeroQuantityError, if user will choose quantity more than 1, system will raise exception named QuantityError.

Class Roll has following methods:

- def __repr__ - returns a string representation of Roll object.

After placing the order by user quantity of chosen product will be reduced in menu. menu.json file will be updated.


Module meat.py:

In this module class Meat was created.

At the top of this module have been imported exceptions like ProductUnavailableError, NegativeValueError, ProductUnavailable from exceptions.py module.
Have been imported also json library and class Menu from menu.py module.

Class Meat constructor has following attributes:
- self.name - name of meat that the user wants to order as string,
- self.price - price of chosen name of product chosen by user.

  In the init method has been implemented validation for checking if product is available in menu, if not raise ProductUnavailableError.
  In the init method has been implemented another validation for quantity attribute. If user will choose quantity less than 0, system will raise exception
  named NegativeValueError otherwise attribute self.quantity is created.
  
Class Meat has following methods:

- def __repr__ - returns a string representation of Meat object.

After placing the order by user quantity of chosen product will be reduced in menu. menu.json file will be updated.
 
 
Module vegetable.py:

In this module class Vegetable was created.

At the top of this module have been imported exceptions like ProductUnavailableError, NegativeValueError, ProductUnavailable from exceptions.py module.
Have been imported also json library and class Menu from menu.py module.

Class Vegetable constructor has following attributes:
- self.name - name of vegetable that the user wants to order as string,
- self.price - price of chosen name of product chosen by user.

  In the init method has been implemented validation for checking if product is available in menu, if not raise ProductUnavailableError.
  In the init method has been implemented another validation for quantity attribute. If user will choose quantity less than 0, system will raise exception
  named NegativeValueError otherwise attribute self.quantity is created.
  
Class Vegetable has following methods:

- def __repr__ - returns a string representation of Vegetable object.

After placing the order by user quantity of chosen product will be reduced in menu. menu.json file will be updated.


Module fruit.py:

In this module class Fruit was created.

At the top of this module have been imported exceptions like ProductUnavailableError, NegativeValueError, ProductUnavailable from exceptions.py module.
Have been imported also json library and class Menu from menu.py module.

Class Fruit constructor has following attributes:
- self.name - name of vegetable that the user wants to order as string,
- self.price - price of chosen name of product chosen by user.

  In the init method has been implemented validation for checking if product is available in menu, if not raise ProductUnavailableError.
  In the init method has been implemented another validation for quantity attribute. If user will choose quantity less than 0, system will raise exception
  named NegativeValueError otherwise attribute self.quantity is created.
  
Class Fruit has following methods:

- def __repr__ - returns a string representation of Fruit object.

After placing the order by user quantity of chosen product will be reduced in menu. menu.json file will be updated.


Module cheese.py:

In this module class Cheese was created.

At the top of this module have been imported exceptions like ProductUnavailableError, NegativeValueError, ProductUnavailable from exceptions.py module.
Have been imported also json library and class Menu from menu.py module.

Class Cheese constructor has following attributes:
- self.name - name of cheese that the user wants to order as string,
- self.price - price of chosen name of product chosen by user.

  In the init method has been implemented validation for checking if product is available in menu, if not raise ProductUnavailableError.
  In the init method has been implemented another validation for quantity attribute. If user will choose quantity less than 0, system will raise exception
  named NegativeValueError otherwise attribute self.quantity is created.
  
Class Cheese has following methods:

- def __repr__ - returns a string representation of Cheese object.

After placing the order by user quantity of chosen product will be reduced in menu. menu.json file will be updated.


Module ham.py:

In this module class Ham was created.

At the top of this module have been imported exceptions like ProductUnavailableError, NegativeValueError, ProductUnavailable from exceptions.py module.
Have been imported also json library and class Menu from menu.py module.

Class Ham constructor has following attributes:
- self.name - name of cheese that the user wants to order as string,
- self.price - price of chosen name of product chosen by user.

  In the init method has been implemented validation for checking if product is available in menu, if not raise ProductUnavailableError.
  In the init method has been implemented another validation for quantity attribute. If user will choose quantity less than 0, system will raise exception
  named NegativeValueError otherwise attribute self.quantity is created.
  
Class Ham has following methods:

- def __repr__ - returns a string representation of Ham object.

After placing the order by user quantity of chosen product will be reduced in menu. menu.json file will be updated.


Module sauce.py:

In this module class Sauce was created.

At the top of this module have been imported exceptions like ProductUnavailableError, NegativeValueError, ProductUnavailable from exceptions.py module.
Have been imported also json library and class Menu from menu.py module.

Class Sauce constructor has following attributes:
- self.name - name of cheese that the user wants to order as string,
- self.price - price of chosen name of product chosen by user.

  In the init method has been implemented validation for checking if product is available in menu, if not raise ProductUnavailableError.
  In the init method has been implemented another validation for quantity attribute. If user will choose quantity less than 0, system will raise exception
  named NegativeValueError otherwise attribute self.quantity is created.
  
Class Sauce has following methods:

- def __repr__ - returns a string representation of Sauce object.

After placing the order by user quantity of chosen product will be reduced in menu. menu.json file will be updated.


Module shopping_cart.py:

In this module class ShoppingCart was created.

Class ShoppingCart constructor has following attributes:

- self.objects - list of objects (products) chosen by user,
- self.to_pay - calculating price of burger.

Class ShoppingCart has following methods:

- def add_product - adding new component of burger to self.objects attribute also self.to_pay attribute is updated.
- def products - property method, user can check what products is in shopping cart,
- def amount - property method, user can check what amount has to pay.


Module exceptions.py:

In this module were created eight classes with exceptions for BurgerBar System.

- class NotExistingFile raise error when file with menu doesn't exist,
- class CategoryUnavailableError raise error when category of product not in menu,
- class ProductAvailableError raise error when product in menu when admin wants to add this product again,
- class ProductUnavailableError raise error when name of product not in menu,
- class ProductUnavailable raise error when name of product is not available,
- class QuantityError raise error when user chose wrong quantity of product,
- class ZeroQuantityError raise error when user chose product with quantity equal to zero,
- class NegativeValueError raise error when user chose product with quantity less than zero.

Module main.py:

Main module for BurgerBar System. Run project and config your own burger! Enjoy!
