from Book import Book

class FictionBook(Book):
    def get_info(self):
        return f"[FictionBook] {self.title} - {self.author} ({self.price}р.)"
