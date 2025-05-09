from stock import Stock
from cart import Cart
from items.menu_item import *

def print_sep():
	print("-----------------------------")

def welcome_screen():
	print_sep()
	print("Please select one of the options below")
	while True:
		print_sep()
		print("1. View the Menu")
		print("2. Order")
		print("3 Checkout")
		print("4. Exit")

		selection = input("Enter one of the numbers\n")

		if selection.isdigit() and int(selection) <= 3:
			return int(selection)
		else:
			print("\nThat wasn't one of the options, try again \n")

def view_menu_screen():
	print("\nThe menu options are:")
	for item in available_stock.return_stock():
		print_sep()
		item.describe()
	print_sep()

def view_drink_menu():
	print("\nThe drink menu options are:")
	for item in available_stock.return_drinks():
		print_sep()
		item.describe()
	print_sep()

def view_book_menu():
	print("\nThe book menu options are:")
	for item in available_stock.return_books():
		print_sep()
		item.describe()
	print_sep()

def view_food_menu():
	print("\nThe food menu options are:")
	for item in available_stock.return_food():
		print_sep()
		item.describe()
	print_sep()

def order_screen(cart, stock):
	print_sep()
	print("Order Screen") # temp

	while True:
		print("Select a number from order menu")
		print("1. Order by name")
		print("2. Check Drink menu")
		print("3. Check Book menu")
		print("4. Check Food menu")
		print("5. Return to main menu\n")
		order_selection = input("Enter the number of the chosen selection\n")
		if order_selection.isdigit() and int(order_selection) in range(1,5):
			order_selection = int(order_selection)
		else:
			print("Invalid input")
			continue
		match order_selection:
			case 1:
				while True:
					addition = input("Enter the name of the item you'd like to add\n")
					item = stock.return_item_by_name(addition)
					if item:
						cart.add_item(item)
						break
					else:
						print("No such item")
			case 2:
				view_drink_menu()
			case 3:
				view_book_menu()
			case 4:
				view_food_menu()
		
# Console Interface
print("Welcome to the Cafe!")
while True:
	# Create Stock object
	available_stock = Stock()
	available_stock.load_from_json()
	# Creat Order object
	user_cart = Cart()
	# Launch the welcome screen
	selection = welcome_screen()
	match selection:
		case 1:
			view_menu_screen()
		case 2:
			order_screen(user_cart, available_stock)
			print(user_cart.calculate_total())
		case 3:
			break # add checkout
		case 4:
			break