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
		print("3. View Cart")
		print("4. Checkout")
		print("5. Exit")

		selection = input("Enter one of the numbers\n")

		if selection.isdigit() and int(selection) <= 5:
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
		if order_selection.isdigit() and int(order_selection) in range(1,6):
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
					else:
						print("No such item")
					print(cart.calculate_total())
					break
			case 2:
				view_drink_menu()
			case 3:
				view_book_menu()
			case 4:
				view_food_menu()
			case 5:
				return cart

def checkout(cart):
	"""
	Checkout function, takes in user cart and calculates total.
	Allows user to confirm they're ready to pay.
	"""
	while True:
		print("Checkout")
		print(f"Your total is: £{cart.calculate_total()}")
		print("Are you ready to pay?")
		print("1. Yes")
		print("2. Return to main menu")
		check_selection = input("Enter one of the numbers\n")
		if check_selection.isdigit() and int(check_selection) in range(1,3):
			check_selection = int(check_selection)
			break
		else:
			print("Invalid input")
	if check_selection == 1:
		print("Thank you for shopping with us!")
		return True
	else:
		return False

def show_cart(cart):
	print_sep()
	if len(cart.return_items()) < 1:
		print("Your cart is empty right now")
		return
	print("Your Cart")
	for item in cart.return_items():
		print_sep()
		item.describe()
		
# Console Interface
print("Welcome to the Cafe!")
# Create Stock object
available_stock = Stock()
# Creat Order object
user_cart = Cart()
while True:
	available_stock.load_from_json()
	# Launch the welcome screen
	selection = welcome_screen()
	match selection:
		case 1:
			view_menu_screen()
		case 2:
			user_cart = order_screen(user_cart, available_stock)
		case 3:
			show_cart(user_cart)
		case 4:
			exit_orders = checkout(user_cart)
			if exit_orders:
				break
		case 5:
			break