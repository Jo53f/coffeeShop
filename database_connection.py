import mysql.connector


def database_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="josef",
        password="pass",
        database="coffee_shop_db"
    )
    return mydb

def load_from_database(table_name):
    mydb = database_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    result = cursor.fetchall()
    cursor.close()
    return result

def insert_into_database(table_name, item):
    mydb = database_connection()
    cursor = mydb.cursor()

    if not item:
        print(f"No is no value to insert into the {table_name} table")
        cursor.close()
        return
    elif table_name == "drinks":
        cursor.execute(f"INSERT INTO {table_name} (name, description, price, hot, amount) VALUES {item.return_tuple()}")
    elif table_name == "books":
        cursor.execute(f"INSERT INTO {table_name} (title, description, price, author) VALUES {item.return_tuple()}")
    elif table_name == "foods":
        cursor.execute(f"INSERT INTO {table_name} (name, description, price, weight) VALUES {item.return_tuple()}")
    else:
        print("Invalid table name")

    #cursor.execute(f"INSERT INTO {table_name} (id, name, description, price, hot, amount) VALUES {values}")
    mydb.commit()

def delete_from_database(item):
    mydb = database_connection()
    cursor = mydb.cursor()

    if not item:
        print("No item to delete")
        cursor.close()
        return
    elif item.return_type() == "Drink":
        table_name = "drinks"
        cursor.execute(f"DELETE FROM {table_name} WHERE drink_id = {item.return_id()}")
    elif item.return_type() == "Book":
        table_name = "books"
        cursor.execute(f"DELETE FROM {table_name} WHERE book_id = {item.return_id()}")
    elif item.return_type() == "Food":
        table_name = "foods"
        cursor.execute(f"DELETE FROM {table_name} WHERE food_id = {item.return_id()}")
    else:
        return
    mydb.commit()
    cursor.close()

#print(type(load_from_database("drinks")[0][3]))
