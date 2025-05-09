from items.menu_item import *

class Cart():
	def __init__(self):
		self.items = []

	def add_item(self, item):
		self.items.append(item)

	def return_items(self):
		return self.items

	def calculate_total(self):
		total = 0
		for item in self.items:
			total += item.get_price()
		return total

# alice = Book("Alice in Wonderland", "A fantasy book about alice and her adventures", 15, "Carrol")
# mocha = Drink("Mocha", "Coffe with hot chocolate", 3.25, True, 250)
# coke = Drink("Coca Cola", "Fizzy Drink", 1.5, False, 350)

# new_cart = Cart()
# new_cart.add_item(alice)
# new_cart.add_item(mocha)
# new_cart.add_item(coke)


# print("Your Cart:")
# for item in new_cart.return_items():
# 	print("")
# 	item.describe()
# print(f"\nYour total is: £{new_cart.calculate_total()}")