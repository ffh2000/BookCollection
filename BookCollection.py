class BookCollection():
    def __init__(self, theme, books, price):
        self.books = books
        self.price = price
        self.theme = theme

    def get_price(self):
        return self.price

    def get_theme(self):
        return self.theme

    def get_info(self):
        books_info = "\n".join([b.get_info() for b in self.books])
        return f"\n=== Коллекция книг [{self.get_theme()}] ===\n{books_info}\nЦена: {self.get_price()}\n"
