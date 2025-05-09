from menu_item import Menu_item

class Drink(Menu_item):
	def __init__(self, name, description, price, hot, amount):
		super().__init__(name, description, price)
		self.hot = hot
		self.amount = amount
		self.type = "Drink"

	def describe(self):
		print(f"{self.type} | {self.name} - {self.amount} ml | {self.get_price()}")
		print(f"Description: {self.description}")
		if self.hot:
			print("Drink is hot")
		else:
			print("Drink is cold")

mocha = Drink("Mocha", "Coffee with chocolate", 2.50, True, 350)
mocha.describe()