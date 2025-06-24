class Menu_item():
	def __init__(self, id=None, name=None, description=None, price=None):
		self.id = id
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

	def return_id(self):
		return self.id

	def return_tuple(self):
		return (self.name, self.description, self.price)

	def to_json(self):
		return {
		"name":self.name,
		"description":self.description,
		"price":self.price,
		"type":self.type
		}

class Drink(Menu_item):
	def __init__(self, id, name, description, price, hot, amount):
		super().__init__(id, name, description, price)
		self.hot = hot
		self.amount = amount
		self.type = "Drink"

	def price_per_litre(self):
		return (self.get_price()/self.amount)*1000

	def describe(self):
		print(f"{self.type} | {self.name} - {self.amount} ml | £{self.get_price():.2f} | £/litre {self.price_per_litre():.2f}")
		print(f"Description: {self.description}")
		if self.hot:
			print("Hot Drink")
		else:
			print("Cold Drink")

	def return_tuple(self):
		return (self.name, self.description, self.price, self.hot, self.amount)

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
	def __init__(self, id, name, description, price, author):
		super().__init__(id, name, description, price)
		self.author = author
		self.type = "Book"

	def describe(self):
		print(f"{self.type} | {self.name} - by {self.author} | £{self.get_price():.2f}")
		print(f"Description: {self.description}")

	def return_tuple(self):
		return (self.name, self.description, self.price, self.author)

	def to_json(self):
		return {
		"name":self.name,
		"description":self.description,
		"price":self.price,
		"type":self.type,
		"author":self.author
		}

class Food(Menu_item):
	def __init__(self, id, name, description, price, weight):
		super().__init__(id, name, description, price)
		self.weight = weight
		self.type = "Food"

	def price_per_kilogram(self):
		return (self.get_price()/self.weight)*1000

	def describe(self):
		print(f"{self.type} | {self.name} - {self.weight} grams | £{self.get_price():.2f} | £/kg {self.price_per_kilogram():.2f}")
		print(f"Description: {self.description}")

	def return_tuple(self):
		return (self.name, self.description, self.price, self.weight)

	def to_json(self):
		return {
		"name":self.name,
		"description":self.description,
		"price":self.price,
		"type":self.type,
		"weight":self.weight
		}