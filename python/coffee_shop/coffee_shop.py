from exceptions import ProductNotAvailable, OrderFulfilled


class CoffeeShop:
    menu = {
        'orange juice': {'type': 'drink', 'price': 2},
        'lemonade': {'type': 'drink', 'price': 1},
        'cranberry juice': {'type': 'drink', 'price': 2},
        'pineapple juice': {'type': 'drink', 'price': 2},
        'lemon iced tea': {'type': 'drink', 'price': 3},
        'vanilla chai latte': {'type': 'drink', 'price': 5},
        'hot chocolate': {'type': 'drink', 'price': 5},
        'iced coffee': {'type': 'drink', 'price': 3},
        'tuna sandwich': {'type': 'food', 'price': 4},
        'ham and cheese sandwich': {'type': 'food', 'price': 3},
        'bacon and egg': {'type': 'food', 'price': 5},
        'steak': {'type': 'food', 'price': 8},
        'hamburger': {'type': 'food', 'price': 5},
        'cinnamon roll': {'type': 'food', 'price': 4}
    }

    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def __repr__(self):
        return f"It is {self.name.replace(' ', '')}. We are welcome!"

    def add_order(self, item):
        if item not in self.menu.keys():
            raise ProductNotAvailable(product=item)

        self.orders.append(item)

    def fulfill_order(self):
        if len(self.orders) != 0:
            removed_item = self.orders.pop(-1)
            return f'{removed_item.title()} is ready!'

        raise OrderFulfilled

    def list_orders(self):
        if self.orders == 0:
            return []

        return [order for order in self.orders]

    def due_amount(self):
        result = 0

        for item in self.orders:
            if item in self.menu.keys():
                result += self.menu[item]['price']

        return result

    def cheapest_item(self):
        return sorted(self.menu.items(), key=lambda item: item[1]['price'])[0][0]

    def expensive_item(self):
        return sorted(self.menu.items(), key=lambda item: item[1]['price'], reverse=True)[0][0]

    def drinks_only(self):
        drinks = []

        for drink in self.menu.items():
            if drink[1]['type'] == 'drink':
                drinks.append(drink[0])

        return drinks

    def food_only(self):
        foods = []

        for food in self.menu.items():
            if food[1]['type'] == 'food':
                foods.append(food[0])

        return foods
