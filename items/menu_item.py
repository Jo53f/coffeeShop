class Menu_item():
	def __init__(self, name, description, price):
		self.name = name
		self.description = description
		self.price = price
		self.type = "Item"

	def describe(self):
		print(f"{self.type} | {self.name} | £{self.get_price():.2f}")
		print(f"Description: {self.description}")

	def get_price(self):
		return self.price

	def return_type(self):
		return self.type

	def to_json(self):
		return {
		"name":self.name,
		"description":self.description,
		"price":self.price,
		"type":self.type
		}

class Drink(Menu_item):
	def __init__(self, name, description, price, hot, amount):
		super().__init__(name, description, price)
		self.hot = hot
		self.amount = amount
		self.type = "Drink"

	def price_per_litre(self):
		return (self.get_price()/self.amount)*1000

	def describe(self):
		print(f"{self.type} | {self.name} - {self.amount} ml | £{self.get_price():.2f} | £/litre {self.price_per_litre():.2f}")
		print(f"Description: {self.description}")
		if self.hot:
			print("Drink is hot")
		else:
			print("Drink is cold")

	def to_json(self):
		return {
		"name":self.name,
		"description":self.description,
		"price":self.price,
		"type":self.type,
		"hot":self.hot,
		"amount":self.amount
		}

class Book(Menu_item):
	"""docstring for Book"""
	def __init__(self, name, description, price, author):
		super().__init__(name, description, price)
		self.author = author
		self.type = "Book"

	def describe(self):
		print(f"{self.type} | {self.name} - by {self.author} | £{self.get_price():.2f}")
		print(f"Description: {self.description}")

	def to_json(self):
		return {
		"name":self.name,
		"description":self.description,
		"price":self.price,
		"type":self.type,
		"author":self.author
		}

class Food(Menu_item):
	def __init__(self, name, description, price, weight):
		super().__init__(name, description, price)
		self.weight = weight
		self.type = "Food"

	def price_per_kilogram(self):
		return (self.get_price()/self.weight)*1000

	def describe(self):
		print(f"{self.type} | {self.name} - {self.weight} grams | £{self.get_price():.2f} | £/kg {self.price_per_kilogram():.2f}")
		print(f"Description: {self.description}")

	def to_json(self):
		return {
		"name":self.name,
		"description":self.description,
		"price":self.price,
		"type":self.type,
		"weight":self.weight
		}