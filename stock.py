from items.menu_item import *
import json

class Stock():
	def __init__(self):
			self.stock = []
	
	def return_stock(self):
		return self.stock

	def return_books(self):
		books = []
		for item in self.stock:
			if item.return_type() == "Book":
				books.append(item)
		return books
		
	def return_food(self):
		food = []
		for item in self.stock:
			if item.return_type() == "Food":
				food.append(item)
		return food

	def return_drinks(self):
		drinks = []
		for item in self.stock:
			if item.return_type() == "Drink":
				drinks.append(item)
		return drinks

	def return_unknown(self):
		unknown = []
		for item in self.stock:
			if item.return_type() != "Drink" and item.return_type() != "Food" and item.return_type() != "Book":
				unknown.append(item)
		return unknown

	def add_item(self, item):
		if(item.name in self.return_names()):
			print("item with such a name already exists")
		else:
			self.stock.append(item)

	def return_names(self):
		stock_names = []
		for item in self.stock:
			stock_names.append(item.name)
		return stock_names

	def return_item_by_name(self, item_name):
		for item in self.stock:
			if item.name == item_name:
				return item
		print("No such item in stock")
		return False

	def clear_stock(self):
		self.stock.clear()

	def save_to_json(self):
		with open('stock.json', 'w') as file:
			json.dump([item.to_json() for item in self.stock], file, indent=4)

	def load_from_json(self):
		with open('stock.json') as file:
			data = json.load(file)
			for field in data:
				if field["type"] == "Drink":
					self.stock.append(Drink(field['name'], field['description'], field['price'], field['hot'], field['amount']))
				elif field["type"] == "Book":
					self.stock.append(Book(field['name'], field['description'], field['price'], field['author']))
				elif field["type"] == "Food":
					self.stock.append(Food(field['name'], field['description'], field['price'], field['weight']))
				else:
					self.stock.append(Menu_item(field['name'], field['description'], field['price']))

# item_stock = Stock()
# item_stock.load_from_json()

# coke = Drink("Coca Cola", "Fizzy Drink", 1.5, False, 350)
# mocha = Drink("Mocha", "Coffee with cocoa", 3.5, True, 400)
# alice = Book("Alice in Wonderland", "A girl on an adventure", 15, "Carol")
# donut = Food("Donut", "A chocolate glazed donut", 4.5, 300)

# item_stock.add_item(coke)
# item_stock.add_item(mocha)
# item_stock.add_item(alice)
# item_stock.add_item(donut)

# available_stock = item_stock.return_drinks()
# available_stock[0].describe()

# item_stock.clear_stock()

# item_stock.save_to_json()

# searched = item_stock.return_item_by_name("Coca Cola")
# searched.describe()

# whats_here = item_stock.return_stock()

# for item in whats_here:
# 	print("")
# 	item.describe()
# 	print("")