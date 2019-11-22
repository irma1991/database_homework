import sqlite3
from book import book
from book import publisher
import pprint


def create_books(book):
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()
    sql_query_not_injectable = "INSERT into books VALUES (?, ?, ?, ?, ?)"
    query_values = (book.book_title, book.author, book.publish_date, book.publisher, book.selling_price)

    cursor.executemany(sql_query_not_injectable, query_values)

    connection.commit()
    connection.close()

book1 = book.book("Prie ezero", "Petras Petraitis", 2015, "Knygynas", 12)
create_books(book1)
print(book1)


def execute_query(query, entry):
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute(query, entry)
    connection.commit()
    connection.close()


def create_table_books():
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute("""CREATE TABLE IF NOT EXISTS books (
                                                            id integer PRIMARY KEY,
                                                            book_title text,
                                                            author text,
                                                            publish_date date,
                                                            publisher text,
                                                            selling_price numeric
                                                            )""")
    connection.commit()
    connection.close()

def create_table_publishers():
        connection = sqlite3.connect("books.db")
        connection_cursor = connection.cursor()
        connection_cursor.execute("""CREATE TABLE IF NOT EXISTS publishers (
                                                        id integer PRIMARY KEY,
                                                        publisher_name text,
                                                        book_title text,
                                                        author text,
                                                        printed_quantity integer,
                                                        printing_price numeric
                                                        )""")
        connection.commit()
        connection.close()


def select_data(query, entry=None):
    if entry is None:
        entry = []
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    connection_cursor.execute(query, entry)
    rows = []
    for row in connection_cursor.execute(query, entry):
        rows.append(row)
    pp = pprint.PrettyPrinter()
    pp.pprint(rows)
    connection.close()


# Insert
def insert_book(book_title, author, publish_date, publisher, selling_price):
    insert_query = """INSERT INTO books (book_title, author, publish_date, publisher, selling_price) 
                      VALUES(?, ?, ?, ?, ?)"""
    book = [book_title, author, publish_date, publisher, selling_price]
    execute_query(insert_query, book)


def insert_publisher(publisher_name, book_title, author, printed_quantity, printing_price):
    insert_query = """INSERT INTO publishers (publisher_name, book_title, author, printed_quantity, printing_price) 
                      VALUES(?, ?, ?, ?, ?)"""
    publisher = [publisher_name, book_title, author, printed_quantity, printing_price]
    execute_query(insert_query, publisher)


# Search
def get_from_books(search_string):
    select_query = """SELECT * FROM books WHERE book_title OR 
                                                author OR 
                                                publish_date OR 
                                                publisher OR 
                                                selling_price LIKE ?"""
    title = ['%' + search_string + '%']
    select_data(select_query, title)


def get_from_publishers(search_string):
    select_query = """SELECT * FROM publishers WHERE publisher_name OR 
                                                     book_title OR 
                                                     author OR 
                                                     printed_quantity OR 
                                                     printing_price LIKE ?"""
    title = ['%' + search_string + '%']
    select_data(select_query, title)


# Update Book methods
def update_book_title(new_value, book_id):
    update_query = """UPDATE books SET book_title = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(update_query, update_data)


def update_book_publisher(new_value, book_id):
    update_query = """UPDATE books SET publisher = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(update_query, update_data)


def update_book_author(new_value, book_id):
    update_query = """UPDATE books SET author = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(update_query, update_data)


def update_book_publish_date(new_value, book_id):
    update_query = """UPDATE books SET publish_date = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(update_query, update_data)


def update_book_selling_price(new_value, book_id):
    update_query = """UPDATE books SET selling_price = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(update_query, update_data)


# Update Publisher methods
def update_publisher_name(new_value, publisher_id):
    update_query = """UPDATE publishers SET publisher_name = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(update_query, update_data)


def update_publisher_book_title(new_value, publisher_id):
    update_query = """UPDATE publishers SET book_title = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(update_query, update_data)


def update_publisher_author(new_value, publisher_id):
    update_query = """UPDATE publishers SET author = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(update_query, update_data)


def update_publisher_printed_quantity(new_value, publisher_id):
    update_query = """UPDATE publishers SET printed_quantity = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(update_query, update_data)


def update_publisher_printing_price(new_value, publisher_id):
    update_query = """UPDATE publishers SET printing_price = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(update_query, update_data)


# Delete
def delete_book_by_id(book_id):
    delete_query = """DELETE FROM books WHERE id = ?"""
    entry_id = [book_id]
    execute_query(delete_query, entry_id)


def delete_publisher_by_id(publisher_id):
    delete_query = """DELETE FROM publishers WHERE id = ?"""
    entry_id = [publisher_id]
    execute_query(delete_query, entry_id)


def get_quantity_price():
    rows=[]
    connection = sqlite3.connect("books.db")
    connection_cursor = connection.cursor()
    select_query = """SELECT (publishers.printed_quantity * SUM(books.selling_price - publishers.printing_price)) AS rez
                        FROM books 
                        INNER JOIN publishers ON books.book_title = publishers.book_title"""
    for row in connection_cursor.execute(select_query):
        rows.append(row)

    pp = pprint.PrettyPrinter()
    pp.pprint(rows)

    connection.close()


create_table_books()
create_table_publishers()
insert_book('Zigmas po dangum', 'Janionis', 1998, 'Alma Litera', 25)
insert_publisher('Alma litera', 'Zigmas po dangum', 'Janionis', 100, 10)
get_from_books('Zigm')
get_from_publishers('Alm')
get_quantity_price()

