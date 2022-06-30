from menu import Menu
from cheese import Cheese
from fruit import Fruit
from ham import Ham
from meat import Meat
from roll import Roll
from sauce import Sauce
from shopping_cart import ShoppingCart
from vegetable import Vegetable


def run():
    products = ['roll', 'meat', 'cheese', 'fruit', 'vegetable', 'ham', 'sauce']
    classes = [Roll, Meat, Cheese, Fruit, Vegetable, Ham, Sauce]

    cart = ShoppingCart()
    menu = Menu()

    while True:
        print('Config your own burger!\n')

        for product, what in zip(products, classes):
            print(f"{product.capitalize()} in our menu: {menu.product_info(category=product)}")
            user_choice = input(f'What kind of {product} do you want to add to the shopping card? ')
            user_quantity = int(input('Enter the quantity: '))
            product = what(name=user_choice, quantity=user_quantity)
            cart.add_product(product=product)
            print(f'You have selected - {cart.products}')
            print(f'Current amount to pay - {cart.amount}')
            print('\t')

        cart.clear_cart()


if __name__ == '__main__':
    run()
