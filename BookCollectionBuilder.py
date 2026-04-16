from BookCollection import BookCollection

class BookCollectionBuilder:
    def __init__(self):
        self.books = []
        self.theme = "Тема по умолчанию"
        self.price = 0

    def add_book(self, book):
        self.books.append(book)

    def set_theme(self, theme):
        self.theme = theme

    def set_price(self, price):
        self.price = price

    def build(self):
        return BookCollection(self.theme, self.books, self.price)