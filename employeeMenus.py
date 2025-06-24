#from console_interface import print_sep
#from console_interface import available_stock
from items.menu_item import *
from stock import Stock


def employee_welcome_screen(available_stock):
    print_sep()
    while True:
        selection = employee_screen()
        match selection:
            case 1:
                selection = stock(available_stock)
                if selection == 7:
                    return 1
            case 2:
                print("Order")
            case 3:
                return 1
            case 4:
                return 2

def employee_screen():
    print_sep()
    print("Welcome to the Employee Screen")
    print_sep()
    while True:
        print("1. Stock")
        print("2. Orders")
        print("3. Return to main menu\n")
        print("4. Exit\n")
        selection = input("Enter one of the numbers\n")
        if selection.isdigit() and int(selection) in range(1,5):
            selection = int(selection)
            return selection
        else:
            print_sep()
            print("Invalid input")
            print_sep()

def stock(available_stock):
    while True:
        print_sep()
        print("Stock options")
        print_sep()
        print("1. View All Stock")
        print("2. View Available Stock -- TODO") # TODO
        print("3. View Unavailable Stock -- TODO") # TODO
        print_sep()
        print("4. Drinks Menu")
        print("5. Foods Menu")
        print("6. Books Menu")
        print_sep()
        print("7. Return to main menu")
        print_sep()
        selection = input("Enter one of the numbers\n")
        if selection.isdigit() and int(selection) in range(1,7):
            selection = int(selection)
            match selection:
                case 1:
                    view_all_stock(available_stock)
                case 4:
                    drinks_menu(available_stock)
                case 5:
                    foods_menu(available_stock)
                case 6:
                    books_menu(available_stock)
        elif selection.isdigit() and int(selection) == 7:
            return 7
        else:
            print_sep()
            print("Invalid input")

def view_all_stock(available_stock):
    print_sep()
    print("All stock")
    all_items = available_stock.return_stock()
    for item in all_items:
        print_sep()
        item.describe()
    print_sep()

def drinks_menu(available_stock):
    while True:
        print_sep()
        print("Drinks menu options")
        print_sep()
        print("1. View All Drinks")
        print_sep()
        print("2. Add Drink to stock")
        print("3. Remove Drink from stock")
        print_sep()
        print("4. Back")
        print_sep()
        selection = input("Enter one of the numbers\n")
        if selection.isdigit() and int(selection) in range(1,5):
            selection = int(selection)
            match selection:
                case 1:
                    drinks = available_stock.return_drinks()
                    if not drinks:
                        print_sep()
                        print("There are no drinks in stock at the moment")
                    for drink in drinks:
                        print_sep()
                        drink.describe()
                    print_sep()
                case 2:
                    add_drink_to_stock(available_stock)
                case 3:
                    remove_drink_from_stock(available_stock)
                case 4:
                    return
        else:
            print_sep()
            print("Invalid input")

def add_drink_to_stock(available_stock):
    print_sep()
    print_sep()
    print("Add drink to stock screen")
    print("The drink must have a name, description, price, boolean value if it's hot, amount in ml")
    print_sep()
    name = input("Enter the name of the drink\n")
    description = input("Enter the description of the drink\n")
    price = input("Enter the price of the drink\n")
    price = float(price)
    hot = input("Is the drink hot? (y/n)\n")
    if hot.lower() == "y":
        hot = True
    else:
        hot = False
    amount = input("Enter the amount of the drink in ml\n")
    amount = int(amount)
    drink = Drink(id=None, name=name, description=description, price=price, hot=hot, amount=amount)
    available_stock.add_item(drink)
    print_sep()
    print("Drink added to stock")
    print_sep()
    available_stock.reload_stock()

def remove_drink_from_stock(available_stock):
    print_sep()
    print("Remove drink from stock screen")
    print_sep()
    drinks = available_stock.return_drinks()
    while True:
        number = 1
        for drink in drinks:
            print_sep()
            print(f"Drink {number}")
            drink.describe()
            number += 1
            print_sep()
        print_sep()
        print("Enter the drink selection number you want to remove")
        print_sep()
        selected = input("Selection Number:\n")
        if selected.isdigit() and int(selected) in range(1,len(drinks)+1):
            selected = int(selected)
            selected_drink = drinks[selected-1]
            available_stock.remove_item(selected_drink)
            print_sep()
            print("Drink removed from stock")
            print_sep()
            available_stock.reload_stock()
            return
        else:
            print_sep()
            print("Invalid input")

