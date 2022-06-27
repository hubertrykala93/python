from menu import Menu
from cheese import Cheese
from fruit import Fruit
from ham import Ham
from meat import Meat
from roll import Roll
from sauce import Sauce
from shopping_card import ShoppingCard
from vegetable import Vegetable


def run():
    products = ['roll', 'meat', 'cheese', 'fruit', 'vegetable', 'ham', 'sauce']
    classes = [Roll, Meat, Cheese, Fruit, Vegetable, Ham, Sauce]

    card = ShoppingCard()
    menu = Menu()

    while True:
        for product, what in zip(products, classes):
            print(f"Rolls in our menu: {menu.product_info(category=product)}")
            user_choice = input(f'What kind of {product} do you want to add to the shopping card? ')
            user_quantity = int(input('Enter the quantity: '))
            product = what(name=user_choice, quantity=user_quantity)
            card.add_product(product=product)
            print(f'You have selected - {card.products}')
            print(f'Current amount to pay - {card.amount}')
            print('\t')


if __name__ == '__main__':
    run()
