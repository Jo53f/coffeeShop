from menu_item import Menu_item

class Food(Menu_item):
	def __init__(self, name, description, price, weight):
		super().__init__(name, description, price)
		self.weight = weight
		self.type = "Food"

	def describe(self):
		print(f"{self.type} | {self.name} - {self.weight} grams | £{self.get_price()}")
		print(f"Description: {self.description}")

donut = Food("Donut", "A chocolate donut", 3.25, 150)
donut.describe()