def foods_menu(available_stock):
    while True:
        print_sep()
        print("Foods menu options")
        print_sep()
        print("1. View All Foods")
        print_sep()
        print("2. Add Food to stock")
        print("3. Remove Food from stock")
        print_sep()
        print("4. Back\n")
        print_sep()
        selection = input("Enter one of the numbers\n")
        if selection.isdigit() and int(selection) in range(1,5):
            selection = int(selection)
            match selection:
                case 1:
                    foods = available_stock.return_foods()
                    if not foods:
                        print_sep()
                        print("There are no foods in stock at the moment")
                    for food in foods:
                        print_sep()
                        food.describe()
                    print_sep()
                case 2:
                    add_food_to_stock(available_stock)
                case 3:
                    remove_food_from_stock(available_stock)
                case 4:
                    return
        else:
            print_sep()
            print("Invalid input")

def add_food_to_stock(available_stock):
    print_sep()
    print("Add food to stock screen")
    print("The food must have a name, description, price, weight in grams")
    print_sep()
    name = input("Enter the name of the food\n")
    description = input("Enter the description of the food\n")
    price = input("Enter the price of the food\n")
    price = float(price)
    weight = input("Enter the weight of the food in grams\n")
    weight = int(weight)
    food = Food(id=None, name=name, description=description, price=price, weight=weight)
    available_stock.add_item(food)
    print_sep()
    print("Food added to stock")
    print_sep()
    available_stock.reload_stock()

def remove_food_from_stock(available_stock):
    print_sep()
    print("Remove drink from stock screen")
    print_sep()
    foods = available_stock.return_foods()
    while True:
        number = 1
        for food in foods:
            print_sep()
            print(f"Food {number}")
            food.describe()
            number += 1
            print_sep()
        print_sep()
        print("Enter the food selection number you want to remove")
        print_sep()
        selected = input("Selection Number:\n")
        if selected.isdigit() and int(selected) in range(1, len(foods) + 1):
            selected = int(selected)
            selected_food = foods[selected - 1]
            available_stock.remove_item(selected_food)
            print_sep()
            print("Food removed from stock")
            print_sep()
            available_stock.reload_stock()
            return
        else:
            print_sep()
            print("Invalid input")


def books_menu(available_stock):
    while True:
        print_sep()
        print("Books menu options")
        print_sep()
        print("1. View All Books")
        print_sep()
        print("2. Add Book to stock")
        print("3. Remove Book from stock")
        print_sep()
        print("4. Back\n")
        print_sep()
        selection = input("Enter one of the numbers\n")
        if selection.isdigit() and int(selection) in range(1, 5):
            selection = int(selection)
            match selection:
                case 1:
                    books = available_stock.return_books()
                    if not books:
                        print_sep()
                        print("There are no books in stock at the moment")
                    for book in books:
                        print_sep()
                        book.describe()
                    print_sep()
                case 2:
                    add_book_to_stock(available_stock)
                case 3:
                    remove_book_from_stock(available_stock)
                case 4:
                    return
        else:
            print_sep()
            print("Invalid input")

def add_book_to_stock(available_stock):
    print_sep()
    print("Add book to stock screen")
    print("The book must have a title, description, price and author")
    print_sep()
    name = input("Enter the title of the book\n")
    description = input("Enter the description of the book\n")
    price = input("Enter the price of the book\n")
    price = float(price)
    author = input("Enter book author\n")
    book = Book(id=None, name=name, description=description, price=price, author=author)
    available_stock.add_item(book)
    print_sep()
    print("Book added to stock")
    print_sep()
    available_stock.reload_stock()

def remove_book_from_stock(available_stock):
    print_sep()
    print("Remove book from stock screen")
    print_sep()
    books = available_stock.return_books()
    while True:
        number = 1
        for book in books:
            print_sep()
            print(f"Book {number}")
            book.describe()
            number += 1
            print_sep()
        print_sep()
        print("Enter the book selection number you want to remove")
        print_sep()
        selected = input("Selection Number:\n")
        if selected.isdigit() and int(selected) in range(1, len(books) + 1):
            selected = int(selected)
            selected_book = books[selected - 1]
            available_stock.remove_item(selected_book)
            print_sep()
            print("Book removed from stock")
            print_sep()
            available_stock.reload_stock()
            return
        else:
            print_sep()
            print("Invalid input")

def print_sep():
    print("-----------------------------")