from menu_item import Menu_item

class Book(Menu_item):
	"""docstring for Book"""
	def __init__(self, name, description, price, author):
		super().__init__(name, description, price)
		self.name = name
		self.description = description
		self.price = price
		self.author = author
		self.item = "Book"

alice = Book("Alice in Wonderland", "A fantasy book", 15, "Timothy")
alice.describe()