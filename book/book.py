class book:
    def __init__(self, book_title, author, publish_date, publisher, selling_price, id = None):
        self.book_title = book_title
        self.author = author
        self.publish_date = publish_date
        self.publisher = publisher
        self.selling_price = selling_price
        self.id = id