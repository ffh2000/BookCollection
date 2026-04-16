from Book import Book

class ScienceBook(Book):
    def get_info(self):
        return f"[ScienceBook] {self.title} - {self.author} ({self.price}р.)"
