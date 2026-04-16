from Book import Book

class ArtBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)
    
    def get_info(self):
        return f"[ArtBook] {self.title} - {self.author} ({self.price}р.)"
