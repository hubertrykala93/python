"""
Menu Exceptions
"""


class NotExistingFile(Exception):

    def __init__(self, file_name, message=" doesn't exist"):
        self.file_name = file_name
        self.message = message

        super(NotExistingFile, self).__init__(file_name, message)

    def __str__(self):
        return self.file_name + self.message


class CategoryUnavailableError(Exception):

    def __init__(self, category, message=' category is unavailable in the menu'):
        self.category = category
        self.message = message

        super(CategoryUnavailableError, self).__init__(category, message)

    def __str__(self):
        return self.category + self.message


class ProductAvailableError(Exception):

    def __init__(self, product, message=' is already listed in the menu'):
        self.product = product
        self.message = message

        super(ProductAvailableError, self).__init__(product, message)

    def __str__(self):
        return self.product + self.message


class ProductUnavailableError(Exception):

    def __init__(self, name, message=' is not listed in the menu'):
        self.name = name
        self.message = message

        super(ProductUnavailableError, self).__init__(name, message)

    def __str__(self):
        return self.name + self.message


"""
Roll Exceptions
"""


class ProductUnavailable(Exception):

    def __init__(self, name, message=' is not available at the moment'):
        self.name = name
        self.message = message

        super(ProductUnavailable, self).__init__(name, message)

    def __str__(self):
        return self.name + self.message


class QuantityError(Exception):

    def __init__(self, name):
        self.name = name
        self.message = f'Only one {self.name} roll can be ordered'

        super(QuantityError, self).__init__(name)

    def __str__(self):
        return self.message


class ZeroQuantityError(Exception):

    def __init__(self, name):
        self.name = name
        self.message = f'Quantity of {self.name} roll must be one, not zero'

    def __str__(self):
        return self.message


class NegativeValueError(Exception):

    def __init__(self, message=f'quantity must be a positive value'):
        self.message = message

    def __str__(self):
        return self.message