from traceback import print_exception

from items.menu_item import *
import json
import database_connection as dc

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
		
	def return_foods(self):
		foods = []
		for item in self.stock:
			if item.return_type() == "Food":
				foods.append(item)
		return foods

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
			#self.stock.append(item)
			self.save_to_database(item)

	def remove_item(self, item):
		self.delete_from_database(item)

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

	def return_item_by_id(self, item_id, type):
		items = []
		if type == "Drink":
			items = self.return_drinks()
		elif type == "Book":
			items = self.return_books()
		elif type == "Food":
			items = self.return_foods()
		else:
			print("No such item type")
			return None

		if 0 < item_id < len(items):
			item = items[item_id-1]
			return item
		else:
			print("No such item in stock")
			return None

	def clear_stock(self):
		self.stock.clear()

	def save_to_database(self, item):
		if item.return_type() == "Drink":
			dc.insert_into_database('drinks', item)
		elif item.return_type() == "Food":
			dc.insert_into_database('foods', item)
		elif item.return_type() == "Book":
			dc.insert_into_database('books', item)
		else:
			print_exception("No such item type, generics are yet to be implemented")

	def delete_from_database(self, item):
		dc.delete_from_database(item)

	def load_drinks(self):
		data = dc.load_from_database("drinks")
		for item in data:
			self.stock.append(Drink(item[0],item[1], item[2], item[3], item[4], item[5]))

	def load_foods(self):
		data = dc.load_from_database("foods")
		for item in data:
			self.stock.append(Food(item[0], item[1], item[2], item[3], item[4]))

	def load_books(self):
		data = dc.load_from_database("books")
		for item in data:
			self.stock.append(Book(item[0], item[1], item[2], item[3], item[4]))

	def load_stock_from_database(self):
		self.load_drinks()
		self.load_foods()
		self.load_books()

	def reload_stock(self):
		self.clear_stock()
		self.load_stock_from_database()

		# 			self.stock.append(Menu_item(field['name'], field['description'], field['price']))

# item_stock = Stock()
# item_stock.load_from_json()

# coke = Drink("Coca Cola", "Fizzy Drink", 1.5, False, 350)
# mocha = Drink(id=None, name="Latte", description="Coffee with milk and sugar", price=3.5, hot=True, amount=400)
# alice = Book("Alice in Wonderland", "A girl on an adventure", 15, "Carol")
# donut = Food("Donut", "A chocolate glazed donut", 4.5, 300)

# item_stock.add_item(coke)
# item_stock.add_item(mocha)
# item_stock.add_item(alice)
# item_stock.add_item(donut)

# available_stock = item_stock.return_drinks()
# available_stock[0].describe()

# item_stock.clear_stock()
#item_stock.load_stock_from_database()

# item_stock.add_item(mocha)
# item_stock.save_to_database(mocha)

# item_stock.save_to_json()

# searched = item_stock.return_item_by_name("Coca Cola")
# searched.describe()

# whats_here = item_stock.return_stock()

# for item in whats_here:
# 	print("")
# 	#print(item.name)
# 	item.describe()
# 	print("")