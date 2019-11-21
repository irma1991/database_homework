import sqlite3
import pprint


def execute_query(db_name, query, entry):
    connection = sqlite3.connect(db_name)
    connection_cursor = connection.cursor()
    connection_cursor.execute(query, entry)
    connection.commit()
    connection.close()


def create_table(db_name, query):
    connection = sqlite3.connect(db_name)
    connection_cursor = connection.cursor()
    connection_cursor.execute(query)
    connection.commit()
    connection.close()


def select_data(db_name, query, entry=None):
    if entry is None:
        entry = []
    connection = sqlite3.connect(db_name)
    connection_cursor = connection.cursor()
    connection_cursor.execute(query, entry)
    connection.commit()
    rows = []
    for row in connection_cursor.execute(query, entry):
        rows.append(row)
    pp = pprint.PrettyPrinter()
    pp.pprint(rows)
    connection.close()


db_books = "books.db"
books_table_query = """CREATE TABLE IF NOT EXISTS books (
                                                        id integer PRIMARY KEY,
                                                        book_title text,
                                                        author text,
                                                        publish_date date,
                                                        publisher text,
                                                        selling_price numeric
                                                        )"""
db_books = "publishers.db"
publishers_table_query = """CREATE TABLE IF NOT EXISTS publishers (
                                                        id integer PRIMARY KEY,
                                                        publisher_name text,
                                                        book_title text,
                                                        author text,
                                                        printed_quantity integer,
                                                        printing_price numeric
                                                        )"""


# Insert
def insert_book(book_title, author, publish_date, publisher, selling_price):
    insert_query = """INSERT INTO books (book_title, author, publish_date, publisher, selling_price) 
                      VALUES(?, ?, ?, ?, ?)"""
    book = [book_title, author, publish_date, publisher, selling_price]
    execute_query(db_books, insert_query, book)


def insert_publisher(publisher_name, book_title, author, printed_quantity, printing_price):
    insert_query = """INSERT INTO publishers (publisher_name, book_title, author, printed_quantity, printing_price) 
                      VALUES(?, ?, ?, ?, ?)"""
    publisher = [publisher_name, book_title, author, printed_quantity, printing_price]
    execute_query(db_books, insert_query, publisher)


# Search
def get_from_books(search_string):
    select_query = """SELECT * FROM books WHERE book_title OR 
                                                author OR 
                                                publish_date OR 
                                                publisher OR 
                                                selling_price LIKE ?"""
    title = ['%' + search_string + '%']
    select_data(db_books, select_query, title)


def get_from_publishers(search_string):
    select_query = """SELECT * FROM publishers WHERE publisher_name OR 
                                                     book_title OR 
                                                     author OR 
                                                     printed_quantity OR 
                                                     printing_price LIKE ?"""
    title = ['%' + search_string + '%']
    select_data(db_books, select_query, title)


# Update Book methods
def update_book_title(new_value, book_id):
    update_query = """UPDATE books SET book_title = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


def update_book_publisher(new_value, book_id):
    update_query = """UPDATE books SET publisher = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


def update_book_author(new_value, book_id):
    update_query = """UPDATE books SET author = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


def update_book_publish_date(new_value, book_id):
    update_query = """UPDATE books SET publish_date = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


def update_book_selling_price(new_value, book_id):
    update_query = """UPDATE books SET selling_price = ? WHERE id = ?"""
    update_data = [new_value, book_id]
    execute_query(db_books, update_query, update_data)


# Update Publisher methods
def update_publisher_name(new_value, publisher_id):
    update_query = """UPDATE publishers SET publisher_name = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


def update_publisher_book_title(new_value, publisher_id):
    update_query = """UPDATE publishers SET book_title = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


def update_publisher_author(new_value, publisher_id):
    update_query = """UPDATE publishers SET author = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


def update_publisher_printed_quantity(new_value, publisher_id):
    update_query = """UPDATE publishers SET printed_quantity = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


def update_publisher_printing_price(new_value, publisher_id):
    update_query = """UPDATE publishers SET printing_price = ? WHERE id = ?"""
    update_data = [new_value, publisher_id]
    execute_query(db_books, update_query, update_data)


# Delete
def delete_book_by_id(book_id):
    delete_query = """DELETE FROM books WHERE id = ?"""
    entry_id = [book_id]
    execute_query(db_books, delete_query, entry_id)


def delete_publisher_by_id(publisher_id):
    delete_query = """DELETE FROM publishers WHERE id = ?"""
    entry_id = [publisher_id]
    execute_query(db_books, delete_query, entry_id)


def get_quantity_price():
    select_query = """SELECT (publishers.printed_quantity * SUM(books.selling_price - publishers.printing_price)) AS rez
                        FROM books 
                        INNER JOIN publishers ON books.book_title = publishers.book_title"""
    select_data(db_books, select_query)


create_table(db_books, books_table_query)
create_table(db_books, publishers_table_query)
# insert_book('Zigmas po dangum', 'Janionis', 1998, 'Alma Litera', 25)
# insert_publisher('Alma litera', 'Zigmas po dangum', 'Janionis', 100, 10)
get_from_books('Zigm')
get_from_publishers('Alm')
get_quantity_price()